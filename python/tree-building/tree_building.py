class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id

    def __eq__(self, other):
        return self.record_id == other.record_id and self.parent_id == other.parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []

    def add_node(self, record):
        node = next((n for n in self.children if n.node_id == record.parent_id), self)
        node.children.append(Node(record.record_id))


def BuildTree(records):
    records.sort(key=lambda x: x.record_id)
    tree_root = None

    if records and records[0] != Record(0, 0):
        raise ValueError("No root record was found")

    if records and list(set(r.record_id for r in records))[-1] != len(records) - 1:
        raise ValueError("The tree must be sequential")

    if records and any(record.parent_id >= record.record_id for record in records[1:]):
        raise ValueError("The record id cannot be equal or bigger than the parent id")

    for record in records:
        if not tree_root:
            tree_root = Node(0)

        else:
            tree_root.add_node(record)

    return tree_root
