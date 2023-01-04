# Assignment 1: RANDOM RESTAURANT PICKER
# Dominic Chen
# Student ID: 501172557

# A problem I have, as well as many others, is the inablity to make a choice.
# For my assignment, I created a program that prompts the user to input a list
# of restaurants, including the cusine, and the program will choose one restaurant
# randomly. This program solves the difficult question of "Where should we eat?" and
# can be used by many people, like couples, friend groups, family, etc. One of the
# most difficult questions to answer can potentially be solved with this program.

# 3 Main outputs:
#   1: Random restaurant with random cusine
#   2: Random restaurantn with select cusine
#   3: User does not want a random choice, nothing returned

import random

# Initialize global lists
# List of possible cusines
cusines = ["chinese","japanese","korean","italian","american","canadian","vietnamese","mexican"]

# Lists for restaurants of each cusine
chineseRest = []
japaneseRest = []
koreanRest = []
italianRest = []
americanRest = []
canadianRest = []
vietnameseRest = []
mexicanRest = []

restList = [chineseRest, japaneseRest, koreanRest, italianRest, americanRest, canadianRest, vietnameseRest, mexicanRest]

# Function 1: Prompts the user to enter the cuinse they have in mind
def promptCusine():
    # The .lower() method is used to match the case of cusines list
    cusine = (input("\nWhat cusine do you crave?(stop to end, or view to preview): ")).lower()
    
    # This gives the user an option to end the prompt or view the progress they have made
    if cusine == "stop" or cusine == "view":
        return cusine
    
    # If the cusine is not found in the cusines list, the while loop will prompt 
    # the user for another cusine until they enter one that matches
    while not cusine in cusines:
        cusine = input("Cusine not found. Try again: ")
        if cusine == "stop" or cusine == "view":
            return cusine
    
    return cusine

# Function 2: Prompts the user to enter the name of the restaurant for 
# corresponding cusine
def promptRestaurant(cusineList):
        rest = input("Enter restaurant name: ")
        cusineList.append(rest)
        print(f"{cusine} restaurant \"{rest}\" added!")

# Function 3: Prints all of the cusines followed with all inputted restaurants 
# for corresponding cusine
def printRestaurants():
    print("\nHere are the lists of restaurants!")
    print(f"Chinese: {chineseRest}")
    print(f"Japanese: {japaneseRest}")
    print(f"Korean: {koreanRest}")
    print(f"Vietnamese: {vietnameseRest}")
    print(f"Italian: {italianRest}")
    print(f"American: {americanRest}")
    print(f"Canadian: {canadianRest}")
    print(f"Mexican: {mexicanRest}")

# Function 4: Automatic load of fake restaurants for test purposes
def loadRestaurants():
    for i in range(1,3):
        restList[0].append(f"Chinese Restaurant {i}")
        restList[1].append(f"Japanese Restaurant {i}")
        restList[2].append(f"Korean Restaurant {i}")
        restList[3].append(f"Italian Restaurant {i}")
        restList[4].append(f"American Restaurant {i}")
        restList[5].append(f"Canadian Restaurant {i}")
        restList[6].append(f"Vietnamese Restaurant {i}")
        restList[7].append(f"Mexican Restaurant {i}")

if __name__ == "__main__":
    
    # Load fake restaurants for testing
    loadRestaurants()
    
    # Initialize local variables
    cusine = ""
    count = 0
    end = False
    continues = ""
    
    # Loop until user enters "stop" for cusine input
    while not cusine == "stop":
        # Assign input to variable
        cusine = promptCusine()
        
        # Comparison string for each possible cusine, then call promptRestaurant
        # function with corresponding cusine restaurant list passed in as the argument
        if cusine == "chinese":
            promptRestaurant(chineseRest)
        elif cusine == "japanese":
            promptRestaurant(japaneseRest)
        elif cusine == "korean":
            promptRestaurant(koreanRest)
        elif cusine == "italian":
            promptRestaurant(italianRest)
        elif cusine == "american":
            promptRestaurant(americanRest)
        elif cusine == "canadian":
            promptRestaurant(canadianRest)
        elif cusine == "vietnamese":
            promptRestaurant(vietnameseRest)
        elif cusine == "mexican":
            promptRestaurant(mexicanRest)
        # If user inputs view, printRestaurants is called to review progress
        elif cusine == "view":
            printRestaurants()
    
    # print statements for format, and a final printRestaurants is called for the
    # user to view possible choices one last time            
    print()
    printRestaurants()
    print("\n")
            
    # Prompt the user if they would like a random choice in case they wish to
    # choose the restaurant themselves
    randomize = (input("Would you like a random choice? (y for yes): ")).lower()
    
    # Executes if the user wishes to have a random choice
    if randomize == "y":
        # Prompt the user if they wish for a certain cusine, narrowing selection if yes
        preferenceChoice = (input("Do you wish for a certain cusine? (y or n): ")).lower()
        
        # Loop until explicitly break
        while True:
            # If user wishes for a certain cusine, prompt user for the cusine
            if preferenceChoice == "y":
                preference = (input("\nWhat is your cusine?: ")).lower()
                
                # If the inputted cusine is not included, continue prompting until input
                # cusine is included in cusines list
                while not preference in cusines:
                    # If user wishes to stop program at this point, they will have the option to
                    if preference == "stop":
                        break
                    preference = (input("Cusine not found. Please try again: "))
                
                # Additional break if user wishes to stop program
                if preference == "stop":
                    break
                
                # Preferred cusine index is stored in variable
                ind = cusines.index(preference)
                
                # If the list of preffered cusine is empty, let the user know
                if len(restList[ind]) == 0:
                    print("There are no restaurants for that cusine. Sorry!")
                    # Let user try again
                    continue
                
                # Select random restaurant from preferred cusine
                rest = restList[ind]
                print(f"Cusine: {preference}\nRestaurant: {rest[random.randint(0,len(rest)-1)]}")
                
                # User is given †he choice to try again if they do not want given restaurant
                continues = input("\nAre you satisfied with this option? (n for no): ")
                
                # Begin back to the beginning of loop if user is not satisfied
                if continues == "n":
                    continue
                
                # Break out of while loop
                break
            
            # If user does not have preference cusine
            else:
                print("\nRandom choice it is:")
                
                # Iterate 100 times max
                while count < 100:
                    # Select random cusine from the cusines list
                    preference = cusines[random.randint(0,len(cusines)-1)]
                    # Get index of corresponding cusine
                    ind = cusines.index(preference)
                    
                    # If the restaurant list of corresponding index is not empty then break from loop
                    if not len(restList[ind]) == 0:
                        break
                    
                    # Increase counter by one
                    count += 1
                # If none is found after 100 iterations then the conclusion of an empty list
                # for all cusine restaurants is made
                else:
                    # Let user know no restaurants were found
                    print("WE CANT FIND ANYTHING")
                    # Flag variable to end iterations
                    end = True
                
                # If flag variable is not triggered
                if not end:
                    
                    # Restaurant list for correpsonding index is selected
                    rest = restList[ind]
                    
                    # Cusine is printed followed by a random restaurant of that cusine
                    print(f"Cusine: {preference}\nRestaurant: {rest[random.randint(0,len(rest)-1)]}")
                    
                    # User is given †he choice to try again if they do not want given restaurant
                    continues = input("\nAre you satisfied with this option? (n for no): ")
                    
                    # Begin back to the beginning of loop if user is not satisfied
                    if continues == "n":
                        continue
                    
            break
    
    # Goodbye message
    print("\nHave a good day!")
            
            
            
            
            
            
    
                