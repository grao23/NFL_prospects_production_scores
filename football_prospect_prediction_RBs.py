# Initialize an empty list to store the runningbacks data
runningbacks = []

# Define the formula to calculate the NFL grade
def calculate_nfl_grade(rb):
    height = rb['height']
    weight = rb['weight']
    rushing_yards = rb['rushing yards']
    rushing_td = rb['rushing tds']
    yards_per_attempt = rb['yards per attempt']
    receptions = rb['Receptions']
    receiving_yards = rb['Receiving yards']
    receiving_td = rb['Receiving Td']
    broken_tackles = rb['broken tackles']
    fumbles = rb['Fumbles']
    runs_for_loss = rb['Runs for loss']
    explosive_factor = rb['Runs for 20 or more']

    # Calculate the NFL grade using a specific formula
    nfl_grade = (
        (height * 0.04) + (weight * 0.04) + (rushing_yards * 0.14)  + (rushing_td * 0.13)
        + (yards_per_attempt * 0.10) + (receptions * 0.04) + (receiving_yards * 0.08) + (receiving_td * 0.13)
        + (broken_tackles * 0.07) - (fumbles * 0.08) - (runs_for_loss * 0.07) + (explosive_factor * 0.08)
    ) / 4
    return nfl_grade

# Function to input runningbacks data and calculate NFL grade
def input_runningbacks_data():
    rb = {}
    rb['name'] = input("Enter Runningback's name: ")
    rb['height'] = float(input("Enter Runningback's height (in inches): "))
    rb['weight'] = float(input("Enter Runningback's weight (in pounds): "))
    rb['rushing yards'] = int(input("Enter Runningback's rushing yards: "))
    rb['rushing tds'] = int(input("Enter Runningback's rushing touchdowns: "))
    rb['yards per attempt'] = float(input("Enter Runningback's yards per attempt: "))
    rb['Receptions'] = int(input("Enter Runningback's receptions: "))
    rb['Receiving yards'] = int(input("Enter Runningback's receiving yards: "))
    rb['Receiving Td'] = int(input("Enter Runningback's receiving touchdowns: "))
    rb['broken tackles'] = int(input("Enter Runningback's broken tackles: "))
    rb['Fumbles'] = int(input("Enter Runningback's fumbles: "))
    rb['Runs for loss'] = int(input("Enter Runningback's runs for loss: "))
    rb['Runs for 20 or more'] = int(input("Enter Runningback's runs for 20 or more: "))

    rb['nfl_grade'] = calculate_nfl_grade(rb)

    return rb

# Function to rank runningbacks based on their NFL grade
def rank_runningbacks():
    ranked_rbs = sorted(runningbacks, key=lambda x: x['nfl_grade'], reverse=True)
    print("\nRunningbacks Ranked by NFL Grade:")
    for i, rb in enumerate(ranked_rbs, 1):
        print(f"{i}. Runningback: {rb['name']}, NFL Grade: {rb['nfl_grade']:.2f}/100")

# Main program loop
while True:
    choice = input("\nEnter '1' to input a new runningback, '2' to rank runningbacks, or '3' to exit: ")
    
    if choice == '1':
        rb = input_runningbacks_data()
        rb['name'] = input("Enter Runningback name: ")
        runningbacks.append(rb)
    elif choice == '2':
        rank_runningbacks()
    elif choice == '3':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")