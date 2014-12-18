# -*- coding: utf-8 -*-
from openerp.models import Model


class BlogPost(Model):
    '''
    inheriting the BlogPost to wirte additional functions for the blog post author information
    '''
    _inherit = "blog.post"

    def get_employee_notes(self):
        '''
        we need to get the employee object to get the note information located in this object.
        the object author_id has no field called notes

        :return notes:
        '''
        notes = ''
        employees = self.env['hr.employee'].search([('address_id', '=', self.author_id.id)])
        if employees:
            notes = employees[0].notes
        return notes

    def get_social_links(self, partner):
        '''
        QWebException: "('AccessError', u'The requested operation cannot be completed due to security restrictions.
        Please contact your system administrator.\n\n(Document type: res.partner, Operation: read)')"

        Cannot read the social links from res partner through the author id, therefore we have to create this function
        to get all social links in a dictionary

        :param partner:
        :return social_links_dict:
        '''

        res_partner = self.env['res.partner'].sudo().browse(partner.id)
        social_links_dict = {}
        if res_partner[0].linkedin:
            social_links_dict['linkedin'] = res_partner[0].linkedin
        if res_partner[0].behance:
            social_links_dict['behance'] = res_partner[0].behance
        if res_partner[0].dribbble:
            social_links_dict['dribbble'] = res_partner[0].dribbble
        if res_partner[0].github:
            social_links_dict['github'] = res_partner[0].github
        if res_partner[0].google_plus:
            social_links_dict['google-plus-square'] = res_partner[0].google_plus
        if res_partner[0].facebook:
            social_links_dict['facebook'] = res_partner[0].facebook
        if res_partner[0].twitter:
            social_links_dict['twitter'] = res_partner[0].twitter

        return social_links_dict

    def get_author_image(self, partner):
        '''
        QWebException: "('AccessError', u'The requested operation cannot be completed due to security restrictions.
        Please contact your system administrator.\n\n(Document type: res.partner, Operation: read)')"

        Cannot read the image from res partner through the author id, therefore we have to create this function
        to get all images

        :param partner:
        :return res_partner_image:
        '''

        res_partner = self.env['res.partner'].sudo().browse(partner.id)
        res_partner_image = res_partner[0].image


        return res_partner_image