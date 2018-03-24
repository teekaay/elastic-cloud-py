from elastic_cloud.utils import ElasticCloudNamespacedClient
from elastic_cloud.utils import _make_path
from elastic_cloud.utils import (GET)

class ApiDocsClient(ElasticCloudNamespacedClient):
    def get_api_docs(self):
        """
        Get the API documentation in Swagger format.
        """
        return self.session.perform_request(GET, _make_path('api-docs', 'swagger.json'))