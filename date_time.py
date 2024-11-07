from datetime import datetime
import pytz

# Get the current time in a specific timezone (e.g., +03:00)
timezone = pytz.timezone('Asia/Calcutta')  # Change this to your desired timezone
current_time = datetime.now(timezone)

# Format the current time
formatted_time = current_time.strftime('%Y-%m-%dT%H:%M:%S.%f%z')

# Adjust the timezone offset to match the format (+03:00)
#take substring from beginning till two characters before the end
#add ":" and then add the last two characters
formatted_time = formatted_time[:-2] + ':' + formatted_time[-2:]

print(f"curernt date and time is={formatted_time}")
