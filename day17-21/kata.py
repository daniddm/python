def to_jaden_case(string):
    for word in string.split(" "):
        print(word)
        if "'" in word:
            word.capitalize()
        else:
            word.title()
    return string

print(to_jaden_case("how can mirrors be real if our eyes aren't real"))
