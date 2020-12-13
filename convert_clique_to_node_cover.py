def convert_clique_to_node_cover(graph, N, k):  # N is the number of nodes in the input graph
    l = N - k
    edge_list = [(edge[0], edge[3]) for edge in
                 graph.split(";")]  # Creates a list of tuples of nodes instead of strings
    node_list = []
    for edge in edge_list:
        if edge[0] not in node_list:
            node_list.append(edge[0])
        if edge[1] not in node_list:
            node_list.append(edge[1])
    complement_graph = []
    for i in range(0, N):  # This block generates the complement of the input graph
        for j in range(i + 1, N):
            if ((node_list[i], node_list[j]) not in edge_list) and ((node_list[j], node_list[i]) not in edge_list):
                complement_graph.append((node_list[i], node_list[j]))
    return "yes" if node_cover(complement_graph, l) == "yes" else "no"


def node_cover(graph, l):  # Code to solve the Node Cover problem not implemented
    pass


if __name__ == '__main__':
    G = "u, w;v, w;v, z;z, y;w, x"
    convert_clique_to_node_cover(G, 6, 4)
