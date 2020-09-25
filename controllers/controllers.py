# -*- coding: utf-8 -*-
# from odoo import http


# class Jobnow(http.Controller):
#     @http.route('/jobnow/jobnow/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jobnow/jobnow/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('jobnow.listing', {
#             'root': '/jobnow/jobnow',
#             'objects': http.request.env['jobnow.jobnow'].search([]),
#         })

#     @http.route('/jobnow/jobnow/objects/<model("jobnow.jobnow"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jobnow.object', {
#             'object': obj
#         })
