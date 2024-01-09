# Software to show the message 'Good morning, Good afternoon or Goodnight'
# depending on the user's time input
# Calibrated to recognize ':' and stop minutes above 60
import os   # Important to clear the console
software_active = True # If the program should repet or end at the final input
leave_software = "" # User input to finish the program
user_time = ""    # User input for the time
user_time_is_float = None # Variable to identify if the input is a acceptable time
minutes = None  # To check if the minutes do not surpass 60

while software_active:

    # User input already replacing two dots
    user_time = input("Forneça um horário: ").replace(":", ".")
    
    # Verifying if the minutes inserted are bellow 60    
    if user_time.find("."):
        minutes = user_time.find(".") + 1
        try:
            float(user_time)
            if int(user_time[minutes]) >= 6:
                user_time = ""
        except:
            pass
    
    # Changing input to float to remain only numbers
    try:
        user_time = float(user_time)
        user_time_is_float = True
    except:
        user_time_is_float = False       
    
    # Float number is used to determine the message
    # If the input is not a float or is above 23h it will display an error    
    if user_time_is_float == True and user_time <= 11:
        print("Good morning!")
    elif user_time_is_float == True and (user_time >= 12 and user_time <= 17):
        print("Good afternoon!")
    elif user_time_is_float == True and (user_time >= 18 and user_time < 24):
        print("Goodnight!")
    else:
        print("You did not input a valid time.")
            
    # New input to end the program or return to the beginning
    leave_software = input("Would you like to end the software? Press [l] to leave: ").lower()
    if leave_software == "l":
        software_active = False
        print("You closed the application.")
    else:
        user_time = ""
        user_time_is_float = None
        leave_software = ""
        os.system("cls")