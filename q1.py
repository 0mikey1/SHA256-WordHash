import hashlib

digest = "69d8c7575198a63bc8d97306e80c26e04015a9afdb92a699adaaac0b51570de7"

with open('words.txt', 'r') as listed_words:

    for line in listed_words:

        for word in line.split():

            if hashlib.sha256(word.encode("ascii", "ignore")).hexdigest() == digest:
                print(word)



