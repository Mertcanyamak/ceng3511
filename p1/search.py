import sys
#-------------------------OPEN GRAPH.TXT FILE---------------------------------------------	

file = open('graph.txt', 'r')
graph = {}
graphCost = {}
lists = []
try:
	for files in file.readlines():
		files = files.replace(" ","")
		files.splitlines(0)
		files = files.rstrip("\n")
		files = files.replace("{","")
		files = files.replace("}","")
		if files != 0:
			files = lists.append(graphCost)
finally:		
	file.close()

#-------------------------BFS ALGORITHM---------------------------------------------	

def bfs(graph, start, end):
	queue = [[start]]
	visited = set()
	while queue:
		path = queue.pop(0) 		# Gets the first path in the queue
		vertex = path[-1] 		# Gets the last node in the path
		if vertex == end:		# Checks if we got to the end
			return path
		elif vertex not in visited: 		# We check if the current node is already in the visited nodes set in order not to recheck it
						# enumerate all adjacent nodes, construct a new path and push it into the queue
			for current_neighbour in graph.get(vertex, []):
				new_path = list(path)
				new_path.append(current_neighbour[0])
				queue.append(new_path)
			visited.add(vertex) 			# Mark the vertex as visited
	return 0

#--------------------------DFS ALGORITHM---------------------------------------------	

def dfs(graph, start, goal):
	stack = [(start, [start])]
	visited = set()
	while stack:
		(vertex, path) = stack.pop()
		if vertex not in visited:
			if vertex == goal:
				return path
			visited.add(vertex)
			for neighbor in sorted(graph[vertex], reverse=True):
				stack.append((neighbor, path + [neighbor]))
	return 0
#-------------------------UCS ALGORITHM---------------------------------------------	

def ucs(G, v):
    visited = set()                  # set of visited nodes
    q = queue.PriorityQueue()        # we store vertices in the (priority) queue as tuples 
                                     # (f, n, path), with
                                     # f: the cumulative cost,
                                     # n: the current node,
                                     # path: the path that led to the expansion of the current node
    q.put((0, v, [v]))               # add the starting node, this has zero *cumulative* cost 
                                     # and it's path contains only itself.

    while not q.empty():             # while the queue is nonempty
        f, current_node, path = q.get()
        visited.add(current_node)    # mark node visited on expansion,
                                     # only now we know we are on the cheapest path to
                                     # the current node.

        if current_node.is_goal:     # if the current node is a goal
            return path              # return its path
        else:
            for edge in  current_node.out_edges:
                child = edge.to()
                if child not in visited:
                    q.put((current_node_priority + edge.weight, child, path + [child]))	

#--------------------------OPEN FILE---------------------------------------------	

start_state = input("Please enter the start state : ")
Goal_state = input("Please enter the goal state : ")

result_bfs = bfs(graph, start_state, Goal_state)
result_dfs = dfs(graph, start_state, Goal_state)

print("BFS : ", end="")
print(*result_bfs, sep=" - ")

print("DFS : ", end="")
print(*result_dfs, sep=" - ")

sys.exit(0)