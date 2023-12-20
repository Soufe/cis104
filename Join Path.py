n = int(input())
path_components = []
for _ in range(n):
    component = input()
    path_components.append(component)

result = '/'.join(path_components)
print(result)