class PyBotProfile:
    """
    Bot Profile
    Instantiate all bot details here. For now, it supports:
    name
    sex
    age
    """
    def __init__(self, name, **kwargs):
        self.name = name
        self.age = kwargs.get('age', None)
        self.sex = kwargs.get('sex', None)

    def initialize_bot_profile(self, nexted):
        """
        Bot inititalizing method. You can call this is
         automatically called to initialize fields in your db
         :rtype: object
        """
        return

    def get_attribute(self, name):
        """

        :param name:
        :return:
        """
        return getattr(self, name)

    def set_attribute(self, name, value):
        """

        :param name:
        :param value:
        :return:
        """
        setattr(self, name, value)
        return self.__dict__[name]


class PyBot:
    """
    Main Bot Class
    """
    def __init__(self, **kwargs):
        self.version = kwargs.get('version')
        

