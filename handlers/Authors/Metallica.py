import aiogram.dispatcher.filters as f
from bs4 import BeautifulSoup
import requests
from menus.Menus import *

#region Metallica Originals Handlers

@dp.callback_query_handler(f.Text(startswith = 'metallica'))
async def send_texts_menu(callback: types.CallbackQuery):
    await callback.message.answer('choose the song', reply_markup = lyricsMenuMetallica)
@dp.callback_query_handler(f.Text(startswith = 'Metallica-Master-Puppets'))
async def send_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f'*Master Of Puppets*:\n```{lyrics}```\nЕсли ты не слышал эту песню, [see that](https://www.youtube.com/watch?v=E0ozmU9cJDg)', parse_mode = 'Markdown',disable_web_page_preview = True)
@dp.callback_query_handler(f.Text(startswith = 'enter-sandman'))
async def send_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/metallica-{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f'''*Enter Sandman:*\n```{lyrics}```\n*Если ты не слышал эту песню*, [смотри тут](https://www.youtube.com/watch?v=CD-E-LDc384)''', parse_mode = 'Markdown',disable_web_page_preview = True)
@dp.callback_query_handler(f.Text(startswith = 'Metallica-Nothing-else-matters'))
async def Ssend_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f''''*Nothing Else Matters*\n```{lyrics}```\n*Если ты не слышал эту песню*, [see that](https://www.youtube.com/watch?v=tAGnKpE4NCI) ''', parse_mode = 'Markdown',disable_web_page_preview = True)
@dp.callback_query_handler(f.Text(startswith = 'unforgiven'))
async def send_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/pantera-{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f'''*The Unforgiven*\n```{lyrics}```\n*Если ты не слышал эту песню*, [see that](hhttps://www.youtube.com/watch?v=Ckom3gf57YwQ)''', parse_mode = 'Markdown',disable_web_page_preview = True)
@dp.callback_query_handler(f.Text(startswith = 'Metallica-Unforgiven-2'))
async def send_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f'''*1The Unforgiven 2*\n```{lyrics}```\n*Если ты не слышал эту песню*, [see that](https://www.youtube.com/watch?v=5bt7kAVxKfs)''', parse_mode = 'Markdown',disable_web_page_preview = True)
@dp.callback_query_handler(f.Text(startswith = 'Metallica-Unforgiven-III'))
async def send_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f'''*The Unforgiven 3*\n```{lyrics}```\n*Если ты не слышал эту песню*, [see that](https://www.youtube.com/watch?v=VD4PYP7WUCA)''', parse_mode = 'Markdown',disable_web_page_preview = True)
@dp.callback_query_handler(f.Text(startswith = 'and-justice-all'))
async def send_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/pantera-{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f'''*..And Justice For All*\n```{lyrics}```\n*Если ты не слышал эту песню*, [see that](https://www.youtube.com/watch?v=2lgGJRWUIvM''', parse_mode = 'Markdown',disable_web_page_preview = True)
@dp.callback_query_handler(f.Text(startswith = 'Metallica-One'))
async def send_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f'''*A New Level*\n```{lyrics}```\n*Если ты не слышал эту песню*, [see that](https://www.youtube.com/watch?v=WM8bTdBs-cw''', parse_mode = 'Markdown',disable_web_page_preview = True)

#endregion