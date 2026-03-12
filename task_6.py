def get_number_towns() -> int:
    '''
    The function reads the number of settlements.

    Returns:
        int: Number of settlements
    '''
    n = int(input('Введите количество населенных пунктов: '))
    
    return n


def get_number_roads() -> int:
    '''
    The function reads the number of roads.

    Returns:
        int: Number of roads
    '''
    m = int(input('Введите количество дорог: '))
    
    return m


def build_net(m: int) -> dict:
    '''
    The function builds a net of settlements and the distances between them.

    Args:
        m (int): Number of roads

    Returns:
        dict: A dictionary of dictionaries. The keys of the main dictionary 
        are cities, and the values are auxiliary dictionaries. The keys of 
        the auxiliary dictionaries are cities, and the values are the distances 
        from the city-key of the main dictionary to the city-key of the 
        auxiliary dictionary.
    '''
    net = {}

    print('Введите параметры дорог между населенными пунктами'
          'в формате: пункт_1 пункт_2 расстояние')

    for _ in range(m):
        town_1, town_2, distance = input().split()
        distance = int(distance)
        
        if town_1 not in net:
            net[town_1] = {}
        if town_2 not in net:
            net[town_2] = {}
        
        net[town_1][town_2] = distance
        net[town_2][town_1] = distance
    
    return net


def get_target_towns() -> tuple:
    '''
    The function reads the start and end towns to find the shortest path between them.

    Returns:
        tuple: (start_town, end_town)
    '''
    start_town, end_town = input('Введите начальный и конечный '
                                 'населенные пункты: ').split()
    
    return start_town, end_town


def find_short_distance(start_town: str, end_town: str, net: dict) -> int:
    '''
    The function finds the shortest distance between two towns
    using Dijkstra's algorithm.

    Args:
        start_town (str): Name of the starting town
        end_town (str): Name of the destination town
        net (dict): Graph representing towns and distances between them.
                   Format: {town1: {town2: distance, town3: distance, ...},
                           town2: {...}, ...}

    Returns:
        int: Shortest distance from start_town to end_town
    '''
    # Create a dictionary: town - distance
    # Distances - distances from start_town to the key town
    # Set start_town to 0, and set the other values to inf
    # until the distance to them is unknown.
    distances = {town : float('inf') for town in net}
    distances[start_town] = 0

    # towns is unvisited
    unvisited = set(net.keys())

    while unvisited:
        # Find the optimal town with minimum distance
        next_town = min(unvisited, key= lambda town: distances[town])

        unvisited.remove(next_town)

        # Iterate tuples: (neighboring town, distance)
        for town, distance in net[next_town].items():
            new_distance = distances[next_town] + distance
            distances[town] = min(new_distance,
                                  distances[town])

    return distances[end_town]


def main() -> None:
    n = get_number_towns()

    m = get_number_roads()

    net = build_net(m)

    start_town, end_town = get_target_towns()
    
    short_distance = find_short_distance(start_town, end_town, net)

    print(short_distance)


if __name__ == '__main__':
    main()
