from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin
from django.views.i18n import set_language
from mezzanine.blog.views import blog_post_list
from mezzanine.conf import settings

admin.autodiscover()

# Add the urlpatterns for any custom Django applications here.
# You can also change the ``home`` view to add your own functionality
# to the project's homepage.
urlpatterns = []

if settings.USE_MODELTRANSLATION:
    urlpatterns += [
        url('^i18n/$', set_language, name='set_language'),
    ]

# Mezzanine's Blog app.
blog_installed = "mezzanine.blog" in settings.INSTALLED_APPS
if blog_installed:
    BLOG_SLUG = settings.BLOG_SLUG.rstrip("/")
    if BLOG_SLUG:
        BLOG_SLUG += "/"
    blog_patterns = [
        url("^%s" % BLOG_SLUG, include("mezzanine_pubsubhubbub_pub.urls")),
    ]
    urlpatterns += blog_patterns

urlpatterns += [
    # HOMEPAGE FOR A BLOG-ONLY SITE
    # -----------------------------
    # This pattern points the homepage to the blog post listing page,
    # and is useful for sites that are primarily blogs. If you use this
    # pattern, you'll also need to set BLOG_SLUG = "" in your
    # ``settings.py`` module, and delete the blog page object from the
    # page tree in the admin if it was installed.
    url("^$", blog_post_list, name="home"),

    # MEZZANINE'S URLS
    # ----------------
    # ADD YOUR OWN URLPATTERNS *ABOVE* THE LINE BELOW.
    # ``mezzanine.urls`` INCLUDES A *CATCH ALL* PATTERN
    # FOR PAGES, SO URLPATTERNS ADDED BELOW ``mezzanine.urls``
    # WILL NEVER BE MATCHED!

    # If you'd like more granular control over the patterns in
    # ``mezzanine.urls``, go right ahead and take the parts you want
    # from it, and use them directly below instead of using
    # ``mezzanine.urls``.
    url("^", include("mezzanine.urls")),
]

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"