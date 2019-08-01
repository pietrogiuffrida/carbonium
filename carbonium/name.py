#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re


class Name:
    def __init__(self, domains, name, alias=None, **kwargs):
        """Name class

        Name is the building block of a carbonium structure.
        It provides an object with few mandatory arguments and
        several, arbitrary, custom properties.

        Args:
            domains (list of str): a list of string that define a multilevel name structure
            name (str): the name of the Name
            alias (str): an alternative name, that can be varied without impact on the code
                that refers to Name.name attribute
            **kwargs:
        """
        self.domains = domains
        self.name = name
        self.alias = alias
        self.properties = ["domains", "name", "alias"]

        for key in kwargs:
            self.properties.append(key)
            self.__setattr__(key, kwargs[key])

    @property
    def domains(self):
        return self._domains

    @domains.setter
    def domains(self, value):
        if not value:
            raise ValueError("domains argument cannot be None")
        if not isinstance(value, list):
            value = [value]
        self._domains = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("name argument cannot be None")
        self.check_identifier(value)
        self._name = value

    @staticmethod
    def check_identifier(identifier):
        invalid = re.search(r"[^a-z0-9_]", identifier, flags=re.IGNORECASE)

        if invalid:
            raise ValueError(
                "Name {} is not a valid identifier ({} is not a valid char)".format(
                    identifier, invalid.group()
                )
            )

    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, value):
        if not value:
            self._alias = self.name
        else:
            self._alias = value

    def get(self, name, default=None):
        return self.__dict__.get(name, default)

    def __str__(self):
        msg = []
        for attr in self.properties:
            msg.append("{} {}".format(attr, getattr(self, attr)))
        return "\n".join(msg)

    def __call__(self):
        return getattr(self, "alias")
