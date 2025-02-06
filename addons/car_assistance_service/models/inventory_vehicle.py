# -*- coding: utf-8 -*-
from odoo import models, fields, _

class AutoInventoryItem(models.Model):
    _name = "auto.inventory.item"
    _description = "Ítem de Inventario del Auto"
    order_id = fields.Many2one(
    comodel_name='order.service.car',
    string='Orden de Servicio'
    )
    auto_id = fields.Many2one(
        comodel_name='auto',
        string='Auto',
        required=True,
        ondelete='cascade'
    )
    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Producto',
        required=True
    )
    is_available = fields.Boolean(
        string='Disponible',
        default=True
    )
    description = fields.Text(string='Descripción')
    