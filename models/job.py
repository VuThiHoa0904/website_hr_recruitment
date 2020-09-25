from odoo import api, fields, models

class Job(models.Model):

    _inherit = 'hr.job'
    _description = "Job Position"

    image_logo = fields.Binary(string="Image", compute='get_logo_company')

    @api.depends('address_id')
    def get_logo_company(self):
        for rec in self:
            rec.image_logo = rec.address_id.image_1920


