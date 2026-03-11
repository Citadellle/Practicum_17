def get_words() -> list:
    '''
    The function reads a string from user input and splits it into words.

    Returns:
        list: List of words from the input string
    '''
    words = input('Введите строку: ').split()
    
    return words


def get_words_frequency(words: list) -> dict:
    '''
    The function calculates the frequency of each word in the list.

    Args:
        words (list): List of words to count frequency for

    Returns:
        dict: Dictionary with words as keys and their frequency as values
    '''
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    return frequency


def sort_words_by_frequency(frequency: dict) -> list:
    '''
    The function sorts words by their frequency in descending order.
    Words with the same frequency maintain their original order.

    Args:
        frequency (dict): Dictionary with words and their frequencies

    Returns:
        list: List of words sorted by frequency in descending order
    '''
    sorted_words = sorted(frequency.keys(), 
                          key= lambda w: frequency[w], 
                          reverse= True)
    
    return sorted_words


def output_words(sorted_words: list) -> None:
    '''
    The function prints each word on a separate line.

    Args:
        sorted_words (list): List of words to be printed
    '''
    for word in sorted_words:
        print(word)
        

def main() -> None:
    words = get_words()

    frequency = get_words_frequency(words)
    
    sorted_words = sort_words_by_frequency(frequency)
    
    output_words(sorted_words)


if __name__ == '__main__':
    main()