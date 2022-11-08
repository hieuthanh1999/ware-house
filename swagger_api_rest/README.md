==============
SWAGGER API Rest
==============

This module provisions you with an API which allows you to access models through HTTP requests.

Documentation generate with Swagger OpenAPI Specification - Version 2.0 (https://swagger.io/specification/v2/)

**Table of contents**

.. contents::
   :local:


Requirements
============

There are no requirements to use this module.


Usage
=====

Documentation URIs
------------------
============================================== ==============================================
URI                                            Description
============================================== ==============================================
`/<api-docs>/v<api_version>`                   API Documentation (generate with swagger)
`/<api-docs>/v<api_version>/swagger.json`      Json Swagger
============================================== ==============================================


API URIs
--------
============================================== ======= ===============================================================
URI                                            Method  Description
============================================== ======= ===============================================================
`/<api>/v<api_version>/<api_name>`             GET     Read all (with optional domain, fields, offset, limit, order)
`/api/v<api_version>/<api_name>/<id>`          GET     Read one (with optional fields)
`/api/v<api_version>/<api_name>`               POST    Create a record
`/api/v<api_version>/<api_name>/<id>`          PUT     Update a record
`/api/v<api_version>/<api_name>/<id>`          DELETE  Delete a record
`/api/v<api_version>/<api_name>/custom`        PUT     Call method (with optional parameters)
`/api/v<api_version>/<api_name>/custom/<id>`   PUT     Call method on record (with optional parameters)
============================================== ======= ===============================================================

Error response
--------------

.. code-block::

    {
        'code': <code>  # Error code,
        'error': <error>  # Error name,
        'description': <description>  # Description of the error,
    }
