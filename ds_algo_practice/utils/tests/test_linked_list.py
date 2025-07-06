import  pytest

from ds_algo_practice.utils.linked_list import LinkedList

class TestLinkedList:
    def test_repr(self):
        sample_ll = LinkedList()
        sample_ll.add_node("1")
        sample_ll.add_node("2")
        sample_ll.add_node("3")
        sample_ll.add_node("4")
        sample_ll.add_node("5")

        assert str(sample_ll) == "<LinkedList(5) [1 -> 2 -> 3 -> 4 -> 5]>"

    def test_length(self):
        sample_ll = LinkedList()
        sample_ll.add_node("1")
        sample_ll.add_node("2")

        assert sample_ll.length == 2

    def test_create_linked_list(self):
        sample_ll = LinkedList()
        sample_ll.add_node("A")
        sample_ll.add_node("B")
        sample_ll.add_node("C")
        sample_ll.add_node("Z")

        assert sample_ll.to_list() == ["A", "B", "C", "Z"]

    def test_delete_linked_list(self):
        sample_ll = LinkedList()
        sample_ll.add_node("A")
        sample_ll.add_node("B")
        sample_ll.add_node("C")
        sample_ll.add_node("Z")
        sample_ll.delete_node(index=1)

        assert sample_ll.to_list() == ["A", "C", "Z"]

    def test_add_at_pos(self):
        sample_ll = LinkedList()
        sample_ll.add_node("1")
        sample_ll.add_node("2")
        sample_ll.add_node("3")
        sample_ll.add_node("5")
        sample_ll.add_node("4", 2)

        assert sample_ll.to_list() == ["1", "2", "3", "4", "5"]

    def test_delete_at_pos(self):
        sample_ll = LinkedList()
        sample_ll.add_node("1")
        sample_ll.add_node("2")
        sample_ll.add_node("2")
        sample_ll.add_node("3")
        sample_ll.add_node("4")
        sample_ll.delete_node(2)

        assert sample_ll.to_list() == ["1", "2", "3", "4"]

    def test_empty_ll_add_at_pos(self):
        sample_ll = LinkedList()

        with pytest.raises(Exception) as exc_info:
            sample_ll.add_node("4", 3)
        assert "Given Index bigger than LinkedList Length" in str(exc_info.value)

    def test_empty_ll_delete_at_pos(self):
        sample_ll = LinkedList()

        with pytest.raises(Exception) as exc_info:
            sample_ll.delete_node(3)
        assert "Given Index bigger than LinkedList Length" in str(exc_info.value)
