def get_dict_size() -> int:
    '''
    The function reads the number of antonym pairs in the dictionary.

    Returns:
        int: Number of antonym pairs in the dictionary
    '''
    n = int(input('Введите количество элементов словаря: '))
    
    return n


def antonym_dict(n: int) -> dict:
    '''
    The function creates a dictionary of antonyms from user input.
    Each pair (word1 word2) adds pairs keys and values:
    word1 -> word2 and word2 -> word1.

    Args:
        n (int): Number of antonym pairs

    Returns:
        dict: Dictionary with words as keys and their antonyms as values
    '''
    antonyms = {}

    print('Введите пары антонимов (через пробел):')

    for _ in range(n):
        line = input().split()
        word1, word2 = line[0], line[1]

        antonyms[word1] = word2
        antonyms[word2] = word1
    
    return antonyms


def get_user_word() -> str:
    '''
    The function reads the word for which you need to find the antonym.

    Returns:
        str: The target word
    '''
    word = input('Введите слово для поиска антонима: ')
    
    return word


def find_antonym(word: str, antonyms: dict) -> str:
    '''
    The function finds the antonym for a given word.
    If the word is not in the dictionary, it returns the word unchanged.

    Args:
        word (str): A word for which you need to find the antonym
        antonyms (dict): Dictionary of antonyms

    Returns:
        str: The antonym of the word or original word if antonym not found
    '''
    if word in antonyms:
        return antonyms[word]
    
    return word


def main() -> None:
    n = get_dict_size()

    antonyms = antonym_dict(n)

    user_word = get_user_word()

    result = find_antonym(user_word, antonyms)
    
    print(result)


if __name__ == '__main__':
    main()
