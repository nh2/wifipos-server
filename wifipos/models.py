import datetime

from mongokit import Document


class Wifisample(Document):

    __database__ = 'wifipos'
    __collection__ = 'wifisamples'

    structure = {
            'pos': (float, float, float),
            'level': float,
            'essid': unicode,
            'bssid': unicode,
            'date_creation': datetime.datetime,
            'submitter_ip': str,  # could also be IPv6
    }

    default_values = {
            'date_creation': datetime.datetime.utcnow
    }

    required_fields = ['pos', 'level', 'essid', 'bssid']

models = [Wifisample]
