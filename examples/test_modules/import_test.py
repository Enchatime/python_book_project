def search4vovels(phrase: str) -> set:   ## example of annotation
    """program for search vovels"""
    vovels = {'a', 'e', 'i', 'o', 'u'}

    return vovels.intersection(set(phrase))  # inner join of 2 sets

def search4letters(phrase: str, letters: str='aieou') -> set:   ## example of annotation
    """program for search letters"""
    return set(letters).intersection(set(phrase))

search4letters('test', 'a')