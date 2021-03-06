import pythainlp
import re

from Tag import Tag
from Token import Token
from Intent import Intent


def get_token(sentence):
    sentence = sentence.strip()
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
    return_list = [Intent.DEFAULT, Intent.DEFAULT.value]
    for a_token in the_token_list:
        lexeme_list.append(a_token.get_lexeme())
    for a_token in the_token_list:
        tag_list.append(a_token.get_tag_name())

    print(lexeme_list)
    print(tag_list)

    for a_greeting_word in greeting_words:
        if a_greeting_word.lower() in [x.lower() for x in lexeme_list]:
            if Tag.NEG.name in tag_list:
                return_list[0] = Intent.GREETING_NEG
            else:
                return_list[0] = Intent.GREETING
            return_list[1] = ""
            return return_list

    if (Tag.XVMM.name in tag_list or Tag.VSTA.name in tag_list) and Tag.VACT.name in tag_list:
        try:
            verb = lexeme_list[(tag_list.index(Tag.VACT.name))]
            print("verb : " + verb)
            lexeme_setence = ''.join(lexeme_list[:])
            if verb == "กิน":
                keyword = ''.join(lexeme_list[lexeme_list.index(verb) + 1:]).strip()
                print("keyword : " + keyword)
                if "ถูก" in keyword:
                    return_list[0] = Intent.RECOMMEND
                    return_list[1] = "expensive" if Tag.NEG.name in tag_list else "cheap"
                    return return_list
                elif "แพง" in keyword:
                    return_list[0] = Intent.RECOMMEND
                    return_list[1] = "cheap" if Tag.NEG.name in tag_list else "expensive"
                    return return_list
                elif "รีบ" in lexeme_setence or "เร็ว" in lexeme_setence or "ใกล้" in lexeme_setence:
                    print("ss")
                    return_list[0] = Intent.RECOMMEND
                    return_list[1] = "far" if Tag.NEG.name in tag_list else "near"
                    return return_list
                elif "ไกล" in lexeme_setence:
                    print("ssTT")
                    return_list[0] = Intent.RECOMMEND
                    return_list[1] = "near" if Tag.NEG.name in tag_list else "far"
                    return return_list
                else:
                    print("ssTTAA")
                    if tag_list[(tag_list.index(Tag.VACT.name) - 2)] == Tag.NEG.name:
                        return_list[0] = Intent.EAT_NEG
                    else:
                        return_list[0] = Intent.EAT
                return_list[1] = keyword

                return return_list
            else:
                print("No verb is matched")
                return return_list
        except ValueError:
            return return_list
    elif Tag.VACT.name in tag_list:
        try:
            lexeme_setence = ''.join(lexeme_list[:])
            if "แนะนำ" in lexeme_list:
                return_list[0] = Intent.RECOMMEND
                if "ถูก" in lexeme_setence:
                    return_list[1] = "expensive" if Tag.NEG.name in tag_list else "cheap"
                    return return_list
                elif "แพง" in lexeme_setence:
                    return_list[1] = "cheap" if Tag.NEG.name in tag_list else "expensive"
                    return return_list
                else:
                    return return_list
            elif "รีบ" in lexeme_setence or "เร็ว" in lexeme_setence or "ใกล้" in lexeme_setence:
                return_list[0] = Intent.RECOMMEND
                return_list[1] = "far" if Tag.NEG.name in tag_list else "near"
                return return_list
            elif "ไกล" in lexeme_setence:
                return_list[0] = Intent.RECOMMEND
                return_list[1] = "near" if Tag.NEG.name in tag_list else "far"
                return return_list
            else:
                print("No verb is matched")
                return return_list
        except ValueError:
            return return_list
    else:
        print("DEFAULT")
        return return_list


example_sentence = "อยากกินข้าวมันไก่เนื้อๆ"
example_sentence2 = "ชอบกินข้าวมันไก่เนื้อๆ"
example_sentence3 = "รู้สึกไม่อยากกินข้าวมันไก่เนื้อๆ"
example_greeting = "สวัสดี"
example_greeting2 = "HeLlo"
example_greeting3 = "hI"
example_test = "วันนึ้รีบกินไรดี"
example_food1 = "  อยากกิน ส้มตำ  "

example_recommend1 = "แนะนำของกินไม่ถูกให้หน่อย"
example_recommend2 = "แนะนำของกินไม่ถูก"
example_recommend3 = "ไม่อยากกินของแพงๆ"

example_distance1 = "วันนี้รีบกินอะไรดี"
example_distance2 = "วันนี้ไม่รีบ กินไรดี"
example_distance3 = "อยากกินร้านอาหารใกล้ๆ"
example_distance4 = "ไม่ค่อยรีบอะกินไหนก็ได้"
example_distance5 = "ไม่อยากกินร้านไกลๆ"

print(pythainlp.postaggers.tag(example_sentence3.strip()))
token_list = get_token(example_sentence3)

the_real_intent = get_intent(token_list)
print("Intent  : {}".format(the_real_intent[0].name))
print("Keyword : {}".format(the_real_intent[1]))
