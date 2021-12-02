# import json

# Method	Description
# dumps()	encoding to JSON objects
# dump()	encoded string writing on file
# loads()	Decode the JSON string
# load()	Decode while JSON file read


# ---------------looking item------------------
# with open('sample.json') as file:
#     data = json.load(file)
#
# print(data['firstName'],data['lastName'],data['address'])

# ---------------looking items------------------
# with open('people.json') as file:
#     data = json.load(file)
#
# for item in data['people']:
#     print(item['firstName'],item['age'])

# ---------------delete and create file---------
# with open('people.json') as file:
#     data = json.load(file)
#
# for item in data['people']:
#     del item['number']
#
# with open('people_new.json', 'w') as file:
#     json.dump(data,file,indent=2)

#--------------example request from inet---------
# from urllib.request import urlopen
# with urlopen("https://data.fixer.io/api/latest") as response:
#      source = response.read()
#
# data = json.loads(source)
#
# print(json.dumps(data, indent=2))


