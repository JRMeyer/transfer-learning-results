import sys

fname=sys.argv[1]

langs={}

with open(fname) as f:
    lines = f.readlines()
    for line in lines:
        cols=line.split()
        print(cols)
        if cols[0] in langs:
            langs[cols[0]][cols[1]] = cols[2]
        elif not cols[0] in langs:
            langs[cols[0]] = {cols[1]:cols[2]}


print("lang", 'dev','test','train')
for lang in langs.keys():
    print(lang, langs[lang]['dev'],langs[lang]['test'],langs[lang]['train'] )

    
# print("lang", 'baseline','froze-1','froze-2','froze-3','froze-4','froze-5','tune-1','tune-2','tune-3','tune-4','tune-5' )
# for lang in langs.keys():
#     print(lang, langs[lang]['baseline'],langs[lang]['froze-1'],langs[lang]['froze-2'],langs[lang]['froze-3'],langs[lang]['froze-4'],langs[lang]['froze-5'],langs[lang]['tune-1'],langs[lang]['tune-2'],langs[lang]['tune-3'],langs[lang]['tune-4'],langs[lang]['tune-5'] )
