import sys


dict_of_checks = {"min_ten": False,
                  "digit": False,
                  "alphabet": False,
                  "small": False,
                  "capital": False
                  }

colors = {
    "red": '\033[31m',
    "green": '\033[32m',
    "White": '\033[37m'
}

def IsValid(string: str) -> bool:
    """
    check validation of string by the rules
    :param string: password
    :return: true if the password is valid else false
    """

    global dict_of_checks

    for ch in string:
        if ch.isnumeric():
            dict_of_checks["digit"] = True

        if ch.isalpha():
            dict_of_checks["alphabet"] = True

        if ch.isupper():
            dict_of_checks["capital"] = True

        if ch.islower():
            dict_of_checks["small"] = True

        if len(string) > 9:
            dict_of_checks["min_ten"] = True

    for item in dict_of_checks:
        if not dict_of_checks[item]:
            return False

    return True


def main():

    password = sys.argv[1]

    dict_of_messages = {"alphabet": "Letter must be entered in the password !!!",
                        "digit": "Number must be entered in the password !!!",
                        "min_ten": "Password too short! At least 10 characters must be entered",
                        "small": "A small letter must be in the password",
                        "capital": "A capital letter must be in the password"
                        }

    if not IsValid(password):
        for item in dict_of_checks:
            if not dict_of_checks[item]:
                raise TypeError(colors["red"] + dict_of_messages[item] + colors["White"])

    print(colors["green"] + "passed the validation" )


if __name__ == "__main__":
    main()
