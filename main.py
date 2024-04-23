def main():
    # Open the file 
    with open("books/frankenstein.txt")as f:
        #read the file to the terminal
        file_contents = f.read()

        word_count = 0
        alphabet = {}

        words = file_contents.split()

        for word in words:
            word_count += 1

            for letter in word:
                if letter.lower() in alphabet:
                    alphabet[letter.lower()] += 1
                else:
                    alphabet[letter.lower()] = 1

        letter = []
        
        for i in alphabet:
            count = alphabet[i]
            letter.append({"name":i, "count":count})
        
        letter.sort(reverse=True, key=sort_on)

        #for i in range(len(letter)):
            #print(f"{letter[i]}")
        
        print(f"--- Begin report of {f.name} ---")
        print(f"{word_count} words found in the document")
        print("")
        for i in letter:
            a = 0
            b = 0
            for j in i:
                m = i[j]
                if a == 0:
                    a = m
                else:
                    b = m
            if a.isalpha():
                print(f"The '{a}' character was found {b} times")
             #   print(m, a, b)
        print("--- End report ---")

def sort_on(dict):
    return dict["count"]


main()

