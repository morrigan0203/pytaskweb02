import pytest


@pytest.fixture()
def selector_username():
    return '//*[@id="login"]/div[1]/label/input'


@pytest.fixture()
def selector_password():
    return '//*[@id="login"]/div[2]/label/input'


@pytest.fixture()
def selector_button():
    return 'button'


@pytest.fixture()
def selector_error_msg():
    return '//*[@id="app"]/main/div/div/div[2]/h2'


@pytest.fixture()
def result_msg():
    return "401"


@pytest.fixture()
def selector_auth_success():
    return '//*[@id="app"]/main/nav/ul/li[3]/a'


@pytest.fixture()
def auth_success_msg():
    return 'Hello, firstname'


@pytest.fixture()
def selector_plus_post():
    return '//*[@id="create-btn"]'


@pytest.fixture()
def selector_post_title():
    return '//*[@id="create-item"]/div/div/div[1]/div/label/input'


@pytest.fixture()
def selector_post_descr():
    return '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea'


@pytest.fixture()
def selector_post_content():
    return '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea'


@pytest.fixture()
def selector_post_create_btn():
    return '//*[@id="create-item"]/div/div/div[7]/div/button'


@pytest.fixture()
def selector_view_post_title():
    return '//*[@id="app"]/main/div/div[1]/h1'
