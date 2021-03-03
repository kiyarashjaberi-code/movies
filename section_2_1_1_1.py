import json
def get_words():
    counter=0
    vocabulary={}
    for i in range(30000):
        try:
            with open('word\\{0}.tsv'.format(i), 'r', encoding='utf-8', newline ='') as f:
                text=f.read()
            text=text.split()
            for item in text:
                if item not in vocabulary:
                    vocabulary[item]=counter
                    counter +=1
        except:
            continue
    return vocabulary

vocabulary =get_words()
with open('vocabulary.json', 'w') as f:
    data = json.dumps(vocabulary)
    f.write(data)