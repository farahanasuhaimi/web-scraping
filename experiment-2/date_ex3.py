import pandas as pd
from datetime import date, timedelta

# Define a function to calculate non-working days for a specific region
def get_non_working_days(region, year):
    # Create a list of non-working days for the specified region
    if region in ['Kedah', 'Kelantan', 'Terengganu', 'Johor']:
        weekend_days = [5, 6]  # Friday and Saturday
    else:
        weekend_days = [5, 6]  # Saturday and Sunday

    # Initialize a list to store the non-working days
    non_working_days = []

    # Iterate through the year and month to identify non-working days
    for month in range(1, 13):  # 1 to 12 months
        for day in range(1, 32):  # 1 to 31 days
            try:
                # Create a date object for the current day
                current_date = date(year, month, day)
                
                # Check if the day of the week is in the weekend_days list
                if current_date.weekday() in weekend_days:
                    non_working_days.append(current_date.strftime('%b %d %Y'))
            except ValueError:
                # Handle exceptions for invalid dates (e.g., February 30)
                pass

    return non_working_days

# Define the year for which you want to calculate non-working days
year = 2023

# List of regions
regions = ['Kedah', 'Kelantan', 'Terengganu', 'Johor', 'Selangor', 'Perak', 'Pahang', 'Melaka', 'Negeri Sembilan', 'Penang', 'Perlis', 'Sabah', 'Sarawak', 'Kuala Lumpur', 'Labuan', 'Putrajaya']

# Calculate and print non-working days for each region
for region in regions:
    non_working_days = get_non_working_days(region, year)
    print(f"Non-working days in {region} for the year {year}:\n")
    for day in non_working_days:
        print(day)
    print("\n")
