# !/bin/bash

./rebuild ~/working/
 
for file in vmware-distrib-0 vmware-distrib-1 vmware-distrib-2 vmware-distrib-3 vmware-distrib-4 vmware-distrib-5; do
    ./destor -c"/home/administrator/destor/destor.config" /home/administrator/datasets/vmware-build/$file
done