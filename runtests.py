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

import os
import sys
import warnings

import django
from django.test.runner import DiscoverRunner

warnings.simplefilter('always')


def runtests():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.settings')

    parent = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, parent)

    django.setup()

    runner = DiscoverRunner(verbosity=1, interactive=True,
                            failfast=False)
    failures = runner.run_tests(())
    sys.exit(failures)

if __name__ == '__main__':
    runtests()
