import json

data = {
    "Name": "gopinath",
    "Email": "gopinath@gmail.com",
    "P_num": "95977004568"
}
with open('C:\\Users\\gopir\\Desktop\\j.json', 'w') as js:
    json.dump(data, js)