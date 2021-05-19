from odoo import fields, models, api


class ListJob(models.Model):
    _name = 'hr.list_job'
    _description = 'Description'

    name = fields.Char("Tên ngành")

class WorkLevel(models.Model):
    _name = 'hr.work_level'
    _description = 'Description'

    name = fields.Char("Tên cấp bậc")

class TypeOfWork(models.Model):
    _name = 'hr.type_of_work'
    _description = 'Description'

    name = fields.Char("Loại hình công việc")

class Experience(models.Model):
    _name = 'hr.experience'
    _description = 'Description'

    name = fields.Char("Kinh nghiêm")

class AcademicLevel(models.Model):
    _name = 'hr.academic_level'
    _description = 'Description'

    name = fields.Char("Trình độ")

class Wage(models.Model):
    _name = 'hr.wage'
    _description = 'Description'

    name = fields.Char("Mức lương")

