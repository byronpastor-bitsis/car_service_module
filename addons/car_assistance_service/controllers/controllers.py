# -*- coding: utf-8 -*-
# from odoo import http


# class CarAssistanceService(http.Controller):
#     @http.route('/car_assistance_service/car_assistance_service', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/car_assistance_service/car_assistance_service/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('car_assistance_service.listing', {
#             'root': '/car_assistance_service/car_assistance_service',
#             'objects': http.request.env['car_assistance_service.car_assistance_service'].search([]),
#         })

#     @http.route('/car_assistance_service/car_assistance_service/objects/<model("car_assistance_service.car_assistance_service"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('car_assistance_service.object', {
#             'object': obj
#         })
