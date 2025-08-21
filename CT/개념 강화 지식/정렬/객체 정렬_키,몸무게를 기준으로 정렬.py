n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

#index를 기준으로 정렬
indices = list(range(n))
indices.sort(key=lambda i : (height[i],-weight[i]))
for i in indices:
    print(name[i], height[i], weight[i])
