import PyICU


def is_thai(chr):
    cVal = ord(chr)
    if 3584 <= cVal <= 3711:
        return True
    return False


def tokenize(txt):
    # print(txt)
    bd = PyICU.BreakIterator.createWordInstance(PyICU.Locale("th"))
    bd.setText(txt)
    lastPos = bd.first()
    retTxt = ""
    try:
        while 1:
            currentPos = next(bd)
            retTxt += txt[lastPos:currentPos]
            if is_thai(txt[currentPos - 1]):
                if currentPos < len(txt):
                    if is_thai(txt[currentPos]):
                        retTxt += "|"
            lastPos = currentPos
    except StopIteration:
        pass
        # retTxt = retTxt[:-1]
    return retTxt


example_sentence = "หิวข้าวจัง"
print(tokenize(example_sentence))
