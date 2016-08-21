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

from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from mezzanine.blog.models import BlogPost
from mezzanine.core.models import CONTENT_STATUS_PUBLISHED
from mezzanine.utils.models import ModelMixin
from mezzanine.utils.sites import current_site_id

from mezzanine_pubsubhubbub_pub import ping_hub


class HubBlogPost(ModelMixin):
    class Meta:
        mixin_for = BlogPost


def notify_blog_post(sender, instance, **kwargs):
    if instance.status == CONTENT_STATUS_PUBLISHED:
        site = Site.objects.get(id=current_site_id())
        rss_url = 'http://' + site.domain + reverse("blog_post_feed", kwargs={"format": "rss"})
        ping_hub(rss_url)

        atom_url = 'http://' + site.domain + reverse("blog_post_feed", kwargs={"format": "atom"})
        ping_hub(atom_url)


post_save.connect(notify_blog_post, sender=HubBlogPost)
