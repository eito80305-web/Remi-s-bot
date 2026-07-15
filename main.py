import discord
from discord.ext import commands
from flask import Flask
import threading
import random
import os

# --- Webサーバー機能（Render用） ---
app = Flask(__name__)
@app.route('/')
def home():
    return "I am alive!"

def run_web_server():
import discord
from discord.ext import commands
from flask import Flask
import threading
import random
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "I am alive!"

def run_web_server():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

# Discord Botの準備
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


class AuthView(discord.ui.View):
    @discord.ui.button(label="認証する", style=discord.ButtonStyle.primary)
    async def button_callback(self, interaction, button):
        # 演算子の選択
        op = random.choice(['+', '-', '*', '/'])
        if op == '/':
            b = random.randint(1, 10)
            a = b * random.randint(1, 10)
        else:
            a = random.randint(1, 50)
            b = random.randint(1, 50)
        
        question = f"{a} {op} {b}"
        answer = int(eval(question))
        
        await interaction.response.send_message(f"認証問題: {question} の答えは？", ephemeral=True)
        # ※答え合わせの処理はさらに拡張できるよ！

@bot.event
async def on_ready():
    print(f"Botがログインしました: {bot.user}")

# 起動
if __name__ == "__main__":
    t = threading.Thread(target=run_web_server)
    t.start()
    bot.run(os.environ['DISCORD_TOKEN']) 

# --- Discord Bot機能 ---
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

class AuthView(discord.ui.View):
    @discord.ui.button(label="認証する", style=discord.ButtonStyle.primary)
    async def button_callback(self, interaction, button):
        # 演算子の選択
        op = random.choice(['+', '-', '*', '/'])
        if op == '/':
            b = random.randint(1, 10)
            a = b * random.randint(1, 10)
        else:
            a = random.randint(1, 50)
            b = random.randint(1, 50)
        
        question = f"{a} {op} {b}"
        answer = int(eval(question))
        
        await interaction.response.send_message(f"認証問題: {question} の答えは？", ephemeral=True)
        # ※答え合わせの処理はさらに拡張できるよ！

@bot.event
async def on_ready():
    print(f"Botがログインしました: {bot.user}")

# 起動
if __name__ == "__main__":
    t = threading.Thread(target=run_web_server)
    t.start()
    bot.run(os.environ['DISCORD_TOKEN'])
