## Script (Python) "typogrify_text"
##parameters=text
##title=Returns text that has been run through smartypants and typogrify markup enhancers

from Products.AAOLMViews.typogrify import typogrify

return typogrify(text)