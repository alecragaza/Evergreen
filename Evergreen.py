import webbrowser
import time
import os
import tkinter
import datetime
from tkinter import messagebox, END

from selenium.webdriver import ActionChains
from tkcalendar import Calendar, DateEntry
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def generate_report():
    vesta_username = "madelainejqui@521"
    vesta_password = "Jan2023$"
    current_date = datetime.datetime.now()

    driver = webdriver.Chrome()
    url = "https://vestaevv.com/"
    driver.get(url)
    driver.maximize_window()

    print("Processing has already started")
    action = ActionChains(driver)
    # customerLogin = driver.find_element(By.ID, "menu-item-1939")
    # time.sleep(5)
    action.move_to_element(driver.find_element(By.ID, "menu-item-1939")).perform()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//li[@id='menu-item-1941']/a[text()='Vesta EVV']"))).click()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "UserNameInput"))).send_keys(vesta_username)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "PasswordInput"))).send_keys(vesta_password)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@id='LoginButton']"))).click()
    WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.LINK_TEXT, "Validate Later"))).click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'title') and text() = 'Reports']"))).click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'title') and text() = 'Management Reports']"))).click()
    action.move_to_element(driver.find_element(By.XPATH,"//span[contains(@class, 'caption-desc') and text() = 'Member / Service Attendant Visit Log']")).click().perform()
    time.sleep(20)
    if current_date.day in range(15, 28):
        



def login_validation():
    system_username = "admin"
    system_password = "admin"
    uname = username.get()
    pword = password.get()

    if uname == system_username and pword == system_password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in")
        login_window.destroy()
        generate_report()
    else:
        if uname == "" and pword == "":
            messagebox.showinfo(title="Error", message="Please enter username and password")
        else:
            messagebox.showerror(title="Error", message="Username and Password does not match")
            username.set("")
            password.set("")


def login_form():
    global login_window
    login_window = tkinter.Tk()
    login_window.title("Evergreen Login")
    login_window.geometry("300x300")
    login_window.configure(bg="#F5F5F5")

    global username
    global password
    username = tkinter.StringVar()
    password = tkinter.StringVar()

    login_frame = tkinter.Frame(bg="#F5F5F5")
    login_label = tkinter.Label(login_frame, text="Login", font=("Montserrat", 16))
    username_label = tkinter.Label(login_frame, text="Username: ", font=("Montserrat", 12))
    username_entry = tkinter.Entry(login_frame, font=("Montserrat", 12), textvariable=username)
    password_label = tkinter.Label(login_frame, text="Password: ", font=("Montserrat", 12))
    password_entry = tkinter.Entry(login_frame, show="*", font=("Montserrat", 12), textvariable=password)
    login_button = tkinter.Button(login_frame, text="Login", command=login_validation, bg="#0B1F65", fg="#F5F5F5",font=("Montserrat", 12))

    login_label.grid(row=0, column=0, columnspan=2, pady=40)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1, pady=5)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1, pady=5)
    login_button.grid(row=3, column=0, columnspan=2, pady=20)

    login_frame.pack()
    login_window.mainloop()


def main():
    login_form()


if __name__ == "__main__":
    main()
