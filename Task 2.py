from statistics import mean

print("Swallow Speed Analysis: Version 1.0\n")

data_list = []  #List to store data
input_data = input("Enter the Next Reading: ") #Input data from user
if input_data == "":    #if no data is entered, exit
    print("No readings entered. Nothing to do.")
else:
    while input_data != "":  
        if input_data[0].upper() == "U":     #User input has to be entered in U20, U30 format (British system)
            print("Reading saved")          
            data_list.append(float(input_data[1:])*1.61)    #Readings stored in list
            input_data = input("Enter the Next Reading: ")
        elif input_data[0].upper() == "E":   #User input has to be entered in E20, E30 format (European system)
            print("Reading saved")
            data_list.append(float(input_data[1:]))         #Readings stored in list
            input_data = input("Enter the Next Reading: ")                    
        else:
            break

    if (len(data_list) != 0):               #If data_list is not empty, results will be displayed
        print("\nResults summary\n")

        print(len(data_list), "Reading Analysed\n")
        print(f"Max Speed: {max(data_list)/1.61:.1f} MPH, {max(data_list):.1f} KPH")
        print(f"Min Speed: {min(data_list)/1.61:.1f} MPH, {min(data_list):.1f} KPH")
        
        average = mean(data_list)
        print(f"Avg Speed: {(average/1.61):.1f} MPH, {average:.1f} KPH.")
    else:
        print("Invalid")
