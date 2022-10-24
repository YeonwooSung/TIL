# Bad practice
class UserAccount_BadPractice:
    def __init__(self, username, password) -> None:
        self.__username = username
        self.__password = password

    def get_username(self):
        return self.__username
    
    def get_password(self):
        return self.__password
    
    def set_username(self, username):
        self.__username = username
    
    def set_password(self, password):
        self.__password = password


# Good practice
class UserAccount_GoodPratice:
    def __init__(self, username, password) -> None:
        self.__username = username
        self.__password = password
    
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, username):
        self.__username = username
    
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password


'''
Property is a decorator which is used to define a method as a property of a class.
It is used to define a getter, setter and deleter for a property.
'''