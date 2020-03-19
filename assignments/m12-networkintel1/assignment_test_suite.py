import pytest

# Problem 1
problem1_target = "Shark('test', 5)"

def test_shark_class_contains_health_variable():

    test = Shark("Testman", 5)

    # Check if self.health was created
    try:
        test.health
    except AttributeError:
        return jel_assert(
            problem1_target,
            False,
            f"do anything because no class instance variable named `health` was found"
        )

    try:
        return jel_assert(
                problem1_target, 
                test.health == 5,
                f"set class instance variable `health` to 5"
            )
    except NameError as e:
        return jel_NameError(problem1_target, e)
    except TypeError as e:
        return jel_TypeError(problem1_target, e)

test2_target = "get_health()"

def test_shark_class_get_health():
    
    test = Shark("Testman", 5)

    # Check if self.health was created
    try:
        test.get_health()
    except AttributeError:
        return jel_assert(
            test2_target,
            False,
            f"do anything because no class method named `get_health()` was found!"
        )

    try:
        return jel_assert(
                test2_target, 
                test.get_health() == 5,
                f"return 5 when constructor was passed 5."
            )
    except NameError as e:
        return jel_NameError(test2_target, e)
    except TypeError as e:
        return jel_TypeError(test2_target, e)

test3_target = "bite()"

def test_shark_class_bite():
    
    test = Shark("Testman", 50)
    target = Shark("Bitee", 50)

    # Check if self.health was created
    try:
        test.bite(target)
    except AttributeError:
        return jel_assert(
            test3_target,
            False,
            f"do anything because no class method named `bite()` was found"
        )

    try:
        return jel_assert(
                test3_target, 
                target.get_health() == 25,
                f"subtract 25 from target's health (got {target.get_health()})"
            )
    except NameError as e:
        return jel_NameError(test3_target, e)
    except TypeError as e:
        return jel_TypeError(test3_target, e)

test4_target = "die()"

def test_shark_class_die():
    
    test = Shark("Testman", 50)
    target = Shark("Bitee", 25)

    # Check if self.health was created
    try:
        target.die()
    except AttributeError:
        return jel_assert(
            test4_target,
            False,
            f"do anything because no class method named `die()` was found"
        )

    try:
        return jel_assert(
                test4_target, 
                target.get_health() == 0,
                f"set health to zero"
            )
    except NameError as e:
        return jel_NameError(test4_target, e)
    except TypeError as e:
        return jel_TypeError(test4_target, e)