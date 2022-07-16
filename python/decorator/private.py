# 1. Custom decorator -> private

import sys, functools

def private(member):
    @functools.wraps(member)
    def wrapper(*function_args):
        myself = member.__name__
        caller = sys._getframe(1).f_code.co_name
        if (not caller in dir(function_args[0]) and not caller is myself):
            raise Exception("%s called by %s is private"%(myself,caller))
        return member(*function_args)
    return wrapper

'''
class test:
    def public_method(self):
        print('public method called')
    @private
    def private_method(self):
        print('private method called')
t = test()
t.public_method()
t.private_method()
'''
