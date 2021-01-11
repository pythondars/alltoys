from enum import Enum
from django.utils.translation import ugettext_lazy as _


class BaseEnum(Enum):
    @classmethod
    def max_length(cls):
        return max(len(x.value) for x in cls)

    @classmethod
    def get_value_tuples(cls):
        return ((item.value, _(item.value.replace("_", " ").title())) for item in cls)


class ToyTypeEnum(BaseEnum):
    ANIMALS = "animals"
    DOLLS = "dolls"
    CARS = "cars"
    EDUCATIONAL_TOYS = "educational_toys"
    ELECTRONIC_TOYS = "electronic_toys"
    Other = "other"


class GenderOfPlayersEnum(BaseEnum):
    BOYS = "boys"
    GIRLS = "girls"
