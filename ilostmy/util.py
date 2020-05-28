from datetime import date


def pprint_iso_date(datestring):
    # return date.fromisoformat(datestring).strftime('%m/%d/%y')
    return date.fromisoformat(datestring).strftime('%x')
