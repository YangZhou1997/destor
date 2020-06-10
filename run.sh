# !/bin/bash

./rebuild ~/working/
 
# for file in 0 1 2 3 4 5; do
#     ./destor -c"/home/administrator/destor/destor.config" /home/administrator/datasets/vmware-build/vmware-distrib-$file
# done

# for file in db0 db1 db2 db3 db4; do
#     ./destor -c"/home/administrator/destor/destor.config" /home/administrator/datasets/db-files/$file
# done

for file in 20200220 20200301 20200401 20200420 20200501 20200520 20200601 latest; do
    ./destor -c"/home/administrator/destor/destor.config" /home/administrator/datasets/wiki/enwiki-$file-abstract.xml
done