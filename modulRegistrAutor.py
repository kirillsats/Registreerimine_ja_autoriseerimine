def kirjuta_failisse(fail: str, login_password_list: list):
    """ Selline funktsioon kirjutab andmed failisse
    :param str fail: Faili nimi, kus salvestatakse andmed
    :param list  login_password_list: Jarjend, kus loginid ja parooolid
    :rtype: list
    """
    failname = "log_pass.txt"

    with open(fail, "w", encoding="utf-8") as f:  # Открывает файл для создания или перезаписи записей
        log_to_str = ",".join(login_password_list[0])
        f.write(log_to_str)
        f.write("\n")
        pass_to_str = ",".join(login_password_list[1])
        f.write(pass_to_str)




def lisamine_failisse(fail: str, login,parool:str):
    """Selline funktsioon liisab andmed failisse
    :param str fail:
    :param str login:
    :param str parool:
    :rtype: list
    """
    failname = "log_pass.txt"
    with open(fail, "r", encoding="utf-8") as f: #открывает файл в режиме чтения
        rida = f.readrida()
        logins_parools = [login,parool]
        for index, line in enumerate(rida):
            rida[index] = line.strip() + ',' + logins_parools[index]
    with open(fail, "w", encoding="utf-8") as f:
        f.write(rida[0])
        f.write("\n")
        f.write(rida[1])


def lugemine_failist(fail: str) -> list:
    """Selline funktsioon loeb andmed failist
    :param fail:
    :return:
    """
    f = open(fail, "r", encoding="utf-8")
    jarjend = []
    rida = f.readlines()
    for lines in rida:
        jarjend.append(lines.strip())


    f.close()
    log = jarjend[0].split(";")
    parools = jarjend[1].split(";")
    login_password_list.append(log)
    login_password_list.append(parools)
def andmete_uuendamine():
    """
    Selline funktsioon ueendab andmed
    :return:
    """
    login_password_list.clear()
    login_password_list.append(lugemine_failist("login_parool.txt"))

login_password_list = []
lugemine_failist("log_pass.txt")
def register(login: str, password: str, ) -> any:
    """
    funktsioon registreerib uue kasutaja
    login (str): kasutaja nimi
    password (str): kasutaja parool
    :rtype: any
    """
    # vaaatame kas kasutaja nimi on juba olemas või ei
    if login in login_password_list[0]:
        print("Kasutaja nimi on juba olemas!")
    #teeme uut kasuatajat
    lisamine_failisse("login_parool.txt", login, password)
    andmete_uuendamine()
    print(login_password_list[0])
    # printime edukat registreerimist
    print("Nüüd on kasutaja registreeritud")
    return login_password_list[0].index(login)


def authorize(kasutaja_nimi: str, parool: str) -> any:
    """
    see funktsioon autoriseerib kasutaja
    login (str): kasutaja nimi
    password (str): kasutaja parool
    :rtype: kasutaja_nimi, parool
    """
    # kontrollime, kas nime on kasutanud või mitte
    if kasutaja_nimi not in login_password_list[0]:
        print("Kahjuks kasutajad selle nimega ei ole :(")
        return False

    index = login_password_list[0].index(kasutaja_nimi)

    #  kontrollime parool
    if parool != login_password_list[1][index]:
        print("Vale parool!")
        return False
    return index

def change_login(indeks: int, new_login: str) -> any:
    """
    See funktsioon muudab kasutaja nime

    login (str): vana kasutaja nimi
    new_login (str): uus kasutaja nimi
    :rtype: any
    """

    #kontrollime, et uue nimi ei ole kasutanud
    if new_login in login_password_list[0]:
        print("Kahjuks on selline nimi juba kasutunud!")
        return False
    # Kasutaja sisselogimisnime muutmine loendis
    login_password_list[0][indeks] = new_login

    print("Kasutaja nimi muudetud edukalt!")
    kirjuta_failisse("login_parool.txt")


# funktsioon et muuta kasutaja parool
def change_password(login: str, new_password: str) -> any:
    """
    see funktsioon muudab kasutaja parooli

    login (str): kasutaja nimi
    new_password (str): kasutaja uus parool
    :rtype: login, new_password
    """
    #kontrollime, et nimi ei ole kasutunud

    index = login_password_list[0].index(login)
    # vahetame kasutaja parooli loendis
    login_password_list[1][index] = new_password

    print("Kasutaja parool muudetud edukalt!")
    kirjuta_failisse("login_parool.txt")


    # funktsioon tagastab kasutaja parool
def recover_password(indeks) -> any:
    """
    Эта функция возвращает пароль пользователя.

    indeks (int): Индекс пароля в списке паролей.
    :rtype: any
    """
    import smtplib, ssl
    from email.message import EmailMessage

    smtp_server = 'smtp.gmail.com'
    port = 587
    sender_email = "dokumnet2016@gmail.com"
    to_email = input("Введите ваш email: ")
    app_password = "ваш_пароль_приложения"

    context = ssl.create_default_context()
    msg = EmailMessage()
    msg.set_content(login_password_list[1][indeks])
    msg["Subject"] = "Восстановление пароля"
    msg["From"] = "dokumnet2016@gmail.com"
    msg["To"] = to_email

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, app_password)  # Вместо обычного пароля используется пароль приложения
        server.send_message(msg)
    except Exception as e:
        print(e)
    finally:
        server.quit()

    return login_password_list[1][indeks]
