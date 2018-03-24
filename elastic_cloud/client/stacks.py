from elastic_cloud.utils import ElasticCloudNamespacedClient
from elastic_cloud.utils import query_params
from elastic_cloud.utils import (GET, POST, DELETE, PUT, PATCH)

class StackClient(ElasticCloudNamespacedClient):
    @query_params('show_deleted')
    def get_all_version_stacks(self, params=None):
        """
        `<https://www.elastic.co/guide/en/cloud-enterprise/current/get-version-stacks.html>`_

        :arg show_deleted: Whether to show deleted stack versions or not
        """
        return self.session.perform_request(GET, _make_path('stack', 'versions'), params=params)

    def submit_stack_pack(self, file):
        with open(file, 'rb') as stack_pack_file:
            files = {
                'file': stack_pack_file
            }
            return self.session.perform_request(POST, _make_path('stack', 'versions'), files=files)

    def mark_stack_for_deletion(self, version):
        return self.session.perform_request(DELETE, _make_path('stack', 'versions', version))

    def get_version(self, version):
        return self.session.perform_request(GET, _make_path('stack', 'versions', version))

    def update_stack_version(self, version, body=None):
        return self.session.perform_request(PUT, _make_path('stack', 'versions', version), body=body)
