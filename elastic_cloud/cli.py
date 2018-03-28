#!/usr/bin/env python

import argparse
import logging
import sys
import json
import jmespath
from textwrap import dedent
from urllib.parse import urlparse
from elastic_cloud.client import ApiDocsClient
from elastic_cloud.client import ElasticsearchClusterClient
from elastic_cloud.client import KibanaClusterClient
from elastic_cloud.client import StackClient
from elastic_cloud.client import PlatformClient
from elastic_cloud.client import PlatformAllocatorClient
from elastic_cloud.client import ElasticCloudSession
from elastic_cloud import __versionstr__

DESCRIPTION = """
Command-line interface for Elastic Cloud.

Examples:

    List all actions for elasticsearch clusters:

    $ elastic-cloud --list-actions --format json --query 'actions[?starts_with(name, `elasticsearch-cluster::`)]'

    Get the API documentation in swagger format

    $ elastic-cloud --client api-docs --action get-api-docs --user myuser --password mypassword

For more information, visit https://elastic.co/guide/en/cloud-enterprise/current/ece-api-reference.html
"""

EPILOG = """
Contribute to elastic-cloud!
    https://github.com/teekaay/elastic-cloud-py
"""

LOG = logging.getLogger('elastic-cloud.cli')

clients = {
    'api-docs': ApiDocsClient,
    'elasticsearch-cluster': ElasticsearchClusterClient,
    'kibana-cluster': KibanaClusterClient,
    'platform': PlatformClient,
    'stacks': StackClient,
    'allocator': PlatformAllocatorClient
}

def init_logging(level='warn'):
    logging.basicConfig(
        level=level,
        format='[%(asctime)s] %(levelname)-8s %(module)-8s %(message)s'
    )

from types import FunctionType

def methods(cls, exclude=[]):
    cls_methods = []
    for x, y in cls.__dict__.items():
        if type(y) == FunctionType and not x.startswith('_') and x not in exclude:
            cls_methods.append({'name': x, 'doc': y.__doc__})
    return cls_methods

def method_to_action(m):
    return m.replace('_', '-')

def action_to_method(a):
    return a.replace('-', '_')

def finalize_result(result, query=None):
    if query:
        return jmespath.search(result, query)
    else:
        return result

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description=dedent(DESCRIPTION),
        epilog=dedent(EPILOG)
    )

    parser.add_argument('--endpoint', type=str, default='https://localhost:12443',
        help='the elastic cloud endpoint')
    parser.add_argument('--user', type=str,
        help='the user to authorize with')
    parser.add_argument('--password', type=str,
        help='the password to authorize with')
    parser.add_argument('--query',
        help='jmespath expression to filter the output')
    parser.add_argument('--body', 
        help='path to a file or raw body')
    parser.add_argument('--list-actions',
        action='store_true',
        help='list all available actions')
    parser.add_argument('--format',
        choices=('json', 'text'),
        help='output format for list-actions',
        default='json'
    )
    parser.add_argument('--debug', action='store_true',
        help='enable verbose logging')
    parser.add_argument('--client',
        choices=[k for k in clients.keys()], 
        help='use an elastic cloud client')
    parser.add_argument('--action', 
        help='execute an api action')
    parser.add_argument('--version',
        action='store_true',
        help='show version')

    args = parser.parse_args()

    if args.version:
        print(__versionstr__)
        return

    action_pairs = []
    for client_name, client_cls in clients.items():
        client_methods = methods(client_cls)
        client_methods = [{'name': method_to_action(m['name']), 'doc': m['doc'] } for m in client_methods]
        for m in client_methods:
            action_pairs.append({'name': '{}::{}'.format(client_name, m['name']), 'doc': m['doc'] })

    print(args)

    if args.list_actions:
        action_pairs = { 'actions': action_pairs }
        if args.query is not None:
            action_pairs = jmespath.search(args.query, action_pairs)
        if args.format == 'json':
            print(json.dumps(action_pairs, indent=2))
        elif args.format == 'text':
            for ap in action_pairs:
                print(ap['name'])
                print('')
                doc = ap['doc']
                if doc is not None:
                    print(dedent(doc))
                print('')
        return 

    init_logging(level='DEBUG' if args.debug else 'WARNING')

    parsed_host = urlparse(args.endpoint)

    if parsed_host.scheme not in ('http', 'https'):
        raise ValueError('invalid scheme [{}]'.format(parsed_host.scheme))
    
    ec_args = {
        'host': parsed_host.hostname,
        'port': parsed_host.port or 443,
        'use_ssl': True if parsed_host.scheme == 'https' else False,
        'http_auth': (args.user, args.password)
    }
    
    ec_session = ElasticCloudSession(**ec_args)

    if args.client not in clients.keys():
        LOG.error('invalid client [%s]', args.client)
        sys.exit(1)

    client_cls = clients[args.client]
    client = client_cls(ec_session)
    
    action_name = action_to_method(args.action)
    
    try:
        action_fn = getattr(client, action_name)
    except Exception as e:
        LOG.error('invalid action [%s]: %s', args.action, e)
        return -1

    try:
        result = action_fn()
        final_result = finalize_result(result, query=args.query)
        print(final_result)
    except Exception as e:
        LOG.error('failed to execute action [%s]: %s', args.action, e)
        return -1

if __name__ == '__main__':
    sys.exit(main())