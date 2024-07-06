calls = 0

def count_calls():
    global calls
    calls = calls + 1

def string_info(string: str):
    count_calls()
    str_var = len(string), string.upper(), string.lower()
    return str_var

def is_contains(string: str, list_to_search: list):
    count_calls()
    presens = False
    i = 0
    while i < len(list_to_search):
        a: str = list_to_search[i]
        if string.lower() == a.lower():
            presens = True
        i = i + 1
    return presens

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
