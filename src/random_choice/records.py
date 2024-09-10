class Probability:
    def __set_name__(self, _, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, obj, **kwargs):
        value = getattr(obj, self.private_name)
        return value

    def __set__(self, obj, value):
        if not 0 <= value <= 1:
            raise ValueError("Probability must be between 0 and 1")
        setattr(obj, self.private_name, value)
