
# Problem 1
problem1_target = "update_username()"

def test_update_username_0():

    example = [
        { "username": "jesse", "password": None},
        { "username": "morty", "password": "ooh wee"}
    ]

    try:
        return jel_assert(
                problem1_target, 
                update_username(example, "jesse", "misterpants") == True,
                f"return True when the username was changed"
            )
    except NameError as e:
        return jel_NameError(problem1_target, e)
    except TypeError as e:
        return jel_TypeError(problem1_target, e)


# Problem 1.3
def test_update_username_2():

    example = [
        { "username": "jesse", "password": None},
        { "username": "morty", "password": "ooh wee"}
    ]

    try:
        return jel_assert(
                problem1_target, 
                update_username(example, "nothere", "bloop") == False,
                f"return False if the username was not found"
            )
    except NameError as e:
        return jel_NameError(problem1_target, e)
    except TypeError as e:
        return jel_TypeError(problem1_target, e)

# Problem 1.2
def test_update_username_1():

    example = [
        { "username": "jesse", "password": None},
        { "username": "morty", "password": "ooh wee"}
    ]

    update_username(example, "jesse", "misterpants")

    try:
        return jel_assert(
                problem1_target, 
                example[0]['username'] == "misterpants",
                f"update the username successfully"
            )
    except NameError as e:
        return jel_NameError(problem1_target, e)
    except TypeError as e:
        return jel_TypeError(problem1_target, e)

# Problem 1.2
def test_update_username_1():

    example = [
        { "username": "jesse", "password": None},
        { "username": "morty", "password": "ooh wee"}
    ]

    update_username(example, "jesse", "misterpants")

    try:
        return jel_assert(
                problem1_target, 
                example[0]['username'] == "misterpants",
                f"update the username successfully"
            )
    except NameError as e:
        return jel_NameError(problem1_target, e)
    except TypeError as e:
        return jel_TypeError(problem1_target, e)
    
# Problem 2

def test_generate_password_for_user_0():

    problem2_target = "generate_password_for_user()"

    example = [
        { "username": "jesse", "password": None},
        { "username": "morty", "password": "ooh wee"}
    ]

    generate_password_for_user(example, "jesse")

    try:
        return jel_assert(
                problem2_target, 
                example[0]['password'] is not None,
                f"update the given user's password correctly (was None, now it's '{example[0]['password']}')"
            )
    except NameError as e:
        return jel_NameError(problem2_target, e)
    except TypeError as e:
        return jel_TypeError(problem2_target, e)
