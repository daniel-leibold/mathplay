from random import randrange

def greeting():
    print("Hallo, wie heißt DU?")
    name = input()
    print("Bist Du ein (j)unge 👦 oder (m)ädchen 👧?")
    gender = input()
    gender_title= ""
    if gender == "j":
        gender_title = "Junge 👦"
    if gender == "m":
        gender_title = "Mädchen 👧"
    print("Wie alt bist Du?")
    age = int(input())
    print("🎂" * age)
    print(f"Hi {name}! Du bist {age} Jahre alt und ein {gender_title}. Lets start! 🚀")

def show_stat(success_count, failure_count, round_count):
    success_rate = success_count / round_count
    failure_rate = failure_count / round_count
    if round_count % 5 != 0:
        return
    print(f"Du hast {round_count} Runden gespielt.")
    if round_count == 10:
            print("Wow! 10 Runden! 🏅")
    if round_count == 20:
            print("Wow! 20 Runden! Silbermedalie! 🥈")
    if round_count == 30:
            print("Wow! 30 Runden! Hall of fame! ⭐")

    print("Erfolgquote 👍: {:.2%}".format(success_rate))
    print("Fehlerquote 👎: {:.2%}".format(failure_rate))
    if success_rate > 0.75:
        print("Wow... Super Erfolgsrate!!! 👏 🏆")
    if failure_rate > 0.25:
        print("mhhh... Mach mal ein Pause. 🍵")

def play():
    round_count = 1
    success_count = 0
    failure_count = 0
    while True:
        suma = randrange(1, 10)
        sumb = randrange(1, 10)
        print(f"Runde {round_count}: Was ist das Ergebnis aus {suma} ➕ {sumb} ?")
        user_input=input()
        if str(user_input).startswith("c"):
            print("SCHADE das du aufhören willst!")
            break
        user = int(user_input)

        if user == (suma + sumb):
            print("Hurra!!! Das stimmt! ❤️")
            success_count += 1
        else:
            print("Leider falsch: ☹️")
            failure_count += 1
        show_stat(success_count, failure_count, round_count)
        round_count += 1

greeting()
play()
