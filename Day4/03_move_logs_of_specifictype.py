with open("Linux_2k.log", "r") as original_file:
    with open("999_auth_log.txt", "w") as auth_failure_logs:
        for line in original_file:
            if "authentication failure" in line:
                auth_failure_logs.write(line)

original_file.close()
auth_failure_logs.close()