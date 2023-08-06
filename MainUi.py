import PySimpleGUI as sg
import Follow
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

font = ("iransans", 11)
sg.theme('LightGrey1')


layout = [
    [
        sg.Text('Virasty Social Bot(v1)', expand_x=True, justification='left')],
    [sg.Text('Phone Number :'), sg.InputText(
        expand_x=True, change_submits=True, key='-PN-',)],
    [sg.Text('Password :'), sg.InputText(
        expand_x=True, change_submits=True, key='-PS-',)],
    [sg.Text('Target User :'), sg.InputText(
        expand_x=True, change_submits=True, key='-TU-',)],
    [sg.HorizontalSeparator(color='#DAE0E6')],

    [sg.Button('Start session'), sg.Button('Close app')],
    [sg.Text('Developed By Amirreza Khezerlou, Khoy',
             expand_x=True, justification='left')]
]


window = sg.Window('Virasti Auto Follow Pro v1', layout, font=font)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close app':
        break
    if event == 'Start session':
        if (values['-PN-'] != '' and values['-PS-'] != '' and values['-TU-'] != ''):
            bot = webdriver.Chrome(executable_path='chromedriver.exe')
            url = 'https://virasty.com/login/mobile'
            Follow.login(bot, url, values['-PN-'],
                         values['-PS-'], values['-TU-'])
        else:
            sg.popup('Empty Feilds Coused Error !')


window.close()
