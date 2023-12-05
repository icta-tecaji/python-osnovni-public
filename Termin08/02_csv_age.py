data=[]

with open('Titanic.csv','r') as f:
    for line in f.readlines():
        line=line.strip()
        line_split=line.split(',')
        data.append(line_split)

age_dist={'0to20':{'survived':0,'died':0},
          '20to40':{'survived':0,'died':0},
          '40to60':{'survived':0,'died':0},
          '60to80':{'survived':0,'died':0},
          '80to100':{'survived':0,'died':0}}

# for line in data:
#     try:
#         age=int(line[6])
#     except ValueError:
#         continue

#     if age<=20:
#         if line[1]=='1':
#             age_dist['0to20']['survived']+=1
#         else:
#             age_dist['0to20']['died']+=1
#     elif age<=40:
#         if line[1]=='1':
#             age_dist['20to40']['survived']+=1
#         else:
#             age_dist['20to40']['died']+=1
#     elif age<=60:
#         if line[1]=='1':
#             age_dist['40to60']['survived']+=1
#         else:
#             age_dist['40to60']['died']+=1
#     elif age<=80:
#         if line[1]=='1':
#             age_dist['60to80']['survived']+=1
#         else:
#             age_dist['60to80']['died']+=1
#     else:
#         if line[1]=='1':
#             age_dist['80to100']['survived']+=1
#         else:
#             age_dist['80to100']['died']+=1

# print(age_dist)    
  

for line in data:
    try:
        age=int(line[6])
    except ValueError:
        continue

    if age<=20:
        key='0to20'
    elif age<=40:
        key='20to40'
    elif age<=60:
        key='40to60'
    elif age<=80:
        key='60to80'
    elif age<=100:
        key='80to100'

    if line[1]=='1':
        age_dist[key]['survived']+=1
    else:
        age_dist[key]['died']+=1

print(age_dist)    
