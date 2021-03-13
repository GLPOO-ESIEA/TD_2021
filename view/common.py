import re


class Common:
    """
    Somme common functions use by views
    """

    def ask(self, key_name: str = "", regex: str = None, default: str = None):
        message = "Enter %s" % key_name
        if default is not None:
            message += "(%s)" % default
        message += ": "
        string = input(message).rstrip()
        if default is not None and string == "":
            return default
        if regex is not None:
            pattern = re.compile(regex)
            while not pattern.match(string):
                print("/!\\ Error input malformed")
                string = input(message)
        return string

    def ask_name(self, key_name="name", default=None):
        return self.ask(key_name=key_name, regex="^[\S-]{2,50}$", default=default).lower()

    def ask_email(self, default=None):
        return self.ask(key_name="email", regex=None, default=default)

    def ask_type(self, default=None):
        return self.ask(key_name="type (admin or customer)", regex="^(admin|customer)$", default=default)

    @staticmethod
    def query_yes_no(question, default="no"):
        """Ask a yes/no question via raw_input() and return their answer.

        "question" is a string that is presented to the user.
        "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning an answer is required of the user).

        The "answer" return value is one of "yes" or "no".
        """
        valid = {"yes": True, "y": True, "ye": True, "oui": True, "o": True,
                 "no": False, "n": False, "non": False}
        if default is None:
            prompt = " [y/n] "
        elif default == "yes":
            prompt = " [Y/n] "
        elif default == "no":
            prompt = " [y/N] "
        else:
            raise ValueError("Invalid default answer: '%s'" % default)

        while True:
            print(question + prompt)
            choice = input().lower()
            if default is not None and choice == '':
                return valid[default]
            elif choice in valid:
                return valid[choice]
            else:
                print("Please answer with 'yes' or 'no' (or 'y' or 'n').\n")