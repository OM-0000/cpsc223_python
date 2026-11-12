""" 
        Request Methods

delete(url, args)               :               used to DELETE all the contents represented by the current target source of the specified URL
get(url, params, args)          :               used to GET information from the server of a specified URL, it only retrieves data and does not affect other resources
head(url, args)                 :               it is the same as GET used specifically to transfer status line and header of the specified URL.
patch(url, data, args)          :               used to send a PATCH request to the URL.
post(url, data, json, args)     :               used to POST data to the server specified by the URL.
put(url, data, args)            :               used to replace all the uploaded contents represented by the current target source of the specified URL.
request(method, url, args)      :               used to REQUEST a specified method of the URL.
"""

import requests as req

# Request from server
r = req.get('https://www.geeksforgeeks.org',)

# get the response code
print(r)

#print some of the lines of the request data
print(r.text[0:1000])