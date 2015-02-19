# -*- coding: utf-8 -*-
from openerp import fields, models

class Users(models.Model):
    _inherit = 'res.users'

    performer = fields.Boolean("Performer", default=False)
    show_ids = fields.Many2many('shows.spectacle', string="Shows")
