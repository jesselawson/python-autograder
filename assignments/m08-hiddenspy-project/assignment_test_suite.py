"""
Assignment test suite for M08 Hidden Spy

"""
# For reference only, since the assignment should contain these
#raw_chars    = ['/',':','.','1','2','3','4','5','6','7','8','9','0',' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#cipher_chars = ['=','+','?','z','y','x','w','v','u','t','s','r','q','!','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a','0','9','8','7','6','5','4','3','2','1']



def generate_encrypt_char_test(target, raw, cipher):
    try:
        return jel_assert(
                target, 
                encrypt_char(raw) == cipher,
                f"return '{cipher}'"
            )
    except NameError as e:
        return jel_NameError(target, e)
    except TypeError as e:
        return jel_TypeError(target, e)


"""
# Generate tests for encrypt_char()
def generate_encrypt_char_tests():
    for i, c in enumerate(raw_chars):
        print(f"def test_encrypt_char_{i}:\n\treturn generate_encrypt_char_test(\"encrypt_char('{c}')\", '{c}', '{cipher_chars[i]}')")

generate_encrypt_char_tests()
"""
def test_encrypt_char_0():
    return generate_encrypt_char_test("encrypt_char('/')", '/', '=')
def test_encrypt_char_1():
    return generate_encrypt_char_test("encrypt_char(':')", ':', '+')
def test_encrypt_char_2():
    return generate_encrypt_char_test("encrypt_char('.')", '.', '?')
def test_encrypt_char_3():
    return generate_encrypt_char_test("encrypt_char('1')", '1', 'z')
def test_encrypt_char_4():
    return generate_encrypt_char_test("encrypt_char('2')", '2', 'y')
def test_encrypt_char_5():
    return generate_encrypt_char_test("encrypt_char('3')", '3', 'x')
def test_encrypt_char_6():
    return generate_encrypt_char_test("encrypt_char('4')", '4', 'w')
def test_encrypt_char_7():
    return generate_encrypt_char_test("encrypt_char('5')", '5', 'v')
def test_encrypt_char_8():
    return generate_encrypt_char_test("encrypt_char('6')", '6', 'u')
def test_encrypt_char_9():
    return generate_encrypt_char_test("encrypt_char('7')", '7', 't')
def test_encrypt_char_10():
    return generate_encrypt_char_test("encrypt_char('8')", '8', 's')
def test_encrypt_char_11():
    return generate_encrypt_char_test("encrypt_char('9')", '9', 'r')
def test_encrypt_char_12():
    return generate_encrypt_char_test("encrypt_char('0')", '0', 'q')
def test_encrypt_char_13():
    return generate_encrypt_char_test("encrypt_char(' ')", ' ', '!')
def test_encrypt_char_14():
    return generate_encrypt_char_test("encrypt_char('a')", 'a', 'p')
def test_encrypt_char_15():
    return generate_encrypt_char_test("encrypt_char('b')", 'b', 'o')
def test_encrypt_char_16():
    return generate_encrypt_char_test("encrypt_char('c')", 'c', 'n')
def test_encrypt_char_17():
    return generate_encrypt_char_test("encrypt_char('d')", 'd', 'm')
def test_encrypt_char_18():
    return generate_encrypt_char_test("encrypt_char('e')", 'e', 'l')
def test_encrypt_char_19():
    return generate_encrypt_char_test("encrypt_char('f')", 'f', 'k')
def test_encrypt_char_20():
    return generate_encrypt_char_test("encrypt_char('g')", 'g', 'j')
def test_encrypt_char_21():
    return generate_encrypt_char_test("encrypt_char('h')", 'h', 'i')
def test_encrypt_char_22():
    return generate_encrypt_char_test("encrypt_char('i')", 'i', 'h')
def test_encrypt_char_23():
    return generate_encrypt_char_test("encrypt_char('j')", 'j', 'g')
def test_encrypt_char_24():
    return generate_encrypt_char_test("encrypt_char('k')", 'k', 'f')
def test_encrypt_char_25():
    return generate_encrypt_char_test("encrypt_char('l')", 'l', 'e')
def test_encrypt_char_26():
    return generate_encrypt_char_test("encrypt_char('m')", 'm', 'd')
def test_encrypt_char_27():
    return generate_encrypt_char_test("encrypt_char('n')", 'n', 'c')
def test_encrypt_char_28():
    return generate_encrypt_char_test("encrypt_char('o')", 'o', 'b')
def test_encrypt_char_29():
    return generate_encrypt_char_test("encrypt_char('p')", 'p', 'a')
def test_encrypt_char_30():
    return generate_encrypt_char_test("encrypt_char('q')", 'q', '0')
def test_encrypt_char_31():
    return generate_encrypt_char_test("encrypt_char('r')", 'r', '9')
def test_encrypt_char_32():
    return generate_encrypt_char_test("encrypt_char('s')", 's', '8')
def test_encrypt_char_33():
    return generate_encrypt_char_test("encrypt_char('t')", 't', '7')
def test_encrypt_char_34():
    return generate_encrypt_char_test("encrypt_char('u')", 'u', '6')
def test_encrypt_char_35():
    return generate_encrypt_char_test("encrypt_char('v')", 'v', '5')
def test_encrypt_char_36():
    return generate_encrypt_char_test("encrypt_char('w')", 'w', '4')
def test_encrypt_char_37():
    return generate_encrypt_char_test("encrypt_char('x')", 'x', '3')
def test_encrypt_char_38():
    return generate_encrypt_char_test("encrypt_char('y')", 'y', '2')
def test_encrypt_char_39():
    return generate_encrypt_char_test("encrypt_char('z')", 'z', '1')

def generate_decrypt_char_test(target, raw, cipher):
    try:
        return jel_assert(
                target, 
                decrypt_char(raw) == cipher,
                f"return '{cipher}'"
            )
    except NameError as e:
        return jel_NameError(target, e)
    except TypeError as e:
        return jel_TypeError(target, e)

"""
# Generate tests for encrypt_char()
def generate_decrypt_char_tests():
    for i, c in enumerate(cipher_chars):
        print(f"def test_decrypt_char_{i}():\n\treturn generate_decrypt_char_test(\"decrypt_char('{c}')\", '{c}', '{raw_chars[i]}')")
generate_decrypt_char_tests()
"""

def test_decrypt_char_0():
    return generate_decrypt_char_test("decrypt_char('=')", '=', '/')
def test_decrypt_char_1():
    return generate_decrypt_char_test("decrypt_char('+')", '+', ':')
def test_decrypt_char_2():
    return generate_decrypt_char_test("decrypt_char('?')", '?', '.')
def test_decrypt_char_3():
    return generate_decrypt_char_test("decrypt_char('z')", 'z', '1')
def test_decrypt_char_4():
    return generate_decrypt_char_test("decrypt_char('y')", 'y', '2')
def test_decrypt_char_5():
    return generate_decrypt_char_test("decrypt_char('x')", 'x', '3')
def test_decrypt_char_6():
    return generate_decrypt_char_test("decrypt_char('w')", 'w', '4')
def test_decrypt_char_7():
    return generate_decrypt_char_test("decrypt_char('v')", 'v', '5')
def test_decrypt_char_8():
    return generate_decrypt_char_test("decrypt_char('u')", 'u', '6')
def test_decrypt_char_9():
    return generate_decrypt_char_test("decrypt_char('t')", 't', '7')
def test_decrypt_char_10():
    return generate_decrypt_char_test("decrypt_char('s')", 's', '8')
def test_decrypt_char_11():
    return generate_decrypt_char_test("decrypt_char('r')", 'r', '9')
def test_decrypt_char_12():
    return generate_decrypt_char_test("decrypt_char('q')", 'q', '0')
def test_decrypt_char_13():
    return generate_decrypt_char_test("decrypt_char('!')", '!', ' ')
def test_decrypt_char_14():
    return generate_decrypt_char_test("decrypt_char('p')", 'p', 'a')
def test_decrypt_char_15():
    return generate_decrypt_char_test("decrypt_char('o')", 'o', 'b')
def test_decrypt_char_16():
    return generate_decrypt_char_test("decrypt_char('n')", 'n', 'c')
def test_decrypt_char_17():
    return generate_decrypt_char_test("decrypt_char('m')", 'm', 'd')
def test_decrypt_char_18():
    return generate_decrypt_char_test("decrypt_char('l')", 'l', 'e')
def test_decrypt_char_19():
    return generate_decrypt_char_test("decrypt_char('k')", 'k', 'f')
def test_decrypt_char_20():
    return generate_decrypt_char_test("decrypt_char('j')", 'j', 'g')
def test_decrypt_char_21():
    return generate_decrypt_char_test("decrypt_char('i')", 'i', 'h')
def test_decrypt_char_22():
    return generate_decrypt_char_test("decrypt_char('h')", 'h', 'i')
def test_decrypt_char_23():
    return generate_decrypt_char_test("decrypt_char('g')", 'g', 'j')
def test_decrypt_char_24():
    return generate_decrypt_char_test("decrypt_char('f')", 'f', 'k')
def test_decrypt_char_25():
    return generate_decrypt_char_test("decrypt_char('e')", 'e', 'l')
def test_decrypt_char_26():
    return generate_decrypt_char_test("decrypt_char('d')", 'd', 'm')
def test_decrypt_char_27():
    return generate_decrypt_char_test("decrypt_char('c')", 'c', 'n')
def test_decrypt_char_28():
    return generate_decrypt_char_test("decrypt_char('b')", 'b', 'o')
def test_decrypt_char_29():
    return generate_decrypt_char_test("decrypt_char('a')", 'a', 'p')
def test_decrypt_char_30():
    return generate_decrypt_char_test("decrypt_char('0')", '0', 'q')
def test_decrypt_char_31():
    return generate_decrypt_char_test("decrypt_char('9')", '9', 'r')
def test_decrypt_char_32():
    return generate_decrypt_char_test("decrypt_char('8')", '8', 's')
def test_decrypt_char_33():
    return generate_decrypt_char_test("decrypt_char('7')", '7', 't')
def test_decrypt_char_34():
    return generate_decrypt_char_test("decrypt_char('6')", '6', 'u')
def test_decrypt_char_35():
    return generate_decrypt_char_test("decrypt_char('5')", '5', 'v')
def test_decrypt_char_36():
    return generate_decrypt_char_test("decrypt_char('4')", '4', 'w')
def test_decrypt_char_37():
    return generate_decrypt_char_test("decrypt_char('3')", '3', 'x')
def test_decrypt_char_38():
    return generate_decrypt_char_test("decrypt_char('2')", '2', 'y')
def test_decrypt_char_39():
    return generate_decrypt_char_test("decrypt_char('1')", '1', 'z')

def generate_encrypt_message_test(raw_msg):

    # Cipher the message
    cipher_msg = ""
    for c in raw_msg:
        for i, raw_c in enumerate(raw_chars):
            if raw_c == c:
                cipher_msg += cipher_chars[i]
                continue
        
    try:
        return jel_assert(
                f"encrypt_message('{raw_msg}')", 
                encrypt_message(raw_msg) == cipher_msg,
                f"return '{cipher_msg}'"
            )
    except NameError as e:
        return jel_NameError(target, e)
    except TypeError as e:
        return jel_TypeError(target, e)

def test_encrypt_message_0():
    return generate_encrypt_message_test("hello, world!")

def test_encrypt_message_1():
    return generate_encrypt_message_test("welcome to the other side")

def test_encrypt_message_2():
    return generate_encrypt_message_test("45 people at 32nd street")

def test_encrypt_message_3():
    return generate_encrypt_message_test("https://jesselawson.org/python")

def generate_decrypt_message_test(cipher_msg):

    # decrypt the message
    raw_msg = ""
    for c in cipher_msg:
        for i, cipher_c in enumerate(cipher_chars):
            if cipher_c == c:
                raw_msg += raw_chars[i]
                continue
        
    try:
        return jel_assert(
                f"decrypt_message('{cipher_msg}')",
                decrypt_message(cipher_msg) == raw_msg,
                f"return '{raw_msg}'"
            )
    except NameError as e:
        return jel_NameError(target, e)
    except TypeError as e:
        return jel_TypeError(target, e)

def test_decrypt_message_0():
    return generate_decrypt_message_test("i77a8+==gl88lep48bc?b9j=a27ibc")

def test_decrypt_message_1():
    return generate_decrypt_message_test("wv!albael!p7!xycm!879ll7")

def test_decrypt_message_2():
    return generate_decrypt_message_test("4lenbdl!7b!7il!b7il9!8hml")

def test_decrypt_message_3():
    return generate_decrypt_message_test("xw7i!pcm!npcpe!87")