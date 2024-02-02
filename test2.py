import requests

# Define the URL for generating a simple password
DINOPASS_URL = "https://dinopass.com/password/simple"

# Function to generate a password from Dinopass
def generate_password():
    response = requests.get(DINOPASS_URL)
    if response.status_code == 200:
        return response.text.strip()
    else:
        print("Failed to generate password.")
        return None

# Main function
# def main():
#     # Generate a password from Dinopass
#     password = generate_password()
#     if password:
#         print("Generated password:", password)
#         # Now you can use the 'password' variable wherever you need it in your script
#         # For example:
#         # do_something_with_password(password)
#     else:
#         print("Password generation failed. Exiting.")

# if __name__ == "__main__":
#     main()


