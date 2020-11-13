import undetected_chromedriver as uc
import time
from random import randrange
import json


def wait_random_time(minimum_wait_time):
    time.sleep(randrange(minimum_wait_time, 10))


with open('./credentials.json', 'r') as f:
    data = json.load(f)

driver = uc.Chrome()
wait_random_time(1)

driver.get('https://www.linkedin.com/login')
wait_random_time(3)

driver.find_element_by_id('username').send_keys(data["username"])
wait_random_time(1)

driver.find_element_by_id('password').send_keys(data["password"])
wait_random_time(1)

driver.find_element_by_xpath('//*[@id="app__container"]/main/div[3]/form/div[3]/button').click()
wait_random_time(3)

driver.find_element_by_xpath('//*[@id="primary-navigation"]/ul/li[2]').click()
wait_random_time(4)

driver.find_element_by_xpath('//*[@id="msg-overlay"]/div[1]').find_element_by_tag_name('button').click()
wait_random_time(1)

for _ in range(10):
    li_list = lis = driver.find_elements_by_class_name('mn-cohort-view--list-item.ember-view')

    for li in li_list:
        div = li.find_element_by_tag_name('div')

        if 'you may know' in div.text:
            print(div.text)
            ppl_btn = div.find_element_by_tag_name('button')
            driver.execute_script("arguments[0].scrollIntoView();", ppl_btn)
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollTop-100)")
            time.sleep(2)
            ppl_btn.click()
            wait_random_time(4)

            ul = driver.find_element_by_class_name('discover-entity-list.ember-view')
            persons = ul.find_elements_by_tag_name('li')

            i = 0
            for person in persons:
                btn = person.find_element_by_class_name('discover-entity-type-card__bottom-container')\
                            .find_elements_by_tag_name('button')[-1]

                if btn.text == 'Connect':
                    i += 1
                    btn.click()
                    wait_random_time(1)

            print(f'Sent to {i} persons')
            dv = driver.find_element_by_class_name(
                'artdeco-modal.artdeco-modal--layer-default.discover-cohort-recommendations-modal')
            dv.find_element_by_tag_name('button').click()
    driver.refresh()
