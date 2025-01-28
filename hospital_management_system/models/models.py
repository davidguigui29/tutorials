# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class hospital_management_system(models.Model):
#     _name = 'hospital_management_system.hospital_management_system'
#     _description = 'hospital_management_system.hospital_management_system'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

