# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2014 Elico Corp All Rights Reserved.
#                       lin.yu@elico-corp.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
	'name': 'Portal Partner Assign',
	'version': '0.1',
	'category': 'Stock',
	'description': """ENG: This module allows accoutant to assign portal user
	""",
	'author': 'www.elico-corp.com',
	'website': 'http://www.elico-corp.com',
	'depends': [],
	'depends': ['portal'],
	'data': [
		'partner_view.xml',
		],
	'installable': True,
	'active': False,
	'images' : [],
}

