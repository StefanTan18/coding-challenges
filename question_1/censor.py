import os
import shutil

def censor(text_file):
    total = 0
    # checks to see what the taboo words are
    with open("taboo") as tf:
        for line in tf:
            for taboo in line.split():
                asteriks = '*' * len(taboo) # assigns the proper number of '*' for the taboo words
                # reads the text file
                fin = open(text_file, "rt")
                text = fin.read()
                words = text.split()
                count = 0
                # counts the number of taboo words in the file
                for i in range(0, len(words)):
                    if (taboo == words[i]):
                        count += 1
                # taboo words are replaced               
                text = text.replace(taboo, asteriks)
                fin.close()
                fin = open(text_file, "wt")
                fin.write(text)
                fin.close()
                total += count
    # File is moved to the trash folder if there are more than 5 taboo words
    if total > 5:
        shutil.move(text_file, "trash/{}".format(text_file))
    # Outputs the number of replacements made in each file
    print("There are {} taboo words in {}.".format(total, text_file))

def main():
    # Replaces taboo word in all text files in this directory
    for file in os.listdir():
        if file.endswith(".txt"):
            censor(file)

if __name__ == "__main__":
    main()