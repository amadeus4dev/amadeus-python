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

    @staticmethod
    def __page_number_for(name, response):
        try:
            url = response.result['meta']['links'][name]
            return url.split('page%5Boffset%5D=')[1].split('&')[0]
        except Exception:
            return None
