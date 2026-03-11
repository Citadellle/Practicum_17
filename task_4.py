def get_dict_size() -> int:
    '''
    The function reads the number of shape categories in the dictionary.

    Returns:
        int: Number of shape categories
    '''
    n = int(input('Введите количество элементов словаря: '))
    
    return n


def create_shape_dict(n: int) -> dict:
    '''
    The function creates a dictionary relating objects to their shapes.
    For each line, the first word is the shape, following words are objects.

    Args:
        n (int): Number of shape categories

    Returns:
        dict: Dictionary with objects as keys and their shapes as values
    '''
    shape_dict = {}

    print('Введите формы и объекты (через пробел)',
          'Например: форма предмет_1 предмет_2 ...',
          sep = '\n')

    for _ in range(n):
        line = input().split()
        shape = line[0]
        objects = line[1:]
        
        for object in objects:
            shape_dict[object] = shape
    
    return shape_dict


def get_user_object() -> str:
    '''
    The function reads the object for which the shape needs to be found.

    Returns:
        str: The user object
    '''
    obj = input('Введите предмет для поиска формы: ')
    
    return obj


def find_shape(obj: str, shape_dict: dict) -> str:
    '''
    The function finds the shape for a given object.
    If the object is not in the dictionary, it returns the object unchanged.

    Args:
        obj (str): The object for which the shape needs to be found
        shape_dict (dict): Dictionary mapping objects to shapes

    Returns:
        str: The shape of the object or original object if not found
    '''
    if obj in shape_dict:
        return shape_dict[obj]
    
    return 'Форма предмета неизвестна'


def main() -> None:
    n = get_dict_size()

    shape_dict = create_shape_dict(n)

    user_object = get_user_object()

    result = find_shape(user_object, shape_dict)
    
    print(result)


if __name__ == '__main__':
    main()
