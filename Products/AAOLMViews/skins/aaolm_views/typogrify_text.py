## Script (Python) "typogrify_text"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=text=None
##title=Returns text that has been run through smartypants and typogrify markup enhancers

from Products.AAOLMViews.typogrify import typogrify

return typogrify(text)