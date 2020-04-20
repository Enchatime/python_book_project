def search4vovels(word: str) -> set:   ## example of annotation
    """program for search vovels"""
    vovels = {'a', 'e', 'i', 'o', 'u'}

    return vovels.intersection(set(word))  # inner join of 2 sets

search4vovels('python')