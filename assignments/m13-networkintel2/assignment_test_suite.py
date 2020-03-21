


def test_problem1a2():

    target = "Class IPAddress"
    msg = "exist and take one constructor argument"

    try:
        a = IPAddress('1.1.1.1')
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)
        


def test_problem3():
    
    target = "Class IPAddress"
    msg = "set class instance variable `ip` properly"
    
    try:
        a = IPAddress('1.1.1.1')
        a.ip == '1.1.1.1'
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)
        
def test_problem4a():
    
    target = "Class IPAddress"
    msg = "set class instance variable `activity` properly"
    
    try:
        a = IPAddress('1.1.1.1')
        a.activity == []
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)
        
def test_problem4b():
    
    target = "Class IPAddress"
    msg = "set class instance variable `activity_url` properly"
    
    try:
        a = IPAddress('1.1.1.1')
        a.activity_url == []
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)

def test_problem4c():
    
    target = "Class IPAddress"
    msg = "set class instance variable `total_activity` properly"
    
    try:
        a = IPAddress('1.1.1.1')
        a.total_activity == 0
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)

def test_problem4d():
    
    target = "Class IPAddress"
    msg = "set class instance variable `failed_logins` properly"
    
    try:
        a = IPAddress('1.1.1.1')
        a.failed_logins == 0
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)


def test_problem4e():
    
    target = "Class IPAddress"
    msg = "set class instance variable `suspicious` properly"
    
    try:
        a = IPAddress('1.1.1.1')
        a.suspicious == False
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)