from Products.CMFCore.DirectoryView import registerDirectory
from Products.AAOLMViews.config import GLOBALS

# next three lines are for importing security routines to allow use of re module
from AccessControl import allow_class, allow_type
from AccessControl import ModuleSecurityInfo


registerDirectory('skins', GLOBALS)

# Parts of the installation process depend on the version of Plone.
# This release supports Plone 2.5 and Plone 3.* 
try:
    from Products.CMFPlone.migrations import v3_0
except ImportError:
    HAS_PLONE30 = False
else:
    HAS_PLONE30 = True
    
# This release also supports Plone 4.0; for now we handle Plone 4.* 
# similar to Plone 3.*
try:
    from Products.CMFPlone.factory import _IMREALLYPLONE4
except ImportError:
    pass
else:
    HAS_PLONE30 = True
    

def initialize(context):
    pass
    

# allow security clearance
ModuleSecurityInfo('re').declarePublic('compile', 'findall',
    'match', 'search', 'split', 'sub', 'subn', 'error',
    'I', 'L', 'M', 'S', 'X')
import re
import typogrify
import smartypants

allow_type(type(re.compile('')))
allow_type(type(re.match('x','x')))
allow_type(type(re.sub('', '', '')))
allow_class(typogrify)
allow_class(smartypants)