#!/usr/bin/env python

# surbhi bhatnagar, july 9th 2018
# sig2lead webapp


#import pybel
import json
import urllib2
import requests
import string

# getting gene name
gene_name=raw_input("Enter Gene: ")
link="http://www.ilincs.org/api/SignatureMeta?filter=%7B%22where%22%3A%7B%22treatment%22%3A%22"+str(gene_name)+"%22%2C%20%22libraryid%22%3A%22LIB_6%22%7D%7D"

#Getting json response
data=json.load(urllib2.urlopen(link))
#response = requests.get(link)
#data = response.json()

# Variable for all signature ids
sigid =[]

for i in data:
    sigid.append(str(i['signatureid']))

# printing all signatures associated with gene
print sigid

# getting concordant signatures for each id
for id in sigid:
    con=[]
    dis=[]
    link="http://www.ilincs.org/api/SignatureMeta/findConcordantSignatures?sigID=%22"+str(id)+"%22&lib=%22LIB_5%22"
    data=json.load(urllib2.urlopen(link))
    for perturbagen in data:
        pid=str(perturbagen['perturbagenID'])
        sim=str(perturbagen['similarity'])

        #concordant
        if sim > 0.321:
            con.append(pid)
        #discordant
        elif sim < -0.235:
            dis.append(pid)

    print "\nsignature ---- > ",id, "concordant ----->", con, "discordant ------>", dis

#    sys.exit()
