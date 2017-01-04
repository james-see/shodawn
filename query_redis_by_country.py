# What: This script gets the total counts for REDIS port open per country code
# Author: James Campbell
# Date: 3 JAN 2016

# imports
try: import shodan
except: exit('please run pip or pip3 install shodan then try running this again')
try: from configs import *  # get api key from gitignore file configs.py
except: exit('please add a configs.py file with apikey var in same directory')

# global class init
api = shodan.Shodan(apikey)

countrycodedefault = 'CA'
countrycodecustom = input('What country code? [default CA]: ')
if countrycodecustom:
	countrycodedefault = countrycodecustom

searchstring = 'port:6379 country:{}'.format(countrycodedefault)

try:
	results = api.search(searchstring)
	print ('Results found: %s' % results['total'])
except shodan.APIError as e:
        print ('Error: %s' % e)

exit('successfully executed version 0.01')