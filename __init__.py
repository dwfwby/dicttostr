def dictToStr(dictionary, separator = ", "):
    if type(dictionary) == dict:
        for i in dictionary.items():
            name, value = i
            dictionary[name] = dictToStr(value)
        return separator.join(" ".join(i) for i in dictionary.items())
    else:
        return str(dictionary)
