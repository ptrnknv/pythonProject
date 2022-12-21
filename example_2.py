def is_palindrome(string):
    if len(string) < 2:
        return True
    else:
        if string[0] == string[-1]:
            return is_palindrome(string[1:-1])
    return False


print(is_palindrome('stepik'))
print(is_palindrome('level'))
print(is_palindrome('122333221'))
print(is_palindrome('b'))
