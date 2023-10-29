import allure
from model.practice_form_full import PracticeFormRegistrationFactCheck
from data.users import User

practice_form = PracticeFormRegistrationFactCheck()


@allure.title("Проверка работы формы регистрации")
@allure.tag("web")
@allure.label("owner", "aistabk")
@allure.description("Проверяем, что после заполнения всех полей проходит регистрация на сайте")
@allure.feature("demoqa.com registration form")
@allure.link('https://demoqa.com', name='Testing')
def test_student_registration_form():
    guest = User(first_name='Имя', last_name='Фамилия', email='testmail@mail.gg', gender='Other',
                 month_of_brith='November', phone_number='2589632147', year_of_brith='2006', day_of_brith='19',
                 subject='Physics',
                 hobby='Reading', picture='hedgehog.jpg', current_address='221b, Baker Street, London, NW1 6XE, UK',
                 state='NCR',
                 city='Delhi')


with allure.step("Открыть страницу для теста"):
    practice_form.open()
with allure.step("Заполнить данные пользователя guest"):
    practice_form.registration(guest)
with allure.step("Пользователь зарегистрирован, данные введены корректно"):
    practice_form.student_should_be_registred(guest)
