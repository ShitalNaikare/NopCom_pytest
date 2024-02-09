import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\Admin\\PycharmProjects\\nopcom_pytest\\configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getEmail():
        Email = config.get('Login_Data','email')
        return Email

    @staticmethod
    def getPassword():
        Password = config.get('Login_Data','password')
        return Password

