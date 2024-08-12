#    Asking the user to enter the text for the program to count.
user_input = input("Enter a text: ")


# Initial function for counting the frequency in the text.
def count_word_frequency(text):
    # To split the text into words
    words = text.split()

    # Dictionary to store the frequencies of the text.
    frequencies = {}
    # Loop through the list of words.
    for word in words:
        # check if the word is there and add one to the value of frequencies
        if word in frequencies:
            frequencies[word] += 1
        # if there isn't that word in the frequency count one.
        else:
            frequencies[word] = 1
    return frequencies


# calling the function count_word_frequency(user_input)
print(count_word_frequency(user_input))
