from elastic_cloud.utils import ElasticCloudNamespacedClient
from elastic_cloud.utils import query_params
from elastic_cloud.utils import _make_path
from elastic_cloud.utils import (GET, POST, DELETE, PUT, PATCH)

class ElasticsearchClusterClient(ElasticCloudNamespacedClient):
    @query_params('from', 'show_hidden', 'show_metadata', 'show_plan_defaults', 'show_plans', 
    'show_security', 'show_system_alerts', 'size')
    def get_clusters(self, params=None):
        return self.session.perform_request(GET, _make_path('clusters', 'elasticsearch'), params=params)

    @query_params('show_metadata', 'show_plan_defaults', 'show_plan_logs', 'show_plans', 
    'show_security', 'show_system_alerts')
    def get_cluster(self, cluster_id, params=None):
        return self.session.perform_request(GET, _make_path('clusters', 'elasticsearch', cluster_id), params=params)

    def delete_cluster(self, cluster_id):
        return self.session.perform_request(DELETE, _make_path('clusters', 'elasticsearch', cluster_id))

    @query_params('validate_only')
    def create_cluster(self, body=None, params=None):
        return self.session.perform_request(POST, _make_path('clusters', 'elasticsearch'), body=body, params=params)

    def generate_diagnostics(self, cluster_id):
        return self.session.perform_request(GET, _make_path('clusters', 'elasticsearch', cluster_id, 'support', '_generate-diagnostics'))

    @query_params('date')
    def generate_logs(self, cluster_id, params=None):
        """
        .. note::
        
            This function is currently not supported in Elastic Cloud Enterprise, only in the SaaS version.
        """
        return self.session.perform_request(GET, _make_path('clusters', 'elasticsearch', cluster_id, 'support', '_generate-logs'), params=params)

    @query_params('cancel_pending', 'group_attribute', 'restore_snapshot', 'skip_snapshot')
    def restart_cluster(self, cluster_id, params=None):
        return self.session.perform_request(POST, _make_path('clusters', 'elasticsearch', cluster_id, '_restart'), params=params)

    @query_params('hide', 'skip_snapshot')
    def shutdown_cluster(self, cluster_id, params=None):
        return self.session.perform_request(POST, _make_path('clusters', 'elasticsearch', cluster_id, '_shutdown'), params=params)

    @query_params('force_update', 'ignore_missing', 'instances_down', 'validate_only')
    def move_instances(self, cluster_id, instance_ids=[], params=None):
        """
        Moves one or more instances belonging to an Elasticsearch cluster

        :arg cluster_id: the elasticsearch cluster id
        :arg instance_ids: either a comma-delimited string of instance ids or a list/tuple of strings
        """
        return self.session.perform_request(POST, _make_path('clusters', 'elasticsearch', cluster_id, 'instances', 
            self._convert_collection_to_path_param(instance_ids), '_move'), params=params)

    @query_params('ignore_missing')
    def start_instances(self, cluster_id, instance_ids=[], params=None):
        return self.session.perform_request(POST, _make_path('clusters', 'elasticsearch', cluster_id, 'instances', 
            self._convert_collection_to_path_param(instance_ids), '_start'), params=params)

    @query_params('ignore_missing')
    def stop_instances(self, cluster_id, instance_ids=[], params=None):
        return self.session.perform_request(POST, _make_path('clusters', 'elasticsearch', cluster_id, 'instances', 
            self._convert_collection_to_path_param(instance_ids), '_stop'), params=params)

    @query_params('ignore_missing')
    def start_maintainance_mode(self, cluster_id, instance_ids=[], params=None):
        return self.session.perform_request(POST, _make_path('clusters', 'elasticsearch', cluster_id, 'instances', 
            self._convert_collection_to_path_param(instance_ids), 'maintenance-mode', '_start'), params=params)
    
    @query_params('ignore_missing')
    def stop_maintainance_mode(self, cluster_id, instance_ids=[], params=None):
        return self.session.perform_request(POST, _make_path('clusters', 'elasticsearch', cluster_id, 'instances', 
            self._convert_collection_to_path_param(instance_ids), 'maintenance-mode', '_start'), params=params)
    
    def set_cluster_name(self, cluster_id, new_name):
        return self.session.perform_request(POST, _make_path('clusters', 'elasticsearch', cluster_id, 'metadata', 'name', new_name))
    
    @query_params('ignore_missing', 'restart_after_update')
    def set_settings_overrides(self, cluster_id, instance_ids=[], body=None, params=None):
        return self.session.perform_request(POST, _make_path('clusters', 'elasticsearch', cluster_id, 'instances', 
            self._convert_collection_to_path_param(instance_ids), 'settings'), params=params, body=body)
    
    def get_cluster_metadata(self, cluster_id):
        return self.session.perform_request(GET, _make_path('clusters', 'elasticsearch', cluster_id, 'metadata', 'settings'))

    @query_params('version')
    def update_cluster_metadata(self, cluster_id, body=None, params=None):
        return self.session.perform_request(PATCH, _make_path('clusters', 'elasticsearch', cluster_id, 'metadata', 'settings'), body=body, params=params)        

    def cancel_monitoring(self, cluster_id):
        return self.session.perform_request(DELETE, _make_path('clusters', 'elasticsearch', cluster_id, 'monitoring'))

    def set_monitoring(self, cluster_id, dest_cluster_id):
        return self.session.perform_request(POST, _make_path('clusters', 'elasticsearch', cluster_id, 'monitoring', dest_cluster_id))

    @query_params('show_plan_defaults')
    def get_plan(self, cluster_id, params=None):
        return self.session.perform_request(GET, _make_path('clusters', 'elasticsearch', cluster_id, 'plan'), params=params)

    @query_params('validate_only')
    def update_plan(self, cluster_id, body=None, params=None):
        return self.session.perform_request(POST, _make_path('clusters', 'elasticsearch', cluster_id, 'plan'), body=body, params=params)

    @query_params('show_plan_defaults', 'show_plan_logs')
    def get_plan_activity(self, cluster_id, params=None):
        return self.session.perform_request(GET, _make_path('clusters', 'elasticsearch', cluster_id, 'plan', 'activity'), params=params)

    @query_params('ignore_missing')
    def cancel_pending_plan(self, cluster_id, params=None):
        return self.session.perform_request(DELETE, _make_path('clusters', 'elasticsearch', cluster_id, 'plan', 'pending'), params=params)

    @query_params('show_plan_defaults')
    def get_pending_plan(self, cluster_id, params=None):
        return self.session.perform_request(GET, _make_path('clusters', 'elasticsearch', cluster_id, 'plan', 'pending'), params=params)

    def _convert_collection_to_path_param(self, collection):
        if isinstance(collection, list) or isinstance(collection, tuple):
            return ','.join(collection)
        elif isinstance(collection, str):
            return collection
        else:
            return None
