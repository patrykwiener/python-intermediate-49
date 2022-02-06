import re


def validate_email(email):
    pattern = r"^(\w+)?[\.-]?\w+@\w+\.\w+$"
    # return bool(re.fullmatch(r"\w+[.-_]?\w*@\w+\.\w{2,3}", email))
    return bool(re.fullmatch(r".+@.+", email))


if __name__ == '__main__':
    assert validate_email('a@a.b.com')
    assert validate_email('patryk-wiener@domain.com')
    assert validate_email('PAtrYk-wIener@domain.com')
    assert validate_email('a@a.a')
    assert not validate_email('@domain.com')
    assert validate_email('a@a')
