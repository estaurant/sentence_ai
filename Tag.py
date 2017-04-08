from enum import Enum


# noinspection SpellCheckingInspection
class Tag(Enum):
    NPRP = "Proper noun"
    NLBL = "Label noun"
    NCMN = "Common noun"
    NTTL = "Title noun"
    PPRS = "Personal pronoun"

    VACT = "Active verb"
    VSTA = "Stative verb"
    VATT = "Attributive verb"
    XVAE = "Post - verb auxiliary"
    XVMM = "Pre - verb before or after negator 'ไม่'"

    NEG = "Negator"

    NONE = "None"

    @classmethod
    def get_enum_from_string(cls, a_string):
        for an_enum in Tag:
            if an_enum.name.lower() == a_string.lower():
                return an_enum
        # In case nothing is matched
        return cls.NONE
