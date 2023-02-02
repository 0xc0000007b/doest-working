import aiogram.dispatcher.filters as f
from bs4 import BeautifulSoup
import requests
from menus.Menus import *

#region Pantera Originals Handlers

@dp.callback_query_handler(f.Text(startswith = 'pantera'))
async def send_texts_menu(callback: types.CallbackQuery):
    await callback.message.answer('choose the song', reply_markup = lyricsMenuPantera)
@dp.callback_query_handler(f.Text(startswith = 'walk'))
async def send_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/pantera-{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f'*Walk*:\n```{lyrics}```\nЕсли ты не слышал эту песню, [see that](https://www.youtube.com/watch?v=TW9uj83Vq-0)', parse_mode = 'Markdown',disable_web_page_preview = True)
@dp.callback_query_handler(f.Text(startswith = 'im-broken'))
async def send_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/pantera-{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f'''*I'm Broken:*\n```{lyrics}```\n*Если ты не слышал эту песню*, [смотри тут](https://www.youtube.com/watch?v=2-V8kYT1pvE)''', parse_mode = 'Markdown',disable_web_page_preview = True)
@dp.callback_query_handler(f.Text(startswith = '10s'))
async def send_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/pantera-{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')

    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f''''*10's*\n```{lyrics}```\n*Если ты не слышал эту песню*, [see that](https://www.youtube.com/watch?v=XV_D1Y_YHlA) ''', parse_mode = 'Markdown',disable_web_page_preview = True)
@dp.callback_query_handler(f.Text(startswith = '13-steps-nowhere'))
async def send_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/pantera-{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f'''*13 Steps Nowhere*\n```{lyrics}```\n*Если ты не слышал эту песню*, [see that](https://www.youtube.com/watch?v=g9jQmvynpTQ)''', parse_mode = 'Markdown',disable_web_page_preview = True)
@dp.callback_query_handler(f.Text(startswith = '25-years'))
async def send_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/pantera-{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f'''*13 Steps Nowhere*\n```{lyrics}```\n*Если ты не слышал эту песню*, [see that](https://www.youtube.com/watch?v=g9jQmvynpTQ)''', parse_mode = 'Markdown',disable_web_page_preview = True)
@dp.callback_query_handler(f.Text(startswith = '25-years'))
async def send_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/pantera-{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f'''*25 Years*\n```{lyrics}```\n*Если ты не слышал эту песню*, [see that](https://www.youtube.com/watch?v=F3AkTh9RZqQ)''', parse_mode = 'Markdown',disable_web_page_preview = True)
@dp.callback_query_handler(f.Text(startswith = '5-minutes-alone'))
async def send_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/pantera-{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f'''*5 Minutes Alone*\n```{lyrics}```\n*Если ты не слышал эту песню*, [see that](https://www.youtube.com/watch?v=7m7njvwB-Ks)''', parse_mode = 'Markdown',disable_web_page_preview = True)
@dp.callback_query_handler(f.Text(startswith = 'a-new-level'))
async def send_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/pantera-{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f'''*A New Level*\n```{lyrics}```\n*Если ты не слышал эту песню*, [see that](https://www.youtube.com/watch?v=li91V6m_OR0)''', parse_mode = 'Markdown',disable_web_page_preview = True)
@dp.callback_query_handler(f.Text(startswith = 'all-over-tonight'))
async def send_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/pantera-{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f'''*All Over Tonight*\n```{lyrics}```\n*Если ты не слышал эту песню*, [see that](https://www.youtube.com/watch?v=l2kwZeuP5ks)''', parse_mode = 'Markdown',disable_web_page_preview = True)
@dp.callback_query_handler(f.Text(startswith = 'avoid-light'))
async def send_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/pantera-{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f'''*Avoid The Light*\n```{lyrics}```\n*Если ты не слышал эту песню*, [see that](https://www.youtube.com/watch?v=SRObGNr2UWQ)''', parse_mode = 'Markdown',disable_web_page_preview = True)
@dp.callback_query_handler(f.Text(startswith = 'becoming'))
async def send_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/pantera-{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f'''*Becoming*\n```{lyrics}```\n*Если ты не слышал эту песню*, [see that](https://www.youtube.com/watch?v=SlG4kSRleTs)''', parse_mode = 'Markdown',disable_web_page_preview = True)
@dp.callback_query_handler(f.Text(startswith = 'biggest-part-me'))
async def send_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/pantera-{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f'''*Becoming*\n```{lyrics}```\n*Если ты не слышал эту песню*, [see that](https://www.youtube.com/watch?v=SRObGNr2UWQ)''', parse_mode = 'Markdown',disable_web_page_preview = True)
@dp.callback_query_handler(f.Text(startswith = 'burnnn'))
async def send_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/pantera-{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f'''*Burnnn*\n```{lyrics}```\n*Если ты не слышал эту песню*, [see that](https://www.youtube.com/watch?v=gAjnIuuY4Ks)''', parse_mode = 'Markdown',disable_web_page_preview = True)
@dp.callback_query_handler(f.Text(startswith = 'demons-be-driven'))
async def send_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/pantera-{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f'''*By Demons Be Driven*\n```{lyrics}```\n*Если ты не слышал эту песню*, [see that](https://www.youtube.com/watch?v=F0mbRWRa0Rg)''', parse_mode = 'Markdown',disable_web_page_preview = True)
@dp.callback_query_handler(f.Text(startswith = 'cat-scratch-fever'))
async def send_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/pantera-{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f'''*Cat Scratch Fever*\n```{lyrics}```\n*Если ты не слышал эту песню*, [see that](https://www.youtube.com/watch?v=5pncni-ZB2s)''', parse_mode = 'Markdown',disable_web_page_preview = True)
@dp.callback_query_handler(f.Text(startswith = 'clash-reality'))
async def send_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/pantera-{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f'''*Clash With Reality*\n```{lyrics}```\n*Если ты не слышал эту песню*, [see that](https://www.youtube.com/watch?v=iD0kELk5AVQ)''', parse_mode = 'Markdown',disable_web_page_preview = True)
@dp.callback_query_handler(f.Text(startswith = 'come-eyes'))
async def send_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/pantera-{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f'''*Come-on Eyes*\n```{lyrics}```\n*Если ты не слышал эту песню*, [see that](https://www.youtube.com/watch?v=FiT6sW7fFYI)''', parse_mode = 'Markdown',disable_web_page_preview = True)
@dp.callback_query_handler(f.Text(startswith = 'dgttm'))
async def send_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/pantera-{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f'''*DGTTM*\n```{lyrics}```\n*Если ты не слышал эту песню*, [see that](https://www.youtube.com/watch?v=P2xwnL3Gc-Y)''', parse_mode = 'Markdown',disable_web_page_preview = True)
@dp.callback_query_handler(f.Text(startswith = 'cemetery-gates'))
async def send_choosed_text(callback:types.CallbackQuery):
    songName = callback.data
    url = f'https://lyricstranslate.com/en/pantera-{songName}-lyrics.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    lyrics = ''
    for row in soup.find_all('div', {'class': 'par'}):
        lyrics += row.text
    await callback.message.answer(f'''*Cemetery Gates*\n```{lyrics}```\n*Если ты не слышал эту песню*, [see that](https://www.youtube.com/watch?v=RVMvART9kb8)''', parse_mode = 'Markdown',disable_web_page_preview = True)

#endregion