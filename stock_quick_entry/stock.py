# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-2013 Elico Corp. All Rights Reserved.
#    Author: Andy Lu <andy.lu@elico-corp.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it wil    l be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import orm


class StockMove(orm.Model):
    _inherit = 'stock.move'

    def product_id_change(self, cr, uid, ids, product, location_id, location_dest_id, date_expected,
                          context=None):
        context = context or {}
        result = {}

        product_obj = self.pool.get('product.product').browse(cr, uid, product, context=context)
        if product_obj and product_obj.uom_id:
            result.update({
                'product_uom': product_obj.uom_id.id,
                'name': product_obj.name,
                'location_id': location_id,
                'location_dest_id': location_dest_id,
                'date_expected': date_expected
            })
        return {'value': result}
