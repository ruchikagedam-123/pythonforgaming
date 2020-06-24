# Firstly we have to import json file which has all the necessary data for Dictionary
import json
# get_close_matches takes the input and cross check the inputed word against the data which is stored in JSON file.
from difflib import get_close_matches

# loading Data
data = json.load(open("data.json"))


# A function which get word from user which is inputted
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0 :
        print("did you mean %s instead" % get_close_matches(word, data.keys())[0])
        decision = input("press y for yes or N for No")
        if decision =="y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decision =="N":
            return("You steps on wrong key")
        else:
            return ("You have entered wrong input please enter just 'y' or 'n' \n")
    else:
        print("You steps on wrong key")

# calling translate method
word = input("Enter the word you want to search   :  \n")
output = translate(word)
if type(output) == list:
    for item in output:
        print("Meaning : ",item)
else:
    print(output)

OUTPUT :
Enter the word you want to search   :  
cl;ose
did you mean close instead
press y for yes or N for Noy
Meaning :  At a little distance.
Meaning :  To make something end.
Meaning :  To move (a door, a window, etc.) so that it closes its opening.
Meaning :  Not far distant in time or space or degree or circumstances.
Meaning :  To become closed.
Meaning :  To cease to operate or cause to cease operating (e.g. a business or a shop).
Meaning :  To complete a business deal, negotiation, or an agreement.
Meaning :  To be priced or listed when trading stops.
Meaning :  To cause a window or an application to disappear on a computer desktop.
