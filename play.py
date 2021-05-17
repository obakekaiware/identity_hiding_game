import os
import random
import PySimpleGUI as sg


def create_massages(word, num_players):
    messages = []
    for _ in range(num_players - 1):
        messages.append('あなたは村人です。')
    messages.append(f'あなたはインサイダーです。\nお題は「{word}」です。')
    random.shuffle(messages)
    return messages


def main():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [
        [sg.Text('お題を入力してください')],
        [sg.InputText()],
        [sg.Text('マスター以外の人数を入力してください（半角数字）')]
        [sg.InputText()],
        [sg.Button('OK')]
    ]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        word = values[0]
        num_players = int(values[1])
        print(values)
        if event == sg.WIN_CLOSED or event == 'OK':
            # if user closes window or clicks cancel
            break
    window.close()

    messages = create_massages(word, num_players)

    os.makedirs('これを配布', exist_ok=True)
    for player_id, message in enumerate(messages):
        with open(f'これを配布/{player_id}.txt', 'w') as file:
            file.write(message)


if __name__ == "__main__":
    main()
