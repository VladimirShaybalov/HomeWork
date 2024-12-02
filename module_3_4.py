def single_root_words(root_word:str,  *other_words:str):
    same_words = []

    for word in other_words:

        if root_word.lower() in word.lower() or (item.lower() for item in other_words):
            same_words.append(word)

    return same_words

result1 = single_root_words('rich', 'Richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)













