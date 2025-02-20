
class FourDigitYearConverter:
    regex = "[0-9]{4}"

    def to_python(value):
        return int(value)

    def to_url(self, value):
        return "%04d" % value
