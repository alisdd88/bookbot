import re

# Main function
def main():
    path = './books/frankenstein.txt'
    with open(path) as f: 
        file_content = f.read()
    word_c = countWords(file_content)
    char_c = countChars(file_content)
    printReport(path, word_c, char_c)

# Generate Report
def printReport(path, words, chars):
    print(f"--- Begin report of {path[2:]} ---")
    print(f"{str(words)} words found in the document\n")
    for k, v in chars.items():
        print(f"The \'{k}\' character was found {str(v)} times")
    print("--- End report ---")

# Word count Function
def countWords(f):
    words = f.split()
    return len(words)

# Char count Function
def countChars(file_content):
    char_list = re.findall("[a-z]", file_content.lower())
    chars = {}
    for char in char_list:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    chars_sorted = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))
    return chars_sorted

main()