import PySimpleGUI as sg
from words import wordsList
import random

sg.theme('dark grey 9')

layout = [
        [sg.Text('')],
        [sg.Text('Type in the text box below')],
        [sg.Input(key='-IN-')],
        [sg.Text(size = (40,1), key = '-OUTPUT-')],
        [sg.Button('Output Text'), sg.Button('Quit'), sg.Button('random word')]
]


window = sg.Window('PySimpleGUI Practice', layout) # Part 3 - Window Defintion

while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if event == 'Ok':
        window['-OUTPUT-'].update(values['-IN-'])
    if event == 'random word':
                window['-OUTPUT-'].update(random.choice(wordsList))
window.close()
