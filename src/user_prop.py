from src.password_generator import generate_password


class User:

    def __init__(self):
        self.flat_num = None
        self.name = None
        self.surname = None
        self.sex = None
        self.birth_date = None
        self.place_of_birth = None
        self.pass_num = None
        self.mail = None
        self.phone_num = None
        self.city_or_village = None
        self.city = None
        self.street = None
        self.house_num = None
        self.post_index = None
        self.password = None

    def get_sex(self):
        while True:
            sex_dec = input('Введите пол:\n1-Мужской,2-Женский\n')
            if sex_dec == '1':
                self.sex = 0
                break
            elif sex_dec == '2':
                self.sex = 1
                break
            else:
                print('Неправильный ввод\n')

    def get_city_or_village(self):
        while True:
            living_dec = input('Это город или село?:\n1-Город,2-Село\n')
            if living_dec == '1':
                self.city_or_village = 0
                break
            elif living_dec == '2':
                self.city_or_village = 1
                break
            else:
                print('Неправильный ввод\n')


    def create(self):
        self.name = input('Введите имя, латиницей, как в загран паспорте\n')
        self.surname = input('Введите фамилию, латиницей, как в загран паспорте\n')
        self.get_sex(self)
        self.birth_date = input('Введите дату рождения в формате "ДД.ММ.ГОД"\n')
        self.place_of_birth = input('Введите место рождения\n')
        self.pass_num = input('Введите номер заграна\n')
        self.mail = input('Введите почту\n')
        self.phone_num = input('Введите номер телефону\n')
        self.get_city_or_village(self)
        self.city = input('Введите город\n')
        self.street = input('Введите улицу\n')
        self.house_num = input('Введите номер дома\n')
        self.flat_num = input('Введите номер квартиры\n')
        self.post_index = input('Введите почтовый индекс\n')
        self.password = generate_password(12)

    def save_data(self):
        sex_to_print = 'Мужской' if self.sex == 0 else 'Женский'
        vil_or_city = 'Город' if self.city_or_village == 0 else "Село"
        content = (f"Имя: {self.name}\n"
                   f"Фамилия: {self.surname}\n"
                   f"Пол: {sex_to_print}\n"
                   f"Дата рождения: {self.birth_date}\n"
                   f"Место рождения: {self.place_of_birth}\n"
                   f"Номер загран паспорта: {self.pass_num}\n"
                   f"Почта: {self.mail}\n"
                   f"Номер телефона: {self.phone_num}\n"
                   f"Адрес: {vil_or_city} {self.city}, {self.street} {self.house_num} {self.flat_num} {self.post_index}\n"
                   f"Пароль: {self.password}\n")
        with open(f'./{self.name.capitalize()}_{self.surname.capitalize()}_Data.txt', 'w') as file:
            file.write(content)

def make_test_user():
    test_user = User
    test_user.name = 'Test_name'
    test_user.surname = 'Test_SR'
    test_user.sex = 0
    test_user.birth_date = '11.11.2011'
    test_user.place_of_birth = 'Test_City'
    test_user.pass_num = 'FC123141'
    test_user.mail = 'test@mail.ru'
    test_user.phone_num = '+38000000'
    test_user.city_or_village = 0
    test_user.city = 'Test-City'
    test_user.street = 'test_str'
    test_user.house_num = '12'
    test_user.flat_num = '1'
    test_user.post_index = '61000'
    test_user.password = generate_password(12)

    return test_user

def main():
    pass

if __name__ == "__main__":
    main()