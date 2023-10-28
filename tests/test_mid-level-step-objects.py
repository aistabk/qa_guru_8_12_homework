from selene.support.shared import browser
import allure
from model.practice_form import PracticeForm


@allure.title("Проверка работы формы регистрации")
@allure.tag("web")
@allure.label("owner", "aistabk")
@allure.description("Проверяем, что после заполнения всех полей проходит регистрация на сайте")
@allure.feature("demoqa.com registration form")
@allure.link('https://demoqa.com', name='Testing')
def test_register_form():
    practice_form = PracticeForm()
    practice_form.open()

    with allure.step("Заполнение полей формы"):
        practice_form.fill_first_name('Имя')
        practice_form.fill_last_name('Фамилия')
        practice_form.fill_email('testmail@mail.gg')
        practice_form.fill_phone_number('2589632147')
        practice_form.gender_select()
        practice_form.fill_date_of_birth(1985, 10, 19)
        practice_form.select_hobby()
        practice_form.fill_subject('P')
    with allure.step("Добавление фотографии"):
        practice_form.add_photo('test_image/hedgehog.jpg')
    with allure.step("Заполнение адреса"):
        practice_form.fill_address('221b', 'Baker Street', 'London', 'NW1 6XE', 'UK')
        practice_form.state_select('NCR').city_select('Delhi')
    with allure.step("Подтверждение регистрации пользователя"):
        browser.element('#submit').click()

    with allure.step("Проверка введенных данных"):
        practice_form.should_registrated_user_with(
            'Имя Фамилия',
            'testmail@mail.gg',
            'Other',
            '2589632147',
            '19 November,1985',
            'Physics',
            'Reading',
            'hedgehog.jpg',
            '221b, Baker Street, London, NW1 6XE, UK',
            'NCR Delhi'
        )
