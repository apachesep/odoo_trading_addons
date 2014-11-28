# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2012 Andrea Cometa All Rights Reserved.
#                       www.andreacometa.it
#                       openerp@andreacometa.it
#    Copyright (C) 2013 Agile Business Group sagl (<http://www.agilebg.com>)
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

from osv import osv, fields, orm
from openerp import SUPERUSER_ID
from openerp.tools.translate import _
from openerp.tools import email_split

# (note that calling '_' has no effect except exporting those strings for translation)
WELCOME_EMAIL_SUBJECT = _("Your OpenERP account at %(company)s")
WELCOME_EMAIL_BODY = _("""Dear %(name)s,

You have been given access to %(portal)s.

Your login account data is:
Database: %(db)s
Username: %(login)s

In order to complete the signin process, click on the following url:
%(url)s

%(welcome_message)s

--
Elico - HK Trading ERP
http://www.elico-corp.com
""")


class res_partner(orm.Model):
    _inherit = 'res.partner'

    _columns = {
        'portal': fields.boolean('Portal?', help="this partner has portal access or not")
    }


class wizard_user(osv.osv_memory):
    _inherit = 'portal.wizard.user'

    def action_apply(self, cr, uid, ids, context=None):
        """
            CAN NOT SUPER original,
            because value is updatd during process
        """
        for wizard_user in self.browse(cr, SUPERUSER_ID, ids, context):
            portal = wizard_user.wizard_id.portal_id
            user = self._retrieve_user(cr, SUPERUSER_ID, wizard_user, context)
            if wizard_user.in_portal:
                # create a user if necessary, and make sure it is in the portal group
                if not user:
                    user = self._create_user(cr, SUPERUSER_ID, wizard_user, context)
                if (not user.active) or (portal not in user.groups_id):
                    user.write({'active': True, 'groups_id': [(4, portal.id)]})
                    # prepare for the signup process
                    user.partner_id.signup_prepare()
                    wizard_user = self.browse(cr, SUPERUSER_ID, wizard_user.id, context)
                    self._send_email(cr, uid, wizard_user, context)
                    # LY 141128 
                    partner = wizard_user.partner_id
                    wizard_user.partner_id.write({'portal': True})
                    # LY end
            else:
                # remove the user (if it exists) from the portal group
                if user and (portal in user.groups_id):
                    # if user belongs to portal only, deactivate it
                    if len(user.groups_id) <= 1:
                        user.write({'groups_id': [(3, portal.id)], 'active': False})
                    else:
                        user.write({'groups_id': [(3, portal.id)]})
                    # LY 141128 
                    partner = wizard_user.partner_id
                    wizard_user.partner_id.write({'portal': False})
                    # LY end

    def _send_email(self, cr, uid, wizard_user, context=None):
        """
            CAN NOT SUPER original,
            because original does not return any value
        """
        """ send notification email to a new portal user
            @param wizard_user: browse record of model portal.wizard.user
            @return: the id of the created mail.mail record
        """
        this_context = context
        this_user = self.pool.get('res.users').browse(cr, SUPERUSER_ID, uid, context)
        if not this_user.email:
            raise osv.except_osv(_('Email Required'),
                _('You must have an email address in your User Preferences to send emails.'))

        # determine subject and body in the portal user's language
        user = self._retrieve_user(cr, SUPERUSER_ID, wizard_user, context)
        context = dict(this_context or {}, lang=user.lang)
        data = {
            'company': this_user.company_id.name,
            'portal': wizard_user.wizard_id.portal_id.name,
            'welcome_message': wizard_user.wizard_id.welcome_message or "",
            'db': cr.dbname,
            'name': user.name,
            'login': user.login,
            'url': user.signup_url,
        }
        mail_mail = self.pool.get('mail.mail')
        mail_values = {
            'email_from': this_user.email,
            'email_to': user.email,
            'subject': _(WELCOME_EMAIL_SUBJECT) % data,
            'body_html': '<pre>%s</pre>' % (_(WELCOME_EMAIL_BODY) % data),
            'state': 'outgoing',
            'type': 'email',
        }
        mail_id = mail_mail.create(cr, uid, mail_values, context=this_context)
        # LY 141128 write message
        # write message_post
        partner_obj = self.pool.get('res.partner')
        partner_obj.message_post(
            cr, uid, [wizard_user.partner_id.id], body=mail_values['body_html'], context=context)
        # LY 141128 END
        return mail_mail.send(cr, uid, [mail_id], context=this_context)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
