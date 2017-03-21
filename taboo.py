# ok

from datetime import datetime, timedelta

class Taboo():
    def __init__(self):
        self.obligations = [] # {activity, cron reoccurance}
        self.trust = 10 # / 100

    def help(self, ):
        frick

    def obligated(self, datetime):
        now  = datetime.datetime.now()

        for obligation in self.obligations:
            # [min, hour, day/month, month, day/week]
            cron = obligation.cron.split(" ")
            # check day of week
            # check month
            # check hour/minute
        return 100

    # questions

    def initiate(self):
        pass

    def reinitiate(self):
        pass


    # replies

    def request_venmo_charge(self, phone, amount, reason):
        pass

    def send_message(self, phone, message):
        pass

    def schedule_action(self):
        # check urgency of thing
        # schedule venmo charges
        # schedule responses
        pass