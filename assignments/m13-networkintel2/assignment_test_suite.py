

# Problem 1
problem1_target = "Class IPAddress"

def test_problem1():

    target = problem1_target

    # Check if self.health was created
    try:
        a = IPAddress('1.1.1.1')
    except Exception as e:
        jel_Exception(target,e)

    try:
        return jel_assert(
                target, 
                a.ip == "1.1.1.1",
                f"set class instance variable `health` to 5"
            )
    except Exception as e:
        jel_Exception(target,e)
