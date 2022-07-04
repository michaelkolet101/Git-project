import sys
from colorama import Fore

dict_of_checks = {"min_ten": False,
                  "digit": False,
                  "alphabet": False,
                  "small": False,
                  "capital": False
                  }


def IsValid(string: str) -> bool:
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
    text_color = not Fore

    dict_of_mssages = {"alphabet": "Letter must be entered in the password !!!",
                       "digit": "Number must be entered in the password !!!",
                       "min_ten": "Password too short !!!",
                       "small": "A small letter must be in the password",
                       "capital": "A capital letter must be in the password"
                       }
    if not IsValid(password):
        for item in dict_of_checks:
            if not dict_of_checks[item]:
                raise TypeError(Fore.RED + dict_of_mssages[item])
                break

    print(Fore.GREEN + "passed the validation")


if __name__ == "__main__":
    main()
