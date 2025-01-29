# Módulo de Gestión de Taller Mecánico para Odoo

Este módulo permite gestionar órdenes de servicio para talleres mecánicos, facilitando el seguimiento de vehículos, inventario de piezas, daños y etapas de reparación. Diseñado para Odoo 16, integra funcionalidades clave como flujos de trabajo, control de inventario y vinculación con clientes y vehículos.

---

## Características Principales

### 1. **Gestión de Órdenes de Servicio**
   - Registro de vehículos, clientes y responsables.
   - Seguimiento de etapas (Borrador, Confirmado, En Progreso, Finalizado).
   - Campos automáticos para fechas de ingreso/salida y números de folio.

### 2. **Control de Inventario Vinculado a Vehículos**
   - Ítems de inventario específicos por auto (ej: radio, llanta de repuesto).
   - Estado de disponibilidad para cada ítem.
   - Reutilización de inventario en órdenes recurrentes del mismo vehículo.

### 3. **Registro de Daños**
   - Descripción detallada de daños (ubicación, tipo, severidad).
   - Soporte para imágenes y notas técnicas.

### 4. **Vistas Personalizadas**
   - **Kanban:** Visualización de órdenes por etapas.
   - **Formulario:** Diseño intuitivo con pestañas para inventario y daños.
   - **Tree y Búsqueda:** Filtros rápidos por cliente, vehículo o estado.

### 5. **Integraciones**
   - Vinculación con módulos estándar: `mail`, `stock`, `account`.
   - Compatible con equipos de ventas (`crm.team`).

---

## Requisitos

- Odoo 16 Community o Enterprise.
- Dependencias: `base`, `mail`, `stock`, `account`.

---

## Instalación

1. **Clonar el módulo** en la carpeta `addons` de Odoo:
   ```bash
   git clone [URL del repositorio] ./addons/car_assistance_service