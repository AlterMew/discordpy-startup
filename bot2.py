import discord
from discord.ext import commands
#pip install discord-buttons-plugin
from discord_buttons_plugin import *
#pip install requests
import requests
bot = commands.Bot(command_prefix = "m!")
buttons = ButtonsClient(bot)
TEXT="おはよう"
Emoji = "\N{SMILING FACE WITH OPEN MOUTH AND TIGHTLY-CLOSED EYES}"
FR = "JA"
EX = "EN"
flg = 0
hozon = " "
cnt = 0
@bot.event
async def on_ready():
	print("準備完了")
  
@buttons.click
async def button_1(ctx):
    await buttons.send(
            content = "", 
            channel = ctx.channel.id,
            components = [
                ActionRow([
                    Button(
                        label="日本語から英語", 
                        style=ButtonType().Primary, 
                        custom_id="button_3"
                    )
                ]),ActionRow([
                    Button(
                        label="日本語から中国語",
                        style=ButtonType().Primary,
                        custom_id="button_4"
                    )
                ]),ActionRow([
                    Button(
                        label="日本語からフランス語", 
                        style=ButtonType().Primary, 
                        custom_id="button_5"
                    )
                ]),
            ]
        )  
    await buttons.send(
            content = "", 
            channel = ctx.channel.id,
            components = [
                ActionRow([
                    Button(
                        label="英語から日本語", 
                        style=ButtonType().Danger, 
                        custom_id="button_6"
                    )
                ]),ActionRow([
                    Button(
                        label="中国語から日本語",
                        style=ButtonType().Danger,
                        custom_id="button_7"
                    )
                ]),ActionRow([
                    Button(
                        label="フランス語から日本語", 
                        style=ButtonType().Danger, 
                        custom_id="button_8"
                    )
                ]),
            ]
        )

    
@buttons.click
async def button_2(ctx):
	await ctx.reply("終了します", flags = MessageFlags().EPHEMERAL)
  
@buttons.click
async def button_3(ctx):
    global flg
    global FR
    global EX
    FR ='JA'
    EX ='EN'
    flg = 1
    await ctx.channel.send('パターン1')
@buttons.click
async def button_4(ctx):
    global flg
    global FR
    global EX
    FR ='JA'
    EX ='ZH'
    flg = 1
    await ctx.channel.send('パターン2')
@buttons.click
async def button_5(ctx):
    global flg
    global FR
    global EX
    FR ='JA'
    EX ='FR'
    flg = 1
    await ctx.channel.send('パターン3') 
@buttons.click
async def button_6(ctx):
    global flg
    global FR
    global EX
    FR ='EN'
    EX ='JA'
    flg = 1
    await ctx.channel.send('パターン4') 
@buttons.click
async def button_7(ctx):
    global flg
    global FR
    global EX
    FR ='ZH'
    EX ='JA'
    flg = 1
    await ctx.channel.send('パターン5') 
@buttons.click
async def button_8(ctx):
    global flg
    global FR
    global EX
    FR ='FR'
    EX ='JA'
    flg = 1
    await ctx.channel.send('パターン6')    
@bot.event

async def on_message(message):
    global flg
    global TEXT
    global hozon
    global cnt
    if flg == 1 :
        flg = 0
        await message.channel.send("翻訳する用語を入力してください") 
        cnt = 100
        
        return
    cnt = cnt + 1
    print(cnt)
    TEXT = message.content 
    if cnt == 101:            
        params = {
            "auth_key":"88af5bb1-1bd1-3a06-9354-9221474c3300:fx",
            "text": TEXT,
            "source_lang": FR,
            "target_lang": EX  
        }
        request = requests.post("https://api-free.deepl.com/v2/translate", data=params)
        result = request.json()
        await message.channel.send("翻訳結果:"+result["translations"][0]["text"])
        await message.channel.send("継続して翻訳しますか?")
        await buttons.send(
		channel = message.channel.id,
		components = [
			ActionRow([
				Button(
					label="翻訳する", 
					style=ButtonType().Primary, 
					custom_id="button_1"
				)
			]),ActionRow([
				Button(
					label="翻訳しない",
					style=ButtonType().Danger,
					custom_id="button_2"
				)
			]),
		]
	)    
        cnt = 0
    await bot.process_commands(message)
    # メッセージ送信者がBotだった場合は無視する
    #if message.author.bot:
        #return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == 'ex1':
        cnt = 0
        TEXT = "おやすみ"
    if message.content == 'ex2':
        params = {
            "auth_key":"88af5bb1-1bd1-3a06-9354-9221474c3300:fx",
            "text": TEXT,
            "source_lang": 'JA', 
            "target_lang": 'EN'  
        }
        request = requests.post("https://api-free.deepl.com/v2/translate", data=params)
        result = request.json()
        await message.channel.send("翻訳結果:"+result["translations"][0]["text"])



@bot.command()
async def create(ctx):
	await buttons.send(
		content = "翻訳する言語を選択してください", 
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(
					label="翻訳する", 
					style=ButtonType().Primary, 
					custom_id="button_1"
				)
			]),ActionRow([
				Button(
					label="翻訳しない",
					style=ButtonType().Danger,
					custom_id="button_2"
				)
			]),
		]
	)
    
@bot.command()
async def frjp(ctx):
	await buttons.send(
		content = "", 
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(
					label="日本語から英語", 
					style=ButtonType().Primary, 
					custom_id="button_3"
				)
			]),ActionRow([
				Button(
					label="日本語から中国語",
					style=ButtonType().Primary,
					custom_id="button_4"
				)
			]),ActionRow([
				Button(
					label="日本語からフランス語", 
					style=ButtonType().Primary, 
					custom_id="button_5"
				)
            ]),
		]
	)
    
@bot.command()
async def exjp(ctx):
	await buttons.send(
		content = "", 
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(
					label="英語から日本語", 
					style=ButtonType().Danger, 
					custom_id="button_6"
				)
			]),ActionRow([
				Button(
					label="中国語から日本語",
					style=ButtonType().Danger,
					custom_id="button_7"
				)
			]),ActionRow([
				Button(
					label="フランス語から日本語", 
					style=ButtonType().Danger, 
					custom_id="button_8"
				)
            ]),
		]
	)

bot.run('MTAxMzE0ODIwMjk2NDM2OTQwOQ.G77AVt.Zru8mOWmGf-AzL-N4vp00lyA0BkfZNtNRcoBvU')