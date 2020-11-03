import os
from selenium import webdriver
import time
from platform import system as system_name

driver = webdriver.Chrome()


def clear():
    if system_name().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')


def login():
    print('Loading Instagram...')
    driver.get(
        'https://www.instagram.com/')
    time.sleep(1.5)
    print('Done')
    print('Logging in...')
    driver.find_element_by_xpath(
        '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input').send_keys(username)
    driver.find_element_by_xpath(
        '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').send_keys(password)
    driver.find_element_by_xpath(
        '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button').click()
    time.sleep(4)
    driver.find_element_by_xpath(
        '/html/body/div[1]/section/main/div/div/div/div/button').click()
    time.sleep(.5)
    driver.find_element_by_xpath(
        '/html/body/div[4]/div/div/div/div[3]/button[2]').click()


def addP(inv):
    driver.find_element_by_xpath(
        '/html/body/div[1]/section/main/section/div[3]/div[2]/div[1]/a/div').click()
    driver.refresh()
    time.sleep(2)
    print('Adding followers...')
    try:
        for i in range(1, int(inv)+1):
            driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/div[2]/div/div/div['+str(i)+']/div[3]/button').click()
            if i % 7 == 0:
                driver.refresh()
                time.sleep(2)
    except:
        print('Error')
        time.sleep(1)
    driver.find_element_by_xpath(
        '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a').click()
    print('Done')


def remF(inv):
    driver.find_element_by_xpath(
        '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img').click()
    driver.find_element_by_xpath(
        '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div').click()
    print('Removing followers...')
    time.sleep(1)
    driver.find_element_by_xpath(
        '/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()
    time.sleep(1)
    try:
        for i in range(1, int(inv)+1):
            driver.find_element_by_xpath(
                '/html/body/div[5]/div/div/div[2]/ul/div/li['+str(i)+']/div/div[3]/button').click()
            driver.find_element_by_xpath(
                '/html/body/div[6]/div/div/div/div[3]/button[1]').click()
            if i % 7 == 0:
                driver.refresh()
                time.sleep(1)
                driver.find_element_by_xpath(
                    '/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()
                time.sleep(.5)
    except:
        print('Error')
    time.sleep(.5)
    driver.find_element_by_xpath(
        '/html/body/div[5]/div/div/div[1]/div/div[2]/button').click()
    driver.find_element_by_xpath(
        '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a').click()


username = input('Instagram follower bot\n'+('-'*25)+'\nInstagram Username: ')
password = input('Instagram Password: ')
login()
while True:
    clear()
    print('Instagram follower bot\n'+('-'*25))
    chc = input('1: Add followers\n2: Remove followers\n0: Exit\nYour input: ')
    if chc == '1':
        num = input(
            'How many people do you want to add?\nNumber: ')
        addP(num)
    elif chc == '2':
        num = input(
            'How many people do you want to remove?\nNumber: ')
        remF(num)
    elif chc == '0':
        break
    else:
        print('Error, please enter 1 2 or 0')
        time.sleep(2)
driver.quit()
clear()
print('Program Done')

