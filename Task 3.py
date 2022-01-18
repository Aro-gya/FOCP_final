import random
print("Welcome to Popchat\nOne of our operators will be pleased to help you today")
helpdesk = ["Elliot","Tyrell","Darlene","Angela"]       #List of helpdesk operators
probability_list = [9,9,9,9,6,9,9,9,9,9]                #List to check for network error

email = input("Please enter your Poppleton email address: ")    #Input email from user
count = 0

valid = False
if "@" in email:            #If "@" is in email, then only the email is valid
    e = email.split("@")    #Split function to split the part before and after the "@"
    count = 0               #count variable to count the number of cahracters before "@"
    for i in e[0]:          #for loop to extract characters before "@"
        count += 1          #Count value increased by 1 for each character

    #If the part before "@" has two or more characters and the domain is correct, then only email is valid
    if count >=2 and e[1] == "pop.ac.uk":   
        valid = True 

        operator = random.choice(helpdesk)             #Pick any operator from the helpdesk list
        probability = random.choice(probability_list)  #Pick any number from probability list

        print("Hi,",e[0].capitalize(),"! Thank you, and welcome to PopChat!")   #
        print("My name is",operator,", and it will be my pleasure to help you.")

        if probability == 6:    #Situation for network error and exit, only sometimes
            print("*** NETWORK ERROR ***")
            print("Thanks,",e[0].capitalize(),"for using PopChat. See you soon!")
            exit()

        #while loop executes only when the email is valid
        while True:
            #user_prompt to ask for what user wants
            user_prompt = input("---> ")        
            #If user_prompt does not match any of the services available, an item from invalid_prompt is displayed 
            invalid_prompt = ["Hmmmmm","Tell me more about it","I didn't understand","Can you repeat it please","Oh yes i see"]
            #If user wants to exit the chat service, an item from exit_prompt must be entered
            exit_prompt = ["EXIT","STOP","QUIT","END","GOODBYE","BYE"]
            #Any replt from invalid_prompt may be displayed
            random_reply = random.choice(invalid_prompt)
            if "WIFI" in user_prompt.upper():
                print("The wifi is excellent around campus.")
            elif "LIBRARY" in user_prompt.upper():
                print("The library is closed today.")
            elif "DEADLINE" in user_prompt.upper():
                print("Your deadline has been extended by two working days.")
            elif "FOOD" in user_prompt.upper() or "CAFETERIA" in user_prompt.upper():
                print("The cafeteria is on the ground floor right next to the lobby.")
            elif "WASHROOM" in user_prompt.upper():
                print("The washroom is around the far-west corner of each floor.")
            elif "COMPUTER LABORATORY" in user_prompt.upper():
                print("The computer labs are at the 3rd floor.")
            elif "SERVER ROOM" in user_prompt.upper():
                print("The server room is off-limits. Authorized personnel only!")
            else:
            #If the request matches any of the one in exit_prompt, then service will stop
                for j in exit_prompt:
                    if j in user_prompt.upper():
                        print("Thanks,",e[0].capitalize(),"for using PopChat. See you soon!")
                        exit()
                else:
                    print(random_reply)
    else:
        #If the email domain doesn't match the requirement, it is invalid
        print("Email is invalid")      
else:
    #If the email doesn't contact "@", then it is invalid
    print("Email is invalid")           
    exit()

