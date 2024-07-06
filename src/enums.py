from enum import Enum


class TypeOfEmployment(Enum):
    ONLINE = "online"
    HYBRID = "hybrid"
    OFFLINE = "offline"


class Sex(Enum):
    MALE = "male"
    FEMALE = "female"


class EducationLevels(Enum):
    higher = "higher"
    secondary = "secondary"
    secondary_professional = "secondary professional"
    master = "master"
