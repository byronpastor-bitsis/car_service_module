# -*- coding: utf-8 -*-
from odoo import models, fields, _

class Auto(models.Model):
    _name = "auto"
    _description = "Auto"

    brand = fields.Char(string="Marca")
    model = fields.Char(string="Modelo")
    plate = fields.Char(string="Placa")
    line = fields.Char(string="Línea")
    color = fields.Char(string="Color")
    engine = fields.Char(string="Motor")
    type = fields.Char(string="Tipo")
    inventory_items_ids = fields.One2many(
        comodel_name='auto.inventory.item',
        inverse_name='auto_id',
        string='Ítems de Inventario'
    )