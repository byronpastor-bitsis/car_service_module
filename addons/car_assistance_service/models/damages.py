# -*- coding: utf-8 -*-
from odoo import models, fields, _  # type: ignore

class OrderServiceCarDamage(models.Model):
    _name = "order.service.car_damage"
    _description = "Vehicle Damage"
       
    order_id = fields.Many2one("order.service.car", string=_("Order of service"), required=True)
    location = fields.Char(string=_("Location of damage"), required=True)
    damage_type = fields.Many2one("order.service.damage_type", string=_("Type of damage"), required=True)
    damage_severity = fields.Many2one("order.service.damage_severity", string=_("Damage severity"), required=True)
    description = fields.Text(string=_("Description"))
    image = fields.Binary(string=_("Image"), help=_("Select image here"))
    create_date = fields.Datetime(string=_("Creation date"), readonly=True)
    write_date = fields.Datetime(string=_("modification date"), readonly=True)

class DamageType(models.Model):
    _name = "order.service.damage_type"
    _description = "damage type"
    
    name = fields.Char(string=_("Name"), required=True)
    description = fields.Text(string=_("description"))
    _sql_constraints = [
        ('unique_name', 'unique(name)', 'El nombre del tipo de daño debe ser único!')
    ]

class DamageSeverity(models.Model):
    _name = "order.service.damage_severity"
    _description = "damage severity"
    
    name = fields.Char(string=_("Name"), required=True)
    _sql_constraints = [
        ('unique_name', 'unique(name)', 'La severidad del daño debe ser única!')
    ]

