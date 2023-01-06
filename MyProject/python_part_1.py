SEPARATOR = '------------------------------------------'

# информация о пользователе
name = ""  # имя пользователя
age = 0  # возраст
phone_number = ""  # номер телефона
e_mail = ""  # электронная почта
zip_code = ""  # почтовый индекс
postal_adress = ""  # почтовый адрес
additional_information = ""  # дополнительно о себе

# информация о компании
PSRNSP = ""  # ОГРНИП (15 цифр)
ITN = ""  # ИНН (12 цифр)
payment_account = ""  # расчетный счет (20 цифр)
my_bank = ""  # мой банк
BIC = ""  # БИК  (9 цифр)
corr_account = ""  # корреспондентский счет (20 цифр)


# функция генерации ответа о клиенте
def general_info_user(name_parameter, age_parameter, phone_number_parameter,
                      e_mail_parameter, zip_code_parameter,
                      postal_adress_parameter,
                      additional_information_parameter):
    # печать разделителя
    print(SEPARATOR)

    # вывод на экран имя пользователя
    print("Имя:    ", name_parameter)
    # проверка слова к возрасту
    if 11 <= age_parameter % 100 <= 19:
        years_parameter = "лет"
    elif age_parameter % 10 == 1:
        years_parameter = "год"
    elif 2 <= age_parameter % 10 <= 4:
        years_parameter = "года"
    else:
        years_parameter = "лет"
    # вывод на экран возраста
    print("Возраст:", age_parameter, years_parameter)
    # вывод на экрам номер телефона
    print("Телефон:", phone_number_parameter)
    # вывод на экран электронной почты
    print("E-mail: ", e_mail_parameter)
    # вывод на экран индекса
    print("Индекс: ", zip_code_parameter)
    # вывод на экран адреса
    print("Адрес: ", postal_adress_parameter)
    # вывод на экран дополнительной информации
    if additional_information:
        print("Дополнительная информация: ", additional_information_parameter)


def аbout_the_company(PSRNSP_parameter, ITN_parameter,
                      payment_account_parameter, my_bank_parameter,
                      BIC_parameter, corr_account_parameter):
    print("Информация о предпринимателе")
    print("ОРГНИП:", PSRNSP_parameter)
    print("ИНН:", ITN_parameter)
    print("Банковские реквизиты")
    print("Р/с:", payment_account_parameter)
    print("Банк:", my_bank_parameter)
    print("БИК:", BIC_parameter)
    print("К/с:", corr_account_parameter)


# вывод на экран информации о программе
print("Приложение MyProfile")
print("Сохраняй информацию о себе и выводи ее в разных форматах")

# запуск программы
while True:
    # запуск основного меню
    print(SEPARATOR)
    print("ГЛАВНОЕ МЕНЮ")
    print("1 - Ввести или обновить информацию")
    print("2 - Вывести информацию")
    print("0 - Завершить работу")

    # выбор действия пользователя
    option = int(input("Введите номер пункта меню: "))
    # если выбран 0, выход из цикла (программы)
    if option == 0:
        break
    # если выбран 1
    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print("ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ")
            print("1 - Личная информация")
            print("2 - Информация о предпринимателе")
            print("0 - Назад")

            option2 = int(input("Введите номер пункта меню: "))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                name = input("Введите имя: ")
                while 1:
                    # validate user age
                    age = int(input("Введите возраст: "))
                    if age > 0:
                        break
                    print("Возраст должен быть положительным")

                # input phone_number
                uph = input("Введите номер телефона (+7ХХХХХХХХХХ): ")
                phone_number = ""
                for ch in uph:
                    if ch == "+" or ("0" <= ch <= "9"):
                        phone_number += ch

                # input e_mail
                e_mail = input("Введите адрес электронной почты: ")

                # input zip_code
                zip_code = input("Введите почтовый индекс: ")

                # оставляем в индексе только числа:
                zip_code = "".join(i for i in zip_code if i.isdigit())

                # input postal_adress
                postal_adress = input("Введите почтовый адрес: ")

                # input additional_information
                additional_information = input(
                    "Введите дополнительную информацию:\n")

            elif option2 == 2:
                # input аbout the company
                while 1:
                    # ввод ОГРНИП
                    PSRNSP = int(input("Введите ОРГНИП: "))

                    # проверка на длину ввода (не менее 15 символов)
                    if len(str(PSRNSP)) == 15:
                        break
                    print("ОРГНИП должен содержать 15 цифр")
                # ввод ИНН
                ITN = input("Введите ИНН: ")
                while 1:
                    # ввод расчетного счета
                    payment_account = int(input("Введите расчетный счет: "))
                    # проверка на длину ввода (не менее 20 символов)
                    if len(str(payment_account)) == 20:
                        break
                    print("Расчетный счет должен содержать 20 цифр")

                # ввод наименования банка пользователя
                my_bank = input("Введите наименование банка: ")
                # ввод БИК компании
                BIC = input("Введите БИК: ")
                # ввод корреспондентского счета
                corr_account = input("Введите корреспондентский счет: ")
            else:
                print("Введите корректный пункт меню")

    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print("ВЫВЕСТИ ИНФОРМАЦИЮ")
            print("1 - Личная информация")
            print("2 - Вся информация")
            print("0 - Назад")

            option2 = int(input("Введите номер пункта меню: "))
            if option2 == 0:
                break

            if option2 == 1:
                general_info_user(name, age, phone_number, e_mail, zip_code,
                                  postal_adress, additional_information)

            elif option2 == 2:
                general_info_user(name, age, phone_number, e_mail, zip_code,
                                  postal_adress, additional_information)
                аbout_the_company(PSRNSP, ITN, payment_account, my_bank, BIC,
                                  corr_account)
            else:
                print("Введён некорректный пункт меню")
    else:
        print("Введён некорректный пункт меню")
