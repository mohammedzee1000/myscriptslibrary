import uuid
import json


class TreeNode:

    def __init__(self, identifier=uuid.uuid4(), nodevalue="root", children=None):

        self._identifier = identifier
        self._node_value = nodevalue
        self._children = []

    def __repr__(self):
        return self._node_value

    def add_child(self, node):

        assert isinstance(node, TreeNode)
        self._children.append(node)

    def del_child(self, node):

        assert isinstance(node, TreeNode)
        self._children.remove(node)

    def children(self):

        return self._children

    def node_value(self):

        return self._node_value

class Tree:

    def __init__(self, root_node):

        assert isinstance(root_node, TreeNode)
        self._root_node = root_node

    def Root_Node(self):

        return self._root_node

    def get_node_by_value(self, value):

        items = self.traverse_depth_first()

        for item in items:

            if item.node_value() == value:

                return item

        return None

    def get_json(self):

        jsondata = None



        return jsondata

    def traverse_depth_first(self, op=None):

        traverse_list = []
        nodes_to_visit = []

        nodes_to_visit.append(self._root_node)

        while len(nodes_to_visit) > 0:

            current_node = nodes_to_visit.pop(0)
            nodes_to_visit[:0] = current_node.children()
            traverse_list.append(current_node)

            if op is not None:
                op(current_node)

        return traverse_list

if __name__ == '__main__':

    t = Tree(TreeNode("1", "root"))
    t.Root_Node().add_child(TreeNode(nodevalue="c1"))
    t.get_node_by_value("c1").add_child(TreeNode(nodevalue="c1c11"))

    print t.traverse_depth_first()