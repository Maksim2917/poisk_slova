def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()

    for el in other_words:
        origin_word = el
        el = el.lower()
        if el.find(root_word) >= 0:
            same_words.append(origin_word)
        else:
            continue
    return(same_words)

result1 = single_root_words('Rich', 'RIchiest', 'oriCHalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print (result1)
print (result2)
