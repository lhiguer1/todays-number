class FourDigitYearConverter:
    regex = r'20\d{2}' # 2000-2099

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return f'{value:04d}'

class TwoDigitMonthConverter:
    regex = r'(?:(?:0[\d])|(?:1[0-2]))' # 01-12

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return f'{value:02d}'

class TwoDigitDayConverter:
    regex = r'(?:3[01]|0\d|[12]\d)' # 01-31

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return f'{value:02d}'