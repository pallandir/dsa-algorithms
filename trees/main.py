from collections import deque


class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value

    def display_graph(self, root):
        if not root:
            return

        queue = deque([root])
        first_level = True
        while queue:
            branches = []
            level_size = len(queue)
            level = [queue[i] for i in range(level_size)]
            print(
                ("\t  " if first_level else "\t")
                + "   ".join(str(node.value) for node in level)
            )
            first_level = False
            for node in level:
                node = queue.popleft()
                if node.left:
                    branches.append("/" if node.left else " ")
                    queue.append(node.left)
                if node.right:
                    branches.append("\\" if node.right else " ")
                    queue.append(node.right)

            if any(b != " " for b in branches):
                print("\t" + "   ".join(branches))


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(4)
    root.left.left = Node(7)
    root.right.right = Node(5)
    root.display_graph(root)
