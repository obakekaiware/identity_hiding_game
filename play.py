import os
import sys
import datetime
import random
import PySimpleGUI as sg


def create_massages(word, num_players):
    messages = []
    for _ in range(num_players - 1):
        messages.append('あなたは村人です。')
    messages.append(f'あなたはインサイダーです。\nお題は「{word}」です。')
    random.shuffle(messages)
    return messages


def input_theme_and_num_players():
    layout = [
        [sg.Text('お題を入力してください')],
        [sg.InputText()],
        [sg.Text('マスター以外の人数を入力してください（半角数字）')],
        [sg.InputText()],
        [sg.Button('OK')]
    ]
    # Create the Window
    window = sg.Window('', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == 'OK':
            word = values[0]
            num_players = int(values[1])
            break
        if event == sg.WIN_CLOSED:
            sys.exit()
    window.close()

    return word, num_players


def input_player_names(num_players):
    layout = [
        [sg.Text('マスター以外の名前を入力してください。')],
    ]
    for _ in range(num_players):
        layout.append([sg.InputText()])
    layout.append([sg.Button('OK')])

    # Create the Window
    window = sg.Window('', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == 'OK':
            names = list(values.values())
            break
        if event == sg.WIN_CLOSED:
            sys.exit()
    window.close()

    return names


def main():
    sg.theme('DarkAmber')   # Add a touch of color

    word, num_players = input_theme_and_num_players()
    messages = create_massages(word, num_players)
    names = input_player_names(num_players)

    now = datetime.datetime.today()
    now = (
        f'{now.year}{now.month:02}{now.day:02}'
        f'_{now.hour:02}{now.minute:02}'
    )
    output_dir = f'results/{now}'
    os.makedirs(output_dir, exist_ok=True)
    for name, message in zip(names, messages):
        output_path = os.path.join(output_dir, f'{name}.txt')
        with open(output_path, 'w') as file:
            file.write(message)


if __name__ == "__main__":
    main()
