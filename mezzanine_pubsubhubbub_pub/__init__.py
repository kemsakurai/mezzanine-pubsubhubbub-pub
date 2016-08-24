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

AUTHOR = 'Ken Sakurai'
EMAIL = 'sakurai.kem@gmail.com'
VERSION = '0.0.1'
SITE = 'https://github.com/kemsakurai/mezzanine-pubsubhubbub-pub'
LICENSE = 'Apache license 2.0'

__version__ = VERSION
UA = 'mezzanine-pubsubhubbub-pub' + '/{0}'.format(__version__)

PROTOCOL_TYPE_HTTP = "http"
PROTOCOL_TYPE_HTTPS = "https"
PROTOCOL_TYPE_BOTH = "both"
PROTOCOL_TYPE_CHOICES = (
    (PROTOCOL_TYPE_HTTP, _("HTTP_ONLY")),
    (PROTOCOL_TYPE_HTTPS, _("HTTPS_ONLY")),
    (PROTOCOL_TYPE_BOTH, _("BOTH")),
)


def ping_hub(feed_url, hub_url=None):
    """
    Makes a POST request to the hub. If no hub_url is provided, the
    value is fetched from the PUSH_HUB setting.
    Returns a dictionary with `requests.models.Response` object to the value
    """
    if hub_url is None:
        hub_url = getattr(settings, 'PUSH_HUB', None)
    if hub_url is None:
        raise ValueError("Specify hub_url or set the PUSH_HUB setting.")
    params = {
        'hub.mode': 'publish',
        'hub.url': feed_url,
    }
    results = {}
    for elem in hub_url:
        result = requests.post(elem, data=params, headers={'User-Agent': UA})
        results.update({elem: result})

    return results
