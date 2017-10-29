import json
from collections import OrderedDict

obj = OrderedDict()
obj["name"] = "이동현"
obj["age"] = '9'
obj["address"] = "청주"

print(obj)
print(json.dumps(obj, ensure_ascii=False, indent="\t"))
