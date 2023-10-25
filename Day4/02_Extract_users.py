# Jul 26 04:05:23 combo su(pam_unix)[27285]: session closed for user cyrus
# Jul 26 04:11:23 combo su(pam_unix)[28514]: session opened for user news by (uid=0)
# Jul 26 04:11:23 combo su(pam_unix)[28514]: session closed for user news
# Jul 27 04:16:07 combo su(pam_unix)[30999]: session opened for user cyrus by (uid=0)
# Jul 27 04:16:08 combo su(pam_unix)[30999]: session closed for user cyrus
# Jul 27 04:21:39 combo su(pam_unix)[31373]: session opened for user news by (uid=0)
# Jul 27 04:21:40 combo su(pam_unix)[31373]: session closed for user news

import re
from collections import Counter

def extract_ips_from_logs(log_file):
    with open(log_file, "r") as file:
        log_data = file.read()
    users = re.findall(r"user[=| ](\w+)", log_data)
    return users

usersarray = extract_ips_from_logs("Linux_2k.log")

user_counts = Counter(usersarray)

high = user_counts.most_common(10)

print(high)

# for ip, count in ip_counts.items():
#     print(f"IP Address {ip} occurred {count} times.")