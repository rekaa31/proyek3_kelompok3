# -*- coding: utf-8 -*-
from odoo import http

class Perencanaan(http.Controller):
    @http.route('/perencanaan/perencanaan/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/perencanaan/perencanaan/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('perencanaan.listing', {
            'root': '/perencanaan/perencanaan',
            'objects': http.request.env['perencanaan.perencanaan'].search([]),
        })

    @http.route('/perencanaan/perencanaan/objects/<model("perencanaan.perencanaan"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('perencanaan.object', {
            'object': obj
        })
