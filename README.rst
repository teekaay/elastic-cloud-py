Python Elastic Cloud (Enterprise) Client
========================================

.. image:: https://travis-ci.org/teekaay/elastic-cloud-py.svg?branch=master
    :target: https://travis-ci.org/teekaay/elastic-cloud-py

.. image:: https://readthedocs.org/projects/elastic-cloud-py/badge/?version=latest
    :target: http://elastic-cloud-py.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Python client for `Elastic Cloud <https://www.elastic.co/cloud>`_. Its goal is to provide
an abstraction for all Elastic Cloud related API operations. 
To get more information about the Elastic Cloud API, visit `this <https://www.elastic.co/guide/en/cloud-enterprise/current/ece-api-reference.html>`_
link.

The main motiviation is to aid in building a solid foundation for building tooling
around Elastic Cloud without having to write a client again and again.

``elastic_cloud`` comes with a basic command line interface. after installation, run ``elastic-cloud --help``
to get information about the usage.

.. note::

    We will refer to the product `Elastic Cloud Enterprise` as to `Elastic Cloud` in the following.
    Note that there is a difference between the hosted (SaaS) and the enterprise (on-promise) variant.

Contents
--------

.. toctree::
   :maxdepth: 2

   api
   Changelog

Compatibility
-------------

The library is compatible with the following Elastic Cloud API versions

- 1.0 (Elastic Cloud Enterprise)
- 1.1 (Elastic Cloud Enterprise)

and with the following Python versions

- 3.x

Installation
------------

Install the ``elastic_cloud`` package with one of the following methods:

Using ``git`` (uses the current master)

::

    git clone https://github.com/teekaay/elastic-cloud-py.git
    cd elastic-cloud-py
    python setup.py install

Using ``pip`` 

::

    pip install elastic-cloud

or, for the latest development version
  
::
    
    pip install https://github.com/teekaay/elastic-cloud-py/archive/master.zip

Example Usage 
-------------

The main entrypoint for library users should be :class:`~elastic_cloud.ElasticCloud` which
contains all sub-clients.

::

    >>> from elastic_cloud import ElasticCloud
    # we will connect to localhost:12443 by default
    >>> ec = ElasticCloud()
    # return values are requests objects
    >>> platform_info = ec.platform.get_platform_info()
    >>> print(platform_info.json())
    {'eula_accepted': True, 'phone_home'enabled': True, 'services': [...], 'version': '<platform-version>'}

Features
--------

This library is a very thin layer above the raw Elastic Cloud REST API. Basically, it 
provides methods that do HTTP calls without any error handling or (de)serializing apart
from what the underlying HTTP client does. Therefor it is suitable for building higher-level
clients on top of ``elastic_cloud``. 

``elastic_cloud`` contains multiple sub-clients which are all contained in the main :class:`~elastic_cloud.ElasticCloud`
class. These are

* :class:`~elastic_cloud.client.PlatformClient`
* :class:`~elastic_cloud.client.PlatformAllocatorClient`
* :class:`~elastic_cloud.client.StackClient`
* :class:`~elastic_cloud.client.PlatformClient`
* :class:`~elastic_cloud.client.ElasticsearchClusterClient`
* :class:`~elastic_cloud.client.KibanaClusterClient`

Each client contains a subset of API calls which are logically separated and can execute the operations described in the section of the 
`API documentation <https://www.elastic.co/guide/en/cloud-enterprise/current/ece-api-reference.html>`_ 

API Call Responses
-------------------

All clients in ``elastic_cloud`` return their result as a ``requests`` result object.
Therefor, they have (among others) two common ways of handling them

::

    >>> get_platform_info_result = ec.platform.get_platform_info()
    >>> print(get_platform_info_result.status_code)
    >>> 200
    >>> print(get_platform_info_result.json())
    {'eula_accepted': True, 'phone_home'enabled': True, 'services': [...], 'version': '<platform-version>'}

Development
-----------

Testing
~~~~~~~~

To run all unit tests 

::

    make test

Currently no integration or functional tests are implemented.

Building 
~~~~~~~~

To build all artifacts (docs and the distribution), run 

::

    make dist
    make docs


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`