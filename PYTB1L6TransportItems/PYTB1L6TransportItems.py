import time 
 #Lists
Factory = [ ] 
Distribution = [ ]
Shop = [ ]

Car = True
while ( Car == True ) :
    print("Factory =" + str(Factory) )
    print("Distribution =" + str(Distribution))
    print("Shop =" + str(Shop) ) 
    print("Do u want to make a car? Y/N")
    Antwoord = input()
    if Antwoord == "Y" or Antwoord == "y":
        print("-----------------------------------------------")
        print("U chose to make a Car.")
        Factory.append("car")
        time.sleep(2)
        print("Car building")
        time.sleep(2)
        print("factory = " + str(Factory))
        print("Distribution =" + str(Distribution))
        print("Shop =" + str(Shop))
        print("-----------------------------------------------")
        time.sleep(2)
        print("Transporting car to the Distribution")
        Distribution.append(Factory.pop())
        time.sleep(2)
        print("The car has reach the Distribution")
        time.sleep(2)
        print("factory = " + str(Factory))
        print("Distribution =" + str(Distribution))
        print("Shop =" + str(Shop))
        print("-----------------------------------------------")
        time.sleep(2)
        print("Transporting car to the Store")
        Shop.append (Distribution.pop())
        time.sleep(2)
        print("The car has reached the store")
        time.sleep(2)
        print("factory = " + str(Factory))
        print("Distribution =" + str(Distribution))
        print("Shop =" + str(Shop))
        print("---------------------------------------------")
        time.sleep(2)
        print("The Car gets bought")
        Shop.clear()
        time.sleep(2)
        print("The Car has been sold")
        time.sleep(2)
        print("factory = " + str(Factory))
        print("Distribution =" + str(Distribution))
        print("Shop =" + str(Shop))
        print("--------------------------------------------")
        time.sleep(2)
        print("Would u like to make more cars?? Y/N")
        Antword = input()
        if Antword == "Y" or Antword == "y":
            Car = True
        else:
            print ("Shutting down the program")
            Car = False
    else:
        print ("Shutting down the program")
        Car = False
