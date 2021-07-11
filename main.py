import openai
from gtts import gTTS
import pyglet
import os
from time import sleep

openai.api_key = ""
completion = openai.Completion()
intro = "I am new and improved Beth!"
start_chat_log = '''Human: Good Day?
AI: Yes
'''


def say(words):
    tts = gTTS(words, lang='en-us')
    filename = 'temp.mp3'
    tts.save(filename)
    music = pyglet.media.load(filename, streaming=False)
    music.play()
    sleep(music.duration)
    os.remove(filename)


def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    prompt = f'{chat_log}Human: {question}\nAI:'
    result = completion.create(
        prompt=prompt, engine="davinci", stop=['\nHuman'], temperature=0.3,
        max_tokens=60,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0)
    answer = result.choices[0].text.strip()
    return answer


def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    return f'{chat_log}Human: {question}\nAI: {answer}\n'


log = None
if __name__ == '__main__':
    say(intro)
    while True:
        query = input('Human: ')
        if query == 'q':
            break
        response = ask(query, log)
        say(response)
        print('AI: ', response)
        log = append_interaction_to_chat_log(query, response, log)
