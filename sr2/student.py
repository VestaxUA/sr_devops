class Student:
    def __init__(self, pib, group, birth_date=None, address=None):
        self.__pib = pib
        self.__group = group
        self.__birth_date = birth_date
        self.__address = address

    def get_pib(self):
        return self.__pib

    def get_group(self):
        return self.__group

    def get_birth_date(self):
        return self.__birth_date

    def get_address(self):
        return self.__address


    def set_pib(self, pib):
        self.__pib = pib

    def set_group(self, group):
        self.__group = group

    def set_birth_date(self, birth_date):
        self.__birth_date = birth_date

    def set_address(self, address):
        self.__address = address