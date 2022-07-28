#!/usr/bin/python

import pg

conn = pg.DB(host="localhost", user="postgres", passwd="postgres", dbname="lincs2lincs")

#print('We made it this far')

result = conn.query("SELECT * FROM lsm_ids WHERE lsm_id = 'LSM-17536' and similarity > 0.9615 ")


#first fetch record, then fetch individual variables (columns)

#for lsm_id, lsm_similar_id, similarity in result:
#    print lsm_id, lsm_similar_id, similarity

print result

conn.close()
