
n = 4
visited = [False for x in range(n)]
graph = [[0, 1, 0, 0],
         [1, 0, 1, 1],
         [0, 1, 0, 0],
         [0, 1, 0, 0]]
adj_list = [[1],
            [0, 2, 3],
            [1],
            [1]]

# def dfs_matrix(current_node):
#     visited[current_node] = True
#     for other_node in range(n):
#         if graph[current_node][other_node] == 1:
#             if visited[other_node] is False:
#                 dfs_matrix(other_node)


def dfs_list(current_node):
    visited[current_node] = True
    length = len(adj_list[current_node])

    for idx in range(length):
        next_node = adj_list[current_node][idx]
        print(visited)
        print(next_node)
        if visited[next_node] is False:
            dfs_list(next_node)



if __name__ == '__main__':
    print('hello')
    # dfs_matrix(0)
    dfs_list(0)
    # reset visited array to all false.





