def print_upper_words(words):
    """ Print each word with uppercase on separate line 

        Example:
        print_upper_words(["apple", "banana", "cherry"])
        APPLE
        BANANA
        CHERRY
    """
    for word in words:
        print(word.upper())

print_upper_words(["apple", "banana", "cherry"]) 


def print_upper_words2(words):
    """ Prints words that start with letter 'e' upper or lower case
        on separate line and all uppercased

        Example:
        print_upper_words2(["electric", "purple", "Elif"])
        should return electric and Elif
    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

print_upper_words2(["electric", "purple", "Elif"])

def print_upper_words3(words, must_start_with):
    """ Print words with whatever letter is passed in that it starts with

        Example:
        print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
        should print "HELLO", "HEY", "YO", and "YES"
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                

print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})