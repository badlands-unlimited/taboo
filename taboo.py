# ok

from datetime import datetime, timedelta

class Taboo():
    def __init__(self):
        self.obligations = [
            {
              'activity': "nap", 
              "start": (16, 0), 
              "length": (3, 0), 
              "frequency": [0,1,2,3,4,5,6], 
              "distractibility": 80
            },
            {
              "activity": "therapy", 
              "start": (15, 0), 
              "length": (1, 0), 
              "frequency": [2], 
              "distractibility": 0
            }
        ] 
        self.trust = 10 # / 100

    def distractibility(self, now):
        # go through and check if there's an obligation right now
        for obligation in obligations:
            if now.weekday() in obligation['frequency']:
                # get length
                (l_hr, l_min) = obligation["length"]
                length = timedelta(hours=l_hr, minutes=l_min)
                # get start time
                (s_hr, s_min) = obligation["start"]
                start  = now.replace(hour=int(s_hr), minute=int(s_min), second=0, microsecond=0)
                if now > start and now < (start + length):
                    return obligation["distractibility"]
        #if not she's free!
        return 100

    # questions

    def initiate(self, phone):
        # check if theres memory
        if hasAccount(phone):
            self.reinitiate(phone)
        else:
            # make an account for the texter
            # 
            pass

    def reinitiate(self):
        pass

    # replies

    # get her a venmo account ???
    def request_venmo_charge(self, phone, amount, reason):
        pass

    def send_message(self, phone, message):
        pass

    def schedule_action(self):
        # check urgency of thing
        # schedule venmo charges
        # schedule responses
        pass

class User():
    def __init__(self, phone):
        return "HELP!!!!!"