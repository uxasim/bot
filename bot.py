import os
import subprocess
from random import randint
from datetime import datetime, timedelta

# Define the file name for adding commit content
file_name = 'file.txt'

# Loop through the past 200 to 360 days
for i in range(2, 200):  # Adjusted range
    # Randomly skip some days
    if randint(1, 10) > 8:  # Skip approximately 20% of the days
        continue
    
    # Calculate the exact date
    commit_date = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d')
    weekday = (datetime.now() - timedelta(days=i)).weekday()
    
    # Skip weekends (Saturday=5, Sunday=6)
    if weekday in [5, 6]:
        continue
    
    # Number of commits for the day
    for _ in range(randint(1, 10)):  # Random commits (1 to 10) per day
        # Write content to the file
        with open(file_name, 'a') as file:
            file.write(f"Commit on {commit_date}\n")
        
        # Stage changes and make a backdated commit
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '--date', commit_date, '-m', f'Commit on {commit_date}'])

# Push all changes at once after all commits are done
subprocess.run(['git', 'push', '-u', 'origin', 'main'])