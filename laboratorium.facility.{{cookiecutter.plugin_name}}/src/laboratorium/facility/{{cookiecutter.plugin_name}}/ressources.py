# -*- coding: utf-8 -*-
"""
:mod:`laboratorium.facility.{{ cookiecutter.plugin_name }}.ressources -- TODO 
============================{{ '=' * cookiecutter.plugin_name|length }}========

.. module:: ressources
    :platform: Unix
    :synopsis: TODO

TODO: Write long description

"""
from laboratorium.core.ressources import Ressources


class {{ cookiecutter.ressource_class_name }}(Ressources):
    """
    """

    def __init__(self):
        """
        """
        pass

    def available(self):
        """
        """
        return 1    

    def submit(self, number_of_processes):
        """
        """
        pass
