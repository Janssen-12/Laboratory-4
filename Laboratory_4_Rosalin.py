class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Display the list (for checking)
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Insert at the end (sample method)
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node


    # a. Remove at beginning

    def remove_beginning(self):
        if self.head is None:
            return None  # Empty list
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data


    # b. Remove at end

    def remove_at_end(self):
        if self.head is None:
            return None  # Empty list

        # If only one node
        if self.head.next is None:
            removed_data = self.head.data
            self.head = None
            return removed_data

        # More than one node
        current = self.head
        while current.next.next:  # Stop before the last node
            current = current.next
        removed_data = current.next.data
        current.next = None
        return removed_data


    # c. Remove a specific data

    def remove_at(self, data):
        if self.head is None:
            return None  # Empty list

        # If the node to remove is the head
        if self.head.data == data:
            removed_data = self.head.data
            self.head = self.head.next
            return removed_data

        # Otherwise, search for it
        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next is None:
            return None  # Data not found

        removed_data = current.next.data
        current.next = current.next.next
        return removed_data

# Example Usage

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)
    ll.display()

    print("\nRemoved from beginning:", ll.remove_beginning())
    ll.display()

    print("\nRemoved from end:", ll.remove_at_end())
    ll.display()

    print("\nRemoved specific (20):", ll.remove_at(20))
    ll.display()

    print("\nAttempt to remove non-existing (100):", ll.remove_at(100))
    ll.display()
