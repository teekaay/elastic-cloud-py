from elastic_cloud.utils import ElasticCloudNamespacedClient
from elastic_cloud.utils import query_params
from elastic_cloud.utils import _make_path
from elastic_cloud.utils import (GET, POST, DELETE, PUT)
from elastic_cloud.utils import SKIP_IN_PATH

class PlatformClient(ElasticCloudNamespacedClient):
    def get_platform_info(self):
        """
        `<https://www.elastic.co/guide/en/cloud-enterprise/current/get-platform.html>`_

        Get information about the current platform.
        """
        return self.session.perform_request(GET, _make_path('platform'))

    @query_params()
    def get_snapshot_repositories(self, params=None):
        return self.session.perform_request(GET, _make_path('platform', 'configuration', 'snapshots', 'repositories'))
    
    @query_params()
    def get_snapshot_repository(self, repository_name, params=None):
        if repository_name in SKIP_IN_PATH:
            raise ValueError('empty value passed for a required argument [repository_name]')
        return self.session.perform_request(GET, _make_path('platform', 'configuration', 'snapshots', 'repositories', repository_name))

    @query_params()
    def delete_snapshot_repository(self, repository_name, params=None):
        if repository_name in SKIP_IN_PATH:
            raise ValueError('empty value passed for a required argument [repository_name]')
        return self.session.perform_request(DELETE, _make_path('platform', 'configuration', 'snapshots', 'repositories', repository_name))

    @query_params('version')
    def set_snapshot_repository(self, repository_name, body=None, params=None):
        if repository_name in SKIP_IN_PATH:
            raise ValueError('empty value passed for a required argument [repository_name]')
        return self.session.perform_request(PUT, _make_path('platform', 'configuration', 'snapshots', 'repositories', repository_name), params=params, body=body)

    def get_tls_certificate(self, service):
        if service not in ('adminconsole', 'proxy', 'ui'):
            raise ValueError('invalid service [%s] supplied' %(service))
        return self.session.perform_request(GET, _make_path('platform', 'configuration', 'security', 'tls', service))

    def set_tls_certificate(self, service, body=None):
        if service not in ('adminconsole', 'proxy', 'ui'):
            raise ValueError('invalid service [%s] supplied' %(service))
        return self.session.perform_request(POST, _make_path('platform', 'configuration', 'security', 'tls', service), body=body)

    def get_enrollment_tokens(self):
        return self.session.perform_request(GET, _make_path('platform', 'configuration', 'security', 'enrollment-tokens'))        

    def create_enrollment_token(self, body=None):
        return self.session.perform_request(POST, _make_path('platform', 'configuration', 'security', 'enrollment-tokens'))        

    def delete_enrollment_token(self, token):
        if token in SKIP_IN_PATH:
            raise ValueError('empty value passed for a required argument [token]')
        return self.session.perform_request(DELETE, _make_path('platform', 'configuration', 'security', 'enrollment-tokens', token))      
    