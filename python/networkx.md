# networkx

## Resources and References

Main:

- [Offical docs](https://networkx.github.io/documentation/stable/)
- [GitHub](https://github.com/networkx/networkx)
- [Python Patterns - Implementing Graphs](https://www.python.org/doc/essays/graphs/)
- Reinhard Diestel: [Graph Theory](http://diestel-graph-theory.com/index.html)

Technical:

- Albert/Barabasi: [Statistical Mechanics of Complex Networks](https://arxiv.org/pdf/cond-mat/0106096.pdf)
- Newman: [The Structure and Function of Complex Networks](https://epubs.siam.org/doi/pdf/10.1137/S003614450342480)

Other:

- [Home page](https://networkx.github.io/)
- [PyPI](https://pypi.org/project/networkx/2.2/)

## Install

```bash
$ conda install networkx[all]
```

## Create a Graph

Graphs are networks consisting of nodes (vertexes) connected by edges.

The most elementary graph object in `networkx` is [`Graph`](https://github.com/networkx/networkx/blob/dd990b60d89b6acc4e49107c1c4c48acc824f211/networkx/classes/graph.py#L289):

```python
>>> import networkx as nx
>>> G = nx.Graph()  # Simple, undirected graph
```

By definition, a Graph is a collection of **nodes** (vertices) along with identified pairs of nodes (called **edges**, links, etc). In NetworkX, **nodes can be any hashable object except `None`** e.g., a text string, an image, an XML object, another Graph, a customized node object, etc.

```python
>>> G.add_node(1)  # Add a single node, optional attributes
>>> G.add_nodes_from([2, 3])  # Add multiple nodes from an iterable
```

At this point, `G` has 3 nodes and no connecting edges.

```python
>>> G.nodes
NodeView((1, 2, 3))
>>> G.number_of_nodes()
3

>>> G.edges()
EdgeView([])
>>> G.number_of_edges()
0

>>> G.is_multigraph()
False
>>> G.is_directed()
False
```

You can initialize from a list of edges.  This will infer the resulting nodes:

```python
>>> I = nx.Graph([(0, 1), (1, 2), (2, 3)])
>>> I.nodes
NodeView((0, 1, 2, 3))
>>> I.edges
EdgeView([(0, 1), (1, 2), (2, 3)])
```

Pass any iterable of hashable items to `.add_nodes_from()`:

```python
>>> G.add_nodes_from(range(100, 110))  # Any iterable
>>> G.nodes
NodeView((1, 2, 3, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109))

>>> G.nodes()
NodeView((1, 2, 3, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, UUID('4dafddd6-b7a1-4e7e-bbec-53adc4781978'), UUID('77797741-34c9-4dea-84f2-e3d43944b4b0')))
```

You can add nodes from one graph to another.  The resulting nodes is their set union:

```python
>>> I.add_nodes_from(G)
>>> I.nodes
NodeView((0, 1, 2, 3, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, UUID('4dafddd6-b7a1-4e7e-bbec-53adc4781978'), UUID('77797741-34c9-4dea-84f2-e3d43944b4b0')))
```

The signature for `.add_edge()` is `add_edge(u_of_edge, v_of_edge, **attr)`.  The nodes `u` and `v` will be automatically added if they are not already in the graph.

```python
>>> I.edges
EdgeView([(0, 1), (1, 2), (2, 3)])
>>> I.add_edge(107, 109)
>>> I.edges
EdgeView([(0, 1), (1, 2), (2, 3), (107, 109)])
>>> I.add_edges_from([(107, 101), (3, uuid.UUID('4dafddd6-b7a1-4e7e-bbec-53adc4781978'))])
>>> I.edges
EdgeView([(0, 1), (1, 2), (2, 3), (3, UUID('4dafddd6-b7a1-4e7e-bbec-53adc4781978')), (101, 107), (107, 109)])
```

To clear all nodes and edges:

```python
>>> I
<networkx.classes.graph.Graph object at 0x1a22244518>
>>> I.nodes
NodeView(())
>>> I.edges
EdgeView([])
```

Two other meaningful attributes of a graph are `.adj` and `.degree`:

- `.degree`: degree of nodes
- `.adj`: adjacencies (neighbors)

Here's an example on a freshly-made graph:

```python
K = nx.Graph()
K.add_edges_from([
    ('a', 'b'),
    ('a', 'c'),
    ('b', 'c'),
    ('d', 'c')
])
```

The graph `K` has 4 nodes and 4 edges:

```python
>>> K.nodes
NodeView(('a', 'b', 'c', 'd'))
```

3 edges stem from the node `c`; 2 stem from `a` and 2 from `b`.  This is the definition of degree, a measure of centrality:

> The degree is by default the number of edges incident to the node.

```python
>>> K.degree
DegreeView({'a': 2, 'b': 2, 'c': 3, 'd': 1})
>>> K.degree['a']
2
```

Thus far, `.edges`, `.nodes`, and `.degree` have all acted like attributes/properties.  That's because they are properties that return class instances.  However, these classes have a `.__call__()` method that mainly serves for getting results on a subset of all nodes by passing an **nbunch**:

```python
>>> #  __call__(self, nbunch=None, data=False, default=None)
>>> K.edges(['a', 'd'])  # Filter to edges containing a or d
EdgeDataView([('a', 'b'), ('a', 'c'), ('d', 'c')])
>>> K.edges('b')  # Filter to edges containing b
EdgeDataView([('b', 'a'), ('b', 'c')])
>>> K.degree({'a', 'c'})
DegreeView({'a': 2, 'c': 3})
```

Lastly there is `.adj`:  (TODO)

```python
>>> K.adj
AdjacencyView({'a': {'b': {}, 'c': {}}, 'b': {'a': {}, 'c': {}}, 'c': {'a': {}, 'b': {}, 'd': {}}, 'd': {'c': {}}})`
>>>
>>> K.edges
EdgeView([('a', 'b'), ('a', 'c'), ('b', 'c'), ('c', 'd')])
>>> for k, v in K.adj.items():
...      print(k, v, sep='\t')
...
a   {'b': {}, 'c': {}}
b   {'a': {}, 'c': {}}
c   {'a': {}, 'b': {}, 'd': {}}
d   {'c': {}}
```

You can remove nodes and edges from the graph in a similar fashion to adding. Use methods:

- `.remove_node()`
- `.remove_nodes_from()`
- `.remove_edge()`
- `.remove_edges_from()`

## Edge Associations

From the docs:

> [A]n edge can be associated with any object `x` using `G.add_edge(n1, n2, object=x)`.
>
> As an example, `n1` and `n2` could be protein objects from the RCSB Protein Data Bank, and `x` could refer to an XML record of publications detailing experimental observations of their interaction.

## Graph, Node, and Edge Attributes

The constructor for `nx.Graph` is `__init__(self, incoming_graph_data=None, **attr)`.  Any keyword arguments captured by `**attr` become the graph's attributes as key-value pairs, captured in the `.graph` attribute:

```python
>>> F = nx.Graph(day="Friday", month="January")
>>> F.graph
{'day': 'Friday', 'month': 'January'}

>>> F.graph['day'] = 'Tuesday'
>>> F.graph
{'day': 'Tuesday', 'month': 'January'}
```

You can modify node attributes directly:

```python
>>> K.nodes
NodeView(('a', 'b', 'c', 'd'))
>>> K.nodes['a']
{}
>>> K.nodes['a']['name'] = 'letter a'
>>> K.nodes['a']
{'name': 'letter a'}
```

## Other Graphs

In directed graphs (digraphs), the connections between nodes have a direction, and are called arcs.

In undirected graphs, the connections have no direction and are called edges.  A directed graph has both an in-degree and an out-degree for each vertex, which are the numbers of incoming and outgoing edges respectively.

Each vertex in a directed graph has both an in-degree j and an out-degree k, and the degree distribution therefore becomes, in general, a double distribution over both degrees.

Each vertex A also belongs to an in-component and an out-component, which are, respectively, the set of vertices from which A can be reached and the set that can be reached from A, by following directed edges only in their forward direction. There is also the strongly connected component, which is the set of vertices which can both reach and be reached from A.

- `DiGraph`: directed graphs
- `MultiGraph`: allow multiple edges between any pair of nodes
- `MultiDiGraph` ([source](https://github.com/networkx/networkx/blob/master/networkx/classes/multidigraph.py)): combination of the above two
- `OrderedGraph`: TODO

Note:

> "Some algorithms work only for directed graphs and others are not well defined for directed graphs. ... The `MultiGraph` and `MultiDiGraph` classes allow you to add the same edge twice, possibly with different edge data. This can be powerful for some applications, but many algorithms are not well defined on such graphs.

Example of a digraph:

```python
>>> D = nx.DiGraph(['ab', 'ac', 'bc', 'bd', 'cd', 'dc', 'ef', 'fc'])  # len-2 str is iterable
>>> D.nodes
NodeView(('a', 'b', 'c', 'd', 'e', 'f'))
```

This graph has six nodes (A-F) and eight arcs.

```python
>>> for k, v in D.adj.items():
...     print(k, v, sep='\t')
...
a   {'b': {}, 'c': {}}
b   {'c': {}, 'd': {}}
c   {'d': {}}
d   {'c': {}}
e   {'f': {}}
f   {'c': {}}
```

In this way, `.adj` is a dictionary whose keys are the nodes.  For each key, the corresponding value is a list containing the nodes that are connected by a direct arc from this node.

## Graph Algorithms

Algorithms in graphs include finding a path between two nodes, finding the shortest path between two nodes, determining cycles in the graph (a cycle is a non-empty path from a node to itself), finding a path that reaches all nodes (the famous "traveling salesman problem"), and so on.  Sometimes the nodes or arcs of a graph have weights or costs associated with them, and we are interested in finding the cheapest path.  There's considerable literature on graph algorithms, which are an important part of discrete mathematics.

Some examples in Python can be found [here](https://www.python.org/doc/essays/graphs/).

## Random Graph


## Other Vocab

Small-world effect: the fact that most pairs of vertices in most networks seem to be connected by a short path through the network.

Geodesic distance:

It is widely assumed [362, 408] that most social
networks show “community structure,” i.e., groups of vertices that have a high density
of edges within them, with a lower density of edges between groups.
