# Network Proframming Python - HTTP Clients

import requests

#send requests
req = requests.get('https://www.geeksforgeeks.org/')

# Show results
print(req.text[:2000], end="\n\n\n\n")

# Creating session
s = requests.Session()
s.get('http://httpbin.org/cookies')

# Getting response
r = s.get('http://httpbin.org/cookies')

# Show response
print(r.text)


# Error handling
try:
    # Creating request
    req = requests.get('https://geeksforgeeks.org/', timeout=0.000001)

except requests.exceptions.RequestException as e:

    # Raising Error
    raise SystemExit(e)