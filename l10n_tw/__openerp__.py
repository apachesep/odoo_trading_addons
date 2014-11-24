# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright Elico (C) 2014 LIN Yu(<lin.yu@elico-corp.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': '台湾会计科目表 - Accounting',
    'version': '0.1',
    'category': 'Localization/Account Charts',
    'author': 'www.elico-corp.com',
    'maintainer':'lin.yu@elico-corp.com',
    'website':'http://elico-corp.com',
    'description': """

    科目类型\会计科目表模板\增值税\辅助核算类别\管理会计凭证簿\财务会计凭证簿

    
    """,
    'depends': ['base','account'],
    'demo': [],
    'data': [
        'account_tax.xml',
        'account_chart_type.xml',
        'account_chart_template.xml',
        'l10n_chart_tw_wizard.xml',
    ],
    'license': 'GPL-3',
    'auto_install': False,
    'installable': True,
    'images': ['images/config_chart_l10n_tw.jpeg','images/l10n_tw_chart.jpeg'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
