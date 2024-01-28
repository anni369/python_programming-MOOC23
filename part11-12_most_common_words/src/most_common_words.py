def most_common_words(filename: str, lower_limit: int):
    with open (filename) as text:
        text = text.read().replace("\n"," ")
        wordlist = text.strip().replace(".","").replace(",","").split(" ")
        print (wordlist)
        dict = {word: wordlist.count(word) for word in wordlist if wordlist.count(word)>= lower_limit}
        print(dict)
        return dict

if __name__ == "__main__":
    most_common_words("comprehensions.txt", 3)