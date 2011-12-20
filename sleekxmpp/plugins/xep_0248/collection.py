"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2010 Nathanael C. Fritz, Erik Reuterborg Larsson
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

import logging

import sleekxmpp
from sleekxmpp.plugins.base import base_plugin
from sleekxmpp.xmlstream import register_stanza_plugin
from sleekxmpp.plugins.xep_0248 import Collection


log = logging.getLogger(__name__)


class xep_0080(base_plugin):

    """
    XEP-0248: PubSub Collection Nodes
    """

    def plugin_init(self):
        """
        Start the XEP-0248 plugin.
        """
        self.xep = '0248'
        self.description = 'Support for collection nodes'
        self.stanza = sleekxmpp.plugins.xep_0248.stanza

    def post_init(self):
        """Handle inter-plugin dependencies."""
        base_plugin.post_init(self)
        self.xmpp['xep_0030'].add_feature(Collection.namespace)
