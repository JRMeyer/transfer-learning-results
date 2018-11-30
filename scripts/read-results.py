import sys
import json
from pprint import pprint

scratch=sys.argv[1]
one=sys.argv[2]
two=sys.argv[3]
three=sys.argv[4]
four=sys.argv[5]
five=sys.argv[6]


master={}
for results, num in [(scratch, 'scratch'), (one, 'one'), (two, 'two'), (three, 'three'), (four, 'four'), (five, 'five')]:
    with open(results) as f:
        data = json.load(f)
        for i in data:
            if i['src'] in master:
                master[i['src']].update({num: i['res']})
            else:
                master[i['src']] = {num : i['res']}



print(master)
