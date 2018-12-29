# -*- coding: utf-8 -*-
"""
:mod:`mahler.scheduler.{{ cookiecutter.plugin_name }} -- {{ cookiecutter.short_description }}
======================={{ '=' * cookiecutter.plugin_name|length }}===={{ '=' * cookiecutter.short_description|length }}

.. module:: {{ cookiecutter.plugin_name }}
    :platform: Unix
    :synopsis: {{ cookiecutter.synopsis }}

TODO: Write long description
"""
from ._version import get_versions

VERSIONS = get_versions()
del get_versions

__descr__ = '{{ cookiecutter.short_description }}'
__version__ = VERSIONS['version']
__license__ = 'GNU GPLv3'
__author__ = u'{{ cookiecutter.author_name }}'
__author_short__ = u'{{ cookiecutter.author_short }}'
__author_email__ = '{{ cookiecutter.author_email }}'
__copyright__ = u'{{ cookiecutter.copyright }}'
__url__ = 'https://github.com/{{ cookiecutter.github_username }}/mahler.scheduler.{{ cookiecutter.plugin_name }}'
