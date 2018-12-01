import numpy as np
import pandas as pd
import sys

def levenshtein(a,b):
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a,b = b,a
        n,m = m,n

    current = list(range(n+1))
    for i in range(1,m+1):
        previous, current = current, [i]+[0]*n
        for j in range(1,n+1):
            add, delete = previous[j]+1, current[j-1]+1
            change = previous[j-1]
            if a[j-1] != b[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)

    return current[n]


def wer(original, result):
    r"""
    The WER is defined as the editing/Levenshtein distance on word level
    divided by the amount of words in the original text.
    In case of the original having more words (N) than the result and both
    being totally different (all N words resulting in 1 edit operation each),
    the WER will always be 1 (N / N = 1).
    """
    # The WER ist calculated on word (and NOT on character) level.
    # Therefore we split the strings into words first:
    original = original.split()
    result = result.split()
    return levenshtein(original, result) / float(len(original))


org=sys.argv[1]
decoded=sys.argv[2]

org_df=pd.read_csv(org, header=None)
org_df.columns=['clip', 'org']
decoded_df=pd.read_csv(decoded, header=None)
decoded_df.columns=['clip', 'decoded']

print(org_df.head())
print(decoded_df.head())

result = pd.merge(org_df, decoded_df, on="clip")

result['wer'] = result[['org','decoded']].apply(lambda x: wer(*x), axis=1)

print(result.wer.mean())

