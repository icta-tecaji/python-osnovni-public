data=[]

with open('Titanic.csv','r') as f:
    for line in f.readlines():
        line=line.strip()
        line_split=line.split(',')
        data.append(line_split)

# for vrstica in data[:5]:
#     #print(vrstica)
#     pass

prezivetje={'male':{'survived':0,'died':0},'female':{'survived':0,'died':0}}
stetje_zivih=0
stetje_mrtivih=0

for vrstica in data:
    #print(vrstica[1])
    if vrstica[1]=='1':
        if vrstica[5]=='male':
            prezivetje['male']['survived']+=1
        elif vrstica[5]=='female':
            prezivetje['female']['survived']+=1
    else:
        if vrstica[5]=='male':
            prezivetje['male']['died']+=1
        else:
            prezivetje['female']['died']+=1

print(f'Število preživelih ženske je: {prezivetje["female"]["survived"]}, umrlih pa: {prezivetje["female"]["died"]}')
print(f'Število preživelih moških je: {prezivetje["male"]["survived"]}, umrlih pa: {prezivetje["male"]["died"]}')


