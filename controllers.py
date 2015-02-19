# -*- coding: utf-8 -*-
from openerp import http

# class Shows(http.Controller):
#     @http.route('/shows/shows/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/shows/shows/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('shows.listing', {
#             'root': '/shows/shows',
#             'objects': http.request.env['shows.shows'].search([]),
#         })

#     @http.route('/shows/shows/objects/<model("shows.shows"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('shows.object', {
#             'object': obj
#         })