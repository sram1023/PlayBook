# import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


def login():
    # email for sign in
    email = WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="ctl00_MainContent_InputLogin"]'))
    )
    email.send_keys('venkat97ram@gmail.com')

    # password for sign in
    # time.sleep(1)

    password = WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="ctl00_MainContent_InputPassword"]'))
    )
    password.send_keys('Qwert123!')
    WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_MainContent_btnLogin"]'))).click()
    # time.sleep(3)

    # password_click = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContent_btnLogin"]')
    # password_click.click()

    print('logged in')


def badminton():
    try:
        badminton = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH,
                                            '//*[@id="ctl00_MainContent__advanceSearchResultsUserControl_Activities_ctrl0_lnkActivitySelect_lg"]')))
        badminton.click()
        print('badmiton selected')
    except:
        home = WebDriverWait(driver, 2).until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ctl18_homeli"]/a')))
        home.click()
        badminton = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH,
                                            '//*[@id="ctl00_MainContent__advanceSearchResultsUserControl_Activities_ctrl0_lnkActivitySelect_lg"]')))
        badminton.click()
        print('badmiton selected')


def booking(court):
    booking_time = 2
    court_no = court
    booking_date = 12
    for x in range(booking_date):
        next_day = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="ctl00_MainContent_Button2"]')))
        next_day.click()
    print('date selected')
    try:
        timing = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located(
                (By.XPATH, '//*[@id="ctl00_MainContent_grdResourceView"]/tbody/tr[' + str(booking_time) + ']/td[' + str(
                    court_no) + ']/input')))
        timing.click()
        print('timing selected')
        for y in range(3):
            members = WebDriverWait(driver, 30).until(
                ec.presence_of_element_located(
                    (By.XPATH,
                     '//*[@id="Wrapper"]/div[1]/div[2]/div[5]/div[2]/span[3]/button')))
            members.click()
            print('members added')
        book_button = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located(
                (By.XPATH, '//*[@id="ctl00_MainContent_ActivityListView_ctrl0_btnBook"]')))
        book_button.click()

        confirm_boooking = WebDriverWait(driver, 30).until(
            ec.presence_of_element_located(
                (By.XPATH, '//*[@id="ctl00_MainContent_btnBasket"]')))
        confirm_boooking.click()
        print('booking confirm')
        return 'Booked'
    except:
        return 'Not Booked'


def main():
    login()
    # for count_no in range(1, 3):
    #     badminton()
    #     status = booking(count_no)
    #     print('Court ' + str(count_no) + ' ' + status)
    # print('Happy Playing')


if __name__ == "__main__":
    browser = "localChrome"
    if browser == "remoteChrome":
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options)
    else:
        driver = webdriver.Chrome()
    driver.get(
        'https://bookings.mytimeleisure.co.uk/connectleisure/mrmlogin.aspx')
    driver.maximize_window()
    print('Browser launch')
    main()
