services1 = {"FTP":21, "SSH":22, "SMTP":25, "HTTP":80}

# MyOwnFunction
def myOwnFunction(services1):
    # Business Logic
    for key,value in services1.items():
        print(key, value)

myOwnFunction(services1)