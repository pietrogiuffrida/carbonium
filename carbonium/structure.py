#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import pickle

from .name import Name

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")


class Structure:
    """Metaclass that creates a collection of :meth:`Name<crif_pyton_libraries.check_columns.Name>` instances

    For each dictionary inside columns list, Columns create an istance of
    :meth:`Name<crif_pyton_libraries.check_columns.Name>` and set its properties.
    Each Name instance is also treated as a Columns property.

    Attributes:
        names (list): an ordered list of all the names contained in columns list.
        domains (set): a set of available domains
    """

    def __init__(self, name_list, *args, **kwargs):
        """Constructor method for Columns

        Args:
            name_list (list): Each dictionary inside columns list
                must respect :envvar:`ordered_columns` syntax.
        """
        self.names = []
        self.domains = set()
        for name_definition in name_list:

            if name_definition["name"] in self.names:
                raise ValueError(
                    "Name {} already present".format(name_definition["name"])
                )

            self._add_name(name_definition)

            for domain in name_definition["domains"]:
                self._add_domain(domain=domain)

    def _add_domain(self, domain):
        self.domains.add(domain)

    def _add_name(self, name_definition):
        name = Name(**name_definition)
        self.names.append(name.name)
        setattr(self, name.name, name)

    def get_names(self, domain=None):
        """Select column names from self.names respecting insertion order.

        Domain and selected arguments can be used to select a sample of names.

        Args:
            domain (str): domain of expected names. Domains refers to domain
                property of :meth:`Name<crif_pyton_libraries.check_columns.Name>`

        Returns:
            selection (list): list of selected columns.

        """

        selection = []
        for name in self.names:

            target = getattr(self, name)

            if not isinstance(target, Name):
                continue

            if domain and domain not in target.domains:
                continue

            selection.append(name)

        return selection

    def __getitem__(self, name):
        return self.__dict__[name]

    def get(self, name, default=None):
        return self.__dict__.get(name, default)

    def dump(self, filename: str, overwrite=False):
        if not filename.endswith(".pkl"):
            filename += ".pkl"

        logger.info("Saving on {}".format(filename))

        if os.path.exists(filename):
            if not overwrite:
                msg = "{} ALREADY EXISTS! I'M NOT ABLE TO OVERWRITE!".format(filename)
                logger.info(msg)
                raise FileExistsError(msg)

            logger.info("Overwriting {}...".format(filename))

        with open(filename, "wb") as output:
            pickle.dump(self.__dict__, output)

    def load(self, filename):
        logger.debug("Loading from {}".format(filename))
        if not os.path.exists(filename):
            logger.error("{} DOES NOT EXISTS!".format(filename))
            raise FileNotFoundError("{} DOES NOT EXISTS!".format(filename))

        with open(filename, "rb") as input_file:
            self.__dict__ = pickle.load(input_file)
