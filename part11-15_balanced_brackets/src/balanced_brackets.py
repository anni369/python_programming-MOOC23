import re
def balanced_brackets(my_string: str):
    string = re.sub("[A-Za-z0-9. !/*+=-]","",my_string)
    print (string)
    if len(string) == 0:
        return True
    if not ((string[0] == '(' and string[-1] == ')') or (string[0] == '[' and string[-1] == ']')):
        return False

    # remove first and last character
    return balanced_brackets(string[1:-1])


if __name__ == "__main__":
    ok = balanced_brackets("(x * (1 + y) / 2)")
    print(ok)
