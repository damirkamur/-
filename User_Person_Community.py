class User:
    def __init__(self, name):
        self.__name = name

    def send_message(self, user, message):
        pass

    def post(self, message):
        pass

    def info(self):
        return ''

    def describe(self):
        print(self.__name, ' | ', self.info())


class Person(User):
    def __init__(self, name, birthday):
        super().__init__(name)
        self.__birthday = birthday

    def info(self):
        return f'Дата рождения: {self.__birthday}'

    def subscribe(self, user):
        pass


class Community(User):
    def __init__(self, name, description):
        super().__init__(name)
        self.__description = description

    def info(self):
        return f'Описание: {self.__description}'


if __name__ == '__main__':
    person = Person('Иван', '10.05.1999')
    person.describe()
    community = Community('Какой-Паблик', 'Описание какого-то паблика')
    community.describe()
