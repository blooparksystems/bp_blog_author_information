# -*- coding: utf-8 -*-
{
    'name': "bp_blog_author_information",

    'summary': """
    enables additional blog author information at the end of the blog""",

    'description': """
    enables additional blog author information at the end of the blog""",

    'author': "BLOOPARK SYSTEMS GMBH. & CO. KG",
    'website': "http://www.bloopark.de",

    'category': 'blog',
    'version': '0.1',

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
