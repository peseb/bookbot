from typing import List


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

def sort_on(dict):
    return dict["num"]

def sort_statistics(stats: dict):
    result = []
    for entry in stats:
        mapped = { "char": entry, "num": stats[entry]}
        result.append(mapped)
    
    result.sort(reverse=True, key=sort_on)
    return result