from Products.CMFCore.utils import getToolByName
from Products.AAOLMViews.config import GLOBALS
from Products.Archetypes.Extensions.utils import install_subskin
import string
from StringIO import StringIO

def install(portal):
    out = StringIO()
    out.write("Installing AAOLMViews\n")

    # copy the News Item for our blog entry
    portal_types = getToolByName(portal, 'portal_types')

    # install our skins
    install_subskin(portal, out, GLOBALS)
    skins_tool = getToolByName(portal, "portal_skins")
    aaolm_skin = "aaolm_views"

    # Iterate over all existing skins and remove the one we don't want
    skins = skins_tool.getSkinSelections()
    for skin in skins:
        path = skins_tool.getSkinPath(skin)
        path = map(string.strip, string.split(path,','))
        if aaolm_skin not in path:
            #path.remove(aaolm_skin) 
            #print >> out, "Removed '%s' from portal_skins." % aaolm_skin
            path = string.join(path, ', ')
            # addSkinSelection will replace existing skins as well.
            skins_tool.addSkinSelection(skin, path)
            print >> out, "Added '%s' to portal_skins." % aaolm_skin
    
    # tweak News Item settings - make default view a Blog Entry
    news_item = getattr(portal_types, 'News Item')
    view = 'blogentry_view'
    news_item.default_view = view
    news_item.immediate_view = view
    if view not in news_item.view_methods:
        news_item._updateProperty('view_methods', news.view_methods + (view,))
        news_item.allow_discussion = True
    print >> out, "Tweaked 'News Item' FTU settings"    
    
    # make new views available to Smart Folder
    views = ['blog_view',               # Blog Listing View
             'toc_view',                # Issue Table of Contents
             'timelinemap_view',        # Timeline + Map for Events
             ]
    topic = portal_types.Topic
    for view in views:
        if view not in topic.view_methods:
            topic._updateProperty('view_methods', topic.view_methods + (view,))
            print >> out, "Made %s available for topics.\n" % view        
        
    # make video_view available to Links
    view = 'video_view'
    link = portal_types.Link
    if view not in link.view_methods:
        link._updateProperty('view_methods', link.view_methods + (view,))
        link.allow_discussion = True
        print >> out, "Made %s available for Links.\n" % view

    # make s3slider_view available to Links
    view = 's3slider_view'
    folder = portal_types.Folder
    if view not in folder.view_methods:
        folder._updateProperty('view_methods', folder.view_methods + (view,))
        print >> out, "Made %s available for Folders.\n" % view

    # allow discussion on Pages, Links, and Events (in addition to News Items and Links)
    page = portal_types.Document
    page.allow_discussion = True
    event = portal_types.Event
    event.allow_discussion = True

    print >> out, "Installation complete."
    return out.getvalue()

def uninstall(portal, reinstall=False):
    out = StringIO()
    out.write('Uninstalling AAOLMViews\n')

    # remove skins
    skins_tool = getToolByName(portal, "portal_skins")
    skin_names = ("aaolm_views")
    skins = skins_tool.getSkinSelections()
    for skin in skins:
        path = skins_tool.getSkinPath(skin)
        path = map(string.strip, string.split(path,','))
        path = [s for s in path if s not in skin_names]
        path = string.join(path, ', ')
        skins_tool.addSkinSelection(skin, path)
        print >> out, "Removed '%s' skin from skins_tool." % skin

    # remove our custom views from Topics
    portal_types = getToolByName(portal, 'portal_types')
    views = ['blog_view',               # Blog Listing View
             'toc_view',                # Issue Table of Contents
             'timelinemap_view',        # Timeline + Map for Events
             ]
    old_view = 'folder_summary_view'
    topic = portal_types.Topic
    for view in views:    
        if view in topic.view_methods:
            # remove installed view from Topic view methods
            view_methods = [v for v in topic.view_methods if v != view]
            topic._updateProperty('view_methods', view_methods)
            print >> out, "Removed '%s' from view_methods for Topics." % view
            # reset views to defaults if they used a view from this product
            brains = portal.portal_catalog.searchResults(portal_type="Topic")
            for brain in brains:
                obj = brain.getObject()
                if view in obj.layout:
                    obj.layout = old_view

    # remove our custom view from Links
    view = 'video_view'
    old_view = 'link_view'
    portal_types = getToolByName(portal, 'portal_types')
    link = portal_types.Link
    
    if view in link.view_methods:
        # remove installed view from Link view methods
        view_methods = [v for v in link.view_methods if v != view]
        link._updateProperty('view_methods', view_methods) 
        print >> out, "Removed '%s' view from Link content type." % view
        # reset views to defaults if they used a view from this product
        brains = portal.portal_catalog.searchResults(portal_type="Link")
        for brain in brains:
            obj = brain.getObject()
            if view in obj.layout:
                obj.layout = old_view
        print >> out, "Removed '%s' from view_methods for Links and reset them to their default view templates." % view

    # remove our custom view from Folders
    view = 's3slider_view'
    old_view = 'atct_album_view'
    portal_types = getToolByName(portal, 'portal_types')
    folder = portal_types.Folder
    
    if view in folder.view_methods:
        # remove installed view from Folder view methods
        view_methods = [v for v in folder.view_methods if v != view]
        folder._updateProperty('view_methods', view_methods) 
        print >> out, "Removed '%s' view from Folder content type." % view
        # reset views to defaults if they used a view from this product
        brains = portal.portal_catalog.searchResults(portal_type="Folder")
        for brain in brains:
            obj = brain.getObject()
            if view in obj.layout:
                obj.layout = old_view
        print >> out, "Removed '%s' from view_methods for Folders and reset them to their default view templates." % view

    # remove our custom view from News Items
    view = 'blog_view'
    old_view = 'newsitem_view'
    portal_types = getToolByName(portal, 'portal_types')
    news_item = getattr(portal_types, 'News Item')
    
    if view in news_item.view_methods:
        # remove installed view from News Item view methods
        view_methods = [v for v in news_item.view_methods if v != view]
        news_item._updateProperty('view_methods', view_methods)
        # news.allow_discussion = False
        news_item.default_view = old_view
        news_item.immediate_view = old_view
        # reset views to defaults if they used a view from this product
        brains = portal.portal_catalog.searchResults(portal_type="News Item")
        for brain in brains:
            obj = brain.getObject()
            if view in obj.layout:
                obj.layout = old_view        
        print >> out, "Removed '%s' from view_methods for News Items and reset them to their default view templates." % view
