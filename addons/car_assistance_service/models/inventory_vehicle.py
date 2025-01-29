# -*- coding: utf-8 -*-
from odoo import models, fields, _

class AutoInventoryItem(models.Model):
    _name = "auto.inventory.item"
    _description = "Ítem de Inventario del Auto"

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