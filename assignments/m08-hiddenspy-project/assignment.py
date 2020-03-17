"""
M08 Project: "The Hidden Spy"

Repl.it Link: https://repl.it/@professorlawson/m08-hiddenspy

Intro

OVERVIEW
==================================================================================

You are a programmer assigned to Lawson's Operational Spy Enforcement Recon team, 
where you work alongside cryptographers from the NSA, CIA, and FBI. You just 
received a new contract: "The Hidden Spy."

SITUATION
--------------------------------------------------------------------------------

Foreign corporate spies have been stealing research and development data from 
government contractors and transmitting these secrets back and forth out in the 
open by encrypting them and publishing them on darknet forums. 

Cryptographers from the Special Projects division have broken the encryption 
algorithm, and you have been brought in to create a Python script that will help 
rapidly encrypt and decrypt messages for the forward spy team. 

We have two major objectives: 

- Objective #1: We need a way to encrypt messages so that our signals intelligence 
  teams can locate and identify the recipient of the stolen data.

- Objective #2: We need a way to decrypt messages that we have intercepted in 
  order to determine the location and identification of the hidden spy who is 
  stealing government secrets. 

MISSION
--------------------------------------------------------------------------------

Your mission is to use cryptographic data provided by the FBI's top 
Cybercrimes and Cryptography expert, Burt Macklin, to write four Python 
functions that will be used to encrypt and decrypt messages. Then, you will 
assist Special Agent Macklin with decrypting some messages to reveal the location 
of the hidden spy. 

DATA & INFORMATION
--------------------------------------------------------------------------------

The folks over at NSA have reverse engineered the algorithm used to encrypt 
the messages. They're calling it the "Swanson Cipher." 

Here it is:

"""

raw_chars    = ['/',':','.','1','2','3','4','5','6','7','8','9','0',' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cipher_chars = ['=','+','?','z','y','x','w','v','u','t','s','r','q','!','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a','0','9','8','7','6','5','4','3','2','1']

"""

This is known as a modified Caesar Cipher. You can learn about this type of 
cryptographic methodology here: https://en.wikipedia.org/wiki/Caesar_cipher

The way it works is as follows:

- Every character in `raw_char` represents an unencrypted character.
- Every character in `cipher_char` represents an encrypted character.
- Every element of `raw_char` is associated with an element of `cipher_char` 
  at the same index.

Numbers are considered characters for this project. In other words, treat 
anything that looks like a number as a character. Do not return or use raw 
numbers; surround any number in quotes like this -> '2', '4', '0', etc.

Assume all letters are uppercase at all times. You do not have to account for 
lowercase letters.

INSTRUCTIONS
================================================================================

01. Modify the function `encrypt_char`.
    It should take one argument: `the_char`, a character.
    It should return the character in `cipher_chars` that is at the same position 
    as `the_char` is in `raw_chars`.
    If no matching character is found in `raw_chars`, 
        it should return an empty character (''). 
    Examples: 
        * encrypt_char('2') should return 'Y'
        * encrypt_char('G') should return 'J'
        * encrypt_char('$') should return ''

02. Modify the function `decrypt_char`.
    It should take one argument: `the_char`, a character.
    It should return the character in `raw_chars` that is at the same position 
    as `the_char` is in `cipher_chars`.
    If no matching character is found in `cipher_chars`,
        it should return an empty character ('').
    Examples:
        * decrypt_char('Q') should return '0'
        * decrypt_char('D') should return 'M'
        * decrypt_char('%') should return ''

03. Modify the function `encrypt_message`.
    It should take one argument: `msg`, a string.
    It should return a new string with each character replaced with a 
        corresponding encrypted character via encrypt_char().
    Examples:
        * encrypt_message('HELLO') should return 'ILEEB'
        * encrypt_message('32ND STREET') should return 'XYCM!879LL7'
        * encrypt_message('I'VE GOT MONEY $$!') should return 'H5L!JB7!DBCL2!'

04. Modify the function `decrypt_message`.
    It should take one argument: `msg`, a string.
    It should return a new string with each character replaced with a 
        corresponding encrypted character via decrypt_char().
    Examples:
        * decrypt_message('H5L!JB7!DBCL2!') should return 'IVE GOT MONEY '
        * decrypt_message('ILEEB') should return 'HELLO'
        * decrypt_message('XW7I!PCM!NPCPE!87') should return ''
   
05. Complete the `DECRYPTION TASKS` section at the bottom of this file. 

06. Ensure there are no errors when you run this script.

07. Submit this completed file to the appropriate assignment in Canvas. 

TIPS FOR SUCCESS
==================================================================================

* You can name your parameters whatever you want; I name them here in the specs 
  to help you understand the instructions.

* "Return" does not mean "print()". It means that the function should "return" 
  a value. 

* If you get errors while working, copy your errors into a search engine and see 
  what StackOverflow discussions and/or blog posts you can find that help you find 
  your way out of a rabbit hole. Remember: A LARGE part of this course is developing 
  your ability to dig yourself out of programming holes; you MUST be comfortable 
  being confused and frustrated, and you MUST know how to get to where you want to 
  be (which, usually, is at the point where your script does what you want it to 
  do). The only way to do that is to practice searching Google or whatever your 
  favorite search engine is. 

* If an instruction is to print a string, then you must make sure 
  you are including ALL punctuation and grammar. For example, you will be
  marked down if the specification includes a period and your solution does 
  not include one. 

* Drink water! Seriously. Get up, go get a drink of water, and breathe in some 
  fresh air for a couple minutes. 

"""

def encrypt_char():
    return ''

def decrypt_char():
    return ''

def encrypt_message():
    return ''

def decrypt_message():
    return ''

"""
DECRYPTION TASKS

Burt Macklin here. FBI. We've intercepted a communication that we believe is 
encrypted with the Swanson Cipher. 

Your task is to decrypt the following message, and investigate any leads that 
arise. Yes, you're a programmer, but today you are an honorary FBI field agent, 
too. Go get 'em!

Remember: our objective is to locate the hidden spy!

BEGIN MESSAGE
--------------------------------------------------------------------------------
4lpabc!aepc8!ip5l!ollc!pn06h9lm?!dll7!dl!p7!7il!cl4!m9ba!ebnp7hbc?!kbeeb4!hc8796n7hbc8!il9l+!i77a8+==jh87?jh7i6o68l9nbc7lc7?nbd=gl88lep48bc=wuxqyksqxvyowzyymoxotsvvuzkxuzyw=9p4=lnvkwsypsvoxupovzzowrvqxyrsrtouzmwwxzrxo=hc7l9nla7lmdl88pjl?ebj
--------------------------------------------------------------------------------
END MESSAGE

After you've decrypted the message and followed any leads, use the secret map 
linked to on the assignment page to answer the question below:

Q: Where do I go to find the hidden spy?
A: 

"""