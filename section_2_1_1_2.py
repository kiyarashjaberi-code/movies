import json

with open('vocabulary.json') as json_file: 
    data = json.load(json_file)
def create_index(data):
    index={}
    for item in data:
        item_list=[]
        for i in range(30000):
            try:
                with open('word\\{0}.tsv'.format(i), 'r', encoding='utf-8', newline ='') as f:
                    text=f.read()
                text=text.split()
                if item in text:
                    item_list.append(i)
            except:
                 continue
        index[data[item]]=item_list
    return index
index =create_index(data)
with open('inverted_index.json', 'w') as f:
        data = json.dumps(index)
        f.write(data)