
# Obfuscated name to prevent possible conflict with student file
test_qwertyuioplkjhgfdsa_number = 0

def jel_assert(target, expr, should_msg):
    global test_qwertyuioplkjhgfdsa_number
    test_qwertyuioplkjhgfdsa_number += 1
    m = f"Test #{test_qwertyuioplkjhgfdsa_number} "
    try:
        expr
    except Exception as e:
        return m + f"FAILED: {target} failed to {should_msg}!\r\t{e.__class__.__name__}: {e}"
    else:
        return m + f"passed: {target} should {should_msg}"

def jel_test(msg):
    # Build the message
    global test_qwertyuioplkjhgfdsa_number
    test_qwertyuioplkjhgfdsa_number += 1
    m = f"Test #{test_qwertyuioplkjhgfdsa_number} "
    
    return m + msg
    
def jel_passing(target, msg):
    return jel_test(f"passed: {target} should {msg}")

def jel_exception(target, e, msg):
    #return jel_assert(target, False,f"work:\r\t{e.__class__.__name__}: {e}")
    return jel_test(f"FAILED: {target} failed to {msg};\r\t{e.__class__.__name__}: {e}")
    
# BEGIN TEST SUITE INJECTION ===================================================

#<TEST_SUITE_INJECTION_MARKER>

# END TEST SUITE INJECTION =====================================================

# Custom test runner
test_results = []
dir_result = dir(sys.modules[__name__])
dir_result
for some_function in dir_result:
    item = getattr(sys.modules[__name__], some_function)
    if some_function.startswith("test_") and callable(item):
        r = item()
        test_results.append(r) # All tests call jel_assert, which returns a string message
output = ""
test_results
for r in test_results:
    output += "* "
    output += str(r) 
    output += "\n\n"
print(output)
        