class ObservationContainer(object):
    """ Wrapper that keeps observation and its neighbours """

    def __init__(self, observation, neighbours):
        self.observation = observation
        self.neighbours = neighbours
