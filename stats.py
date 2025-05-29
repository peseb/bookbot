def word_count(text: str):
    words = text.split()
    return len(words)

def char_count(text: str):
    characters = {}
    for c in text:
        lower = c.lower()
        if lower in characters:
            characters[lower]+=1
        else:
            characters[lower]=1
    return characters