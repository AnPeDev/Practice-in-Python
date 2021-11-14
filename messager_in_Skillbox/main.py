# + Database
# send = put message into database
# get messages

db = []


def send_message(name, text):
    message = {
        'name': name,
        'text': text,
        'time': '12 jan 2021 16:29:31'  # TODO
    }
    db.append(message)


send_message('Nick', 'Hello, Ivan!')
send_message('Ivan', 'Hello, Nick!')
send_message('Nick', '1+1?')
send_message('Nick', '=2')
