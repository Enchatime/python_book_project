def search4vovels(word):
    """program for search vovels"""
    vovels = {'a', 'e', 'i', 'o', 'u'}

    found = vovels.intersection(set(word))  # inner join of 2 sets

    for vovel in found:
        print(vovel)

search4vovels('test')