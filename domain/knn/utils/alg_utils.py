class AlghoritmUtils:

    @staticmethod
    def normalize_observation(o, min_x, min_y, max_x, max_y):
        """ Returns normalized observation """
        normalized_x = AlghoritmUtils.normalize_value(o.x, min_x, max_x)
        normalized_y = AlghoritmUtils.normalize_value(o.y, min_y, max_y)
        return o.change_data(normalized_x, normalized_y)

    @staticmethod
    def normalize_value(value, min, max):
        """ Returns normalized value """
        return 1.0 * ((value - min) / (max - min))

    @staticmethod
    def denormalize_observation(o, min_x, min_y, max_x, max_y):
        """ Returns denormalized observation """
        denormalized_x = AlghoritmUtils.denormalize_value(o.x, min_x, max_x)
        denormalized_y = AlghoritmUtils.denormalize_value(o.y, min_y, max_y)
        return o.change_data(denormalized_x, denormalized_y)

    @staticmethod
    def denormalize_value(value, min, max):
        """ Returns denormalized value """
        return 1.0 * value * (max - min) + min

    @staticmethod
    def remove_most_distanced_neighbour(neighbours):
        """ Removes neighbour with biggest distance from current neighbours list """
        if len(neighbours) <= 0:
            return

        neighbour_to_delete = neighbours[0]

        for i in range(1, len(neighbours)):
            n = neighbours[i]
            if n['distance'] > neighbour_to_delete['distance']:
                neighbour_to_delete = n

        neighbours.remove(neighbour_to_delete)
