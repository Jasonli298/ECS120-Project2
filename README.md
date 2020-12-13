# ECS120 Project 2
I attempted to write a Python program that implements an algorithm that polyreduces *Clique* problem to the *Node Cover* problem. I'm using the techique given by Richard Karp in the textbook.

The converted program takes in 3 parameters: `graph`, `N `, `k`, which are the input graph represented in a single ASCII string, the number of nodes in the graph, and the number *K* in the *Clique* problem, which finds if there's a clique with size *K* inside the graph.

First I calculated the number `l = N - k`, which is latered used to solve the problem using *Node Cover*. Then I splitted the input graph as a string into a list of tuples that consists of 2 nodes, which represents an edge connecting the 2 nodes.
```python
node_list = []
for edge in edge_list:
    if edge[0] not in node_list:
        node_list.append(edge[0])
    if edge[1] not in node_list:
        node_list.append(edge[1])
```            
This block traverses the list of edges and appends all the nodes into a list called `node_list`, which is later used to generate the complement of the input graph. 
```python
complement graph = []
for i in range(0, N):  # This block generates the complement of the input graph
    for j in range(i + 1, N):
        if ((node_list[i], node_list[j]) not in edge_list) and ((node_list[j], node_list[i]) not in edge_list):
            complement_graph.append((node_list[i], node_list[j]))
```
Then this block first choose 2 nodes, then checks if there's already an edge connecting them in the original graph. If not, it then inserts a tuple into the `complement_graph` list.
After this is done, it inputs the generated `complement_graph` and `l` into `node_cover()` function, which is assumed to exist and solves the *Node Cover* problem in NP-Complete time.
Finally, this line returns `"yes"` if `node_cover()` return `"yes"`, and `"no"` if `node_cover()` returns `"no"`.
```python
return "yes" if node_cover(complement_graph, l) == "yes" else "no"
```
The function `convert_clique_to_node_cover()` polyreduces *Clique* to *Node Cover* because in order to generate the complement graph, it traverses the original graph in polynomial time, and maps positive instances of *Clique* to positive instances of *Node Cover*, and negative instances of *Clique* to negative instances of *Node Cover*.
