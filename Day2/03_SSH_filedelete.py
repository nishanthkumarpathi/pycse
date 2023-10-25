import paramiko

def ssh_delete_line_with_string(host, port, username, password, file_path, target_string):
    try:
        # Create an SSH client instance
        ssh = paramiko.SSHClient()

        # Automatically add the server's host key (this is insecure and used for demonstration; in a real-world scenario, you'd verify the host key)
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the SSH server
        ssh.connect(host, port, username, password)

        # Fetch the file content
        sftp = ssh.open_sftp()
        with sftp.file(file_path, 'r') as file:
            lines = file.readlines()

        # Remove lines containing the target string (case-insensitive) using a for loop
        new_lines = []
        for line in lines:
            if target_string.lower() not in line.lower():
                new_lines.append(line)
                
        # Write the updated content back to the file
        with sftp.file(file_path, 'w') as file:
            file.writelines(new_lines)

        print(f"Lines containing '{target_string}' (case-insensitive) have been deleted from {file_path}!")

        # Close the SFTP and SSH connections
        sftp.close()
        ssh.close()

    except Exception as e:
        print(f"An error occurred: {e}")


# Usage
host = "192.168.56.118"
port = 22  # Default SSH port
username = "nishanth"
password = "nishanth"
file_path = "/home/nishanth/Desktop/tobedeleted/delete.txt"
target_string = "casb"

ssh_delete_line_with_string(host, port, username, password, file_path, target_string)
