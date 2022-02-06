import re


def search_sample():
    match = re.search(r"[A-Z]la", "ala Ola Ela")  # <4, 7)
    print(match)
    print(match.group(0))

    # brak trafien
    match = re.search(r"[A-Z]la", "ala ala ala")
    print(match)

    # or
    # regex = re.compile(r"[A-Z]la")
    # match = regex.search("ala Ola Ela")
    # print(match)
    # print(match.group(0))


def match_sample():
    # None - tekst rozpoczyna sie od ala
    match = re.match(r"[A-Z]la", "ala Ola Ela")
    print(match)

    # Ola - teskt rozpoczyna sie od Ola
    match = re.match(r"[A-Z]la", "Ola ala Ela")
    print(match)


def fullmatch_sample():
    match = re.fullmatch(r"[A-Z]la", "Ela")
    match = re.search(r"^[A-Z]la$", "Ela")
    print(match)

    # None - sprawdza caly teskst
    match = re.fullmatch(r"[A-Z]la", "Ola ala Ela")
    match = re.search(r"^[A-Z]la$", "Ola ala Ela")
    print(match)


def findall_sample():
    match_list = re.findall(r".la", "Ola ala Ela")
    print(match_list)

    # ['Ola', 'Ela']
    match_list = re.findall(r"[O,E]la", "Ola ala Ela")
    print(match_list)


def finditer_sample():
    iter = re.finditer(r".la", "Ola ala Ela")
    for elem in iter:
        print(elem)


def split_sample():
    split_list = re.split(r",|\.", "apple,pear,grapes,carrot.cabbage,veggies.fruit,yard")
    print(split_list)


def sub_sample():
    updated_str = re.sub(r"[a-z]{4}", "psa", "Ala ma kota")
    print(updated_str)

    updated_str = re.sub(r"[A-Z][a-z]+", "Python",
                         "naszym ulubionym jezykiem programowania jest Java")
    print(updated_str)


def subn_sample():
    updated_str = re.subn(r"[a-z]{5}", "psa", "Ala ma kota i kota")
    print(updated_str)

    updated_str = re.subn(r"[A-Z][a-z]+", "Python",
                          "naszym ulubionym jezykiem programowania jest Java")
    print(updated_str)


if __name__ == '__main__':
    search_sample()
    match_sample()
    fullmatch_sample()
    findall_sample()
    finditer_sample()
    split_sample()
    sub_sample()
    subn_sample()
