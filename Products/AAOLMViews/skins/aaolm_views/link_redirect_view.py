## Script (Python) "link_redirect_view"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
"""
Redirect to the Link target URL, if and only if:
 - redirect_links property is enabled in portal_properties/site_properties
 - AND current user doesn't have permission to edit the Link
 - SBG: Added lack of redirect for links with a defaultView='video_view'
   which allows for showing oembed links as content
"""

from Products.CMFCore.utils import getToolByName

ptool = getToolByName(context, 'portal_properties')
mtool = getToolByName(context, 'portal_membership')

redirect_links = getattr(ptool.site_properties, 'redirect_links', False)
can_edit = mtool.checkPermission('Modify portal content', context)
video = 'video_view' in context.defaultView()  # custom

if video:                                      # custom
    # video_view.pt shows the link to anyone   # custom
    return context.video_view()                # custom
if redirect_links and not can_edit:
    return context.REQUEST.RESPONSE.redirect(context.getRemoteUrl())
else:
    # link_view.pt is a template in the plone_content skin layer
    return context.link_view()
