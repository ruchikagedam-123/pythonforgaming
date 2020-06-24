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
