#!python

import json
import pandas as pd
import re

# Read the json file
with open('canada-tbs-links.json', encoding="utf-8") as f:
    data = json.load(f)
data = data['response']['docs']

# data is a list of dictionaries
data_df = pd.DataFrame(data)
pd.json_normalize(data[0])

#https://stackoverflow.com/a/60264302
def list2Str(lst):
    if type(lst) is list: # apply conversion to list columns
        return";".join(map(str, lst))
    else:
        return lst

sel_data = data_df.loc[:,['tstamp','host','url','description_str','title','content','keywords_str']]
sel_data = sel_data.apply(lambda x: [list2Str(i) for i in x])


def split_keywords(list_of_keywords):
    keywords = []
    try:
        if ',' in list_of_keywords or ';' in list_of_keywords or '\n' in list_of_keywords:
            keywords = re.split(r',|;|\n', list_of_keywords)
            # Assuming list:
            assert type(keywords) is list
            for i in keywords:
                if len(i) <= 2:
                    keywords.remove(i)
        elif type(list_of_keywords) is float:
            return None
        else:
            keywords = [list_of_keywords]
        #[print(len(i), "/", len(list_of_keywords)) for i in keywords]

        keywords = [i.strip().lower() for i in keywords]
        #print("\n", list_of_keywords, "######################", keywords)
        return keywords
    except:
        pass
sel_data['keywords_split'] = [split_keywords(x) for x in sel_data['keywords_str']]
sel_data.to_csv('sel_data.csv', index=False, sep='\t', columns=['tstamp','host','url','description_str','title','keywords_split'])

######### Create a list of all keywords

keywords_all = []
for i in sel_data['keywords_split']:
    if i is not None:
        keywords_all.extend(i)

for i in keywords_all:
    if len(i) <= 2:
        keywords_all.remove(i)
keywords_all = list(set(keywords_all))
for i in keywords_all:
    if len(i) <= 2:
        keywords_all.remove(i)
        
keywords_all.sort()
keywords_all.sort(key=len)
keywords_all
pd.DataFrame(keywords_all).to_csv('keywords_all.csv', index=False, header=False)
