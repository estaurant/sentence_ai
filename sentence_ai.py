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


def get_intent(the_token_list):
    lexeme_list = []
    tag_list = []
    for a_token in the_token_list:
        lexeme_list.append(a_token.get_lexeme())
    for a_token in the_token_list:
        tag_list.append(a_token.get_tag_name())

    print(lexeme_list)
    print(tag_list)

    if Tag.XVMM.name or Tag.VSTA.name in tag_list and Tag.VACT.name in tag_list:
        return_list = []
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


example_sentence = "อยากกินข้าวมันไก่เนื้อๆ"
example_sentence2 = "ชอบกินข้าวมันไก่เนื้อๆ"
example_sentence3 = "้รู้สึกไม่อยากกินข้าวมันไก่เนื้อๆ"
print(pythainlp.postaggers.tag(example_sentence))
token_list = get_token(example_sentence)

the_real_intent = get_intent(token_list)
print("Intent  : {}".format(the_real_intent[0].name))
print("Keyword : {}".format(the_real_intent[1]))
