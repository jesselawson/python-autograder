
import os



# For the M13 
class IPAddress:
    def __init__(self, ip):
        self.ip = ip
        self.activity = []
        self.activity_url = []
        self.total_activity = 0
        self.failed_logins = 0
        self.suspicious = False
        # ip = the ip address of the record
        # failed_logins = The number of failed logins this ip has had
        # flar = "Failed Login Activity Ratio". (failed_logins) / (total_activity)

    def is_suspicious(self):
        return self.suspicious

    def set_as_suspicious(self):
        self.suspicious = True

    def get_ip(self):
        return self.ip

    def add_activity(self, some_activity, some_url):
        self.activity.append(some_activity)
        self.activity_url.append(some_url)
        
        # Recalculate total_activity and failed_logins
        self.total_activity += 1
        if some_activity == "login_failed":
            self.failed_logins += 1

    def get_total_activity(self):
        return self.total_activity
        #return len(self.activity)

    def get_failed_logins(self):
        return self.failed_logins
        #num_failed = 0
        #for a in self.activity:
        #    num_failed += 1 if a == "login_failed"
        #return num_failed

    def get_flar(self):
        return round( (self.get_failed_logins() / self.get_total_activity()), 2)