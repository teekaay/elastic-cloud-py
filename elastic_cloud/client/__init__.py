from elasticsearch.connection.http_requests import RequestsHttpConnection
from .allocator import PlatformAllocatorClient
from .elasticsearch_cluster import ElasticsearchClusterClient
from .kibana_cluster import KibanaClusterClient
from .stacks import StackClient
from .platform import PlatformClient
from .api_docs import ApiDocsClient

class ElasticCloudSession(RequestsHttpConnection):
    """
    Represents a connection to ElasticCloud. Used for performing HTTP requests

    .. note::
        This is a wrapped session/connection object from 
        :class:`elasticsearch.connection.http_requests.RequestsHttpConnection`.
    """
    pass

class ElasticCloud(object):
    def __init__(self, host='localhost', port=12443, use_ssl=True, username=None, password=None, **kwargs):
        """
        Creates a new ElasticCloud instance. 

        :param host: The host to connect to (without the protocol)
        :param port: The port where the Elastic Cloud coordinator listens on
        :param use_ssl: If true, HTTPS will be used, otherwise HTTP will be used
        :param username: The username for authorizing against ElasticCloud
        :param password: The password for authorizing against ElasticCloud
        :param kwargs: Additional parameters to pass to :class:`elastic_cloud.client.ElasticCloudSession`
        """
        self.session = ElasticCloudSession(host=host, port=port, use_ssl=use_ssl, http_auth=(username, password), **kwargs)

        self.stacks = StackClient(self.session)
        self.elasticsearch_cluster = ElasticsearchClusterClient(self.session)
        self.kibana_cluster = KibanaClusterClient(self.session)
        self.platform = PlatformClient(self.session)
        self.allocators = PlatformAllocatorClient(self.session)
        self.api_docs = ApiDocsClient(self.session)