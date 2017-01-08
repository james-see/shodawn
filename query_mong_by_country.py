# What: This script gets the total counts for M O N G O D B port open per country code
# Author: James Campbell
# Date: 7 JAN 2017
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
try: from pymongo import MongoClient
except: exit('must pip3 install pymongo')
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

searchstring = 'port:27017 country:{}'.format(countrycodedefault)

try:
    results = api.search(searchstring)
    print ('Results found: %s' % results['total'])
except shodan.APIError as e:
        print ('Error: %s' % e)
# if we got results, let's investigate them further...
if int(results['total']) > 0:
    defaultanswer = 'y'
    customanswer = input("Do you want to check all results for open access (not working yet for mongo)? [Y/n]: ")
    # sensible default is yes
    if customanswer:
        if customanswer == 'Y':
            customanswer = 'y'
        defaultanswer = customanswer
    if defaultanswer == 'y':
        i = 0
        # for each item we only need the ip address, but let's also print other info as well
        for item in results['matches']:
            #client = MongoClient(item['ip_str'], 27017)
            client = MongoClient(item['ip_str'], 27017)
            try: databases = client.database_names()
            except: continue
            print("databases {} ".format(databases))
            # exit('working so far') # testing
            if not len(databases) > 0:
                continue
            else:
                print('ip address: {}, org: {}, hostname(s): {}'.format(item['ip_str'], item['org'], item['hostnames']))
                i = i + 1
    else:
        exit('thanks for playing version 0.11')
print("MONGODB report for country {}: ".format(countrycodedefault))
print("=============="*2)
print("total found in shodan: {}".format(results['total']))
print("total open to the world (no authentication at all): {}".format(i))
exit('successfully executed version 0.15')
