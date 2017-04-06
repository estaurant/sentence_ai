import PyICU
import random
from enum import Enum


def is_thai_word(char):
    cVal = ord(char)
    if 3584 <= cVal <= 3711:
        return True
    return False


def tokenize(sentence):
    token_list = []
    the_word = ""
    bd = PyICU.BreakIterator.createWordInstance(PyICU.Locale("th"))
    bd.setText(sentence)
    first_position = bd.first()
    try:
        while 1:
            current_position = next(bd)
            the_word = the_word + sentence[first_position:current_position]
            if is_thai_word(sentence[current_position - 1]):
                if current_position < len(sentence):
                    if is_thai_word(sentence[current_position]):
                        token_list.append(the_word)
                        the_word = ""

            first_position = current_position
    except StopIteration:
        pass
        # Add the last word into list
        token_list.append(the_word)
    return token_list


class Intent(Enum):
    NEGATIVE = "negative"
    GREETING = "greeting"
    GREETING_NEG = "greeting_negative"
    DEFAULT = "default"


def get_intent(sentence):
    print(tokenize(sentence))
    the_intents = []

    for a_word in tokenize(sentence):
        print(a_word)
        if a_word.lower() in greeting_words:
            the_intents.append(Intent.GREETING)
        elif a_word.lower() in negative_words:
            the_intents.append(Intent.NEGATIVE)
        else:
            the_intents.append(Intent.DEFAULT)

    print(the_intents)

    is_sentence_negative = find_negative_intent(sentence)
    print("Negative sentence : {}".format(is_sentence_negative))
    for a_negative_intent in the_intents:
        if a_negative_intent == Intent.NEGATIVE:
            the_intents.remove(a_negative_intent)

    if Intent.DEFAULT in the_intents:
        print("It is DEFAULT")
        return Intent.DEFAULT
    else:
        print("It is not DEFAULT")
        return get_real_intent(is_sentence_negative, random.choice(the_intents), the_intents)


def find_negative_intent(sentence):
    # Check whether or not  it is a negative sentence when there are multiple negative words
    is_sentence_negative = False
    for a_negative_word in negative_words:
        for a_word in tokenize(sentence):
            print("{} : {}".format(a_word, a_negative_word))
            if a_word == a_negative_word and a_negative_word in sentence:
                print(" >{} : {}".format(a_word, a_negative_word))
                is_sentence_negative = not is_sentence_negative
    return is_sentence_negative


def get_real_intent(is_sentence_negative, a_intent, the_intents):
    print("Real intents : {}".format(the_intents))
    if a_intent in the_intents:
        if a_intent == Intent.GREETING:
            return Intent.GREETING if not is_sentence_negative else Intent.GREETING_NEG
    else:
        print("Unrecognized intent")
        return Intent.DEFAULT


greeting_words = ["สวัสดี", "hey", "hello", "hi"]
negative_words = ["ไม่"]
ignored_words = ["ครับ, คับ, คะ, ค่ะ"]

example_sentence = "ไม่สวัสดี"

print("OUTPUT INTENT : {}".format(get_intent(example_sentence).value))
