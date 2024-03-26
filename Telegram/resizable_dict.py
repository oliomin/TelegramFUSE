

class ResizableDict:
    def __init__(self, default_factory = None):
        self.preimage = []
        self.image    = []
        self.default_factory = default_factory

    def __getitem__(self, key):
        try:
            _id = self.preimage.index(key)
            return self.image[_id]
        except ValueError:
            if self.default_factory:
                self[key] = self.default_factory()
                return self[key]
            else:
                raise IndexError

    def __setitem__(self, key, value):
        try:
            _id = self.preimage.index(key)
        except ValueError:
            self.preimage.append(key)
            self.image.append(value)
        else:
            self.image[_id] = value
        assert len(self.preimage) == len(self.image)

    def __delitem__(self, key):
        try:
            _id = self.preimage.index(key)
            del self.preimage[_id]
            del self.image[_id]
        except ValueError:
            raise IndexError

    def __repr__(self):
        _ = {k: v for k, v in zip(self.preimage, self.image)}
        return repr(_)

    def items(self):
        return zip(self.preimage, self.image)

    def keys(self):
        return self.preimage

    def values(self):
        return self.values
