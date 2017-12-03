import json
from collections import OrderedDict

obj = OrderedDict()
obj["name"] = "이동현"
obj["age"] = '9'
obj["address"] = "청주"

print(json.dumps(obj, ensure_ascii=False, indent="\t"))

"""
응답 json
{
	"name": "이동현",
	"age": "9",
	"address": "청주"
}
"""

with open('test.json','r') as make:
    data = json.load(make)
    print(data)

"""
{
    "add":123,
    "test":"hello"
}
"""