# What: This script ensures that you have shodan-cli / shodan python installed on your system and can connect to the API
# Author: James Campbell
# Date: 3 JAN 2016

# imports
try: import shodan
except: exit('please run pip or pip3 install shodan then try running this again')
try: from configs import *  # get api key from gitignore file configs.py
except: exit('please add a configs.py file with apikey var in same directory')

# global class init
api = shodan.Shodan(apikey)

# Wrap the request in a try/ except block to catch errors
try:
        # Search Shodan
        results = api.count('apache country:CA')

        # Show the results
        print ('Success. Results found for test count query, apache users in Canada: %s' % results['total'])
except shodan.APIError as e:
        print ('Error: %s' % e)
