def get_number_of_relations() -> int:
    '''
    The function reads the number of parent-child relationships.

    Returns:
        int: Number of relationships
    '''
    n = int(input('Введите количество родительских отношений: '))
    
    return n


def build_tree(n: int) -> dict:
    '''
    The function builds a family tree from parent-child relationships.

    Args:
        n (int): Number of relationships

    Returns:
        dict: Dictionary with parent names as keys and list of children as values
    '''
    tree = {}

    print('Введите пары родитель - потомок:')

    for _ in range(n):
        parent, child = input().split()
        
        if parent in tree:
            tree[parent].append(child)
        else:
            tree[parent] = [child]
        
        # Adding children to the tree
        if child not in tree:
            tree[child] = []
    
    return tree


def get_target_person() -> str:
    '''
    The function reads the name for which the count descendants to be found.

    Returns:
        str: The target person name
    '''
    name = input('Введите имя для поиска кол-ва потомков: ')
    
    return name


def count_descendants(person: str, tree: dict) -> int:
    '''
    Recursive function that counts all descendants:
        (children, grandchildren, ...)
    for a entered person in the family tree.

    Args:
        person (str): The name of the entered person
        tree (dict): Family tree dictionary

    Returns:
        int: Total number of descendants
    '''
    if person not in tree:
        return 0
    
    total = 0
    # We recursively go through each child, adding him and 
    # the number of his children.
    for child in tree[person]:
        total += (1 + count_descendants(child, tree))
    
    return total


def main() -> None:
    n = get_number_of_relations()

    family_tree = build_tree(n)

    target_person = get_target_person()

    result = count_descendants(target_person, family_tree)
    
    print(result)


if __name__ == '__main__':
    main()