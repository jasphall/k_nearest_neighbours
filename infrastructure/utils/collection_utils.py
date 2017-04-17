class CollectionUtils(object):

    @staticmethod
    def unwrap_elements(elements):
        result = []

        for e in elements:
            if isinstance(e, list):
                for subelement in e:
                    result.append(subelement)
            else:
                result.append(e)

        return result
