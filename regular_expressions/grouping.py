import re

if __name__ == "__main__":
    text = "Tomasz W. (33 l.), widziany ostatnio w Krakowie"
    # pattern = r"([A-Z][a-z]+ [A-Z]\.) \((\d+) l.\)"
    match = re.search(r"([A-Z][a-z]+ [A-Z]\.) \((\d+) l\.\)", text)
    print(match)
    print(match.groups())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))

    text = "Tomasz (33 l.) i Ewa (24 l.) umówili się na jutro na wspólne zakupy"
    # pattern = r"([A-Z]{1}[a-z]+) \((\d+) l.\)"
    print(re.findall(r"([A-Z][a-z]+) \((\d+) l.\)", text))
