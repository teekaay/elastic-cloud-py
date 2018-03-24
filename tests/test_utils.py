from nose.tools import assert_equals
from elastic_cloud.utils import _make_path
from elastic_cloud.utils import convert_collection_to_path_param

def test_make_path_standard():
    args = ['elasticsearch', 'clusters']
    expected = '/api/v1/elasticsearch/clusters'
    assert_equals(_make_path(*args), expected)

def test_make_path_with_invalid_params():
    args = ['elasticsearch', 'clusters', None]
    expected = '/api/v1/elasticsearch/clusters'
    assert_equals(_make_path(*args), expected)

def test_convert_collection_to_path_param():
    collection = ['instance-1', 'instance-2']
    expected = 'instance-1,instance-2'
    assert_equals(convert_collection_to_path_param(collection), expected)

    collection = 'instance-1,instance-2'
    assert_equals(convert_collection_to_path_param(collection), expected)

    assert_equals(convert_collection_to_path_param(None), None)