
# Test suite for M03 Chat Bot

# Attention to syntax;
# Attention to specifications;
# Troubleshooting



def test_2a():
    target = "process_input()"
    try:
        jel_assert(
        target,
        process_input("What is your name?") == "My name is CHAT BOT.",
        "return 'My name is CHAT BOT' when asked what its name is"
    )
    except NameError as e:
        return jel_NameError(target, e)
    except TypeError as e:
        return jel_TypeError(target, e)

def test_2b():
    target = "process_input()"
    try:
        jel_assert(
        target,
        process_input("What is the answer to life?") == "Proper hydration!",
        "return 'Proper hydration!' when asked what the answer to life is"
    )
    except NameError as e:
        return jel_NameError(target, e)
    except TypeError as e:
        return jel_TypeError(target, e)

def test_2c():
    target = "process_input()"
    try:
        jel_assert(
        target,
        process_input("What is 56*13?") == "That's easy: 728!",
        "return 'That\'s easy: 728!' when asked what 56*13 is"
    )
    except NameError as e:
        return jel_NameError(target, e)
    except TypeError as e:
        return jel_TypeError(target, e)

def test_2d():
    target = "process_input()"
    try:
        jel_assert(
        target,
        process_input("Are you sentient?") == "What do you think?",
        "return 'What do you think?' when asked what the answer to life is"
    )
    except NameError as e:
        return jel_NameError(target, e)
    except TypeError as e:
        return jel_TypeError(target, e)

def test_2e():
    target = "process_input()"
    try:
        jel_assert(
        target,
        process_input("Are you sentient?") == "What do you think?",
        "return 'What do you think?' when asked what the answer to life is"
    )
    except NameError as e:
        return jel_NameError(target, e)
    except TypeError as e:
        return jel_TypeError(target, e)
        
def test_2f():
    target = "process_input()"
    try:
        jel_assert(
        target,
        process_input("What did you cost?") == f"Total funding was ${total_grant_funds + total_donations}",
        "return total funding when asked how much it cost"
    )
    except NameError as e:
        return jel_NameError(target, e)
    except TypeError as e:
        return jel_TypeError(target, e)
        