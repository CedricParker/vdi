#!/usr/bin/env python
import csv
import sys



outfile=open('/run/media/c.parker/blue/vdi/group_vars/IPA/usernames.yml','w')
L = "---\nusernames:\n"
outfile.write(L)

groupoutfile=open('/run/media/c.parker/blue/vdi/group_vars/IPA/names.yml','w')
K = "---\nnames:\n"
groupoutfile.write(K)

with open(sys.argv[1]) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
	first_name = row['fname']
        last_name = row['lname']
        outfile.write("  - { user: \'" + first_name + "." + last_name + "\', fname: \'" + first_name + "\', lname: \'" + last_name + "\'}\n")
        groupoutfile.write("  - " + first_name + "." + last_name + "\n")

outfile.close()
groupoutfile.close()
