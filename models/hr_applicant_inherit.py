from odoo import api, fields, models
from datetime import date, timedelta
from odoo.modules.module import get_module_resource
import base64

class Job(models.Model):

    _inherit = 'hr.applicant'
    _description = "Applicant information"


    fb = fields.Char(string='Facebook', required=False, compute='get_info_personal')
    gender = fields.Selection(
        string='Giới tính',
        selection=[('male', 'Nam'),
                   ('female', 'Nữ'),
                   ('other', 'Khác'),
                ], required=False, compute='get_info_personal')
    date_of_birth = fields.Char(string='Ngày sinh', required=False, compute='get_info_personal')
    street2 = fields.Char(string='Địa chỉ', required=False,compute='get_info_personal')
    city_id = fields.Many2one(
        comodel_name='res.city',
        string='Quận/Huyện',required=False, domain="[('state_id', '=?', state_id)]", compute='get_info_personal')
    state_id = fields.Many2one(
        comodel_name='res.country.state',
        string='Tỉnh/Thành phố', required=False, compute='get_info_personal')
    career_goals = fields.Text(string='Mục tiêu nghề nghiệp', required=False, compute='get_career_goals')
    education = fields.Text(string='Học vấn', required=False, compute='get_education')
    experience = fields.Text(string='Kinh nghiệm làm việc', required=False, compute='get_experience')
    skill = fields.Text(string='Các kĩ năng', required=False, compute='get_skill')
    prize = fields.Text(string='Giải thưởng', required=False, compute='get_prize')

    @api.model
    def _default_image(self):
        image_path = get_module_resource('jobnow', 'static/src/img', 'default_image.png')
        return base64.b64encode(open(image_path, 'rb').read())
    image = fields.Image(default=_default_image, compute='get_image')

    @api.depends("attachment_ids")
    def get_image(self):
        for rec in self:
            for ig in rec.attachment_ids:
                rec.image = ig.datas

    @api.depends("description")
    def get_info_personal(self):
        l = self.description.splitlines(5)
        for rec in self:
            rec.fb = l[3][11:len(l[3])]
            rec.gender = l[4][9:len(l[4])-1]
            rec.date_of_birth = l[5][16:len(l[5])]
            rec.state_id = int(l[6][11:len(l[6])-1])
            rec.city_id = int(l[7][10:len(l[7])-1])
            rec.street2 = l[8][10:len(l[8])-1]
            rec.type_id = int(l[9][12:len(l[9])-1])
            # self.type_id.id = int(l[7][12:len(l[12])-1])
        # if self.description.index('partner_date_of_birth') and self.description.index('\n'):
        #     a = self.description.index('partner_date_of_birth')
        #     b = self.description.index('state_id')
        #     self.date_of_birth = self.description[a+24:b]
        # else:
        #     self.career_goals = " "

    @api.depends("description")
    def get_career_goals(self):
        if self.description.index('career_goals') and self.description.index('experience'):
            a = self.description.index('career_goals')
            b = self.description.index('experience')
            self.career_goals = self.description[a+14:b]
        else:
            self.career_goals = " "

    @api.depends("description")
    def get_experience(self):
        if self.description.index('experience') and self.description.index('education'):
            a = self.description.index('experience')
            b = self.description.index('education')
            self.experience = self.description[a+12:b]
        else:
            self.experience = " "
    @api.depends("description")
    def get_education(self):
        if self.description.index('education') and self.description.index('skill'):
            a = self.description.index('education')
            b = self.description.index('skill')
            self.education = self.description[a+11:b]
        else:
            self.education = " "
    @api.depends("description")
    def get_skill(self):
        if self.description.index('skill') and self.description.index('prize'):
            a = self.description.rindex('skill')
            b = self.description.index('prize')
            self.skill = self.description[a+7:b]
        else:
            self.skill = " "
    @api.depends("description")
    def get_prize(self):
        if self.description.index('prize'):
            a = self.description.rindex('prize')
            b = len(self.description)
            self.prize = self.description[a+7:b]
        else:
            self.prize = " "


class Partner(models.Model):

    _inherit = 'res.partner'

    @api.model
    def _default_image(self):
        if self.company_type == "person":
            image_path = get_module_resource('jobnow', 'static/src/img', 'default_image.png')
        else:
            image_path = get_module_resource('jobnow', 'static/src/img', 'company_image.png')
        return base64.b64encode(open(image_path, 'rb').read())

    image_1920 = fields.Binary(default=_default_image)
    city_id = fields.Many2one(
        comodel_name='res.city',
        string='Quận/Huyện', required=False, domain="[('state_id', '=?', state_id)]", ondelete='restrict')
    state_id = fields.Many2one(
        comodel_name='res.country.state',
        string='Tỉnh/Thành phố', required=False)