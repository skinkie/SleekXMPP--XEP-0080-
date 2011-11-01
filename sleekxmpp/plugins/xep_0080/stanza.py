"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2010  Nathanael C. Fritz
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

from sleekxmpp.stanza.rootstanza import RootStanza
from sleekxmpp.plugins import xep_0082

class Geoloc(RootStanza):

    """
    XMPP's <geoloc> stanza allows entities to know the current
    geographical or physical location of an entity. (XEP-0080: User Location)

    Example <geoloc> stanzas:
        <geoloc xmlns='http://jabber.org/protocol/geoloc'/>

        <geoloc xmlns='http://jabber.org/protocol/geoloc' xml:lang='en'>
          <accuracy>20</accuracy>
          <country>Italy</country>
          <lat>45.44</lat>
          <locality>Venice</locality>
          <lon>12.33</lon>
        </geoloc>

    Stanza Interface:
        accuracy -- Horizontal GPS error in meters; this element obsoletes the <error/> element
        alt -- Altitude in meters above or below sea level
        area -- A named area such as a campus or neighborhood
        bearing -- GPS bearing (direction in which the entity is heading to reach its next waypoint), measured in decimal degrees relative to true north
        building -- A specific building on a street or in an area
        country -- The nation where the user is located
        countrycode -- The ISO 3166 two-letter country code
        datum -- GPS datum (WGS84)
        description -- A natural-language name for or description of the location
        error -- Horizontal GPS error in arc minutes; this element is deprecated in favor of <accuracy/>
        floor -- A named floor such as a campus or neighborhood
        lat -- Latitude in decimal degrees North
        locality -- A locality within the administrative region, such as a town or city
        lon -- Longitude in decimal degrees East
        postalcode -- A code used for postal delivery
        region -- An administrative region of the nation, such as a state or province
        room -- A particular room in a building
        speed -- The speed at which the entity is moving, in meters per second
        street -- A thoroughfare within the locality, or a crossing of two thoroughfares
        text -- A catch-all element that captures any other information about the location
        timestamp -- UTC timestamp specifying the moment when the reading was taken
        uri -- A URI or URL pointing to information about the location

    Attributes:
        None

    Methods:
        get_interface -- Get the value of the <interface> element.
        set_interface -- Set the value of the <interface> element.
    """

    namespace = 'http://jabber.org/protocol/geoloc'
    name = 'geoloc'
    interfaces = set(('accuracy', 'alt', 'area', 'bearing', 'building', 'country', 'countrycode', 'datum', 'dscription', 'error', 'floor', 'lat', 'locality', 'lon', 'postalcode', 'region', 'room', 'speed', 'street', 'text', 'timestamp', 'uri'))
    sub_interfaces = set(('accuracy', 'alt', 'area', 'bearing', 'building', 'country', 'countrycode', 'datum', 'dscription', 'error', 'floor', 'lat', 'locality', 'lon', 'postalcode', 'region', 'room', 'speed', 'street', 'text', 'timestamp', 'uri'))
    plugin_attrib = name

    def exception(self, e):
        """
        Override exception passback for presence.
        """
        pass

    def set_accuracy(self, accuracy):
        """
        Set the value of the <accuracy> element.

        Arguments:
            accuracy -- Horizontal GPS error in meters; this element obsoletes the <error/> element
        """
        self._set_sub_text('accuracy', text=str(accuracy))
        return self
    
    def get_accuracy(self):
        """
        Return the value of the <accuracy> element as an integer.
        """
        p = self._get_sub_text('accuracy')
        if not p:
            return None
        else:
            try:
                return int(p)
            except ValueError:
                return None

    def set_alt(self, alt):
        """
        Set the value of the <alt> element.

        Arguments:
            alt -- Altitude in meters above or below sea level
        """
        self._set_sub_text('alt', text=str(alt))
        return self
    
    def get_alt(self):
        """
        Return the value of the <alt> element as an integer.
        """
        p = self._get_sub_text('alt')
        if not p:
            return None
        else:
            try:
                return int(p)
            except ValueError:
                return None

    def set_area(self, area):
        """
        Set the value of the <area> element.

        Arguments:
            area -- A named area such as a campus or neighborhood
        """
        self._set_sub_text('area', text=area)
        return self

    def get_area(self):
        """
        Return the value of the <area> element.
        """
        return self._get_sub_text('area')

    def set_bearing(self, bearing):
        """
        Set the value of the <bearing> element.

        Arguments:
            bearing -- GPS bearing (direction in which the entity is heading to reach its next waypoint), measured in decimal degrees relative to true north
        """
        self._set_sub_text('bearing', text=str(bearing))
        return self

    def get_bearing(self):
        """
        Return the value of the <bearing> element as a float.
        """
        p = self._get_sub_text('bearing')
        if not p:
            return None
        else:
            try:
                return float(p)
            except ValueError:
                return None

    def set_building(self, building):
        """
        Set the value of the <building> element.

        Arguments:
            building -- A specific building on a street or in an area
        """
        self._set_sub_text('building', text=building)
        return self

    def get_building(self):
        """
        Return the value of the <building> element.
        """
        return self._get_sub_text('building')

    def set_country(self, country):
        """
        Set the value of the <country> element.

        Arguments:
            country -- The nation where the user is located
        """
        self._set_sub_text('country', text=country)
        return self

    def get_country(self):
        """
        Return the value of the <country> element.
        """
        return self._get_sub_text('country')

    def set_countrycode(self, countrycode):
        """
        Set the value of the <countrycode> element.

        Arguments:
            countrycode -- The ISO 3166 two-letter country code
        """
        self._set_sub_text('countrycode', text=countrycode)
        return self

    def get_countrycode(self):
        """
        Return the value of the <countrycode> element.
        """
        return self._get_sub_text('countrycode')

    def set_datum(self, datum):
        """
        Set the value of the <datum> element.

        Arguments:
            datum -- GPS datum (WGS84)
        """
        self._set_sub_text('datum', text=datum)
        return self
 
    def get_datum(self):
        """
        Return the value of the <datum> element.
        """
        return self._get_sub_text('datum')
   
    def set_description(self, description):
        """
        Set the value of the <description> element.

        Arguments:
            description -- A natural-language name for or description of the location
        """
        self._set_sub_text('description', text=description)
        return self
 
    def get_description(self):
        """
        Return the value of the <description> element.
        """
        return self._get_sub_text('description')
   
    def set_error(self, error):
        """
        Set the value of the <error> element.

        Arguments:
            error -- Horizontal GPS error in arc minutes; this element is deprecated in favor of <accuracy/>
        """
        self._set_sub_text('error', text=str(error))
        return self

    def get_error(self):
        """
        Return the value of the <error> element as a float.
        """
        p = self._get_sub_text('error')
        if not p:
            return None
        else:
            try:
                return float(p)
            except ValueError:
                return None

    def set_floor(self, floor):
        """
        Set the value of the <floor> element.

        Arguments:
            floor -- A named floor such as a campus or neighborhood
        """
        self._set_sub_text('floor', text=floor)
        return self
 
    def get_floor(self):
        """
        Return the value of the <floor> element.
        """
        return self._get_sub_text('floor')
   
    def set_lat(self, lat):
        """
        Set the value of the <lat> element.

        Arguments:
            lat -- Latitude in decimal degrees North
        """
        self._set_sub_text('lat', text=str(lat))
        return self
    
    def get_lat(self):
        """
        Return the value of the <lat> element as a float.
        """
        p = self._get_sub_text('lat')
        if not p:
            return None
        else:
            try:
                return float(p)
            except ValueError:
                return None
  
    def set_locality(self, locality):
        """
        Set the value of the <locality> element.

        Arguments:
            locality -- A locality within the administrative region, such as a town or city
        """
        self._set_sub_text('locality', text=locality)
        return self
 
    def get_locatity(self):
        """
        Return the value of the <locatity> element.
        """
        return self._get_sub_text('locatity')
 
    def set_lon(self, lon):
        """
        Set the value of the <lon> element.

        Arguments:
            lon -- Longitude in decimal degrees East
        """
        self._set_sub_text('lon', text=str(lon))
        return self

    def get_lon(self):
        """
        Return the value of the <lon> element as a float.
        """
        p = self._get_sub_text('lon')
        if not p:
            return None
        else:
            try:
                return float(p)
            except ValueError:
                return None

    def set_postalcode(self, postalcode):
        """
        Set the value of the <postalcode> element.

        Arguments:
            postalcode -- A code used for postal delivery
        """
        self._set_sub_text('postalcode', text=postalcode)
        return self

    def get_postalcode(self):
        """
        Return the value of the <postalcode> element.
        """
        return self._get_sub_text('postalcode')

    def set_region(self, region):
        """
        Set the value of the <region> element.

        Arguments:
            region -- An administrative region of the nation, such as a state or province
        """
        self._set_sub_text('region', text=region)
        return self

    def get_region(self):
        """
        Return the value of the <region> element.
        """
        return self._get_sub_text('region')

    def set_room(self, room):
        """
        Set the value of the <room> element.

        Arguments:
            room -- A particular room in a building
        """
        self._set_sub_text('room', text=room)
        return self
 
    def get_room(self):
        """
        Return the value of the <room> element.
        """
        return self._get_sub_text('room')
   
    def set_speed(self, speed):
        """
        Set the value of the <speed> element.

        Arguments:
            speed -- The speed at which the entity is moving, in meters per second
        """
        self._set_sub_text('speed', text=str(speed))
        return self
    
    def get_speed(self):
        """
        Return the value of the <speed> element as a float.
        """
        p = self._get_sub_text('speed')
        if not p:
            return None
        else:
            try:
                return float(p)
            except ValueError:
                return None

    def set_street(self, street):
        """
        Set the value of the <street> element.

        Arguments:
            street -- A thoroughfare within the locality, or a crossing of two thoroughfares
        """
        self._set_sub_text('street', text=street)
        return self

    def get_street(self):
        """
        Return the value of the <street> element.
        """
        return self._get_sub_text('street')

    def set_text(self, text):
        """
        Set the value of the <text> element.

        Arguments:
            text -- A catch-all element that captures any other information about the location
        """
        self._set_sub_text('text', text=text)
        return self

    def get_text(self):
        """
        Return the value of the <text> element.
        """
        return self._get_sub_text('text')

    def set_timestamp(self, timestamp):
        """
        Set the value of the <timestamp> element.

        Arguments:
            timestamp -- UTC timestamp specifying the moment when the reading was taken
        """
        self._set_sub_text('timestamp', text=str(xep_0082.datetime(timestamp)))
        return self

    def get_timestamp(self):
        """
        Return the value of the <timestamp> element as a DateTime.
        """
        p = self._get_sub_text('timestamp')
        if not p:
            return None
        else:
            return xep_0082.datetime(p)

    def set_uri(self, uri):
        """
        Set the value of the <uri> element.

        Arguments:
            uri -- A URI or URL pointing to information about the location
        """
        self._set_sub_text('uri', text=uri)
        return self

    def get_uri(self):
        """
        Return the value of the <uri> element.
        """
        return self._get_sub_text('uri')
