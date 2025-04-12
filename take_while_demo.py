# https://www.kdnuggets.com/lesser-known-python-functions-that-are-super-useful
from itertools import takewhile

# Processing log entries until an error
log_entries = [
	"INFO: System started",
	"INFO: Loading data",
	"INFO: Processing users",
	"ERROR: Database connection failed",
	"INFO: Retrying connection",
]

# Get all logs until first error
normal_operation = list(takewhile(
	lambda x: not x.startswith("ERROR"),
	log_entries
))
print("Logs before first error:")
for entry in normal_operation:
    print(entry)