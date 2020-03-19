# This script is intended to automatically generate log files 
# for use in the M13, 14, and 15 assignments. 

# log entry format: <timestamp> <ip> <activity> <url>

import random

possible_activities = [
        'login_success',
        'get_request',
        'post_request',
        '404_error',
        '500_error',
        'node_wait',
        'redirect_to',
        'login_failed',
        'login_failed'
    ]

url_builder_parts_left = [
    'nsa.gov/',
    'dmbnode3.nsa.gov/',
    'dmdnode2.nsa.gov/',
    'sigintportal.nsa.gov/',
    'elintportal.nsa.gov/',
    'humintportal.nsa.gov/',
    'siprnet-gateway.nsa.gov/',
    'siprnet-reports.nsa.gov/',
    'projectelliot.nsa.gov/',
    'project7.nsa.gov/'
]

url_builder_parts_right = [
    'adm_groups/finder/',
    'adm_groups/reports/',
    'account/settings/',
    'reports/query/',
    'reports/std/batch/',
    'services/',
    'cms/account/settings/',
    'cms/account/roles/',
    'cms/builder/',
    'dept_resources/manager/',
    'dept_resources/fileshare/',
    'snet_3/fileshare/',
    'snet_6/fileshare/',
    'local_fs/public/',
    'local_fs/private/',
    'portalguard/sso/',
    'reports/manager/',
    'reports/webfeed/'

]

def get_random_url():
    a = url_builder_parts_left[random.randint(0,len(url_builder_parts_left)-1)]
    b = url_builder_parts_right[random.randint(0,len(url_builder_parts_right)-1)]

    return f"{a}{b}"

def get_random_activity():
    return possible_activities[random.randint(0, len(possible_activities)-1)]


def get_random_timestamp():
    a = str(random.randint(0,2000))
    b = str(random.randint(2001,5000))
    c = str(random.randint(5001,99000))
    return f"{a}{b}{c}"

# 192.168.5.44
#   a.  b. c. d.

known_bad_ips = [
    '192.168.31.4',
    '192.168.55.89',
    '192.168.55.24',
    '192.168.31.6'
]

known_good_ips = [
    '192.168.55.75',
    '192.168.55.90',
    '192.168.31.3',
    '192.168.31.11',
    '192.168.31.12',
    '192.168.31.4',
    '192.168.31.2',
    '192.168.31.13',
    '192.168.31.14',
    '192.168.31.19',
    '192.168.55.91',
    '192.168.55.92',
    '192.168.55.93.',
    '192.168.55.94',
    '192.168.55.81',
    '192.168.55.82',
    '192.168.55.83',
    '192.168.55.84'
]

def get_random_ip():
    # Gen random ones, but also select some from a known list to ensure 
    # the likelihood of offenders in the resultant traffic log file

    if random.random() > 0.8: # So, 20% of the time, theoretically
        return known_bad_ips[random.randint(0,len(known_bad_ips)-1)]
    else:
        return known_good_ips[random.randint(0,len(known_good_ips)-1)]

def main():
    
    
    
    f = open("traffic_logs.txt", "w")

    for a in range(10000):

        
        some_ip = get_random_ip()
        some_timestamp = get_random_timestamp()
        
        # If we have an IP from our known_ips, default activity to "login_failed"
        include = True if random.random() > 0.5 else False
        some_activity = "login_failed" if some_ip in known_bad_ips and include == True else get_random_activity()

        some_url = get_random_url()
        

        f.write(f"{some_timestamp} {some_ip} {some_activity} {some_url}\n")

    f.close()

    


if __name__ == '__main__':
    main()
        

