# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word_list = list(word)
    word_sorted = sorted(word_list)

    anagram_list = list(anagram)
    anagram_sorted = sorted(anagram_list)

    return (word_sorted == anagram_sorted)

print(find_anagram("below", "elbow")) 
print(find_anagram("hello", "check"))
