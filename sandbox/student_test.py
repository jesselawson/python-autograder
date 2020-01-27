import pytest

# Step 1: place "import pytest" at start of file
# Include any assignment data relevant for the student, like the 
# date I graded it and whatnot

# STUDENT CODE
def helper(string):
  return string[:5]


# ASSIGNMENT TEST SUITE

fail_messages = []
pass_messages = []

def jel_assert(expr, should_msg):
  msg = None
  if expr != True:
    msg = f"Failed to {should_msg}"
    fail_messages.append(msg)
    pytest.fail(msg)
  else:
    msg = f"Passed: {should_msg}"
    pass_messages.append(msg)

def test_helper_returns_first_five_characters():
  jel_assert(helper("QWERTYUIOP") == "QWERT", "return first five characters")

def test_helper_returns_first_six_characters():
  jel_assert(helper("QWERTYUIOP") == "QWERTY", "return first six characters")

#def test_helper_returns_first_five():
#  jel_assert(helper("QWERTYUIOP") == "AWERT", "Helper did not get the first five characters!")

def jel_postprocessing():
  global fail_messages
  global pass_messages
  """Perform postprocessing on test suite and results"""
  print(f"Total tests: {len(fail_messages) + len(pass_messages)}")
  for t in pass_messages:
    print(t)
  for t in fail_messages:
    print(t)

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    terminalreporter.section('Failed tests')
    failures = [report.nodeid.split('::')[-1]
                for report in terminalreporter.stats.get('failed', [])]
    terminalreporter.write('\n'.join(failures) + '\n')
    jel_postprocessing()