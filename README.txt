Products.AAOLMViews

Custom Plone views for Advanced Aquarist's Online Magazine

Description
===========

This product is a heavy customization of the codebase that is used for Scrawl,
a "dirt-simple blog product for Plone."  The codebase was chosen as it easily 
made custom views available to different content items.  

Products.AAOLMViews creates custom views for primarily Topics along with 
News Items and Links. It also creates template over-rides to Documents (Pages) 
and Events.  Below are the views that are registered / customized:

Topics (new views):
* Blog Listing - lists items like a blog
* Magazine Issue Table of Contents
* Events Listing that uses Simile Timeline + Google Maps to visualize Events
* Slideshow for Photos

News Items (new views):
* Blog Entry (see note)

Links (new views):
* Video View - links to YouTube, Vimeo, etc show up as Videos

Events (customized):
* Added Google Map + Map Link for driving directions

Pages (customized):
* Contributors are now listed as Authors


This product, like Scrawl, works in Plone 2.1, 2.5, 3.x, and 4.0.

Note: Blog Entry shows either the description of each contained blog entry 
(if it exists) or the entire body in it, so it's up to the user to limit those 
results in an intelligent way so that page loads doesn't take too long.


Installation
============

The installer registers a new skins folder, aaolm_views, and adds the 
appropriate new views to Topics, News Items, Links, Events, and Pages. The new
views are then available from the appropriate content types and can be selected
from the view dropdown list on that content type. Upon uninstallation, the new 
views are unregistered from all of the appropriate content types and any content
that uses one of the unregistered views is reset to its appropriate default 
template. 

Installing using buildout
-------------------------

Simply add Products.AAOLM to your eggs list and rerun buildout.

Installing as an old-style product
----------------------------------

Download the product from:
http://github.com/sgraber/Products.AAOLMViews/archives/master.

Place AAOLMViews in the Products directory of your Zope instance
and restart the server.

Final step: Add to your Plone site
----------------------------------

Either go to the 'Site Setup' page in Plone and click on
'Add/Remove Products' or use the Quick Installer in the ZMI.


Written by
==========

Shane Graber <sgraber@gmail.com>
ONE/Northwest <jonb@onenw.org>


