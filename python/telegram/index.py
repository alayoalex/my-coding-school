import json
import os

# encoding='ISO-8859-1'


def openfile():
    with open('result.json', 'r', encoding='ISO-8859-1') as result:
        return json.loads(result.read())


def count_messages():
    data = openfile()
    count = 0
    for message in data['messages']:
        if message['type'] == 'message':
            count += 1
    return count


def get_messages():
    data = openfile()
    m = []
    for message in data['messages']:
        if message['type'] == 'message':
            m.append(message['text'])
    return m


def show_messages():
    messages = get_messages()
    for m in messages:
        print(m)


if __name__ == '__main__':
    show_messages()
