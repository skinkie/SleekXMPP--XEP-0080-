"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2011  Nathanael C. Fritz
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

from sleekxmpp import Event
from sleekxmpp.plugins import xep_0004
from sleekxmpp.plugins.xep_0060.stanza.pubsub import Pubsub


class Collection(ElementBase):
    namespace = 'http://jabber.org/protocol/pubsub'
    name = 'collection'
    plugin_attrib = name
    interfaces = set(('node',))


class Associate(ElementBase):
    namespace = 'http://jabber.org/protocol/pubsub'
    name = 'associate'
    plugin_attrib = name
    interfaces = set(('node','options'))
    
    def __init__(self, *args, **kwargs):
        ElementBase.__init__(self, *args, **kwargs)

    def get_options(self):
        config = self.xml.find('{jabber:x:data}x')
        form = xep_0004.Form(xml=config)
        return form

    def set_options(self, value):
        self.xml.append(value.getXML())
        return self

    def del_options(self):
        config = self.xml.find('{jabber:x:data}x')
        self.xml.remove(config)


class Disassociate(ElementBase):
    namespace = 'http://jabber.org/protocol/pubsub'
    name = 'disassociate'
    plugin_attrib = name
    interfaces = set(('node',))


register_stanza_plugin(Event, Collection)
register_stanza_plugin(Pubsub, Collection)
register_stanza_plugin(Collection, Associate)
register_stanza_plugin(Collection, Disassociate)
