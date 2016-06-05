import sys
import re
import json
from collections import Counter

words = re.findall('\w+', sys.stdin.read().lower())
counter = Counter(words)
print json.dumps([{key: value} for key, value in counter.most_common()])
