from odoo import models, fields, api, _

class OrderServiceCar(models.Model):
    _name = "order.service.car"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Order Service Car"

    # --- Campos Nuevos ---
    customer_id = fields.Many2one(
        comodel_name='res.partner',
        string='Cliente',
        required=True,
        tracking=True
    )
    auto_id = fields.Many2one(
        comodel_name='auto',
        string='Auto',
        required=True,
        tracking=True
    )
    job_title = fields.Char(
        string='Título del Trabajo',
        required=True,
        tracking=True
    )

    # --- Campos Existentes ---
    order_number = fields.Integer(
        string="Número de Folio",
        required=True,
        default=lambda self: self._generate_order_number(),
        readonly=True
    )
    check_in = fields.Date(string="Fecha de Ingreso")
    check_out = fields.Date(string="Fecha de Salida")
    is_towed = fields.Boolean(string="Ingreso en Grúa")
    sales_person_id = fields.Many2one("res.users", string="Responsable")
    notes = fields.Text(string="Observaciones")
    inventory_items_ids = fields.Many2many(
        comodel_name='order.service.car.inventory',
        string='Inventario'
    )
    damage_ids = fields.One2many(
        comodel_name='order.service.car_damage',
        inverse_name='order_id',
        string='Daños'
    )

    # --- Campos de Etapas y Equipos ---
    stage_id = fields.Many2one(
        comodel_name='order.service.stage',
        string='Etapa',
        tracking=True,
        group_expand='_read_group_stage_ids',
        default=lambda self: self._default_stage_id(),
        ondelete='restrict'
    )
    team_id = fields.Many2one(
        comodel_name='crm.team',  # Usar modelo correcto para equipos
        string='Equipo de Ventas',
        check_company=True,
        domain="[('company_id', '=', company_id)]",
        compute='_compute_team_id',  # Campo calculado
        store=True  # Almacenar en la base de datos
    )
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Responsable',
        default=lambda self: self.env.user,
        tracking=True
    )
    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Compañía',
        default=lambda self: self.env.company
    )

    # --- Campos de Tipo y Estado ---
    type = fields.Selection([
        ('reparacion', 'Reparación'),
        ('mantenimiento', 'Mantenimiento')
    ], string='Tipo', required=True, tracking=15, index=True, default='mantenimiento')

    # --- Métodos ---
    @api.model
    def _generate_order_number(self):
        """ Genera un número de folio automático. """
        last_order = self.search([], order='order_number desc', limit=1)
        return (last_order.order_number or 0) + 1

    def _default_stage_id(self):
        """ Obtiene la primera etapa disponible. """
        return self.env['order.service.stage'].search([], limit=1).id

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        """ Expande todas las etapas en la vista Kanban. """
        return self.env['order.service.stage'].search([])

    @api.depends('user_id')
    def _compute_team_id(self):
        """ Asigna el equipo de ventas basado en el usuario responsable. """
        for order in self:
            if order.user_id and order.user_id.sale_team_id:
                order.team_id = order.user_id.sale_team_id
            else:
                order.team_id = False
    inventory_items_ids = fields.Many2many(
    comodel_name='auto.inventory.item',
    relation='order_service_car_inventory_rel',  # Nombre de la tabla intermedia
    column1='order_id',  # Columna que referencia a order.service.car
    column2='inventory_item_id',  # Columna que referencia a auto.inventory.item
    string='Ítems de Inventario'
    )

    # --- Métodos ---
    @api.depends('auto_id')
    def _compute_inventory_items(self):
        """ Calcula los ítems de inventario basados en el auto seleccionado. """
        for order in self:
            if order.auto_id:
                order.inventory_items_ids = order.auto_id.inventory_items_ids
            else:
                order.inventory_items_ids = False
    # En el modelo order.service.car
    @api.onchange('auto_id')
    def _onchange_auto_id(self):
        if self.auto_id:
            self.inventory_items_ids = self.auto_id.inventory_items_ids
        else:
            self.inventory_items_ids = False