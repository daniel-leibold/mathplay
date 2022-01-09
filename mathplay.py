import os
from random import randrange

class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

def greeting():
    print("Hallo, wie heißt DU?")
    name = input()
    print("Bist Du ein (j)unge 👦 oder (m)ädchen 👧?")
    gender = input()
    gender_title = ""
    if gender == "j":
        gender_title = "Junge 👦"
    if gender == "m":
        gender_title = "Mädchen 👧"
    print("Wie alt bist Du?")
    age = int(input())
    print("🎂" * age)
    print(
        f"Hi {name}! Du bist {age} Jahre alt und ein {gender_title}. Lets start 🚀!")
    return User(name, age, gender)

def show_stat(user: User, success_count, failure_count, round_count):
    success_rate = success_count / round_count
    failure_rate = failure_count / round_count
    if round_count % 5 != 0:
        return
    print("*" * 50)
    print(f"{user.name} hast {round_count} Runden gespielt.")
    if round_count == 10:
        print(f"Wow {user.name}! 10 Runden! 🏅")
    if round_count == 20:
        print("Wow! 20 Runden! Silbermedalie! 🥈")
    if round_count == 30:
        print(f"30 Runden {user.name}! Wirklich ganz Toll! Du bist in der Hall of fame! ⭐")

    print("Erfolgquote 👍: {:.2%}".format(success_rate))
    print("Fehlerquote 👎: {:.2%}".format(failure_rate))
    if success_rate > 0.75:
        print(f"Wow... Super Erfolgsrate {user.name}!!! 👏 🏆")
    if failure_rate > 0.25:
        print("mhhh... Mach mal ein Pause. 🍵")
    print("*" * 50)

def play(user: User):
    round_count = 1
    success_count = 0
    failure_count = 0
    while True:
        suma = randrange(1, 10)
        sumb = randrange(1, 10)
        print(
            f"Runde {round_count}: Was ist das Ergebnis aus {suma} ➕ {sumb} ?")
        user_input = input()
        if str(user_input).startswith("c"):
            print("SCHADE, dass Du aufhören willst!")
            break
        user_value = int(user_input)

        if user_value == (suma + sumb):
            print("Hurra!!! Das stimmt! ❤️")
            success_count += 1
        else:
            print(f"Leider falsch: ☹️. {user.name} versuche es nochmal!")
            failure_count += 1
        show_stat(user, success_count, failure_count, round_count)
        round_count += 1


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')
    # print out some text

if __name__ == "__main__":
    screen_clear()
    user = greeting()
    play(user)
