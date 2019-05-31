import copy


# A set of helper methods to allow the validating of
# arguments past into the Client
class Pagination(object):

    def previous(self, response):
        return self.__page('previous', response)

    def next(self, response):
        return self.__page('next', response)

    def first(self, response):
        return self.__page('first', response)

    def last(self, response):
        return self.__page('last', response)

    # PRIVATE

    def __page(self, name, response):
        page_number = self.__page_number_for(name, response)
        if page_number is None:
            return None
        params = copy.deepcopy(response.request.params)
        if 'page' not in params:
            params['page'] = {}
        params['page']['offset'] = page_number
        return self.request(
            response.request.verb,
            response.request.path,
            params
        )

    def __page_number_for(self, name, response):
        try:
            return response.result['meta']['links'][name].split('=')[-1]
        except Exception:
            return None
