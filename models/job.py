from odoo import api, fields, models

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
        required=False,)
    date_submit = fields.Date(
        string='Hạn nộp hồ sơ',
        required=False)
    area_id = fields.Many2many(
        comodel_name='jobnow.list_job',
        string='Lĩnh vực',
        required=False)

    work_level_id = fields.Many2one(
        comodel_name='jobnow.work_level',
        string='Yêu cầu cấp bậc',
        required=False)

    type_of_work_id = fields.Many2one(
        comodel_name='jobnow.type_of_work',
        string='Loại hình công việc',
        required=False)

    experience_id = fields.Many2one(
        comodel_name='jobnow.experience',
        string='Yêu cầu kinh nghiệm',
        required=False)

    academic_level_id = fields.Many2one(
        comodel_name='jobnow.academic_level',
        string='Yêu cầu trình độ',
        required=False)

    wage_id = fields.Many2one(
        comodel_name='jobnow.wage',
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

    @api.depends('address_id')
    def get_logo_company(self):
        for rec in self:
            rec.image_logo = rec.address_id.image_1920


