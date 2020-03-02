"""
Assignment test suite for M08 "Mid-Term"


"""

# Problem 1
problem1_target = "get_server_details()"

# Random to ensure
testsuite_asdf987_server_ips = ["192.168.0.1", "192.168.11.6", "192.168.12.5", "192.168.45.0"]
testsuite_asdf987_server_names = ["App Server", "Database 1", "Database 2", "Node Balancer"]

def test_get_server_details_0():

    details = get_server_details()
    
    # details[0]
    d0 = f"{testsuite_asdf987_server_ips[0]} ({testsuite_asdf987_server_names[0]})"
    try:
        return jel_assert(
                problem1_target, 
                details[0] == d0,
                f"return a list where element 0 == \"{d0}\""
            )
    except NameError as e:
        return jel_NameError(problem1_target, e)
    except TypeError as e:
        return jel_TypeError(problem1_target, e)

def test_get_server_details_1():

    details = get_server_details()
    
    # details[1]
    d1 = f"{testsuite_asdf987_server_ips[1]} ({testsuite_asdf987_server_names[1]})"
    try:
        return jel_assert(
                problem1_target, 
                details[1] == d1,
                f"return a list where element 1 == \"{d1}\""
            )
    except NameError as e:
        return jel_NameError(problem1_target, e)
    except TypeError as e:
        return jel_TypeError(problem1_target, e)

def test_get_server_details_2():

    details = get_server_details()
    
    # details[2]
    d2 = f"{testsuite_asdf987_server_ips[2]} ({testsuite_asdf987_server_names[2]})"
    try:
        return jel_assert(
                problem1_target, 
                details[2] == d2,
                f"return a list where element 2 == \"{d2}\""
            )
    except NameError as e:
        return jel_NameError(problem1_target, e)
    except TypeError as e:
        return jel_TypeError(problem1_target, e)

def test_get_server_details_3():

    details = get_server_details()
    
    # details[3]
    d3 = f"{testsuite_asdf987_server_ips[3]} ({testsuite_asdf987_server_names[3]})"
    try:
        return jel_assert(
                problem1_target, 
                details[3] == d3,
                f"return a list where element 3 == \"{d3}\""
            )
    except NameError as e:
        return jel_NameError(problem1_target, e)
    except TypeError as e:
        return jel_TypeError(problem1_target, e)

# Problem 2
problem2_target = "get_failed_logins()"

def test_get_failed_logins():

    logins = get_failed_logins()
    
    should_be = [
        '20200106|login_failed|fdf79s8d987d8fd87',
        '20200106|login_failed|a0a0a9d8dd7d6d556',
        '20200107|login_failed|fkjehn4i4n5o4i4j4',
        '20200108|login_failed|cx89xc8xc98cx9c80',
        '20200110|login_failed|d09s09d0sd90sd90d',
        '20200111|login_failed|45kjl45kj3l4kj5k4',
        '20200111|login_failed|wernelkrnr8f79879',
        '20200113|login_failed|cv89d7f984h4k4kjh',
        '20200113|login_failed|fdffasrt434534tgf'
    ]
    try:
        return jel_assert(
                problem2_target, 
                logins == should_be,
                f"return a list containing all failed logins"
            )
    except NameError as e:
        return jel_NameError(problem1_target, e)
    except TypeError as e:
        return jel_TypeError(problem1_target, e)

def test_get_sevice_on_port_3000():
    problem3_target = "get_service_on_port(3000)"
    result = get_service_on_port(3000)
    expected_output = "Service (local dev server) is listening on port 3000."
    
    try:
        return jel_assert(
                problem3_target, 
                result == expected_output,
                f"return a string == \"{expected_output}\""
            )
    except NameError as e:
        return jel_NameError(problem3_target, e)
    except TypeError as e:
        return jel_TypeError(problem3_target, e)

def test_get_sevice_on_port_8081():

    problem3_target = "get_service_on_port(8081)"
    result = get_service_on_port(8081)
    expected_output = "Service (Nginx Reverse Proxy) is listening on port 8081."
    
    try:
        return jel_assert(
                problem3_target, 
                result == expected_output,
                f"return a string == \"{expected_output}\""
            )
    except NameError as e:
        return jel_NameError(problem3_target, e)
    except TypeError as e:
        return jel_TypeError(problem3_target, e)

def test_get_sevice_on_port_2500():

    problem3_target = "get_service_on_port(2500)"
    result = get_service_on_port(2500)
    expected_output = "Service (SMTP Server ID 030001) is listening on port 2500."
    
    try:
        return jel_assert(
                problem3_target, 
                result == expected_output,
                f"return a string == \"{expected_output}\""
            )
    except NameError as e:
        return jel_NameError(problem3_target, e)
    except TypeError as e:
        return jel_TypeError(problem3_target, e)

def test_get_sevice_on_port_4005():

    problem3_target = "get_service_on_port(4005)"
    result = get_service_on_port(4005)
    expected_output = "Service (Crash Scanner 3000F13) is listening on port 4005."
    
    try:
        return jel_assert(
                problem3_target, 
                result == expected_output,
                f"return a string == \"{expected_output}\""
            )
    except NameError as e:
        return jel_NameError(problem3_target, e)
    except TypeError as e:
        return jel_TypeError(problem3_target, e)


def test_get_sevice_on_port_6800():

    problem3_target = "get_service_on_port(6800)"
    result = get_service_on_port(6800)
    expected_output = "Service (Telemetry Collector P278081B) is listening on port 6800."
    
    try:
        return jel_assert(
                problem3_target, 
                result == expected_output,
                f"return a string == \"{expected_output}\""
            )
    except NameError as e:
        return jel_NameError(problem3_target, e)
    except TypeError as e:
        return jel_TypeError(problem3_target, e)

def test_get_sevice_on_port_6800():

    problem3_target = "get_service_on_port(9999)"
    result = get_service_on_port(9999)
    expected_output = "No service is listening on port 9999."
    
    try:
        return jel_assert(
                problem3_target, 
                result == expected_output,
                f"return a string == \"{expected_output}\""
            )
    except NameError as e:
        return jel_NameError(problem3_target, e)
    except TypeError as e:
        return jel_TypeError(problem3_target, e)

# PROBLEM 4

def test_convert_jpg_to_tif():
    problem4_target = "convert_jpg_to_tif(\"something.jpg\")"
    result = convert_jpg_to_tif("something.jpg")
    expected_output = "something.tif"
    
    try:
        return jel_assert(
                problem4_target, 
                result == expected_output,
                f"return the string \"{expected_output}\""
            )
    except NameError as e:
        return jel_NameError(problem3_target, e)
    except TypeError as e:
        return jel_TypeError(problem3_target, e)


def test_get_files_from_day1():
    problem4_target = "get_files_from_day(\"jan\", \"04\")"
    result = get_files_from_day("jan", "04")
    expected_output = [
        'jan04_walkinthepark.tif',
        'jan04_dogsitting.tif'
    ]
    
    try:
        return jel_assert(
                problem4_target, 
                result == expected_output,
                f"return a list containing {expected_output}"
            )
    except NameError as e:
        return jel_NameError(problem3_target, e)
    except TypeError as e:
        return jel_TypeError(problem3_target, e)

def test_get_files_from_day2():
    problem4_target = "get_files_from_day(\"jan\", \"05\")"
    result = get_files_from_day("jan", "05")
    expected_output = [
        'jan05_firstkiss.tif',
        'jan05_wedding1.tif',
        'jan05_wedding2.tif',
        'jan05_firstkiss2.tif',
        'jan05_bridesmaids.tif',
        'jan05_morebridesmaids.tif',
        'jan05_groom.tif'
    ]
    
    try:
        return jel_assert(
                problem4_target, 
                result == expected_output,
                f"return a list containing {expected_output}"
            )
    except NameError as e:
        return jel_NameError(problem3_target, e)
    except TypeError as e:
        return jel_TypeError(problem3_target, e)

def test_get_files_from_day3():
    problem4_target = "get_files_from_day(\"jan\", \"06\")"
    result = get_files_from_day("jan", "06")
    expected_output = [
        'jan06_funny1.tif',
        'jan06_parkschematics.tif',
        'jan06_angryparkperson.tif',
        'jan06_parkpersoninmud.tif',
        'jan06_parkpersoncrying.tif',
        'jan06_mehelpingparkperson.tif',
        'jan06_parkpersonthankingme.tif',
        'jan06_parkperson2.tif',
        'jan06_funny2.tif',
        'jan06_funny3.tif',
    ]
    
    try:
        return jel_assert(
                problem4_target, 
                result == expected_output,
                f"return a list containing {expected_output}"
            )
    except NameError as e:
        return jel_NameError(problem3_target, e)
    except TypeError as e:
        return jel_TypeError(problem3_target, e)

def test_get_files_from_day4():
    problem4_target = "get_files_from_day(\"feb\", \"25\")"
    result = get_files_from_day("feb", "25")
    expected_output = [
        'feb25_weirdobjectinsky.tif',
        'feb25_hugemeteorthing.tif',
        'feb25_ufo1.tif',
        'feb25_ufo2.tif',
        'feb25_spaceshiplanding.tif',
        'feb25_spaceship_exterior1.tif',
        'feb25_spaceship_exterior2.tif',
        'feb25_spaceshipdooropening.tif',
        'feb25_weirdaliendude.tif',
        'feb25_turnsoutthealientsarefemale.tif',
        'feb25_carnage1.tif',
        'feb25_carnage2.tif',
        'feb25_alienpressconference_cancelingallstudentloans.tif',
        'feb25_alienpressconference_cancelingearth.tif',
        'feb25_alienspresentingmewithweirdobject.tif',
        'feb25_mylastcorporealexistence.tif',
        'feb25_goodbyecruelworld.tif'
    ]
    
    try:
        return jel_assert(
                problem4_target, 
                result == expected_output,
                f"return a list containing {expected_output}"
            )
    except NameError as e:
        return jel_NameError(problem3_target, e)
    except TypeError as e:
        return jel_TypeError(problem3_target, e)