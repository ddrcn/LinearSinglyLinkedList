# Global constants indicating indices in the linked list node
VALUE = 0
NEXT = 1


# Adds element to back of List
def add_to_back(value, head, tail):
    item = [value, None]
    if head is None:
        head = item
    else:
        tail[NEXT] = item
    tail = item
    return head, tail


# Remove element from front of List
def remove_from_front(head, tail):
    if head is None:
        print('List is Empty')
    elif head == tail:
        head = tail = None
    else:
        head = head[NEXT]
    return head, tail


# Adds element to front of List
def add_to_front(value, head, tail):
    item = [value, None]
    if head is None:
        head = item
        tail = item
    else:
        head = [value, head]
    return head, tail


# Removes element from back of List
def remove_from_back(head, tail):
    if tail is None:
        print('List is Empty')
    elif head == tail:
        head = tail = None
    else:
        old = current = head
        while current is not tail:
            old = current
            current = current[NEXT]
        old[NEXT] = None
        tail = old
    return head, tail


# Returns length of List
def length(head, tail):
    if head is None:
        return 0
    item = head
    count = 1
    while item is not tail:
        count += 1
        item = item[NEXT]
    return int(count)


# Returns element by index
def get_element_at(value, head, tail):
    int(value)
    if (value > length(head, tail) - 1) or (value < 0):
        print('Element at ' + str(value) + ' not found! Value is None')
        return None
    else:
        item = head
        for i in range(value):
            item = item[NEXT]
        return item[VALUE]


# Finds first index with value
def find(value, head, tail):
    current = head
    for i in range(length(head, tail)):
        if value == current[VALUE]:
            print('Value ' + str(value) + ' was found at index = ' + str(i))
            return
        current = current[NEXT]
    print('Value ' + str(value) + ' was not found!')


# Finds all values in List
def find_all(value, head, tail):
    current = head
    success = False
    for i in range(length(head, tail)):
        if value == current[VALUE]:
            print('Value ' + str(value) + ' was found at index = ' + str(i))
        current = current[NEXT]
        success = True
    if not success:
        print('Value ' + str(value) + ' was not found!')


# Print element by element
def print_elements(head, tail):
    if head is None:
        print('List is empty!')
        return
    item = head
    while item is not tail:
        print(item[VALUE])
        item = item[NEXT]
    print(item[VALUE])


# Start our program
# These variables are used to work with the list
head = tail = None

head, tail = add_to_front(22, head, tail)
head, tail = remove_from_back(head, tail)
head, tail = add_to_front(27, head, tail)
head, tail = add_to_back(3, head, tail)
head, tail = add_to_back(4, head, tail)
head, tail = add_to_back(5, head, tail)
head, tail = add_to_front(5, head, tail)
head, tail = add_to_back('asd', head, tail)
head, tail = add_to_back(7, head, tail)
head, tail = add_to_back(5, head, tail)
head, tail = add_to_back('asd', head, tail)
print(head, tail)
print(length(head, tail))
print("")
find_all(5, head, tail)
find('asd', head, tail)
print(get_element_at(6, head, tail))
print_elements(head, tail)
print(length(head, tail))
print(tail)
