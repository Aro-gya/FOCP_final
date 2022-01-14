print("Stop! Who would cross the Bridge of Death\nMust answer me these questions three, 'ere the other side he see.")

#Input name from user
question_1 = input("What is your name? ")                       
question_1 = question_1.upper()                                 

#If King passes, access is granted without further questions
if "ARTHUR" in question_1:                                      
    print("My liege! You may pass!")
else:
#If Knight passes, he is asked further questions
    question_2 = input("What do you seek? ")                    
    question_2 = question_2.upper()                             

    #If it isn't "The Grail" the Knight seeks, he is denied access
    if "GRAIL" not in question_2:                               
        print("Only those who seek the Grail may pass!")
    else:
        #Now he is asked of his favourite colour
        question_3 = input("What is your favourite color? ")    
        question_3 = question_3.upper()                         
        
        #Knight's favourite colour must start with the first letter of his name
        #If answer is correct, he is allowed to pass
        if question_3[0]==question_1[0]:                       
            print("You may pass!")        

        #If the Knight does not know his favourite colour, he has to face the Gorge of Eternal Peril                      
        else:
            print("Incorrect! You must now face the Gorge of Eternal Peril")