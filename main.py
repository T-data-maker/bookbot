def main ():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print (file_contents)
    return (file_contents)
main()
def count_words(text):
    words = text.split()
    #print (words)
    i=0
    for word in words: 
        i+=1
    print (i)
count_words(main())
def count_characters(text):
    lowered_text = text.lower()
    letter_count = {chr(i): 0 for i in range(97, 123)}
    
    for char in lowered_text:
        if char.isalpha():  
            letter_count[char] += 1  
    return (letter_count)
count_characters(main())
def sort_on(dictionary):
    sorted_dict = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict
if __name__ == "__main__":
    content = main()
    word_count = count_words(content)
    print(f"{word_count} words found in the document\n")

    letter_counts = count_characters(content)
    sorted_letters = sort_on(letter_counts)

    # Print sorted letter counts
    for letter, count in sorted_letters:
        print(f"The '{letter}' character was found {count} times")