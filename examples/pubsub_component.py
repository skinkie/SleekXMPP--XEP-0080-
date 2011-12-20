#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2010  Nathanael C. Fritz
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

import sys
import logging
import time
from optparse import OptionParser

import sleekxmpp
from sleekxmpp.componentxmpp import ComponentXMPP
from sleekxmpp.exceptions import XMPPError

# Python versions before 3.0 do not use UTF-8 encoding
# by default. To ensure that Unicode is handled properly
# throughout SleekXMPP, we will set the default encoding
# ourselves to UTF-8.
if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf8')
else:
    raw_input = input


class EchoComponent(ComponentXMPP):

    """
    A simple SleekXMPP component that echoes messages.
    """

    def __init__(self, jid, secret, server, port):
        ComponentXMPP.__init__(self, jid, secret, server, port)

        # The session_start event will be triggered when
        # the bot establishes its connection with the server
        # and the XML streams are ready for use. We want to
        # listen for this event so that we we can intialize
        # our roster.
        self.add_event_handler("session_start", self.start)
        #self.add_event_handler("disco_items_query", self._get_items2)
        
        self.add_event_handler("pubsub_subscribe", self._subscribe)
        self.add_event_handler("pubsub_unsubscribe", self._unsubscribe)
        self.add_event_handler("pubsub_get_items", self._get_items)

        self.add_event_handler("pubsub_set_items", self._set_items)
        self.add_event_handler("pubsub_create_node", self._create_node)
        self.add_event_handler("pubsub_delete_node", self._delete_node)
        self.add_event_handler("pubsub_retract_node", self._retract)
        self.add_event_handler("pubsub_get_config_node", self._get_config_node)

        self.auto_authorize = True # Automatic bidirectional subscriptions
        self.auto_subscribe = True


    def _unsubscribe(self, iq):
        raise XMPPError(condition='feature-not-implemented')

    def _subscribe(self, iq):
        # self._check_subscription(iq['from'].full)
        raise XMPPError(condition='feature-not-implemented')

    def _get_items(self, iq):
        raise XMPPError(condition='feature-not-implemented')
    
    def _set_items(self, iq):
        raise XMPPError(condition='feature-not-implemented')

    def _create_node(self, iq):
        raise XMPPError(condition='feature-not-implemented')

    def _delete_node(self, iq):
        raise XMPPError(condition='feature-not-implemented')

    def _retract(self, iq):
        raise XMPPError(condition='feature-not-implemented')

    def _get_config_node(self, iq):
        raise XMPPError(condition='feature-not-implemented')

    def start(self, event):
        """
        Process the session_start event.

        Typical actions for the session_start event are
        requesting the roster and broadcasting an intial
        presence stanza.

        Arguments:
            event -- An empty dictionary. The session_start
                     event does not provide any additional
                     data.
        """
        return


if __name__ == '__main__':
    # Setup the command line arguments.
    optp = OptionParser()

    # Output verbosity options.
    optp.add_option('-q', '--quiet', help='set logging to ERROR',
                    action='store_const', dest='loglevel',
                    const=logging.ERROR, default=logging.INFO)
    optp.add_option('-d', '--debug', help='set logging to DEBUG',
                    action='store_const', dest='loglevel',
                    const=logging.DEBUG, default=logging.INFO)
    optp.add_option('-v', '--verbose', help='set logging to COMM',
                    action='store_const', dest='loglevel',
                    const=5, default=logging.INFO)

    # JID and password options.
    optp.add_option("-j", "--jid", dest="jid",
                    help="JID to use")
    optp.add_option("-p", "--password", dest="password",
                    help="password to use")
    optp.add_option("-s", "--server", dest="server",
                    help="server to connect to")
    optp.add_option("-P", "--port", dest="port",
                    help="port to connect to")

    opts, args = optp.parse_args()

    if opts.jid is None:
        opts.jid = raw_input("Component JID: ")
    if opts.password is None:
        opts.password = getpass.getpass("Password: ")
    if opts.server is None:
        opts.server = raw_input("Server: ")
    if opts.port is None:
        opts.port = int(raw_input("Port: "))

    # Setup logging.
    logging.basicConfig(level=opts.loglevel,
                        format='%(levelname)-8s %(message)s')

    # Setup the EchoComponent and register plugins. Note that while plugins
    # may have interdependencies, the order in which you register them does
    # not matter.
    xmpp = EchoComponent(opts.jid, opts.password, opts.server, opts.port)
    xmpp.registerPlugin('xep_0030') # Service Discovery
    xmpp.registerPlugin('xep_0060') # PubSub

    # Connect to the XMPP server and start processing XMPP stanzas.
    if xmpp.connect():
        xmpp.process(threaded=False)
        print("Done")
    else:
        print("Unable to connect.")
