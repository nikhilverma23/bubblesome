#  Add project directory to PYTHON_PATH

import os, sys
path = '/home/nmweb/nmweb/'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'nmweb.settings'

# BEGIN WORKAROUND FOR 500 ERROR WHEN DEBUG=False
#
from django.core.management.validation import get_validation_errors 
try: 
     from cStringIO import StringIO 
except ImportError: 
     from StringIO import StringIO 
s = StringIO() 
num_errors = get_validation_errors(s, None) 
#
# END WORKAROUND

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
