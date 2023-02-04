from selenium import webdriver
from urllib.request import urlretrieve
from gtts import *

print('%%%%%%%%%%%%%&&')
print('%%%%%%%%%%%%%%%&&')
print('%%%%.,.,.,.,%%%%%&')
print('%%%%.,.,.,.,%%%%%&')
print('%%%%.,.,.,.,%%%%%&')
print('%%%%%%%%%%%%%%%%%&')
print('%%%%%%%%%%%%%%%%%&                     Made by Freddy!')
print('%%%%%%%%%%%%%%%%%&')
print('%%%%---------%%%%&')
print('%%%%---------%%%%&')
print('%%%%---------%%%%&')
print('%%%%%%%%%%%%%%%%%&')
print('%%%%%%%%%%%%%%%%%&')

while True:
    input1 = input('Task: ')
    if input1 == 'help':
        print('         help: this command;-;        ')
        print('         playvideo: You type the link after this command incluing https        ')
        print('         downloadfile: Download the file you want, After typing this command you type the link incluing https        ')
        print('         exit: Exit the app;-;        ')
        print('         googleaudio: Record a google translator audio, but requires a document text       ')
    if input1 == 'playvideo':
        link = input('Link: ')
        chrome = webdriver.Chrome()
        chrome.get(link)
    if input1 == 'downloadfile':
        linkdown = input('Link: ')
        name = input('Name: ')
        local = input('Local: ')
        def download():
            urlretrieve(linkdown, name)
        download(local)
    if input1 == 'exit':
        break
    if input1 == '':
        print('Sorry, type one commad? or use help?')
    if input1 == 'googleaudio':
        talk = input('Local from document text: ')
        name1 = input('Name: ')
        with open(talk,'r') as audiogoogle:
            for audiomaker in audiogoogle:
                audio = gTTS(audiomaker, lang='en-US')
                audio.save(f'{name1}.mp3')