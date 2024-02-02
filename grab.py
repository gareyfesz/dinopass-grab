import requests

# define dinopass url for generating a simple password

dinopass_url = "https://dinopass.com/password/simple"

def generate_password():
    response = requests.get(dinopass_url)
    if response.status_code == 200:
        return response.text.strip()
    else:
        print("failed to query api")
        return none
    

def main():
    password = generate_password()
    if password:
        print("generated password:", password)