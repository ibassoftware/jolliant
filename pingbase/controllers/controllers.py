# -*- coding: utf-8 -*-
# from odoo import http


# class Pingbase(http.Controller):
#     @http.route('/pingbase/pingbase/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pingbase/pingbase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pingbase.listing', {
#             'root': '/pingbase/pingbase',
#             'objects': http.request.env['pingbase.pingbase'].search([]),
#         })

#     @http.route('/pingbase/pingbase/objects/<model("pingbase.pingbase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pingbase.object', {
#             'object': obj
#         })
