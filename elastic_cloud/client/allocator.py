from elastic_cloud.utils import ElasticCloudNamespacedClient
from elastic_cloud.utils import query_params
from elastic_cloud.utils import _make_path
from elastic_cloud.utils import (GET, POST, DELETE, PUT, PATCH)

CLUSTER_TYPES = (
    ELASTICSEARCH, KIBANA, ALL
) = (
    'elasticsearch', 'kibana', None
)

class PlatformAllocatorClient(ElasticCloudNamespacedClient):
    @query_params('q')
    def get_allocators(self, params=None):
        return self.session.perform_request(GET, _make_path('platform', 'infrastructure', 'allocators'), params=params)

    def search_allocators(self, body=None, params=None):
        return self.session.perform_request(POST, _make_path('platform', 'infrastructure', 'allocators' '_search'), body=body, params=params)
    
    @query_params('remove_instances')
    def delete_allocator(self, allocator_id, params=None):
        return self.session.perform_request(DELETE, _make_path('platform', 'infrastructure', 'allocators', allocator_id), params=params)

    def get_allocator(self, allocator_id, params=None):
        return self.session.perform_request(GET, _make_path('platform', 'infrastructure', 'allocators', allocator_id), params=params)

    @query_params('allocator_down', 'force_update', 'validate_only')
    def move_clusters(self, allocator_id, body=None, params=None):
        return self.session.perform_request(POST, _make_path('platform', 'infrastructure', 'allocators', allocator_id, 'clusters', '_move'), body=body, params=params)

    @query_params('allocator_down', 'force_update', 'validate_only')
    def move_clusters_by_type(self, allocator_id, cluster_type=None, body=None, params=None):
        if cluster_type not in CLUSTER_TYPES:
            raise ValueError('invalid cluster_type parameter [%s]' %(cluster_type))
        return self.session.perform_request(GET, _make_path('platform', 'infrastructure', 'allocators', allocator_id, 
            'clusters', cluster_type, '_move'), body=body, params=params)

    def get_allocator_metadata(self, allocator_id, params=None):
        return self.session.perform_request(GET, _make_path('platform', 'infrastructure', 'allocators', allocator_id, 'metadata'), params=params)

    @query_params('version')
    def set_allocator_metadata(self, allocator_id, body=None, params=None):
        return self.session.perform_request(PUT, _make_path('platform', 'infrastructure', 'allocators', allocator_id, 'metadata'), body=body, params=params)

    @query_params('version')
    def delete_allocator_metadata_item(self, allocator_id, key, params=None):
        return self.session.perform_request(DELETE, _make_path('platform', 'infrastructure', 'allocators', allocator_id, 'metadata', key), params=params)

    @query_params('version')
    def set_allocator_metadata_item(self, allocator_id, key, body=None, params=None):
        return self.session.perform_request(PUT, _make_path('platform', 'infrastructure', 'allocators', allocator_id, 'metadata', key), body=body, params=params)

    def get_allocator_settings(self, allocator_id, params=None):
        return self.session.perform_request(GET, _make_path('platform', 'infrastructure', 'allocators', allocator_id, 'settings'), params=params)

    @query_params('version')
    def set_allocator_settings(self, allocator_id, body=None, params=None):
        return self.session.perform_request(PUT, _make_path('platform', 'infrastructure', 'allocators', allocator_id, 'settings'), body=body, params=params)

    @query_params('version')
    def update_allocator_settings(self, allocator_id, body=None, params=None):
        return self.session.perform_request(PATCH, _make_path('platform', 'infrastructure', 'allocators', allocator_id, 'settings'), body=body, params=params)
