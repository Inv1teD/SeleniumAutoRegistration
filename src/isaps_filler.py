import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def fill_Isaps_with_data(user):
    driver = webdriver.Chrome(
        executable_path='./chrome_driver/chromedriver.exe')
    url = "https://new.isaps.pl/Rekrutacja/Studia"
    print('Started driver!')
    try:
        driver.get(url=url)
        time.sleep(2)
        print('Opened web!')
        driver.find_element(By.XPATH, '/html/body/nav/div/div[2]/button').click()
        print('First action is success!')
        driver.find_element(By.XPATH, '/html/body/nav/div/div[2]/ul/li[3]/a').click()
        time.sleep(5)
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/section/section[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div[11]') \
            .click()
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/section/section[1]/div[2]/div/div[2]/div/div/div[3]/div[2]/button') \
            .click()
        time.sleep(2)
        driver.find_element(By.XPATH,'/html/body/div[1]/section/section[2]/div[2]/div/div/div/form/div/div/div[1]/div[1]/div[1]/div[1]/input')\
            .send_keys(user.name)
        driver.find_element(By.ID, 'PersonalData_LastName').send_keys(user.surname)
        driver.find_element(By.XPATH,'/html/body/div[1]/section/section[2]/div[2]/div/div/div/form/div/div/div[1]/div[1]/div[1]/div[4]/span/span/span[2]')\
            .click()
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[16]/div/div[3]/ul/li[2]').click()
        driver.find_element(By.ID, 'PersonalData_BirthDate').send_keys(user.birth_date)
        driver.find_element(By.ID, 'PersonalData_BirhPlace').send_keys(user.place_of_birth)
        driver.find_element(By.XPATH, '/html/body/div[1]/section/section[2]/div[2]/div/div/div/form/div/div/div[1]/div[1]/div[2]/div[3]/span/span/span[2]')\
            .click()
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[18]/div/span/input').send_keys('ukr')
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[18]/div/div[3]/ul/li').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/section/section[2]/div[2]/div/div/div/form/div/div/div['
                                      '1]/div[1]/div[2]/div[5]/div[1]/div/span')\
            .click()
        time.sleep(1)
        driver.find_element(By.ID, 'PersonalData_Passport').send_keys(user.pass_num)
        driver.find_element(By.XPATH, '/html/body/div[1]/section/section[2]/div[2]/div/div/div/form/div/div/div['
                                      '1]/div[1]/div[2]/div[5]/div[2]/div[2]/span/span/span[2]')\
            .click()
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[19]/div/span/input').send_keys('ukr')
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[19]/div/div[3]/ul/li').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/section/section[2]/div[2]/div/div/div/form/div/div/div[1]/div[1]/div['
                            '2]/div[5]/div[3]/span/span/span[2]')\
            .click()
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[20]/div/span/input').send_keys('ukr')
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[20]/div/div[3]/ul/li').click()
        driver.find_element(By.ID, 'PersonalData_PrivateEmail').send_keys(user.mail)
        driver.find_element(By.ID, 'PersonalData_CellPhone').send_keys(user.phone_num)
        print('First page filled! Going next one!')
        driver.find_element(By.XPATH, '/html/body/div[1]/section/section[2]/div[2]/div/div/div/form/div/div/div['
                                      '1]/div[2]/button[2]')\
            .click()
        # -----Adress
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/section/section[2]/div[2]/div/div/div/form/div/div/div['
                                      '2]/div[1]/div[''1]/span/span/span[2]')\
            .click()
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[21]/div/span/input').send_keys('ukr')
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[21]/div/div[3]/ul/li').click()
        time.sleep(1)
        driver.find_element(By.ID, 'PersonalData_City').send_keys(user.city)
        if user.city_or_village == 0:
            driver.find_element(By.XPATH, '/html/body/div[1]/section/section[2]/div[2]/div/div/div/form/div/div/div['
                                          '2]/div[1]/div[4]/label[1]')\
                .click()
        else:
            driver.find_element(By.XPATH, '/html/body/div[1]/section/section[2]/div[2]/div/div/div/form/div/div/div['
                                          '2]/div[1]/div[4]/label[2]')\
                .click()
        driver.find_element(By.ID, 'PersonalData_Street').send_keys(user.street)
        driver.find_element(By.ID, 'PersonalData_HouseNo').send_keys(user.house_num)
        driver.find_element(By.ID, 'PersonalData_FlatNo').send_keys(user.flat_num)
        driver.find_element(By.ID, 'PersonalData_ZipCode').send_keys(user.post_index)
        driver.find_element(By.ID, 'PersonalData_PostOffice').send_keys('-')
        print('Second page filled! Going next one!')
        driver.find_element(By.ID, 'Next2').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/section/section[2]/div[2]/div/div/div/form/div/div/div['
                                      '3]/div[1]/div[1]/span/span[2]/span/span[2]')\
            .click()
        time.sleep(1)
        print('Third page filled! Going next one!')
        driver.find_element(By.ID, 'Next5').click()
        print('Fourth page filled! Going next one!')
        driver.find_element(By.ID, 'Password').send_keys(user.password)
        driver.find_element(By.ID, 'Password2').send_keys(user.password)
        driver.find_element(By.XPATH, '/html/body/div[1]/section/section[2]/div[2]/div/div/div/form/div/div/div['
                                      '4]/div[3]/p[1]/input')\
            .click()
        driver.find_element(By.XPATH, '/html/body/div[1]/section/section[2]/div[2]/div/div/div/form/div/div/div['
                                      '4]/div[3]/p[2]/input')\
            .click()
        print('Finished!\nSaving data to txt file!')
        # driver.find_element(By.XPATH, '').click() ##Final Confirm!
        user.save_data(user)
        print("User's data saved!")
        time.sleep(30)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def main():
    fill_Isaps_with_data()


if __name__ == '__main__':
    main()
