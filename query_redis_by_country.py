# What: This script gets the total counts for REDIS port open per country code
# Author: James Campbell
# Date: 3 JAN 2017
# Updated: 7 JAN 2017
print("       .__               .___                    ")
print("  _____|  |__   ____   __| _/____ __  _  ______  ")
print(" /  ___/  |  \ /  _ \ / __ |\__  \\\ \/ \/ /    \ ")
print(" \___ \|   Y  (  <_> ) /_/ | / __ \\\     /   |  \\")
print("/____  >___|  /\____/\____ |(____  /\/\_/|___|  /")
print("     \/     \/            \/     \/           \/ ")
print("\n")
print("+++++"*15)
print("disclaimer: this is a pentesting tool to check your own servers for database")
print("vulnerabilities and only checks if ports are wide open, it does not try to")
print("login with fake credentials, brute force, or any other traditional 'hack'")
print("method to gain access.")
print("+++++"*15)
print("\n")
# imports
try: import redis
except: exit('must pip install redis')
try: import shodan
except: exit('please run pip or pip3 install shodan then try running this again')
try: from configs import *  # get api key from gitignore file configs.py
except: exit('please add a configs.py file with apikey var in same directory')

# global class init
api = shodan.Shodan(apikey)

# sensible default country is Canada (blame canada)
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

# if we got results, let's investigate them further...
if int(results['total']) > 0:
    defaultanswer = 'y'
    customanswer = input("Do you want to check all results for open access? [Y/n]: ")
    # sensible default is yes
    if customanswer:
        if customanswer == 'Y':
            customanswer = 'y'
        defaultanswer = customanswer
    if defaultanswer == 'y':
        i = 0
        # for each item we only need the ip address, but let's also print other info as well
        for item in results['matches']:
            openredis = redis.Redis(host=item['ip_str'], port=6379, socket_timeout=30)
            try: ponger = openredis.ping()
            except: continue
            if not ponger:
                continue
            else:
                print('ip address: {}, org: {}, hostname(s): {}'.format(item['ip_str'], item['org'], item['hostnames']))
                i = i + 1
    else:
        exit('thanks for playing version 0.11')
print("total open to the world: {}".format(i))
exit('successfully executed version 0.11')
