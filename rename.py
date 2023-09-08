


def space_to_underscore(text):
    new_text = ""
    for character in text:
        if character == " ":
            new_text += "_"
            continue
        new_text += character
    return new_text

def underscore_to_space(text):
    new_text = ""
    for character in text:
        if character == "_":
            new_text += " "
            continue
        new_text += character
    return new_text