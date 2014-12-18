# -*- coding: utf-8 -*-
{
    'name': "Blog extended Author Information",

    'summary': """
    enables additional blog author information at the end of the blog""",

    'description': """
    enables additional blog author information at the end of the blog""",

    'author': "bloopark systems GmbH & Co. KG",
    'website': "http://www.bloopark.de",

    'category': 'blog',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'website_blog',
        'bp_8_0_social_media_for_res_partner'
    ],

    # always loaded
    'data': [
        'views/blog_post.xml'
    ],
}
