import pythainlp
import re

from Tag import Tag
from Token import Token
from Intent import Intent


def get_token(sentence):
    tag_list = pythainlp.postaggers.tag(sentence)
    temp_token_list = []
    for anElement in tag_list:
        extracted = re.search("\('(.+?)', '?(.+?)'?\)", str(anElement))
        lexeme = ""
        tag = ""
        try:
            if extracted:
                lexeme = extracted.group(1)
                tag = Tag.get_enum_from_string(extracted.group(2))
        except IndexError:
            lexeme = ""
            tag = Tag.NONE
            print("error : " + lexeme)
        token = Token(lexeme, tag)
        temp_token_list.append(token)
    return temp_token_list


greeting_words = ["สวัสดี", "hello", "hi"]


def get_intent(the_token_list):
    lexeme_list = []
    tag_list = []
    return_list = []
    for a_token in the_token_list:
        lexeme_list.append(a_token.get_lexeme())
    for a_token in the_token_list:
        tag_list.append(a_token.get_tag_name())

    print(lexeme_list)
    print(tag_list)

    for a_greeting_word in greeting_words:
        if a_greeting_word.lower() in [x.lower() for x in lexeme_list]:
            if Tag.NEG.name in tag_list:
                return_list.append(Intent.GREETING_NEG)
            else:
                return_list.append(Intent.GREETING)
            return_list.append("")
            return return_list

    if (Tag.XVMM.name or Tag.VSTA.name in tag_list) and Tag.VACT.name in tag_list:
        try:
            verb = lexeme_list[(tag_list.index(Tag.VACT.name))]
            print("verb : " + verb)
            if verb == "กิน":
                keyword = ''.join(lexeme_list[lexeme_list.index(verb) + 1:])
                print("keyword : " + keyword)
                if tag_list[(tag_list.index(Tag.VACT.name) - 2)] == Tag.NEG.name:
                    return_list.append(Intent.EAT_NEG)
                else:
                    return_list.append(Intent.EAT)
                return_list.append(keyword)

                return return_list
        except ValueError:
            return_list.append(Intent.DEFAULT)
            return_list.append(Intent.DEFAULT.name)
            return return_list
    else:
        return_list.append(Intent.DEFAULT)
        return_list.append(Intent.DEFAULT.name)
        return return_list


example_sentence = "อยากกินข้าวมันไก่เนื้อๆ"
example_sentence2 = "ชอบกินข้าวมันไก่เนื้อๆ"
example_sentence3 = "้รู้สึกไม่อยากกินข้าวมันไก่เนื้อๆ"
example_greeting = "สวัสดี"
example_greeting2 = "HeLlo"
example_greeting3 = "hI"
print(pythainlp.postaggers.tag(example_greeting3))
token_list = get_token(example_greeting3)

the_real_intent = get_intent(token_list)
print("Intent  : {}".format(the_real_intent[0].name))
print("Keyword : {}".format(the_real_intent[1]))
