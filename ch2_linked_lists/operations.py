from .linked_lists import SingleLink

def create_link_list(vals):
    single_link = SingleLink()
    for val in vals:
        single_link.push(val)

    return single_link

#2.1
def single_link_duplicate_delete_buffered(single_link):
    explored = set()
    current = single_link.head
    previous = False
    while current:
        if current.data in explored:
            previous.next = current.next
        else:
            explored.add(current.data)
            previous = current
        current = current.next
    
def single_link_duplicate_runner_delete(single_link):
    current = single_link.head
    while current:
        runner = current
        while runner.next:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

#2.2
def single_link_k_to_last(single_link, k):
    list_length = 0
    current = single_link.head
    while current:
        list_length += 1
        current = current.next

    if k > list_length:
        raise ValueError(f"Element position ({k}) larger than length of Linked List ({list_length})")

    position = list_length - k
    current = single_link.head
    for _ in range(0, position):
        current = current.next

    return current.data

def single_link_k_to_last_print(node, k):
    if node is None:
        return 0
    index = single_link_k_to_last_print(node.next, k) + 1
    if index == k:
        print(node.data)
    return index

def single_link_k_to_last_recursive(node, k, index=-1):
    if node is None:
        return -99
    if index == k:
        return node.data
    index += 1
    value = single_link_k_to_last_recursive(node.next, k, index)
    if value>0:
        return value
    return -98

#2.3
def remove_node_from_link(node):
    if not node:
        raise AttributeError(f"Not a Node in Link List: {node}")
    next = node.next
    if not next:
        raise ValueError("Cannot Remove last node without access to preceding Node")
    node.data = next.data
    node.next = next.next

#2.4
def _last_node(link):
    current_node = link.head
    while current_node.next:
        current_node = current_node.next

    return current_node

def partition_around_value(link_list, partition_value):
    lower_list = SingleLink()
    greater_equal_list = SingleLink()
    current_node = link_list.head
    while current_node:
        if current_node.data < partition_value:
            lower_list.push(current_node.data)
        else:
            greater_equal_list.push(current_node.data)

        current_node = current_node.next

    last_node = _last_node(lower_list)
    current_node = greater_equal_list.head
    while current_node:
        last_node.next = current_node
        last_node = current_node
        current_node = current_node.next

    return lower_list

#2.5
def sum_two_reverse_order_digit_lists(list_1, list_2):
    new_list = SingleLink()
    node_1 = list_1.head
    node_2 = list_2.head
    remainder = 0
    while node_1 and node_2:
        value = node_1.data + node_2.data + remainder
        if remainder:
            remainder = 0
        if value >= 10:
            value -= 10
            remainder += 1
        new_list.push(value)

        node_1 = node_1.next
        node_2 = node_2.next

    if node_1 and not node_2:
        node_ = node_1
    elif node_2 and not node_1:
        node_ = node_2
    else:
        node_ = None

    while node_:
        value = node_.data + remainder
        new_list.push()

    return new_list

#2.6
def reverse_link_list(link):
    node = link.head
    current = node.next

    while current:
        link.head = current
        current = current.next
        link.head.next = node
        node = link.head

def is_palindrome_link_list(link):
    comp_list = SingleLink()
    current = link.head
    runner = link.head
    while runner:
        comp_list.push(current.data)
        runner = runner.next
        if not runner:
            break
        runner = runner.next
        current = current.next

    reverse_link_list(comp_list)
    comp = comp_list.head
    while current:
        if current.data != comp.data:
            return False
        current = current.next
        comp = comp.next

    return True

#2.7
def intersecting_list(list_1, list_2, offset):
    if offset < 0:
        offset *= -1
        longer_node = list_2.head
        shorter_node = list_1.head
    else:
        longer_node = list_1.head
        shorter_node = list_2.head
    while offset > 0:
        longer_node = longer_node.next
        offset -= 1

    while longer_node is not None:
        if id(longer_node) == id(shorter_node):
            return longer_node
        longer_node = longer_node.next
        shorter_node = shorter_node.next

    return False

def get_length(link_list):
    count = 0
    current = link_list.head
    while current is not None:
        count += 1
        current = current.next

    return count

def intersection_with_offset_calc(list_1, list_2):
    offset = get_length(list_1) - get_length(list_2)
    return intersecting_list(list_1, list_2, offset)

#2.8
def dual_list_transit_runner(traverser, runner):
    steps = 0
    while runner is not None:
        steps += 1
        runner = runner.next.next if runner.next is not None else runner.next
        traverser = traverser.next
        if id(runner) == id(traverser):
            return steps, runner

    return 0, runner

def link_loop_detection(link_list):
    traverser = link_list.head
    runner = link_list.head
    steps, runner = dual_list_transit_runner(traverser, runner)
    if steps == 0:
        return False
    else:
        traverser = link_list.head
        steps, runner = dual_list_transit_runner(traverser, runner)

        return steps if steps else False
