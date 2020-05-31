path = "/etc/hosts"
redirect = "127.0.0.1"

websitelist = ["www.facebook.com"]

with open(path, 'r+') as file:
    content = file.read()
    for website in websitelist:
        if website in content:
            pass
        else:
            file.write(redirect + " " + website + "\n")
