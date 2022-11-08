# -*- encoding: utf-8 -*-
{
    "name": "API Rest",
    "version": "1.0.0",
    "sequence": 100,
    "category": "Tools",
    "author": "AHT ASIA",
    "license": 'AGPL-3',
    "description": """
This module provisions you with an API which allows
you to access models through HTTP requests.
Documentation generate with Swagger OpenAPI
Specification - Version 2.0 (https://swagger.io/specification/v2/)

Suggestions & Feedback to: Corentin POUHET-BRUNERIE & Julien DRECQ
    """,
    "depends": [
        'base',
    ],
    "data": [
        # Security
        'security/groups.xml',
        'security/ir.model.access.csv',
        # Views
        'views/api_rest_version_views.xml',
        'views/api_rest_path_views.xml',
        'views/api_rest_tag_views.xml',
        'views/api_rest_log_views.xml',
        'views/swagger_templates.xml',
    ],
    'assets': {
        'smile_api_rest.assets_swagger': [
            'smile_api_rest/static/lib/swagger-ui-3.38.0/swagger-ui.css',
            'smile_api_rest/static/lib/swagger-ui-3.38.0/swagger-ui-bundle.js',
            'smile_api_rest/static/lib/swagger-ui-3.38.0/swagger-ui-standalone-preset.js',
        ],
    },
    "test": [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
