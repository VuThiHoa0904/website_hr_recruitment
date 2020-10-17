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
    def sitemap_jobs(env, rule, qs):
        if not qs or qs.lower() in '/jobs':
            yield {'loc': '/jobs'}

    @http.route([
        '/jobs',
        '/jobs/country/<model("res.country"):country>',
        '/jobs/department/<model("hr.department"):department>',
        '/jobs/country/<model("res.country"):country>/department/<model("hr.department"):department>',
        '/jobs/office/<int:office_id>',
        '/jobs/country/<model("res.country"):country>/office/<int:office_id>',
        '/jobs/department/<model("hr.department"):department>/office/<int:office_id>',
        '/jobs/country/<model("res.country"):country>/department/<model("hr.department"):department>/office/<int:office_id>',
    ], type='http', auth="public", website=True, sitemap=sitemap_jobs)
    def jobs(self, country=None, department=None, office_id=None, **kwargs):
        env = request.env(context=dict(request.env.context, show_address=True, no_tag_br=True))

        Country = env['res.country']
        Jobs = env['hr.job']

        # List jobs available to current UID
        domain = request.website.website_domain()
        job_ids = Jobs.search(domain, order="is_published desc, no_of_recruitment desc").ids
        # Browse jobs as superuser, because address is restricted
        jobs = Jobs.sudo().browse(job_ids)

        # Default search by user country
        if not (country or department or office_id or kwargs.get('all_countries')):
            country_code = request.session['geoip'].get('country_code')
            if country_code:
                countries_ = Country.search([('code', '=', country_code)])
                country = countries_[0] if countries_ else None
                if not any(j for j in jobs if j.address_id and j.address_id.country_id == country):
                    country = False

        # Filter job / office for country
        if country and not kwargs.get('all_countries'):
            jobs = [j for j in jobs if
                    j.address_id is None or j.address_id.country_id and j.address_id.country_id.id == country.id]
            offices = set(j.address_id for j in jobs if
                          j.address_id is None or j.address_id.country_id and j.address_id.country_id.id == country.id)
        else:
            offices = set(j.address_id for j in jobs if j.address_id)

        # Deduce departments and countries offices of those jobs
        departments = set(j.department_id for j in jobs if j.department_id)
        countries = set(o.country_id for o in offices if o.country_id)

        if department:
            jobs = [j for j in jobs if j.department_id and j.department_id.id == department.id]
        if office_id and office_id in [x.id for x in offices]:
            jobs = [j for j in jobs if j.address_id and j.address_id.id == office_id]
        else:
            office_id = False

        # Render page
        return request.render("website_hr_recruitment.index", {
            'jobs': jobs,
            'countries': countries,
            'departments': departments,
            'offices': offices,
            'country_id': country,
            'department_id': department,
            'office_id': office_id,
        })

    @http.route('''/jobs/detail/<model("hr.job", "[('website_id', 'in', (False, current_website_id))]"):job>''',
                type='http', auth="public", website=True)
    def jobs_detail(self, job, **kwargs):
        jobs = http.request.env['hr.job'].sudo().search([['area_id', 'in', job.area_id.id]])
        if not job.can_access_from_current_website():
            raise NotFound()

        return request.render("website_hr_recruitment.detail", {
            'job': job,
            'jobs': jobs,
            'main_object': job,
        })

    @http.route('/jobs/search', type='http', auth="public", website=True)
    def jobs_search(self, **kwargs):
        job_name = kwargs.get('job_name')
        jobs = http.request.env['hr.job'].sudo().search([['name', 'ilike', job_name]])
        # if not job.can_access_from_current_website():
        #     raise NotFound()

        return request.render("website.jobs-search", {
            # 'job': jobs,
            'jobs': jobs,
            # 'main_object': job,
        })

    @http.route('/', type='http', auth="public", website=True)
    def index(self, **kw):
        jobs = http.request.env['hr.job']
        companys = http.request.env['res.partner']
        return request.render("website.homepage",{
            'jobs': jobs.sudo().search([]),
            'companys': companys.sudo().search([])
        })
        # homepage = request.website.homepage_id
        # if homepage and (homepage.sudo().is_visible or request.env.user.has_group('base.group_user')) and homepage.url != '/':
        #     return request.env['ir.http'].reroute(homepage.url)
        #
        # website_page = request.env['ir.http']._serve_page()
        # if website_page:
        #     return website_page
        # else:
        #     top_menu = request.website.menu_id
        #     first_menu = top_menu and top_menu.child_id and top_menu.child_id.filtered(lambda menu: menu.is_visible)
        #     if first_menu and first_menu[0].url not in ('/', '', '#') and (not (first_menu[0].url.startswith(('/?', '/#', ' ')))):
        #         return request.redirect(first_menu[0].url)
        # raise request.not_found()
