from odoo import api, fields, models


class Stage(models.Model):
    _name = "order.service.stage"
    _description = "Order Service Stages"
    _order = "sequence, id"

    name = fields.Char('Stage Name', required=True)
    sequence = fields.Integer(default=10)
    fold = fields.Boolean('Folded in Kanban')
    is_done = fields.Boolean('Stage Done')
    # Corregir prioridades
    priority = fields.Selection(
        [('0', 'Very Low'),
         ('1', 'Low'),
         ('2', 'Medium'),
         ('3', 'High'),
         ('4', 'Very High')],
        'Priority'
    )
