CTFC - "Capital in the Twenty-First Century"
===

## Required systems
- Python 2.7.10
- pip 8.1.2

```
pip install --requirement required_packages.txt
```


## Word count in the book
- Execute `wc.py` command like below
    - It only takes around 0.3 second on my MacBook
    - [jq](https://stedolan.github.io/jq/) is a optional command to make json prettier

```
$ time cat var/plain.txt | src/wc.py | jq . > var/wc.json
cat var/plain.txt  0.00s user 0.00s system 2% cpu 0.143 total
python wc.py  0.26s user 0.08s system 95% cpu 0.356 total
jq . > var/wc.json  0.03s user 0.00s system 8% cpu 0.374 total
```


## For replication
1. Extract plain text data from the book like below
    - There's 258837 words in the text I used as you can see below
    - I put the data at `var/plain.txt` for reviewing

```
$ time bash pdf2txt.py -t text  ${__PATH_TO_BOOK__}.pdf | tee var/plain.txt | wc --words
258837
bash pdf2txt.py -t text ~/Downloads/9780674430006.pdf  160.69s user 0.34s system 99% cpu 2:41.16 total
tee var/plain.txt  0.00s user 0.01s system 0% cpu 2:41.16 total
wc --words  0.52s user 0.00s system 0% cpu 2:41.16 total
```
