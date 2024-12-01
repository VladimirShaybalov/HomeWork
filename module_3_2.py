

def send_email(message: str, recipient: str, sender="university.help@gmail.com"):
    if "@" not in recipient or "@" not in sender\
            or not recipient.endswith((".com", ".ru", ".net")) or not sender.endswith((".com", ".ru", ".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")

result1 = (send_email(message='', recipient = "university.helpgmail.com",sender="university.help@gmail.com"))
result2 = (send_email(message='', recipient = "university.help@gmail.com",sender="university.help@gmail.com"))
result3 = (send_email(message='', recipient = "university.help@gmail.ru",sender="university.help@gmail.com"))




