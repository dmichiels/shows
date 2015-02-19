# -*- coding: utf-8 -*-

from openerp import models, fields, api
from datetime import timedelta

class Shows(models.Model):
    _name = 'shows.shows'

    name = fields.Char(required="True")
    spectacle_id = fields.Many2one('shows.spectacle', string="Spectacle", required="True")

    responsible_id = fields.Many2one('res.users')

    starting_date = fields.Datetime(string="Starting date")
    duration = fields.Float(help="Duration in days",
                            default=1)
    end_date = fields.Datetime(string="End Date", store=True,
                           compute='_get_end_date',
                           inverse='_set_end_date')

    street = fields.Char()
    city = fields.Char()
    zipcode = fields.Char()
    country_id = fields.Many2one('res.country',
                                 ondelete='set null',
                                 string="country"
                              )
    info = fields.Text()

    presence_ids = fields.One2many('shows.performer_date', 'date_id', string="Presence")
     
    nb_participant = fields.Integer(compute='_get_nb_participant')
    nb_expected_participant = fields.Integer(compute='_get_expected_participant')
    nb_max_participant = fields.Integer(compute='_get_max_participant')

    stage_id = fields.Many2one('shows.stage', string="Stages")

    @api.one
    def on_change_stage_id(self, stage_id):
        self.stage_id = stage_id

    @api.one
    @api.depends('starting_date', 'duration')
    def _get_end_date(self):
        if not (self.starting_date and self.duration):
            self.end_date = self.starting_date
            return
        start = fields.Datetime.from_string(self.starting_date)
        duration = timedelta(days=self.duration, seconds=-1)
        self.end_date = start+duration

    @api.one
    def _set_end_date(self):
        if not (self.starting_date and self.end_date):

            return

        start_date = field.Datetime.from_string(self.starting_date)
        end_date = fields.Datetime.from_string(self.end_date)
        self.duration = (end_date - start_date).days + 1

    @api.one
    @api.depends('presence_ids')
    def _get_nb_participant(self):
        self.nb_participant = len(self.presence_ids.search(['&',
                                                            ('date_id', '=', self.id),
                                                            ('state', '=', 'present')]))

    @api.one
    @api.depends('spectacle_id')
    def _get_expected_participant(self):
        self.nb_expected_participant = len(self.spectacle_id.performer_ids)

    @api.one
    @api.depends('presence_ids', 'nb_expected_participant')
    def _get_max_participant(self):
        absent = len(self.presence_ids.search(['&',
                                               ('date_id', '=', self.id),
                                               ('state', '=', 'absent')]))
        self.nb_max_participant = self.nb_expected_participant - absent

    @api.model
    def stage_groups(self, present_ids, domain, **kwargs):
        companies = self.env['shows.stage'].search([])
        name = companies.name_get()
        folded = companies.folded_get()
        return name, folded
        
    _group_by_full = {
        'stage_id': stage_groups,
    }

class Stage(models.Model):
    _name = 'shows.stage'
    
    name = fields.Char(required="True")
    sequence = fields.Integer(default=1)
    folded = fields.Boolean(default=False)

    def folded_get(self):
        res = {}
        for stage in self:
            if stage.folded:
                res[stage.id] = stage.folded
        return res
        
    
class Spectacle(models.Model):
    _name='shows.spectacle'

    name= fields.Char(required="True")
    performer_ids = fields.Many2many('res.users',
                                     domain=[('performer', '=', True)])

class Performer_Date(models.Model):
    _name='shows.performer_date'
    
    performer_id = fields.Many2one('res.users',
                                   domain=[('performer', '=', True)])
    date_id = fields.Many2one('shows.shows')

    state = fields.Selection([
        ('present', "Present"),
        ('absent', "Absent"),
        ('undefined', "Undefined")
        ], default='undefined')
    
    
