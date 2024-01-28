def lengths(strings: list):
    return {n:len(n) for n in strings}



if __name__ == "__main__":
    word_list = ["once", "upon" , "a", "time", "in"]
    word_lengths = lengths(word_list)
    print(word_lengths)