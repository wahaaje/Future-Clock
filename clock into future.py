

def calculate_future_hour():
    time = int(input("Enter the current hour (1-12): "))
    am_or_pm = input("Enter am or pm: ")
    future_hours = int(input("Enter the number of hours into the future: "))

    # Convert hour to 24-hour format for easier calculations
    if am_or_pm.lower() == "pm":
        time += 12

    # Calculate future hour
    future_time = (time + future_hours) % 24

    # Convert back to 12-hour format
    if future_time == 0:
        future_time = 12
        future_am_or_pm = "am"
    elif future_time < 12:
        future_am_or_pm = "am"
    else:
        future_time -= 12
        future_am_or_pm = "pm"

    print(f"The hour {future_hours} hours into the future will be {future_time} {future_am_or_pm}.")

# Run the program
calculate_future_hour()
