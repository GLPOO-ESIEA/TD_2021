class View:
    """
    Base object for view, show function must be implemented for all view
    """

    def error_message(self, message: str):
        print("/!\\ %s" % message.upper())

    def succes_message(self, message: str = ""):
        print("Operation succeeded: %s" % message)

    def show(self):
        print("/!\\ Not implemented View")
