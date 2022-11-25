class BaseConverter:
    def to_python(self, value):
        return int(value)

class FourDigitYearConverter(BaseConverter):
    regex = r'(20[2-9]\d)' # 2020-2100

    def to_url(self, value):
        return f'{value:04d}'

class TwoDigitMonthConverter(BaseConverter):
    regex = r'(0[1-9]|1[0-2])' # 01-12

    def to_url(self, value):
        return f'{value:02d}'

class TwoDigitDayConverter(BaseConverter):
    regex = r'(3[01]|0\d|[12]\d)' # 0-31

    def to_url(self, value):
        return f'{value:02d}'
