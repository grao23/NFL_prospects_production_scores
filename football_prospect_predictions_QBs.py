1# Initialize an empty list to store the quarterback data
quarterbacks = []

# Define the formula to calculate the NFL grade
def calculate_nfl_grade(qb):
    height = qb['height']
    weight = qb['weight']
    passing_yards = qb['passing yards']
    passing_tds = qb['passing tds']
    interceptions = qb['interceptions']
    rushing_yards = qb['rushing yards']
    rushing_tds = qb['rushing tds']
    sacks_taken = qb['sacks taken']
    completion_percentage = qb['completion percentage']
    yards_per_pass_attempt = qb['yards per pass attempt']

    # Calculate the NFL grade using a specific formula
    nfl_grade = (
        ((height * 0.05) + (weight * 0.03) + (passing_yards * 0.145) +
        (passing_tds * 0.15) - (interceptions * 0.3) + (rushing_yards * 0.055) +
        (rushing_tds * 0.055) - (sacks_taken * 0.075) +
        (completion_percentage * 0.09) + (yards_per_pass_attempt * 0.06)) / 10
    )
    return nfl_grade

# Function to input quarterback data and calculate NFL grade
def input_quarterback_data():
    qb = {}
    qb['height'] = float(input("Enter quarterback's height (in inches): "))
    qb['weight'] = float(input("Enter quarterback's weight (in pounds): "))
    qb['passing yards'] = int(input("Enter quarterback's passing yards: "))
    qb['passing tds'] = int(input("Enter quarterback's passing touchdowns: "))
    qb['interceptions'] = int(input("Enter quarterback's interceptions: "))
    qb['rushing yards'] = int(input("Enter quarterback's rushing yards: "))
    qb['rushing tds'] = int(input("Enter quarterback's rushing touchdowns: "))
    qb['sacks taken'] = int(input("Enter quarterback's sacks taken: "))
    qb['completion percentage'] = float(input("Enter quarterback's completion percentage: "))
    qb['yards per pass attempt'] = float(input("Enter quarterback's yards per pass attempt: "))
    qb['nfl_grade'] = calculate_nfl_grade(qb)

    return qb

# Function to rank quarterbacks based on their NFL grade
def rank_quarterbacks():
    ranked_qbs = sorted(quarterbacks, key=lambda x: x['nfl_grade'], reverse=True)
    print("\nQuarterbacks Ranked by NFL Grade:")
    for i, qb in enumerate(ranked_qbs, 1):
        print(f"{i}. Quarterback: {qb['name']}, NFL Grade: {qb['nfl_grade']:.2f}/100")

# Main program loop
while True:
    choice = input("\nEnter '1' to input a new quarterback, '2' to rank quarterbacks, or '3' to exit: ")
    
    if choice == '1':
        qb = input_quarterback_data()
        qb['name'] = input("Enter quarterback's name: ")
        quarterbacks.append(qb)
    elif choice == '2':
        rank_quarterbacks()
    elif choice == '3':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")