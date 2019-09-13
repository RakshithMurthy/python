                        LIST PROGRAM
def listfun():
    carlist = ["swift","audi","benz","duster"]
    print(" i have", len(carlist), "cars to buy")


    print("\n i also have to buy mg ")
    carlist.append("mg")
    print("my car list is now", carlist)

    print(" i will sort my list now")
    carlist.sort()
    print(" sorted car list is" , carlist)


    print(" the first car i will buy is", carlist[2])
    newcar= carlist[2]
    del carlist[2]
    print("i bought the", newcar)
    print(" the car list is now", carlist)
listfun()                                
                                  
                                  
                                  output
                                  
                                  
           i have 4 cars to buy

 i also have to buy mg 
my car list is now ['swift', 'audi', 'benz', 'duster', 'mg']
 i will sort my list now
 sorted car list is ['audi', 'benz', 'duster', 'mg', 'swift']
 the first car i will buy is duster
i bought the duster
 the car list is now ['audi', 'benz', 'mg', 'swift']                            
                                  
                                  
                                  
