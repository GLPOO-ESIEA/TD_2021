from enum import Enum


class CommandStatusEnum(Enum):

    PENDING = 'pending'
    DELIVERED = 'delivered'
    CANCELLED = 'cancelled'

    def __str__(self):
        return self.value
