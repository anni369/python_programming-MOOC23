def begin_with_vowel(words: list):
    return [n for n in words if n[0] in "aeiouAEIOU"]


if __name__ == "__main__":
    word_list = ["automobile","motorbike","Animal","cat","Dog","APPLE","orange"]
    for vowelled in begin_with_vowel(word_list):
        print(vowelled)
