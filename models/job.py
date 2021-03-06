from odoo import api, fields, models
from datetime import date, timedelta

class Job(models.Model):

    _inherit = 'hr.job'
    _description = "Job Position"

    # user_id = fields.Many2one('res.users', string='', index=True, compute="get_user",
    #                           track_visibility='onchange', track_sequence=2, default=lambda self: self.env.user)
    image_logo = fields.Binary(string="Image", compute='get_logo_company')
    # def get_user(self):
    #     context = self._context
    #     current_uid = context.get('uid')
    #     self.user_id = self.env['res.users'].browse(current_uid)

    gender = fields.Selection(
        string='Yêu cầu giới tính',
        selection=[('nam', 'Nam'),
                   ('nu', 'Nữ'),
                   ('none', 'Không yêu cầu'),],
        required=False, default='none')
    date_submit = fields.Date(
        string='Hạn nộp hồ sơ',
        required=False)
    area_id = fields.Many2many(
        comodel_name='hr.list_job',
        string='Lĩnh vực',
        required=False)

    work_level_id = fields.Many2one(
        comodel_name='hr.work_level',
        string='Yêu cầu cấp bậc',
        required=False)

    type_of_work_id = fields.Many2one(
        comodel_name='hr.type_of_work',
        string='Loại hình công việc',
        required=False)

    experience_id = fields.Many2one(
        comodel_name='hr.experience',
        string='Yêu cầu kinh nghiệm',
        required=False)

    academic_level_id = fields.Many2one(
        comodel_name='hr.academic_level',
        string='Yêu cầu trình độ',
        required=False)

    wage_id = fields.Many2one(
        comodel_name='hr.wage',
        string='Mức lương',
        required=False)

    job_requirement = fields.Html(
        string='Yêu cầu công việc',
        required=False)

    vested_interest = fields.Html(
        string='Quyền lợi được hưởng',
        required=False)

    description = fields.Html(
        string='Mô tả công việc',
        required=False)

    flash_job = fields.Boolean(string='Flash Job', default=False)
    job_hurry = fields.Boolean( string='Việc tuyển gấp', required=False)
    attractive_job = fields.Boolean( string='Việc hấp dẫn', required=False)

    @api.depends('address_id')
    def get_logo_company(self):
        for rec in self:
            rec.image_logo = rec.address_id.image_1920

    # @api.depends("date_submit")
    # def get_flash_job(self):
    #     current_dt = date.today()
    #     for rec in self:
    #         if rec.date_submit:
    #             end = rec.date_submit
    #             date_calc = ((end - current_dt).days / 60)
    #             print("+++===========")
    #             print(date_calc)
    #             # Age should be greater than 0
    #             if date_calc > 0:
    #                 rec.flash_job = True
    #             else:
    #                 rec.flash_job = False


