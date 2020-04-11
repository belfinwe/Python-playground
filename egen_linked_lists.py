# From ReadlPython: https://realpython.com/linked-lists-python/

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    """Custom linked list class, from RealPython."""
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        """
        The method above goes through the list and yields every single node.
        """
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty!")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next  # Den nye noden "får" referansen til den neste noden
                node.next = new_node  # Målnoden refererer til den nye noden
                return

        raise Exception(f"Node with data '{target_node_data}' not found")

    def add_before(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty!")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception(f"Node with data {target_node_data} not found.")

    def egen_test(self):
        for node in self:
            print(node)

    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception("List is empty.")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next == node.next
                return
            previous_node = node

        raise Exception(f"Node with {target_node_data} not found.")


# Testing
if __name__ == "__main__":
    llist = LinkedList()

    first_node = Node("a")
    llist.head = first_node
    print(f"{llist}\n")

    andre_node = Node("b")
    tredje_node = Node("c")
    first_node.next = andre_node
    andre_node.next = tredje_node

    print(f"{llist}\n")

    llist.add_first(Node("æ"))
    print(f"Legger til et nytt element foran:\n{llist}\n")

    llist.add_last(Node("d"))
    print(f"Legger til et nytt element til slutt:\n{llist}\n")

    llist.add_after("æ", Node("ø"))
    print(f"Legger til eit nytt element etter 'æ':\n{llist}\n")

    llist.add_before("æ", Node("z"))
    print(f"Legger til eit nytt element før 'æ':\n{llist}\n")

    llist.add_before("a", Node("å"))
    print(f"Legger til eit nytt element før 'a':\n{llist}\n")

    llist.remove_node("z")
    print(f"Fjerner eit element, 'z':\n{llist}\n")

    print("Egen testing:")
    llist.egen_test()

'''
If you feel comfortable with what you’ve learned and you’re craving more,
then feel free to pick one of the challenges below:

- [ ] Create a method to retrieve an element from a specific position:
      get(i) or even llist[i].
- [ ] Create a method to reverse the linked list: llist.reverse().
- [ ] Create a Queue() object inheriting this article’s
      linked list with enqueue() and dequeue() methods.

'''

