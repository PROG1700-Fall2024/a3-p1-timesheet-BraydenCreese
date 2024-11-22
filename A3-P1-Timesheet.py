#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #: Brayden Creese
#Student Name: W0491583

def timeSheet():

    dailyHours = []

    for i in range(5):
        while True:
            try:
                hoursWorked = float(input(f"Enter hours worked on Day #{i + 1}: "))
                if hoursWorked < 0:
                    print("Invalid Input! Please enter a postive number for 'hours worked'.")
                    continue
                dailyHours.append(hoursWorked)
                break
            except ValueError:
                print("Invalid Input! Please enter a valid number for 'hours worked'.")

    print("-" * 60)


    mostHours = max(dailyHours)
    mostHourDay = []
    for i in range(len(dailyHours)):
        if dailyHours[i] == mostHours:
            mostHourDay.append(f"Day {i+1}")

    totalHours = sum(dailyHours)
    averageHours = totalHours / len(dailyHours)

    slackDays = []
    for i in range(len(dailyHours)):
        if dailyHours[i] < 7:
            slackDays.append(f"Day {i+1}")


    return mostHourDay, mostHours, totalHours, averageHours, slackDays


def main():

    mostHourDay, mostHours, totalHours, averageHours, slackDays = timeSheet()

    print(f"The most hours worked was on:\n {mostHourDay} when you worked {mostHours} hours.")
    print("-" * 60)
    print(f"The total number of hours worked was: {totalHours}")
    print(f"The average number of hours worked on each day was: {averageHours}")
    print("-" * 60)
    print(f"Days you slacked off (i.e. worked less then 7 hours): {', '.join(slackDays) if slackDays else 'None'}") 


main()
