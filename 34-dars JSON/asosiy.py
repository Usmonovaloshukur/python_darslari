import json
import requests

# data = {
#     "Model" : "Malibu",
#     "Rang" : "Qora",
#     "Yil" :2020,
#     "Narh" :40000
# }
#
# data_json = json.dumps(data, indent=4)
#
# print(type(data))
# print(type(data_json))
#
# datafromjson = json.loads(data_json)
#
# print(datafromjson)

# talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
# talaba = json.loads(talaba_json)
# print(f"{talaba['ism']} {talaba['familiya']} {talaba['tyil']}-yilda tug'ilgan")
# print(type(talaba_json))

# talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
# data = {
#     "Model" : "Malibu",
#     "Rang" : "Qora",
#     "Yil" :2020,
#     "Narh" :40000
# }
#
# with open("talaba.json", "w") as f:
#     json.dump(talaba_json, f)
#
# with open("talaba.json") as fayl:
#     talaba = json.load(fayl)
#
# talaba_dict = json.loads(talaba)
# print(type(talaba_dict))
#
# with open("data.json", "w") as fayl:
#     json.dump(data, fayl)
#
# with open('data.json') as fayl:
#     data_dict = json.load(fayl)
# print(data_dict)


# with open("students.json") as fayl:
#     talabalar = json.load(fayl)
#
# for talaba in talabalar['student']:
#     print(f"{talaba['name']} {talaba['lastname']}, {talaba['year']}-kurs, {talaba['faculty']} fakulteti talabasi")

link = "https://uz.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=Python"

response = requests.get(link)
info = response.json()

with open("api-result.json") as fayl:
    data = json.load(fayl)

print(info['query']['pages']['13801']['title'])
print(info['query']['pages']['13801']['extract'])