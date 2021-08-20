import datetime


class DateTime:
    """
    Provides methods to retrieve date and/or time data
    """

    @staticmethod
    def get_current_hour() -> int:
        return datetime.datetime.now().hour

    @staticmethod
    def get_current_time() -> str:
        return datetime.datetime.now().strftime("%I:%M")

    @staticmethod
    def get_todays_date() -> dict:
        return {
            'day': str(datetime.datetime.now().day),
            'month': str(datetime.datetime.now().month),
            'year': str(datetime.datetime.now().year)
        }



