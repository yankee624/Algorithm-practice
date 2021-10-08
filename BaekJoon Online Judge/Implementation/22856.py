N = int(input())
tree = {}
total_edges = 0
for _ in range(N):
    val, left_val, right_val = map(int, input().split())
    tree[val] = [left_val, right_val]
    total_edges += (left_val != -1) + (right_val != -1)

rightmost_path_edges = -1
curr_node = 1
while curr_node != -1:
    curr_node = tree[curr_node][1]
    rightmost_path_edges += 1

if total_edges == 0:
    print(0)
else:
    print(total_edges * 2 - rightmost_path_edges)


