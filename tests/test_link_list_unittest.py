from ch2_linked_lists.operations import *
import unittest

class TestDeleteDuplicates(unittest.TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        self.init_single_link = self._create_without_duplicate()

    def _create_with_duplicate(self):
        data = [1,1,2,3,4,2,5,3,6,6,6]
        return create_link_list(data)

    def _create_without_duplicate(self):
        data = [1,2,3,4,5,6,7]
        return create_link_list(data)

    def _data_as_digit(self, link, reverse=False):
        text = ''
        node = link.head
        while node:
            text += str(node.data)
            node = node.next

        if reverse:
            text = text[::-1]

        return int(text)

    def test_push_create(self):
        length = 0
        current_node =self.init_single_link.head
        while current_node is not None:
            length += 1
            current_node = current_node.next
        self.assertEqual(length, 7, 'Should have made 7 Nodes')

    def test_get_data(self):
        data = self.init_single_link.get_data()
        self.assertSequenceEqual(data, [1,2,3,4,5,6,7], "Creation data should match retrieved data")

    def test_buffer_delete_with_duplicates(self):
        single_link = self._create_with_duplicate()
        single_link_duplicate_delete_buffered(single_link)
        results = single_link.get_data()
        self.assertSequenceEqual(results, [1, 2, 3, 4, 5, 6], "Should Have Two Deletes with Buffer on Inputs")

    def test_buffer_delete_without_duplicates(self):
        single_link = self._create_without_duplicate()
        single_link_duplicate_delete_buffered(single_link)
        results = single_link.get_data()
        self.assertSequenceEqual(results, [1, 2, 3, 4, 5, 6, 7], "Should Have no Deletes with Buffer on Inputs")

    def test_runner_delete_with_duplicates(self):
        single_link = self._create_with_duplicate()
        single_link_duplicate_runner_delete(single_link)
        results = single_link.get_data()
        self.assertSequenceEqual(results, [1, 2, 3, 4, 5, 6], "Should Have Two Deletes with Runner on Inputs")

    def test_runner_delete_without_duplicates(self):
        single_link = self._create_without_duplicate()
        single_link_duplicate_runner_delete(single_link)
        results = single_link.get_data()
        self.assertSequenceEqual(results, [1, 2, 3, 4, 5, 6, 7], "Should Have no Deletes with Runner on Inputs")

    def test_kth_element_from_end(self):
        single_link = self._create_without_duplicate()
        result = single_link_k_to_last(single_link, 3)
        self.assertEqual(result, 5, '3 from last should be 5')

    def test_kth_element_from_end_recursive(self):
        single_link = self._create_without_duplicate()
        result = single_link_k_to_last_recursive(single_link.head, 3)
        self.assertEqual(result, 5, '3 from last should be 5')

    def test_intersection_one(self):
        list_1 = create_link_list([1,2,3,4])
        list_2 = create_link_list([5,6,7,8])
        current_node = list_1.head
        add_node = list_2.head
        while True:
            if current_node.data == 4:
                current_node.next = add_node.next
                break
            current_node = current_node.next
        result = intersection_with_offset_calc(list_1, list_2)
        self.assertEqual(result.data, 6, 'Intersection Data should be 6')

    def test_intersection_two(self):
        list_1 = create_link_list([1, 2, 3, 4])
        list_2 = create_link_list([5, 6, 7, 8])
        current_node = list_2.head
        add_node = list_1.head
        while True:
            if current_node.data == 7:
                current_node.next = add_node.next.next
                break
            current_node = current_node.next
        result = intersection_with_offset_calc(list_1, list_2)
        self.assertEqual(result.data, 3, 'Intersection Data should be 3')

    def test_intersection_no_overlap(self):
        list_1 = create_link_list([1, 2, 3, 4])
        list_2 = create_link_list([5, 6, 7, 8])
        result = intersection_with_offset_calc(list_1, list_2)
        self.assertEqual(result, False, 'No Intersection Data Should Return False')

    def test_internal_loop(self):
        single_link = self._create_with_duplicate()
        current_node = single_link.head
        while True:
            if current_node.data == 5:
                current_node.next = single_link.head.next.next.next.next.next.next
                break
            current_node = current_node.next
        result = link_loop_detection(single_link)
        self.assertEqual(result, 6, 'Loop Created starting at position 6')

    def test_internal_loop_without_loop(self):
        single_link = self._create_with_duplicate()
        result = link_loop_detection(single_link)
        self.assertEqual(result, False, 'No Loop Should Return False')

    def test_remove_node_through_access(self):
        single_link = self._create_without_duplicate()
        node = single_link.head.next.next.next
        remove_node_from_link(node)
        self.assertEqual(single_link.head.next.next.next.data, 5, 'Deleting Node should be 5')

    def test_value_partition(self):
        single_link = create_link_list([3,5,8,5,10,2,1])
        partitoned_list = partition_around_value(single_link, 5)
        new_collection = []
        current_node = partitoned_list.head
        while current_node:
            new_collection.append(current_node.data)
            current_node = current_node.next

        lower_group = new_collection[:3]
        lower_group.sort()
        self.assertSequenceEqual(lower_group, [1, 2, 3], "Should only be lower value 5, the set partition")

    def test_sum_reversed(self):
        link_1 = create_link_list([7,1,6])
        link_2 = create_link_list([5,9,2])
        sum_list = sum_two_reverse_order_digit_lists(link_1, link_2)
        end_value = self._data_as_digit(sum_list, reverse=True)

        self.assertEqual(end_value, 912, 'Total Should Be 912')

    def test_reverse_link_list(self):
        link = create_link_list([1,2,3,4,5])
        reverse_link_list(link)
        self.assertEqual(link.head.data, 5, 'End value 5 should be Head Data')

    def test_true_palindrome(self):
        link = create_link_list([1, 4, 3, 4, 1])
        result = is_palindrome_link_list(link)
        self.assertEqual(result, True, 'Data is a Palindrome')

    def test_false_palindrome(self):
        link = create_link_list([1, 2, 4, 4, 1])
        result = is_palindrome_link_list(link)
        self.assertEqual(result, False, 'Data is Not a Palindrome')

    def test_true_palindrome_even_length_text(self):
        link = create_link_list(['A','B','B','A'])
        result = is_palindrome_link_list(link)
        self.assertEqual(result, True, 'Even Length Text Data is a Palindrome')
