# -*- coding: utf-8 -*-
"""
:mod:`mahler.scheduler.{{ cookiecutter.plugin_name }}.resources -- TODO
======================={{ '=' * cookiecutter.plugin_name|length }}========

.. module:: resources
    :platform: Unix
    :synopsis: TODO

TODO: Write long description

"""
from mahler.core.resources import Resources


class {{ cookiecutter.resource_class_name }}(Resources):
    """
    """

    def __init__(self):
        """
        """
        pass

    def available(self):
        """
        """
        raise NotImplemented()

    def submit(self, tasks, **kwargs):
        """
        """
        pass
