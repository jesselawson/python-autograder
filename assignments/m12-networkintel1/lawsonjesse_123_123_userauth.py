
import os



# The class LogParser will parse a directory of log files in the following format:
# <timestamp> <ip> <activity> <url>

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


class LogParser:
    def __init__(self, filename, sensitivity = 0.75):
        self.filename = filename
        self.all_ips = [] # A list of all tracked IPs (IPAddress objects)
        
        # The sensitivity is a decimal from 0 to 1, representing the percent 
        # of total activity that can be failed logins before marking the IP
        # as suspicious. 
        self.sensitivity = sensitivity
        self.verified = False
        self.complete = False

        # Verify filename exists
        if os.path.exists(filename):
            self.verified = True


    def parse(self):
        """
        Primary function of LogParser objects. This parses self.filename 
        and extracts any suspicious_ips (according to self.sensitivity), recording 
        them in the self.suspicious_ips dict.
        """
        if not self.verified:
            print(f"Error: Could not parse {filename}. I don't think it exists.")
            exit() # Quit the program

        # Open the file and start tracking IPs
        print("Parsing log file...")
        with open(self.filename, "r") as the_file:
            for line in the_file:
                # line format: <timestamp> <ip> <activity> <url>
                parts = line.split()
                the_ip = parts[1]
                the_activity = parts[2]
                the_url = parts[3]

                #print(f"Parsing IP {the_ip}:")

                # Assume this is a new IP.
                a_new_ip = True
                
                # Loop through all_ips and if we find it, set a_new_ip to false,
                # and add the activity to our IP.
                for ip in self.all_ips:
                    #print(f"Comparing {ip.get_ip()} == {the_ip}...")
                    if ip.get_ip() == the_ip:
                        #print(f"\tNot a new IP!")
                        a_new_ip = False
                        ip.add_activity(the_activity, the_url)

                if a_new_ip:
                    #print(f"\tCreating new object...")
                    the_ip_object = IPAddress(the_ip)
                    the_ip_object.add_activity(the_activity, the_url)
                    self.all_ips.append(the_ip_object)
                    
        
        # Now we're finished parsing each line in the file

        # We now need to flag any IP with flar > sensitivity as suspicious

        # Loop through all_ips and find any whose flar is > sensitivity
        print("Analyzing suspicious activity...")
        for ip in self.all_ips:
            if ip.get_flar() > self.sensitivity:
                #print(f"Setting {the_ip} as suspicious ({ip.get_flar()})")
                ip.set_as_suspicious()
        

    

    def report(self, out_file = "report.txt"):
        # Writes the suspicious IPs to out_file (a file)
        # Format: <ip> <flar> (<total_activity>/<num_failed_logins>)
        
        f = open("report.txt", "w")

        print("Building report...")

        for ip in self.all_ips:
            #print(f"report(): Checking IP {ip.get_ip()}... ")
            if ip.is_suspicious():
                f.write(f"{ip.get_ip()} {ip.get_flar()} ({ip.get_total_activity()}/{ip.get_failed_logins()})\n")
        
        f.close()

def main():
    
    parser = LogParser("traffic_logs.txt", 0.35) # Parse file "traffic_logs.txt" with 35% sensitivity

    parser.parse()

    parser.report("report.txt")

if __name__ == '__main__':
    main()