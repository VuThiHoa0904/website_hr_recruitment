from werkzeug import urls

from odoo import api, fields, models
from odoo.tools.translate import html_translate

class Job(models.Model):

    _inherit = 'res.company'
    _description = "Job Position"
    _inherit = ['mail.thread']
