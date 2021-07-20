def print_upper_words(words, must_start_with={}):
    """ Accept a list of strings as the first argument and prints each separately to the console in uppercase.
    For example ["hello", "World"] will print:
    HELLO
    WORLD

    Optionally, can pass in a set of lowercase one-letter strings as the second argument.
    E.g. {"a", "d", "z"}
    Only words that begin with one of those letters will be printed to the console.
    """
    for word in words:
        if not must_start_with:
            print(word.upper())
        elif word[0].lower() in must_start_with:
            print(word.upper())

print_upper_words(["Hello", "hey", "goodbye", "yo", "yes"])

print_upper_words(["Hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})