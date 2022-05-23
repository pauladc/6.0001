# Problem Set 4B
# Name: Paula Contreras
# Collaborators: None
# Time Spent: 5:00
# Late Days Used: 0

import string
import random
import json

### HELPER CODE ###


def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # inFile: file
    with open(file_name, 'r') as inFile:
        # wordlist: list of strings
        wordlist = []
        for line in inFile:
            wordlist.extend([word.lower() for word in line.split(' ')])
        return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"").lower()
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story[:-1]


def get_story_pads():
    with open('pads.txt') as json_file:
        return json.load(json_file)


WORDLIST_FILENAME = 'words.txt'
### END HELPER CODE ###


class Message(object):
    def __init__(self, input_text):
        '''
        Initializes a Message object

        input_text (string): the message's text

        a Message object has one attribute:
            self.message_text s(tring, determined by input text)
        '''
        # instantiate object
        self.message_text = input_text

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        # getter method
        return self.message_text

    def shift_char(self, char, shift):
        '''
        Used to shift a character as described in the pset handout

        char (string): the single character to shift.
                    ASCII value in the range: 32<=ord(char)<=126
        shift (int): the amount to shift char by. -95<shift<95

        Returns: (string) the shifted character with ASCII value in the range [32, 126]
        '''
        # applies shift to character
        charVal = ord(char)
        charVal += shift
        if charVal < 32:
            charVal = 32 - charVal
            charVal = 127 - charVal
        if charVal > 126:
            charVal = charVal - 126
            charVal = 31 + charVal
        return chr(charVal)

    def apply_pad(self, pad):
        '''
        Used to calculate the ciphertext produced by applying a one time pad to self.message_text.
        For each character in self.message_text at index i shift that character by
            the amount specified by pad[i]

        pad (list of ints): a list of integers used to encrypt self.message_text
                        len(pad) == len(self.message_text)
                        elements of pad are in the range (-95, 95)

        Returns: (string) The ciphertext produced using the one time pad
        '''
        # applies series of shifts to characters
        cipher = []
        if pad != None:
            for i in range(len(pad)):
                cipher.append(Message.shift_char(
                    self, Message.get_message_text(self)[i], pad[i]))
            return ''.join(cipher)


class PlaintextMessage(Message):
    def __init__(self, input_text, pad=None):
        '''
        Initializes a PlaintextMessage object.

        input_text (string): the message's text
        pad (list of ints OR None): the pad to encrypt the input_text or None if left empty
            if pad!=None then len(pad) == len(self.message_text)
            and elements of pad are in the range [0, 95)

        A PlaintextMessage object inherits from Message. It has three attributes:
            self.message_text (string, determined by input_text)
            self.pad (list of integers, determined by pad
                or generated from self.generate_pad() if pad==None)
            self.encrypted_message_text (string, input_text encrypted using self.pad)
        '''
        # instantiate object
        Message.__init__(self, input_text)
        if pad == None:
            self.pad = PlaintextMessage.generate_pad(self)
        else:
            self.pad = pad
        self.encrypted_message_text = PlaintextMessage.apply_pad(self, self.pad)

    def generate_pad(self):
        '''
        Generates a one time pad which can be used to encrypt self.message_text.

        The pad should be generated by making a new list and for each character
            in self.message_text chosing a random number in the range [0, 95) and
            adding that number to the list.
        Hint: random.randint(a,b) returns a random integer N such that a<=N<=b

        Returns: (list of integers) the new one time pad
        '''
        # generates random pad if none instantiated
        genPad = []
        for e in self.get_message_text():
            genPad.append(random.randint(0, 94))
        return genPad

    def get_pad(self):
        '''
        Used to safely access self.pad outside of the class

        Returns: a COPY of self.pad
        '''
        # getter method for COPY of pad
        return self.pad[:]

    def get_encrypted_message_text(self):
        '''
        Used to safely access self.encrypted_message_text outside of the class

        Returns: self.encrypted_message_text
        '''
        # getter method for message
        self.encrypted_message_text = PlaintextMessage.apply_pad(self, self.pad)
        return self.encrypted_message_text

    def change_pad(self, new_pad):
        '''
        Changes self.pad of the PlaintextMessage, and updates any other
        attributes that are determined by the pad.

        new_pad (list of ints): the new one time pad that should be associated with this message.
            len(pad) == len(self.message_text)
            and elements of pad are in the range [0, 95)

        Returns: nothing
        '''
        # changes values for encrypted message and pad
        if new_pad != None:
            for i in range(len(new_pad)):
                self.pad[i] = new_pad[i]
            self.encrypted_message_text = PlaintextMessage.apply_pad(self, self.pad)
        else:
            self.encrypted_message_text = PlaintextMessage.apply_pad(self, self.generate_pad())


class EncryptedMessage(Message):
    def __init__(self, input_text):
        '''
        Initializes an EncryptedMessage object

        input_text (string): the ciphertext of the message

        an EncryptedMessage object inherits from Message. It has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
                            on the given file WORDLIST_FILENAME)
        '''
        # instantiate object
        Message.__init__(self, input_text)
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self, pad):
        '''
        Decrypts self.message_text that was encrypted with pad as described in the writeup

        pad (list of ints): the new one time pad used to encrypt the message.
            len(pad) == len(self.message_text)
            and elements of pad are in the range [0, 95)

        Returns: the plaintext message
        '''
        toReturn = []
        for i in range(len(pad)):
            # appends shifted (backwards) characters to a list
            toReturn.append(self.shift_char(
                self.get_message_text()[i], -pad[i]))
            # changes list into string
        return ''.join(toReturn)

    def decrypt_message_try_pads(self, pads):
        '''
        Finds the pad in pads which when used to decrypt self.message_text results
        in a plaintext with the most valid English words. In the event of ties return
        the first pad that results in the maximum number of valid English words.

        pads (list of lists of ints): A list of pads which might have been used
            to encrypt self.message_text

        Returns: (list of ints, string) a tuple of the best pad and the decrypted plaintext
        '''
        maxNum = 0
        bestPad = []
        listWords = []
        for pd in pads:
            # checks every pad in list
            count = 0
            wordString = EncryptedMessage.decrypt_message(self, pd)
            # splits string by spaces
            listWords = wordString.split(' ')
            for word in listWords:
                # checks each string in list for validity
                if is_word(self.valid_words, word):
                    # adds one for each valid word
                    count += 1
            # checks if count if higher than maximum, updates maximum and saves pad
            if count > maxNum:
                maxNum = count
                bestPad = pd
        # accounts for case where no pads produce valid words
        if maxNum == 0:
            return (pads[0], EncryptedMessage.decrypt_message(self, pads[0]))
        return (bestPad, EncryptedMessage.decrypt_message(self, bestPad))


def decode_story():
    '''
    Write your code here to decode Bob's story using a list of possible pads
    Hint: use the helper functions get_story_string and get_story_pads and your EncryptedMessage class.

    Returns: (string) the decoded story

    '''
    secretStory = EncryptedMessage(get_story_string())
    tup = EncryptedMessage.decrypt_message_try_pads(
        secretStory, get_story_pads())
    return tup[1]


if __name__ == '__main__':
    # # Uncomment these lines to try running decode_story()
    story = decode_story()
    print("Decoded story: ", story)
