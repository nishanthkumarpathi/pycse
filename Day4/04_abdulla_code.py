import re
from collections import Counter

# Define a function to extract IP addresses from a log file
def extract_ips_from_log(log_file_path):
# Open the log file and read its content
    with open(log_file_path, 'r') as file:
        log_data = file.read()
# Use a regular expression to find all IP addresses in the log data
    user = re.findall(r"user[=| ](\w+)", log_data)
    return user


# Call the function and print the extracted IP addresses
usersarray = extract_ips_from_log('Linux_2k.log')

user_counts = Counter(usersarray)

high = user_counts.most_common(10)

print(high)