
class FENStringConverter:
    regex = '[^\.]{8,100}'

    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return value


class FileExtensionConverter:
    regex = '(svg|jpg|png)'

    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return value
