import discord
import requests
from bs4 import BeautifulSoup

# Webページを取得して解析する



# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'ODk4MDc5OTQ1MzMzNTU1MjQx.YWfAIA._CoA_44Yp7Qzb0Yu_nJKeZzgzzM'

# 接続に必要なオブジェクトを生成
client = discord.Client()
# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
   

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    if message.content == 'DH1':
        session = '1'
        sessionurl = 'https://fortnitetracker.com/events/epicgames_S18_DuosHypeCup_ASIA?window=S18_DuosHypeCup_ASIA_Event' + session
              
        print(sessionurl)
        
    elif message.content == 'DH2':
        session = '2'
        sessionurl = 'https://fortnitetracker.com/events/epicgames_S18_DuosHypeCup_ASIA?window=S18_DuosHypeCup_ASIA_Event' + session
              
        print(sessionurl)
    
    elif message.content == 'DH3':
        session = '3'
        sessionurl = 'https://fortnitetracker.com/events/epicgames_S18_DuosHypeCup_ASIA?window=S18_DuosHypeCup_ASIA_Event' + session
              
        print(sessionurl)
    elif message.content == 'DH4':
        session = '4'
        sessionurl = 'https://fortnitetracker.com/events/epicgames_S18_DuosHypeCup_ASIA?window=S18_DuosHypeCup_ASIA_Event' + session
              
        print(sessionurl)
    elif message.content == 'DH5':
        session = '5'
        sessionurl = 'https://fortnitetracker.com/events/epicgames_S18_DuosHypeCup_ASIA?window=S18_DuosHypeCup_ASIA_Event' + session
              
        print(sessionurl)
    elif message.content == 'DH6':
        session = '6'
        sessionurl = 'https://fortnitetracker.com/events/epicgames_S18_DuosHypeCup_ASIA?window=S18_DuosHypeCup_ASIA_Event' + session
              
        print(sessionurl)
    elif message.content == 'DH7':
        session = '7'
        sessionurl = 'https://fortnitetracker.com/events/epicgames_S18_DuosHypeCup_ASIA?window=S18_DuosHypeCup_ASIA_Event' + session
              
        print(sessionurl)
    
    
       
   
    load_url = sessionurl
    html = requests.get(load_url)

    soup = BeautifulSoup(html.content, "html.parser")
    text = str(soup)
    text_find = text.find('"rank": 99')
    text_find2 = text_find - 9
    text_find3 = text_find - 12
    text2 = text[text_find3:text_find2]
    border = text.find('"rank": 50')
    border1 = border - 9
    border2 = border - 12
    text3 = text[border2:border1]
    top = text.find('"rank": 10')
    top1 = top - 9
    top2 = top -12
    text4 = text[top2:top1]
    if text2 == 'ody':
        text2 = '※未開催※'
    url = str(load_url)
    name1= url.find('Cup_ASIA_E')
    name2 = name1 - 8
    name3 = name1 + 8
    name = url[name2:name3]
    await message.channel.send(name)
    await message.channel.send('現在の99位のポイント:')
    await message.channel.send(      text2)
    await message.channel.send('現在の50位のポイント:')
    await message.channel.send(      text3)
    await message.channel.send('現在の10位のポイント:')
    await message.channel.send(      text4)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)