import datetime


class Time:
    # TODO -> Crea un método que te devuelva la current hour
    def get_current_time(self):
        return datetime.datetime.now().strftime("%I:%M")

    def get_todays_date(self) -> dict:
        # day = str(datetime.datetime.now().day)
        # month = str(datetime.datetime.now().month)
        # year = str(datetime.datetime.now().year)

        date_dict = {'day': str(datetime.datetime.now().day),
                     'month': str(datetime.datetime.now().month),
                     'year': str(datetime.datetime.now().year)}

        return date_dict



