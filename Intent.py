from enum import Enum


class Intent(Enum):
    GREETING = "greeting"
    GREETING_NEG = "greeting_negative"
    EAT = "eat"
    EAT_NEG = "eat_negative"
    RECOMMEND = "recommend"
    DEFAULT = "default"
