from odoo import api, fields, models


class HospitalPatient(models.Model):
    _inherit = "sale.order"

    description = fields.Text(string='Description')