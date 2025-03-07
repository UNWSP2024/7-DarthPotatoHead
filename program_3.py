# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For example it might be stored like this:
    
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
#Empty list to append new lists to.
    all_entered_values = []
    keep_going = "y"
    while keep_going != "n":
        date = int(input("Enter the year date: "))
        state = str(input("Enter name of state: "))
        population = int(input("Enter population: "))
#Append these three variables as a new list.
        all_entered_values.append([date, state, population])
#Check if user would like to continue.
        keep_going = str(input("Would you like to enter more information? Enter 'y' for 'yes' "
                               "or 'n' for 'no': "))
    # Now have the user enter a year.
    sum_date = int(input("Enter a date for which populations to sum: "))
#Check that value entered for year is valid.
    while sum_date < 0:
        date = int(input("~Error, input cannot be less than zero~ Enter a date for which populations to sum: "))
#Call next function, passing in these values.
    sum_population_for_year(all_entered_values, sum_date)
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year

#Function to find items with a year matching the one the user entered and then total those items' populations.
def sum_population_for_year(list, year):
    # Loop through and sum the populations for the appropriate year. 
    # e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
    # or 3,421,988 if they enterd 2011 for the year to sum.

    pop_sum = 0
#Loop through the list's items, namely other lists.
    for item in range(len(list)):
#Check if the first item in the list within the list matches the user's input year.
        if list[item][0] == year:
#If yes, adds the third index (population) to the pop_sum variable.
            pop_sum += list[item][2]
    # print the totalled population
    print(f"This is the total population for the items having a date of {year}: {pop_sum}")
# Call the main function.

if __name__ == '__main__':
    main()