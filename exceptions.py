
class Error(BaseException):
    """Base class for exceptions in this module."""
    pass


class ResourceNotFound(Error):
    pass


class InvalidData(Error):
    pass


class NotEnoughArticle(Error):
    pass


class Conflict(Error):
    pass
