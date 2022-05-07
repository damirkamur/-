class Person:
    def __init__(self, name, patronymic, surname, contacts):
        self.__name = name
        self.__patronymic = patronymic
        self.__surname = surname
        self.__contacts = contacts

    def get_phone(self):
        return self.__contacts.get('private')

    def get_name(self):
        return f'{self.__surname} {self.__name} {self.__patronymic}'

    def get_work_phone(self):
        return self.__contacts.get('work')

    def get_sms_text(self):
        return f'Уважаемый {self.__name} {self.__patronymic}! ' \
               f'Примите участие в нашем беспроигрышном конкурсе для физических лиц'


class Company:
    def __init__(self, name, type_, contacts, *args):
        self.__name = name
        self.__type_ = type_
        self.__contacts = contacts
        self.workers = list(args)

    def get_phone(self):
        number = self.__contacts.get('contact')
        if number:
            return number
        for worker in self.workers:
            number = worker.get_work_phone()
            if number:
                return number
        return

    def get_name(self):
        return self.__name

    def get_sms_text(self):
        return f'Для компании {self.__name} есть супер предложение! ' \
               f'Примите участие в нашем беспроигрышном конкурсе для {self.__type_}'


def send_sms(*args):
    for elem in args:
        phone = elem.get_phone()
        if phone:
            print(f'Отправлено СМС на номер {phone} с текстом: {elem.get_sms_text()}')
        else:
            print(f'Не удалось отправить сообщение абоненту: {elem.get_name()}')


if __name__ == '__main__':
    person1 = Person('Степан', 'Петрович', 'Джобсов', {'private': 555})
    person2 = Person('Боря', 'Иванович', 'Гейтсов', {'private': 777, 'work': 888})
    person3 = Person('Семен', 'Робертович', 'Возняцкий', {'work': 789})
    person4 = Person('Леонид', 'Арсенович', 'Торвальдсон', {})
    company1 = Company('Яблочный комбинат', 'ООО', {'contact': 111}, person1)
    company2 = Company('ПластОкно', 'АО', {'non_contact': 222}, person2)
    company3 = Company('Пингвинья ферма', 'Ltd', {'non_contact': 444}, person4)
    send_sms(person1, person2, person3, person4, company1, company2, company3)
