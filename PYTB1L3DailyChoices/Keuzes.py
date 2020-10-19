print("Alaram gaat af wat doeje, slapen of wakker worden ?")
choice = input()
if choice == 'wakker worden':
    print("Je wordt goed wakker!")
elif choice == 'slapen':
    print("Je wordt te laat wakker.")
else:
    print(choice, " Is geen keuze u kunt kiezen uit slapen of wakker")

    

print("Je hebt een keuze om te ontbijten doen of niet doen ?")
choice = input()
if choice == 'niet doen':
    print("Je neemt geen ontbijt.")
elif choice == 'doen':
    print("Je neemt een lekker ontbijt")
else:
    print(choice, "Dit was geen optie u kon kiezen uit doen of niet doen")


print("Je moet naar school toe, OV of fiets ?")
choice = input()
if choice == 'OV':
    print("Je bent optijd gekomen")
elif choice == 'fiets':
    print("Je bent telaat.")
else:
    print(choice, "Dit was geen optie u kon kiezen uit OV of fiets")


print("Je hebt pauze, naar buiten of binnen blijven?")
choice = input()
if choice == 'buiten':
    print("Je hebt het koud.")
elif choice == 'binnen':
    print("Je hebt het warm omdat je binnen bent gebleven.")
else:
    print(choice, "Dit was geen optie u kon kiezen uit buiten en binnen ")



print("Je bent klaar en gaat naar huis, eten halen of geen eten halen?")
choice = input()
if choice == 'eten':
    print("Je hebt gegeten.")
elif choice == 'geen eten':
    print("Je hebt niet gegeten en hebt thuis honger")
else:
    print(choice, "Dit was geen optie u kon kiezen uit ")

