from modulRegistrAutor import *
login = []
kasuataja_samasajas = []
parool = []


kasuataja_samasajas = None

while True:
    print(login_password_list)
    print(kasuataja_samasajas)
    print("Teie valik: ")
    print("1.Registreerimine")
    print("2.Sisselogimine")
    print("3.Vahetada kasutaja login")
    print("4.Vahetada parool")
    print("5.Exit")

    # valik
    valik = input("Tehke oma valik: ")
    if valik == "1":
        if kasuataja_samasajas is not None:       #проверка переменной
            print("Teil on kasutajakonto")
            continue
        login = input("Sisestage oma login: ")
        parool = input("Sisestage oma parool: ")
        index = register(login, parool)
        kasuataja_samasajas = index
    elif valik == "2":
        if kasuataja_samasajas is not None:
            print("Te juba olete")
            continue
        kasutajanimi = input("Sisestage oma login: ")
        parool = input("Sisestage oma  paroool:")
        kasutaja_indeksi = authorize(kasutajanimi, parool)
        kasuataja_samasajas = kasutaja_indeksi
    elif valik == "3":
        if kasuataja_samasajas is None:
            print("Te peate kontole sisse logima:")
            continue
        uus_login = input("Sisestage uus login: ")
        change_login(kasuataja_samasajas, uus_login)
    elif valik == "4":
        if kasuataja_samasajas is not None:
            print("Te olete juba registreeritud")
            continue
        nimi = input("Sisesta teie nimi: ")
        if nimi not in login_password_list[0]:
            print("Ei ole kasutajat selle nimega!")
            continue

        parool = recover_password(login_password_list[0].index(nimi))
        vana_parool = input("sisesta sinu vana parooli, mis saadakse e-postisse: ")
        if vana_parool != parool:
            print("vale parool!")
            continue
        kasuataja_samasajas = login_password_list[0].index(nimi)   #возвращает индекс первого вхождения элемента в списке

    elif valik == "5":
        kasuataja_samasajas = None