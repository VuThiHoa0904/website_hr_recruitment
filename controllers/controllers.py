# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.portal.controllers.web import Home
from odoo.http import request

class Website(Home):
    # @http.route('/jobnow/jobnow/', auth='public')
    # def index(self, **kw):
    #     return "Hello, world"
    #
    # @http.route('/jobnow/jobnow/objects/', auth='public')
    # def list(self, **kw):
    #     return http.request.render('jobnow.listing', {
    #         'root': '/jobnow/jobnow',
    #         'objects': http.request.env['jobnow.jobnow'].search([]),
    #     })
    #
    # @http.route('/jobnow/jobnow/objects/<model("jobnow.jobnow"):obj>/', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('jobnow.object', {
    #         'object': obj
    #     })
    @http.route('/', type='http', auth="public", website=True)
    def index(self, **kw):
        jobs = http.request.env['hr.job']
        return request.render({
            'jobs':  jobs.sudo().search([])
        })
        homepage = request.website.homepage_id
        if homepage and (homepage.sudo().is_visible or request.env.user.has_group('base.group_user')) and homepage.url != '/':
            return request.env['ir.http'].reroute(homepage.url)

        website_page = request.env['ir.http']._serve_page()
        if website_page:
            return website_page
        else:
            top_menu = request.website.menu_id
            first_menu = top_menu and top_menu.child_id and top_menu.child_id.filtered(lambda menu: menu.is_visible)
            if first_menu and first_menu[0].url not in ('/', '', '#') and (not (first_menu[0].url.startswith(('/?', '/#', ' ')))):
                return request.redirect(first_menu[0].url)
        raise request.not_found()
