
from odoo import api, fields, models

# model for practice appform
class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "patient profile"

    name = fields.Char(string='Name', required=True)

    age = fields.Integer(string='Age')

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male',)

    note = fields.Text(string='Description')
