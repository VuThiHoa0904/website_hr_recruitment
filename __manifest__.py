# -*- coding: utf-8 -*-
{
    'name': "Website tuyển dụng",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'website_hr_recruitment',
                'website',
                'website_partner',
                'hr_recruitment',
                'website_mail',
                'website_form'],

    # always loaded
    'data': [
        # 'views/views.xml',
        'views/list_job_view.xml',
        'views/job_inherit.xml',
        'security/group_user.xml',
        'security/ir.model.access.csv',
        # 'security/record_rule.xml',
        'views/hr_applicant_view.xml',
        'views/res_partner_inherit.xml',
        'report/cv_application.xml',
        'browser/add_lib_fontend.xml',

        'data/config_data.xml',
        'views/website_hr_recruitment_templates.xml',
        'views/hr_recruitment_views.xml',
        'views/hr_job_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
