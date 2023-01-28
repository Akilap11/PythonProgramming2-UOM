first_dict=dict()
secondy_way={}

scores={'saman':75,'nimal':50}
print(scores['saman'])
print(scores.get('nimal'))

#add
scores['sunil']=60
print(scores)

#update
scores['saman']=10
print(scores)

#get list of all keys and values
all_keys=list(scores.keys())
print(all_keys)

all_values=list(scores.values())
print(all_values)

for key in scores:
    print(key,scores[key])

#remove
scores.pop('nimal')
print(scores)
#remove all
scores.clear()
print(scores)