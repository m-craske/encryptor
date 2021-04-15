#
# File: cramy021_encryptor.py
# Author: Marc Craske
# Email Id: cramy021
# Date: 2020.05.04
# Description: Programming Assignment 2 - Ceasar Cipher
#
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

# Function to display my details.
def display_details():
    print('File     : cramy021_encryptor.py')
    print('Author   : Marc Craske')
    print('Email Id : cramy021')
    print('Description: Programming Assignment 2 - Ceasar Cipher')
    print('This is my own work as defined by the University\'s Academic Misconduct policy.\n')


# Function for displaying menu and prompting user for their choice. Returns their choice.
def get_menu_choice():
    print('\n*** Menu ***')
    print('\n1. Encrypt string')
    print('2. Decrypt string')
    print('3. Brute force decryption')
    print('4. Quit\n')
    
    # Prompt user for choice, and store as integer.
    m_command = int(input('What would you like to do [1,2,3,4]? '))    
    
    # Validate the correct integer is entered by user.
    while not 1 <= m_command <= 4:
        print('Invalid choice, please enter either 1, 2, 3 or 4.')
        m_command = int(input('\nWhat would you like to do [1,2,3,4]? '))
    
    # Return the menu command
    return m_command


# Function for prompting and validating user for an offset value.
def get_offset():
    
    # Prompt user for the offset value and assign to integer.
    offset = int(input('Please enter offset value (1 to 94): '))
    
    # Validate the integer entered is within the required range.
    while not 1 <= offset <= 94:
        offset = int(input('Please enter offset value (1 to 94): '))
    
    # Return the offset value.
    return offset


display_details()

# Initialise variable.
menu_item = 0

# Run and loop entire program unless user chooses to quit using choice 4.
while menu_item != 4:
    
    # Variable set to whatever is returned by the function.
    menu_item = get_menu_choice()
    
    # First choice. Encryption process.
    if menu_item == 1:

        # Variables.
        user_input = input('\nPlease enter string to encrypt: ')          # Prompt user for the string to encrypt.
        decrypted = list(user_input)                                      # Store users string as a list.
        encrypted_step1 = []                                              # Step 1 variable for the encryption process.
        encrypted_step2 = []                                              # Step 2 variable for the encryption process.
        encrypted = ''                                                    # The encrypted value as a string.
        
        # Call function, and store returned result to variable.
        offset = get_offset()
        
        # Convert user string into the integer (ASCII value), stored as a list.
        for x in decrypted:
            encrypted_step1.append(ord(x))
        
        # Apply the offset value to the integer. If it is larger than 126, wrap back to 1 by taking away 95.
        for x in range(0, len(encrypted_step1)):
            encrypted_step1[x] = encrypted_step1[x] + offset
            if encrypted_step1[x] > 126:
                encrypted_step1[x] = encrypted_step1[x] - 95
        
        # Convert the integer (ASCII) back to a string. This is still in a list.
        for x in encrypted_step1:
            encrypted_step2.append(chr(x))
        
        # Assign the list values to a string.
        index = 0
        while index < len(encrypted_step2):
            encrypted += encrypted_step2[index]
            index = index + 1
        
        print('\nEncrypted string:')
        print(encrypted)
    
    # Second choice. Decryption process.
    elif menu_item == 2:

        # Variables.
        user_input = input('\nPlease enter the string to decrypt: ')      # Prompt user for the string to decrypt.
        encrypted = list(user_input)                                      # Store users string as a list.
        decrypted_step1 = []                                              # Step 1 variable for the decryption process.
        decrypted_step2 = []                                              # Step 2 variable for the decryption process.
        decrypted = ''                                                    # The decryption value as a string.
        
        # Call function, and store returned result to variable.
        offset = get_offset()
            
        # Convert user string to an integer (ASCII), stored as a list.
        for x in encrypted:
            decrypted_step1.append(ord(x))
            
        # Apply the offset value to the integer. If it is smaller than 32, add back 95..
        for x in range(0, len(decrypted_step1)):
            decrypted_step1[x] = decrypted_step1[x] - offset
            if decrypted_step1[x] < 32:
                decrypted_step1[x] = decrypted_step1[x] + 95
                
        # Convert the integer (ASCII) back to a string. This is still in a list.
        for x in decrypted_step1:
            decrypted_step2.append(chr(x))
            
        # Assign the list values to a string.
        index = 0
        while index < len(decrypted_step2):
            decrypted += decrypted_step2[index]
            index = index + 1
        
        print('\nDecrypted string:')
        print(decrypted)

    # Third choice. Brute force.    
    elif menu_item == 3:
        
        # Variables.
        user_input = input('\nPlease enter the string to decrypt: ')      # Prompt user for the string to decrypt.
        encrypted = list(user_input)                                      # Store users string as a list.    
        offset = 1                                                        # Offset counter
        
        # Just adding a blank line. Nothing to see here.
        print()
        
        # Loop through until 94 iterations are made.
        while offset < 95:
            
            # Variables. These need to be reinitialised inside the loop.
            decrypted_step1 = []                                              # Step 1 variable for the decryption process.
            decrypted_step2 = []                                              # Step 2 variable for the decryption process.
            decrypted = ''                                                    # The decryption value as a string.
            
            # Convert user string to an integer (ASCII), stored as a list.
            for x in encrypted:
                decrypted_step1.append(ord(x))
                
            # Apply the offset value to the integer. If it is smaller than 32, add back 95..
            for x in range(0, len(decrypted_step1)):
                decrypted_step1[x] = decrypted_step1[x] - offset
                if decrypted_step1[x] < 32:
                    decrypted_step1[x] = decrypted_step1[x] + 95
                    
            # Convert the integer (ASCII) back to a string. This is still in a list.
            for x in decrypted_step1:
                decrypted_step2.append(chr(x))
                
            # Assign the list values to a string.
            index = 0
            while index < len(decrypted_step2):
                decrypted += decrypted_step2[index]
                index = index + 1
            
            # Display text and decrypted string to screen.
            print('Offset:', offset, '= Decryptred string: ', decrypted)
            
            # Add 1 to offset counter.
            offset += 1
            
    # Fourth choice. Exit.        
    elif menu_item == 4:
        print('\nGoodbye.')
