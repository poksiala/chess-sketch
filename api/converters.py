
class FENStringConverter:
    regex = \
        '([RNBQKPrnbqkp1-8]{1,8}/){7}[RNBQKPrnbqkp1-8]{1,8}' + \
        '\s[wb]\s[KQkq\-]{1,4}\s[a-h36\-]\s\d*\s\d*'

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
