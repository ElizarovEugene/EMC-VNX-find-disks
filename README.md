The script for determining the part numbers of the disks and their number by the SPCollect dump
Data of disks by their party numbers can be found in the document:
https://www.emc.com/collateral/TechnicalDocument/docu31714.pdf

To run the script you need to specify the path to the file SPA_cfg_info.txt which is in the archive * _SPA_datetime _ * _ sus.zip

You will end up with
```
Total drives: 120
--------------------
005050957PWR - 1
EMC 600-GB 6GB 15K 3.5 SAS HD
--------------------
005050854PWR - 2
EMC 600-GB 6G 15K 3.5 SAS HDD
--------------------
005050927PWR - 3
EMC 600-GB 6G 15K 3.5 SAS HDD
--------------------
005050140PWR - 1
EMC 2-TB 6G 7.2K 3.5 SAS HDD
--------------------
005052060PWR - 1
None
--------------------
005049274 - 33
EMC 600-GB 6G 15K 3.5 SAS HDD
--------------------
005049277PWR - 68
EMC 2-TB 6GB 7.2K 3.5 SAS HD
--------------------
005049496PWR - 3
EMC 2-TB 6G 7.2K 3.5 SAS HDD
--------------------
005049675PWR - 6
EMC 600-GB 6G 15K 3.5 SAS HDD
--------------------
005049449PWR - 2
EMC 2-TB 6G 7.2K 3.5 SAS HDD
--------------------

```
