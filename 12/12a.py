from dataclasses import dataclass, field
from enum import Enum
from typing import List, Set
from pprint import pprint


with open('input.txt') as fl:
    all_lines = fl.read().splitlines()

class NodeType(Enum):
    START = 0
    END = 1
    SMALL = 2
    BIG = 3

def get_node_type(name: str):
    if name == 'start':
        return NodeType.START
    if name == 'end':
        return NodeType.END
    if name.islower():
        return NodeType.SMALL
    return NodeType.BIG

@dataclass
class Node:
    name: str
    cave: NodeType
    links: List['Node'] = field(default_factory=list)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

# name: str --> Node()
nodes = {}

# Create connections
for line in all_lines:
    a, b = line.split('-')

    if a not in nodes:
        nodes[a] = Node(a, get_node_type(a))
    if b not in nodes:
        nodes[b] = Node(b, get_node_type(b))

    an = nodes[a]
    bn = nodes[b]

    # Dual link
    if an not in bn.links:
        bn.links.append(an)
    if bn not in an.links:
        an.links.append(bn)

# Traverse. Latest elem is the current node
def traverse(nodes: List[Node]):

    cn = nodes[-1]

    if cn.cave == NodeType.END:
        return [nodes]

    if cn.cave == NodeType.START and len(nodes) > 1:
        return []

    if cn.cave == NodeType.SMALL and nodes.count(cn) > 1:
        return []

    # Traverse
    all_paths = []
    for nxt in cn.links:
        paths = traverse([*nodes, nxt])
        all_paths.extend(paths)

    return all_paths

pz = traverse([nodes['start']])
print('LENGTH:', len(pz))
    




