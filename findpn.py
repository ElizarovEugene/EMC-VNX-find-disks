#!/usr/bin/python
'''
The script for determining the part numbers of the disks and their number by the SPCollect dump
To run the script you need to specify the path to the file SPA_cfg_info.txt which is in the archive * _SPA_datetime _ * _ sus.zip
'''

import re
import requests

def find_disk_info(part):
    for r in (('PWR', ''), ('EFD', '')):
        part = part.replace(*r)

    r = requests.get('http://www.harddrivesdirect.com/advanced_search_result_exact.php?keywords=' + part)
    text = r.text
    disk = re.search(r'<span class=roboto_blue12>(.*)<\/span>&nbsp;<span class=roboto_light_blue12>&nbsp;</span>', text)
    if disk:
        disk = disk.group(1).replace(part + ' ', '')
        return disk

filepath = '/Users/korp/Downloads/VNX5400.zip Folder/CKM00151600783_SPA_2018-06-05_13-53-31_3c9016_data.zip Folder/CKM00151600783_SPA_2018-06-05_13-53-31_3c9016_sus.zip Folder/SPA_cfg_info.txt'

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
print '-' * 20
for key, val in count.items():
    disk = find_disk_info(key)
    print str(key) + ' - ' + str(val)
    print disk
    print '-' * 20
