print '''
    3. write a program to list all the repos from given url which is not forked i.e. "fork" = False.
    https://api.github.com/users/mralexgray/repos
'''
import json

print "Option 1 : Read JSON contents from current file \n"

jsondata = [{'1':'one', '2':'two', '3':'three'}]
print 'The JSON Data is : ' + str(jsondata)

json_encoded = json.dumps(jsondata)
#print json_encoded

json_decoded = json.loads(json_encoded)
#print json_decoded

print "\nOption 2 : Read JSON File contents from local System \n"

with open("/home/inpro/ipinfra/learndjango/repos.josn") as json_file:
    json_data = json.load(json_file)
    print(json_data)

print "\nOption 3 : Get JSON Response contents from URL \n"

import urllib2
jsonurl = 'https://api.github.com/users/mralexgray/repos'
returnjsonData = urllib2.urlopen(jsonurl)
jsonContent = json.loads(returnjsonData.read())
#print jsonContent

for jnode in jsonContent:
	if(jnode['fork'] == False):
	    print('HTML URL = ' + jnode['html_url'] + ', API URL = ' + jnode['url'] + str('\n'))







