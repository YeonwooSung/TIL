import re



# By using the regular expressions, you could implement e-mail/password validation functions easily.

def check_password(password):
    result = re.search(r'.{8,}', password)
    if not result:
        print('Minimum length of password is 8')
        return

    print(password)
    result = re.search(r'[a-z]+', password)
    if not result:
        print('The password should contain at least 1 lower case character!')
        return

    result = re.search(r'[A-Z]+', password)
    if not result:
        print('The password should contain at least 1 upper case character!')
        return
    
    result = re.search(r'[0-9]+', password)
    if not result:
        print('The password should contain at least 1 number!')
        return
    
    result = re.search(r'[@#$%^&+=]', password)
    if not result:
        print('The password should contain at least one of [@#$%^&+=]!')
        return

    print('Password valudation success')


check_password('Your@password!!321')



# You could also implement string.split() method by using the regex

def split_with_regex(pattern, string):
    result = re.split(pattern, string)
    if not result:
        print('No matching data!')
        return None, None
    
    print('Found matching data: {}'.format(result))
    return result[0], result[1]


split_with_regex('@', 'nothing@testing.com')
