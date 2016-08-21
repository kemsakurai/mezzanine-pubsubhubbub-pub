"""
   Copyright 2016 Kem

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from django.contrib import admin
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost
from mezzanine.utils.sites import current_site_id

from mezzanine_pubsubhubbub_pub import ping_hub


class HubBlogPostAdmin(BlogPostAdmin):
    def save_form(self, request, form, change):
        """
        Super class ordering is important here - user must get saved first.
        """
        result = BlogPostAdmin.save_form(self, request, form, change)
        site = Site.objects.get(id=current_site_id())
        rss_url = 'http://' + site.domain + reverse("blog_post_feed", kwargs={"format": "rss"})
        ping_hub(rss_url)

        atom_url = 'http://' + site.domain + reverse("blog_post_feed", kwargs={"format": "atom"})
        ping_hub(atom_url)
        return result


admin.site.register(BlogPost, BlogPostAdmin)
