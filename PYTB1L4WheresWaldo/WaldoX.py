import random
people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)
stoel = people.index("Waldo")

for x in people:
    print(x)
    if x == "Waldo":
        break
print("Waldo zit op stoel nummer", stoel + 1)
#Er is geen stoel nummer 0
