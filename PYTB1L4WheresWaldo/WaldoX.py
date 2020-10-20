import random
people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)

stoel = 0

for x in people:
    print(x)
    stoel += 1
    if x == "Waldo":
        break
        
print(stoel)
        
print("Waldo zit op stoel nummer", stoel)


print(people)
