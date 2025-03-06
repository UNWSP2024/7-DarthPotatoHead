#Program Written By: Ainsley Bellamy
#Date Written: 03/06/2025
#Program Title: Rainfall_Operations


# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.

#Constant number of months.
MONTHS = 12
#Function that gets the amount of rainfall per month and returns a list of those values.
def get_rainfall():
    rainfallPerMonth = [0] * MONTHS
    for index in range(MONTHS):
        rainfallPerMonth[index] = float(input(f"Enter amount of rainfall for month {index + 1}: "))
#Error handling.
        while rainfallPerMonth[index] <= 0:
            rainfallPerMonth[index] = float(input(f"~Error: Input cannot be less than or equal to zero~ Enter "
                                                  f"Amount of rainfall for month {index + 1}: "))
    return rainfallPerMonth

#Function that then performs operations on list and displays the desires results, including the summed total,
#average of those values, highest, and lowest.
def main():
    rainfall = get_rainfall()
    total_rainfall = sum(rainfall)
    monthly_average = total_rainfall / len(rainfall)
    lowest = min(rainfall)
    highest = max(rainfall)
    print(f"Year Total\t\t\tMonthly Average\t\t\tLowest Rainfall\t\t\tHighest Rainfall")
    print("------------------------------------------------------------------------------------")
    print(f"{total_rainfall:<20.2f}{monthly_average:^20.2f}{lowest:^20.2f}{highest:>20.2f}")

if __name__ == "__main__":
    main()