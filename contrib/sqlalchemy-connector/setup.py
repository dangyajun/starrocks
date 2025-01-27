#! /usr/bin/python3
# Copyright 2021-present StarRocks, Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import re
import sys

from setuptools import setup

v = open(
    os.path.join(
        os.path.dirname(os.path.realpath(sys.argv[0])), "sqlalchemy_starrocks", "__init__.py"
    )
)
VERSION = re.compile(r".*__version__ = \"(.*?)\"", re.S).match(v.read()).group(1)
v.close()


setup(
    name = "sqlalchemy-starrocks",
    version = VERSION,
    description = "StarRocks Dialect for SQLAlchemy",
    long_description_content_type = "text/markdown",
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: StarRocks License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Database :: Front-Ends",
    ],
    install_requires = ["sqlalchemy"],
    tests_require = [],
    keywords = "db database analytics starrocks superset sqlalchemy dialect",
    author = "fujianhj",
    author_email = "fujianhj@gmail.com",
    url = "https://github.com/StarRocks/starrocks/contrib/sqlalchemy-connector",
    license = "StarRocks",
    packages = ['sqlalchemy_starrocks'],
    include_package_data = True,
    zip_safe = False,
    entry_points = {
        'sqlalchemy.dialects': [
            'starrocks = sqlalchemy_starrocks.dialect:StarRocksDialect',
            'sr = sqlalchemy_starrocks.dialect:StarRocksDialect',
        ]
    },
)
