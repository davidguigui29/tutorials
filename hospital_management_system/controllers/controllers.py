# -*- coding: utf-8 -*-
# from odoo import http


# class HospitalManagementSystem(http.Controller):
#     @http.route('/hospital_management_system/hospital_management_system', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital_management_system/hospital_management_system/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital_management_system.listing', {
#             'root': '/hospital_management_system/hospital_management_system',
#             'objects': http.request.env['hospital_management_system.hospital_management_system'].search([]),
#         })

#     @http.route('/hospital_management_system/hospital_management_system/objects/<model("hospital_management_system.hospital_management_system"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital_management_system.object', {
#             'object': obj
#         })

