import json

with open("podatki.json",'r') as f:
    data=json.load(f)

    max_pay=0
    max_pay_name=''

    for employee in data['company']['employees']:
        #print(employee)
        #print(type(employee))
        placa=employee['payble']['salary']
        bonus=employee['payble']['bonus']
        placilo_skupaj=placa+bonus

        if placilo_skupaj>max_pay:
            max_pay=placilo_skupaj
            max_pay_name=employee['name']     
            
    print(f'Največ plačo ima {max_pay_name} in znaša {max_pay} EUR')
