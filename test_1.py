import yaml
import time
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])


def test_step1(selector_username, selector_password, selector_button, selector_error_msg, result_msg):
    input1 = site.find_element("xpath", selector_username)
    input1.clear()
    input1.send_keys("test")
    input2 = site.find_element("xpath", selector_password)
    input2.clear()
    input2.send_keys("test")
    button = site.find_element("css", selector_button)
    button.click()
    label = site.find_element("xpath", selector_error_msg)
    error = label.text
    assert error == result_msg


def test_step2(selector_username, selector_password, selector_button, selector_auth_success, auth_success_msg):
    input1 = site.find_element("xpath", selector_username)
    input1.clear()
    input1.send_keys(testdata["username"])
    input2 = site.find_element("xpath", selector_password)
    input2.clear()
    input2.send_keys(testdata["password"])
    button = site.find_element("css", selector_button)
    button.click()
    label = site.find_element("xpath", selector_auth_success)
    auth_success_txt = label.text
    assert auth_success_txt == auth_success_msg


def test_step3(selector_plus_post, selector_post_title, selector_post_descr, selector_post_content,
               selector_post_create_btn, selector_view_post_title):
    plus_post = site.find_element("xpath", selector_plus_post)
    plus_post.click()
    title = site.find_element("xpath", selector_post_title)
    title.clear()
    title.send_keys("01")
    descr = site.find_element("xpath", selector_post_descr)
    descr.clear()
    descr.send_keys("01")
    content = site.find_element("xpath", selector_post_content)
    content.clear()
    content.send_keys("01")
    create_btn = site.find_element("xpath", selector_post_create_btn)
    create_btn.click()
    time.sleep(3)
    title2 = site.find_element("xpath", selector_view_post_title)
    title_txt = title2.text
    assert "01" == title_txt
