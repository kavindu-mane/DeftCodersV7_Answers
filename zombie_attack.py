def dfs(visited , graphs , root):
    if root not in visited:
        visited.add(root)
        for k in graphs[root]:
            dfs(visited, graphs , k)

visited = set()
graphs = {}
towns = int(input())
roads = int(input())
combinations = []
max_len = 0
for k in range(1 , towns +1):
    graphs[k] = []
for _ in range(roads):
    line = list(map(int , input().split()))
    if(line[1] not in graphs[line[0]] and line[1] != line[0]):
        graphs[line[0]].append(line[1])
    if(line[0] not in graphs[line[1]] and line[1] != line[0]):
        graphs[line[1]].append(line[0])
            
for k in graphs.keys():
    visited.clear()
    dfs(visited , graphs , k)
    if(list(visited) not in combinations):
        combinations.append(list(visited))
for lst in combinations:
    if(len(lst) > max_len):
        max_len = len(lst)
print(max_len)
