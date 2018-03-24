from __future__ import absolute_import

VERSION = (1,1)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

API_VERSION = 1
__apiversionstr__ = 'v%s' %(API_VERSION)

from .client import ElasticCloud
from .client import ElasticCloudSession