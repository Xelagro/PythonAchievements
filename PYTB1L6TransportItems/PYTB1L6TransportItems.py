import time 
 
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
        print("Making car")
        Factory.append("car")
        time.sleep(2)
        print("Car has been build")
        time.sleep(2)
        print("factory = " + str(Factory))
        print("Distribution =" + str(Distribution))
        print("Shop =" + str(Shop))
        print("-----------------------------------------------")
        time.sleep(2)
        print("Car is transporting to the Distribution")
        Distribution.append(Factory.pop())
        time.sleep(2)
        print("The car has reached Distribution")
        time.sleep(2)
        print("factory = " + str(Factory))
        print("Distribution =" + str(Distribution))
        print("Shop =" + str(Shop))
        print("-----------------------------------------------")
        time.sleep(2)
        print("Car is transporting to the Store")
        Shop.append (Distribution.pop())
        time.sleep(2)
        print("The car has reached the Store")
        time.sleep(2)
        print("factory = " + str(Factory))
        print("Distribution =" + str(Distribution))
        print("Shop =" + str(Shop))
        print("---------------------------------------------")
        time.sleep(2)
        print("Someone bought the car")
        Shop.clear()
        time.sleep(2)
        print("The car has been sold")
        time.sleep(2
        print("factory = " + str(Factory))
        print("Distribution =" + str(Distribution))
        print("Shop =" + str(Shop))
        print("--------------------------------------------")
        time.sleep(2)
        print("Would you like to make more cars? Y/N")
        Antword = input()
        if Antword == "Y" or Antword == "y":
            Car = True
        else:
            print ("Shutting down the program")
            Car = False
    else:
        print ("Shutting down the program")
        Car = False
