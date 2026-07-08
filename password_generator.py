import random # Importing the random module to randomly select password characters

# Bundling the password generation code into a function
def generate_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    while True: # Main loop to keep asking for password length until a valid input is given
        try:
            password_result = "" # Password container
            password_length = int(input("How long would you like your password to be? (Example: 8) ")) # Asking the password length from the user
            
            if password_length <= 0:
                print("Please enter a positive number.")
                continue # Restart the loop
            elif password_length < 8:
                sure = input("Are you sure? (yes/no): ")
                if sure.lower() != "yes":
                    continue
            elif password_length > 20:
                print("Too long, isn't it? Please enter a number between 8 and 20.")
                continue
            for i in range(password_length): # Looping through the range of the password length
                password_result += random.choice(characters) # Randomly selecting a character from the characters variable
            print(f"Your generated password is: {password_result}")
            break
        except ValueError:
            print("Numbers only, please!")


# Asking the user whether they are satisfied or no
while True:
    generate_password()

    Retry = input("Retry? (yes/no) ")
    if Retry.lower() != "yes":
        print("Thank you for using this Password Generator!")
        break
