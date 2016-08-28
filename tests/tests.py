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
from __future__ import unicode_literals

import requests
from django.conf import settings
from mezzanine.utils.tests import TestCase
from mock import patch

from mezzanine_pubsubhubbub_pub import PROTOCOL_TYPE_HTTP, PROTOCOL_TYPE_HTTPS, PROTOCOL_TYPE_BOTH
from mezzanine_pubsubhubbub_pub.models import HubBlogPost


def mocked_requests_post(*args, **kwargs):
    return "mockResponse"


class HubBlogPostTest(TestCase):
    def setUp(self):
        self.tmp_settings = settings

    def tearDown(self):
        settings = self.tmp_settings

    @patch.object(requests, "post", side_effect=mocked_requests_post)
    def test_no_notify(self, mock_post):
        blog_post = HubBlogPost()
        blog_post.user_id = 1
        blog_post.status = 1
        settings.PUSH_URL_PROTOCOL = PROTOCOL_TYPE_HTTP
        blog_post.save()
        self.assertFalse(mock_post.called)

    @patch.object(requests, "post", side_effect=mocked_requests_post)
    def test_notify_http(self, mock_post):
        blog_post = HubBlogPost()
        blog_post.user_id = 1
        blog_post.status = 2
        settings.PUSH_URL_PROTOCOL = PROTOCOL_TYPE_HTTP
        blog_post.save()

        call_args_list = mock_post.call_args_list
        call = call_args_list[0]
        expected = self.create_extpected(u'http://example.com/feeds/rss/')
        self.assertEqual(expected, call)

        call = call_args_list[1]
        expected = self.create_extpected(u'http://example.com/feeds/atom/')
        self.assertEqual(expected, call)

    @patch.object(requests, "post", side_effect=mocked_requests_post)
    def test_notify_https(self, mock_post):
        blog_post = HubBlogPost()
        blog_post.user_id = 1
        blog_post.status = 2
        settings.PUSH_URL_PROTOCOL = PROTOCOL_TYPE_HTTPS
        blog_post.save()

        call_args_list = mock_post.call_args_list
        call = call_args_list[0]
        expected = self.__create_extpected(u'https://example.com/feeds/rss/')
        self.assertEqual(expected, call)

        call = call_args_list[1]
        expected = self.__create_extpected(u'https://example.com/feeds/atom/')
        self.assertEqual(expected, call)

    @patch.object(requests, "post", side_effect=mocked_requests_post)
    def test_notify_both(self, mock_post):
        blog_post = HubBlogPost()
        blog_post.user_id = 1
        blog_post.status = 2
        settings.PUSH_URL_PROTOCOL = PROTOCOL_TYPE_BOTH
        blog_post.save()

        call_args_list = mock_post.call_args_list
        call = call_args_list[0]
        expected = self.create_extpected(u'http://example.com/feeds/rss/')
        self.assertEqual(expected, call)

        call = call_args_list[1]
        expected = self.create_extpected(u'http://example.com/feeds/atom/')
        self.assertEqual(expected, call)

        call = call_args_list[2]
        expected = self.create_extpected(u'https://example.com/feeds/rss/')
        self.assertEqual(expected, call)

        call = call_args_list[3]
        expected = self.create_extpected(u'https://example.com/feeds/atom/')
        self.assertEqual(expected, call)

    def __create_extpected(self, feed_url):
        return ((u'https://pubsubhubbub.appspot.com/',), {u"data": {u'hub.url': feed_url,
                                                                    u'hub.mode': u'publish'}, u"headers": {
            u'User-Agent': u'mezzanine-pubsubhubbub-pub/0.0.1'}},)
