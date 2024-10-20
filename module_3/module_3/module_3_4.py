def single_root_words(root_word, *other_words):
    same_words = []
    root_word_over = root_word.lower()
    for root in other_words:
        word_lower = root.lower()
        if root_word_over in word_lower or word_lower in  root_word_over:
            same_words.append(root)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
