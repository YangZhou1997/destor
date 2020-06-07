# !/bin/bash

./rebuild ~/working/
 
# for file in vmware-distrib-0 vmware-distrib-1 vmware-distrib-2 vmware-distrib-3 vmware-distrib-4 vmware-distrib-5; do
#     ./destor -c"/home/administrator/destor/destor.config" /home/administrator/datasets/vmware-build/$file
# done

# for file in db0 db1 db2 db3 db4; do
#     ./destor -c"/home/administrator/destor/destor.config" /home/administrator/datasets/db-files/$file
# done

for file in enwiki-20200220-abstract.xml enwiki-20200301-abstract.xml enwiki-20200401-abstract.xml enwiki-20200420-abstract.xml enwiki-20200501-abstract.xml enwiki-20200520-abstract.xml enwiki-20200601-abstract.xml enwiki-latest-abstract.xml; do
    ./destor -c"/home/administrator/destor/destor.config" /home/administrator/datasets/wiki/$file
done