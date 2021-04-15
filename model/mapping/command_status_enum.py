from enum import Enum


class CommandStatusEnum(Enum):
    """
    Defines Commands available status
    An enumeration is a set of symbolic names (members) bound to unique, constant values.
    https://docs.python.org/3/library/enum.html
    """

    PENDING = 'pending'
    DELIVERED = 'delivered'
    CANCELLED = 'cancelled'

    def __str__(self):
        return self.value
