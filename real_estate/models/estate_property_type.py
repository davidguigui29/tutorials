# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Property types model"

    # partner_id = fields.Many2one("res.partner", string="Partner")
    name = fields.Char(required=True)
