# !/bin/bash
# mkdir -p ~/dataset/
# mkdir -p ~/dataset/fslhomes/
# mkdir -p ~/dataset/macos/

# cd ~/dataset/fslhomes/ && wget --random-wait -r -np -e robots=off -U -R "index.html*" -c http://tracer.filesystems.org/traces/fslhomes/2012/
# cd ~/dataset/macos/ && wget --random-wait -r -np -e robots=off -U -R "index.html*" -c http://tracer.filesystems.org/traces/macos/2012/

wiki_link=(https://dumps.wikimedia.org/enwiki/20200220/enwiki-20200220-abstract.xml.gz https://dumps.wikimedia.org/enwiki/20200301/enwiki-20200301-abstract.xml.gz https://dumps.wikimedia.org/enwiki/20200401/enwiki-20200401-abstract.xml.gz https://dumps.wikimedia.org/enwiki/20200420/enwiki-20200420-abstract.xml.gz https://dumps.wikimedia.org/enwiki/20200501/enwiki-20200501-abstract.xml.gz https://dumps.wikimedia.org/enwiki/20200520/enwiki-20200520-abstract.xml.gz https://dumps.wikimedia.org/enwiki/20200601/enwiki-20200601-abstract.xml.gz https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-abstract.xml.gz)

for link in https://dumps.wikimedia.org/enwiki/20200301/enwiki-20200301-abstract.xml.gz https://dumps.wikimedia.org/enwiki/20200401/enwiki-20200401-abstract.xml.gz https://dumps.wikimedia.org/enwiki/20200420/enwiki-20200420-abstract.xml.gz https://dumps.wikimedia.org/enwiki/20200501/enwiki-20200501-abstract.xml.gz https://dumps.wikimedia.org/enwiki/20200520/enwiki-20200520-abstract.xml.gz https://dumps.wikimedia.org/enwiki/20200601/enwiki-20200601-abstract.xml.gz https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-abstract.xml.gz; do
    cd ~/datasets/wiki && wget $link
done