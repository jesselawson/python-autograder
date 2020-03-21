

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
        
    
    
        
