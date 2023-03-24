class base:
    __instance = 0

    def __init__(self, parent=None, type=''):
        self.parent = parent
        self.name = "object_" + type + str(base.__get_instance())

    @classmethod
    def __get_instance(cls):
        cls.__instance += 1
        return cls.__instance - 1
