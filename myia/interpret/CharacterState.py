from enum import Enum


class CharacterState(Enum):
    ALONE = 1
    ALONE_IN_DARKNESS = 2
    IN_GROUP = 3
    IN_GROUP_IN_DARKNESS = 4
