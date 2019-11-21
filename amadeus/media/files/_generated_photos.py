from amadeus.client.decorator import Decorator


class GeneratedPhotos(Decorator, object):
    def get(self, **params):
        '''
        Returns a link with a rendered image of a landscape

        .. code-block:: python

        amadeus.media.files.generated_photos.get(category='MOUNTAIN')

        :param category: the type of landscape to be generated,
            ``"MOUNTAIN"`` or ``"BEACH"``

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v2/media/files/generated-photos', **params)
