#!/usr/bin/python
'''
The script for determining the part numbers of the disks and their number by the SPCollect dump
Data of disks by their party numbers can be found in the document:
https://www.emc.com/collateral/TechnicalDocument/docu31714.pdf

To run the script you need to specify the path to the file SPA_cfg_info.txt which is in the archive * _SPA_datetime _ * _ sus.zip
'''

import re

filepath = 'SPA_cfg_info.txt'

parse = False
total = 0
count = {}

f = open(filepath)
for line in f:
    command = re.search('.*NavisecCli.exe -np getdisk -tla', line)
    if command:
        parse = True
    
    if parse:        
        part = re.search('Clariion TLA Part Number:(.*)\n', line)
        if part:
            pn = part.group(1).strip()
            total += 1
            if pn in count.keys():
                count[pn] += 1
            else:
                count[pn] = 1

print 'Total drives: ' + str(total)
for key, val in count.items():
    print str(key) + ' - ' + str(val)
 