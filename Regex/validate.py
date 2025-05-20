# email = input("email: ").strip()

# if loop
# if "@" in email and "." in email:
#     print("valid")
# else:
#     print("invalid")

# username, domain = email.split("@")

# example: saipraneeth@gmail.edu (no specific ending like .in, .com)
# if (username) and ("." in domain):
#     print("valid")
# else:
#     print("invalid")

# if username and domain.endswith((".com", ".in")):
#     print("Valid")
# else:
#     print("Invalid")

## regex library
import re

email = input("email: ").strip()

# if re.search(r"^[^@]+@[^@]+\.com$", email):
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$", email):
# if re.search(r"^(\w|.)+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")