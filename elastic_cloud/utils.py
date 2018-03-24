from elasticsearch.client.utils import _make_path as make_path
from elasticsearch.client.utils import query_params as qp
from elastic_cloud import API_VERSION 

GET = 'GET'
PUT = 'PUT'
DELETE = 'DELETE'
PATCH = 'PATCH'
POST = 'POST'

def query_params(*args):
    return qp(*args)

def _make_path(*args):
    """
    Concatenate a list of strings to form a URL path.
    
    :args args: a list of strings to concatenate
    :return: the concatenated path

    .. note:: This is a patched version of :func:`elasticsearch.client.utils._make_path`
        to include the `/api/<version>` part.
    """
    return make_path('api', 'v%s' %(API_VERSION), *args)

def convert_collection_to_path_param(collection):
    """
    Convert a list of elements to a valid path parameter by concatenating 
    with ",".
    This is used when calling some endpoints that require a list of instance ids.
    If the collection parameter is not of type ``list``, ``tuple``, ``str`` or ``int``, ``None`` is returned.

    :param collection: Some object that may be a collection
    :return: Either a comma-separated list of the elements or None if invalid type
    """
    if isinstance(collection, list) or isinstance(collection, tuple):
        return ','.join(collection)
    elif isinstance(collection, str) or isinstance(collection, int):
        return str(collection)
    else:
        return None    

class ElasticCloudNamespacedClient(object):
    def __init__(self, session):
        """ 
        Creates a new namespaced client. 

        :param session: A :class:`elastic_cloud.session.ElasticCloudSession` 
            object for executing HTTP requests
        """
        self.session = session