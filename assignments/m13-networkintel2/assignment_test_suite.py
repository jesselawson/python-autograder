

# Problem 1
problem1_target = "Class IPAddress"

def test_problem1a():

    target = problem1_target
    msg = "exist and take one constructor argument"

    try:
        a = IPAddress('1.1.1.1')
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)
        


def test_problem1b():
    target = problem1_target
    msg = "set class isntance variable `ip` properly"
    try:
        a = IPAddress('1.1.1.1')
        a.ip == '1.1.1.1'
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)

def test_problem1c():
    target = problem1_target
    msg = "contain a dictionary class instance variable named `activity`"
    try:
        a = IPAddress('1.1.1.1')
        type(a.activity) == 'dict'
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)

def test_problem1d():
    target = problem1_target
    msg = "contain a class instance variable named `activity_url`"
    try:
        a = IPAddress('1.1.1.1')
        type(a.activity_url) == 'dict'
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)

def test_problem1d():
    target = problem1_target
    msg = "contain a class instance variable named `total_activity`"
    try:
        a = IPAddress('1.1.1.1')
        a.total_activity
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)
        
def test_problem1e():
    target = problem1_target
    msg = "contain an integer class instance variable named `failed_logins`"
    try:
        a = IPAddress('1.1.1.1')
        assert isinstance(a.failed_logins, int), f"Expected int, got {str(type(a.failed_logins))} instead."
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)
    
def test_problem1f():
    target = problem1_target
    msg = "contain a boolean class instance variable named `suspicious`"
    try:
        a = IPAddress('1.1.1.1')
        assert isinstance(a.suspicious, bool), f"Expected boolean, got {str(type(a.suspicious))} instead."
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)

"""
5.  Create a member function of the IPAddress class called `is_suspicious`.
    It should return the class instance variable `suspicious`.
"""

problem5_target = "IPAddress.is_suspicious()"

def test_problem5a():
    target = problem5_target
    msg = "exist"
    try:
        a = IPAddress('1.1.1.1')
        a.is_suspicious()
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)

def test_problem5b():
    target = problem5_target
    msg = "return self.suspicious"
    try:
        a = IPAddress('1.1.1.1')
        a.suspicious = True
        assert a.is_suspicious() == True, f"failed to {msg}!"
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)
"""

6.  Create a member function of the IPAddress class called `set_as_suspicious`.
    It should set the class instance variable `suspicious` to True.
"""
problem6_target = "IPAddress.set_as_suspicious()"
def test_problem6a():
    target = problem6_target
    msg = "exist"
    try:
        a = IPAddress('1.1.1.1')
        a.set_as_suspicious()
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)

problem6b_target = "IPAddress.set_as_suspicious()"
def test_problem6b():
    target = problem6_target
    msg = "set self.suspicious to True"
    try:
        a = IPAddress('1.1.1.1')
        a.set_as_suspicious()
        assert a.suspicious == True, f"Expected `True`, got {str(a.suspicious)} instead."
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)

"""
7.  Create a member function of the IPAddress class called `get_ip`.
    It should return the class instance variable `ip`.
"""

problem7_target = "IPAddress.get_ip()"
def test_problem7a():
    target = problem7_target
    msg = "exist"
    try:
        a = IPAddress('1.1.1.1')
        a.get_ip()
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)

def test_problem7b():
    target = problem7_target
    msg = "return IP address"
    try:
        a = IPAddress('1.1.1.1')
        assert a.get_ip() == '1.1.1.1', f"Expected '1.1.1.1', got {a.get_ip()} instead."
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)


"""
8.  Create a member function of the IPAddress class called `add_activity`.
    It should take two parameter: `some_activity` and `some_url`.
    It should append `some_activity` to the `activity` class instance variable.
    It should append `some_url` to the `activity_url` class instance variable.
    It should increment the `total_activity` class instance variable by 1.
    It should increment the `failed_logins` class instance variable by 1
        if `some_activity` is "login_failed". 
"""

problem8_target = "IPAddress.add_activity()"
def test_problem8a():
    target = problem8_target
    msg = "exist and take two arguments"
    try:
        a = IPAddress('1.1.1.1')
        a.add_activity(None, None)
        #assert a.get_ip() == '1.1.1.1', f"Expected '1.1.1.1', got {a.get_ip()} instead."
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)

def test_problem8b():
    target = problem8_target
    msg = "append `some_url` to the `activity_url` class instance variable."
    try:
        a = IPAddress('1.1.1.1')
        a.add_activity("test", "test.com")
        assert a.activity_url[0] == "test.com", f"Expected 'test.com', got {a.activity[0]} instead."
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)

def test_problem8c():
    target = problem8_target
    msg = "append `some_activity` to the `activity` class instance variable."
    try:
        a = IPAddress('1.1.1.1')
        a.add_activity("test", "test.com")
        assert a.activity[0] == "test", f"Expected 'test', got {a.activity[0]} instead."
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)

def test_problem8d():
    target = problem8_target
    msg = "increment the `total_activity` class instance variable by 1"
    try:
        a = IPAddress('1.1.1.1')
        a.total_activity = 0
        a.add_activity("test", "test.com")
        assert a.total_activity == 1, f"Expected total_activity == 1, got {str(a.total_activity)} instead."
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)

def test_problem8e():
    target = problem8_target
    msg = "increment the `failed_logins` class instance variable by 1 if `some_activity` == 'login_failed'"
    try:
        a = IPAddress('1.1.1.1')
        a.total_activity = 0
        a.failed_logins = 0
        a.add_activity("login_failed", "test.com")
        assert a.failed_logins == 1, f"Expected failed_logins == 1, got {str(a.failed_logins)} instead."
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)

"""
9.  Create a member function of the IPAddress class called `get_total_activity`.
    It should return the `total_activity` class instance variable.
"""

problem9_target = "IPAddress.get_total_activity()"

def test_problem9a():
    target = problem9_target
    msg = "exist"
    try:
        a = IPAddress('1.1.1.1')
        a.get_total_activity()
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)

def test_problem9b():
    target = problem9_target
    msg = "return the `total_activity` class instance variable"
    try:
        a = IPAddress('1.1.1.1')
        a.add_activity("login_failed", "test.com")
        assert a.get_total_activity() == 1, f"Expected get_total_activity() == 1, got {str(a.get_total_activity())} instead."
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)
"""
10. Create a member function of the IPAddress class called `get_failed_logins`.
    It should return the `failed_logins` class instance variable. 
"""

problem10_target = "IPAddress.get_failed_logins()"

def test_problem_10a():
    target = problem10_target
    msg = "exist"
    try:
        a = IPAddress('1.1.1.1')
        a.get_failed_logins()
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)

def test_problem_10b():
    target = problem10_target
    msg = "return the `failed_logins` class instance variable"
    try:
        a = IPAddress('1.1.1.1')
        a.failed_logins = 10
        assert a.get_failed_logins() == 10, f"Given dummy data, expected get_failed_logins() == 10. Got {a.get_failed_logins()} instead."
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)

"""
11. Create a member function of the IPAddress class called `get_flar`.
    It should return `get_failed_logins()` divided by `get_total_activity()` 
        rounded to the nearest two decimals.
    Hint: Use the round() function:
        return round(first_func() / second_func(), 2)
"""

problem11_target = "IPAddress.get_flar()"

def test_problem_11a():
    target = problem11_target
    msg = "exist"
    try:
        a = IPAddress('1.1.1.1')
        a.failed_logins = 10
        a.total_activity = 20
        a.get_flar()
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)

def test_problem_11b():
    target = problem11_target
    msg = "return get_failed_logins() / get_total_activity() rounded to nearest 2 decimals"
    try:
        a = IPAddress('1.1.1.1')
        a.failed_logins = 10
        a.total_activity = 20
        assert a.get_failed_logins() / a.get_total_activity() == a.get_flar(), f"Expected {a.get_failed_logins() / a.get_total_activity()}. Got {a.get_flar()} instead."
    except Exception as e:
        return jel_exception(target,e,msg)
    else:
        return jel_passing(target,msg)
