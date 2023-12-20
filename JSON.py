import json
def convert_to_json_string(n, key_value_pairs):
    data = {}
    for pair in key_value_pairs:
        key, value = pair.split()
        data[key] = value
    json_string = json.dumps(data, sort_keys=True)
    return json_string

#input
n = int(input())
key_value_pairs = [input() for _ in range(n)]

#output
result = convert_to_json_string(n, key_value_pairs)
print(result)