def get_dict_size() -> int:
    '''
    The function reads the number of word pairs in the dictionary.

    Returns:
        int: Number of word pairs in the dictionary
    '''
    n = int(input('Введите количество пар слов словаря: '))
    
    return n


def create_dict(n: int) -> dict:
    '''
    The function creates a Russian-English dictionary from user input.

    Args:
        n (int): Number of word pairs to enter

    Returns:
        dict: Dictionary with Russian words as keys and 
              English translations as values
    '''
    dictionary = {}

    print('Введите пары слов:')

    for _ in range(n):
        russian, english = input().split()
        dictionary[russian] = english
    
    return dictionary


def get_phrase() -> str:
    '''
    The function reads the phrase in Russian entered by the user

    Returns:
        str: The user phrase
    '''
    phrase = input('Введите фразу для перевода: ')
    
    return phrase


def translate_phrase(phrase: str, dictionary: dict) -> str:
    '''
    The function translates a phrase from Russian 
    into English using a dictionary.
    Words not found in the dictionary remain unchanged.

    Args:
        phrase (str): The phrase to translate from Russian
        dictionary (dict): Russian-English dictionary

    Returns:
        str: Translated phrase in English
    '''
    words = phrase.split()
    translated_words = []
    
    for word in words:
        if word in dictionary:
            translated_words.append(dictionary[word])
        else:
            translated_words.append(word)
    
    translated_phrase = ' '.join(translated_words)
    
    return translated_phrase


def main() -> None:
    n = get_dict_size()

    dictionary = create_dict(n)

    phrase = get_phrase()

    translated_phrase = translate_phrase(phrase, dictionary)
    
    print(translated_phrase)


if __name__ == '__main__':
    main()