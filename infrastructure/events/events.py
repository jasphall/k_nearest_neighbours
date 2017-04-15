from infrastructure.events.point_added_event import PointAddedEvent


class Events(object):
    """ Container for different types of events """
    point_added = PointAddedEvent()