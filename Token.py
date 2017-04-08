class Token(object):

    lexeme = ""
    tag = ""

    def __init__(self, lexeme, tag):
        self.lexeme = lexeme
        self.tag = tag

    def get_lexeme(self):
        return self.lexeme

    def get_tag(self):
        return self.tag

    def get_tag_name(self):
        return self.tag.name

    def __str__(self):
        return "Lexeme : " + self.lexeme + ", Tag : " + self.tag.name
