import re

def match(phrase):
    find = "hello world";
    if (re.search(find, phrase) != None):
        print("Match Found")
    else: print("No Match")

def vowels(phrase):
    find = r'[aeiouAEIOU]{3,}'

    matches = re.findall(find,phrase)
    print(matches)
    return matches
    
def flightCode(phrase):
    find= r'^[A]{2}\d{3,4}$'
    if re.match(find, phrase):
       print(f"{phrase} is a valid code") 
       return True
    else:
       print(f"{phrase} is an invalid code") 
       return False




vowels("The gooey peanut butter and jelly sandwich was a beauty")

match('hello world')

flightCode("AA123 extratext")