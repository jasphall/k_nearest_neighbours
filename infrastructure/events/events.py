from infrastructure.events.alghoritm_property_changed_event import AlghoritmPropertyChangedEvent
from infrastructure.events.point_added_event import PointAddedEvent
from infrastructure.events.point_classified_event import PointClassifiedEvent


class Events(object):
    """ Container for different types of events """
    point_added = PointAddedEvent()

    point_classified = PointClassifiedEvent()

    knn_property_changed = AlghoritmPropertyChangedEvent()