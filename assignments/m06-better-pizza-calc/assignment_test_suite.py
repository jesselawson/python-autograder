"""
Assignment test suite for M06 "Better Pizza Tool"

A lot of these tests are the same ones that are used for the Module 5 
project. 

"""

# Problem 1
problem1_target = "topping_ids"

def build_test_for_topping(id, price):
    try:
        return jel_assert(
                problem3_target, 
                get_topping_cost(id) == price,
                f"return {price} when given '{id}'"
        )
    except NameError as e:
        return jel_NameError(problem3_target, e)
    except TypeError as e:
        return jel_TypeError(problem3_target, e)

def test_get_size_cost_L():
    try:
        return jel_assert(
                problem1_target, 
                get_size_cost('L') == 5.00, 
                "return 5.00 when given 'L'"
            )
    except NameError as e:
        return jel_NameError(problem1_target, e)
    except TypeError as e:
        return jel_TypeError(problem1_target, e)

def test_get_size_cost_M():
    try:
        return jel_assert(
                problem1_target, 
                get_size_cost('M') == 4.00, 
                "return 4.00 when given 'M'"
            )
    except NameError as e:
        return jel_NameError(problem1_target, e)
    except TypeError as e:
        return jel_TypeError(problem1_target, e)

def test_get_size_cost_S():
    try:
        return jel_assert(
                problem1_target, 
                get_size_cost('S') == 3.00, 
                "return 3.00 when given 'S'"
            )
    except NameError as e:
        return jel_NameError(problem1_target, e)
    except TypeError as e:
        return jel_TypeError(problem1_target, e)      

# Problem 2
problem2_target = "get_sauce_cost()"

def test_get_sauce_cost_R():
    try:
        return jel_assert(
                problem2_target, 
                get_sauce_cost('R') == 1.35, 
                "return 1.35 when given 'R'"
            )
    except NameError as e:
        return jel_NameError(problem2_target, e)
    except TypeError as e:
        return jel_TypeError(problem2_target, e)

def test_get_sauce_cost_W():
    try:
        return jel_assert(
                problem2_target, 
                get_sauce_cost('W') == 2.15, 
                "return 2.15 when given 'W'"
        )
    except NameError as e:
        return jel_NameError(problem2_target, e)
    except TypeError as e:
        return jel_TypeError(problem2_target, e)

# Problem 3
problem3_target = "get_topping_cost()"

def build_test_for_topping(id, price):
    try:
        return jel_assert(
                problem3_target, 
                get_topping_cost(id) == price,
                f"return {price} when given '{id}'"
        )
    except NameError as e:
        return jel_NameError(problem3_target, e)
    except TypeError as e:
        return jel_TypeError(problem3_target, e)

def test_get_topping_cost_C():
    return build_test_for_topping('C', 0.45)

def test_get_topping_cost_I():
    return build_test_for_topping('I', 0.85)

def test_get_topping_cost_P():
    return build_test_for_topping('P', 0.55)

def test_get_topping_cost_O():
    return build_test_for_topping('O', 0.25)

def test_get_topping_cost_H():
    return build_test_for_topping('H', 1.15)

def test_get_topping_cost_K():
    return build_test_for_topping('K', 0.75)

def test_get_topping_cost_Y():
    return build_test_for_topping('Y', 2.10)

def test_get_topping_cost_N():
    return build_test_for_topping('N', 0.95)

# Problem 4
problem4_target = "get_specialty_cost()"

def test_get_specialty_cost_california():
    try:
        return jel_assert(
                problem4_target, 
                get_specialty_cost("A") == (
                    get_topping_cost("C") + 
                    get_topping_cost("Y") + 
                    get_topping_cost("N")
                ), 
                "return 3.50 when given 'A' (The Super California)"
            )
    except NameError as e:
        return jel_NameError(problem4_target, e)
    except TypeError as e:
        return jel_TypeError(problem4_target, e)

def test_get_specialty_cost_manhattan():
    try:
        return jel_assert(
                problem4_target, 
                get_specialty_cost("B") == (
                    get_topping_cost("H") + 
                    get_topping_cost("O") + 
                    get_topping_cost("C") +
                    get_topping_cost("K")
                ), 
                "return 2.60 when given 'B' (The Salty Manhattan)"
            )
    except NameError as e:
        return jel_NameError(problem4_target, e)
    except TypeError as e:
        return jel_TypeError(problem4_target, e)

def test_get_specialty_cost_unkissable():
    try:
        return jel_assert(
                problem4_target, 
                get_specialty_cost("C") == (
                    get_topping_cost("K") + 
                    get_topping_cost("Y")
                ), 
                "return 2.85 when given 'C' (The Unkissable)"
            )
    except NameError as e:
        return jel_NameError(problem4_target, e)
    except TypeError as e:
        return jel_TypeError(problem4_target, e)

def test_get_specialty_cost_mcmeatface():
    try:
        return jel_assert(
                problem4_target, 
                get_specialty_cost("D") == (
                    get_topping_cost("C") + 
                    get_topping_cost("I") +
                    get_topping_cost("P") +
                    get_topping_cost("O")
                ), 
                "return 2.10 when given 'D' (Meaty McMeatface)"
            )
    except NameError as e:
        return jel_NameError(problem4_target, e)
    except TypeError as e:
        return jel_TypeError(problem4_target, e)

def test_get_specialty_cost_vegetarian():
    try:
        return jel_assert(
                problem4_target, 
                get_specialty_cost("E") == (
                    get_topping_cost("O") + 
                    get_topping_cost("N")
                ), 
                "return 1.20 when given 'E' (The Vegetarian)"
            )
    except NameError as e:
        return jel_NameError(problem4_target, e)
    except TypeError as e:
        return jel_TypeError(problem4_target, e)

