import discord
from discord import app_commands
from discord.ext import commands
from flask import Flask
import threading
import random
import os

# --- 設定 ---
GUILD_ID = 1523313663107272765
ROLE_ID = 1523313663107272770

# --- Webサーバー機能（Render用） ---
app = Flask(__name__)

@app.route('/')
def home():
    return "I am alive!"

def run_web_server():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

# --- Discord Bot機能 ---
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

class AuthView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="認証する", style=discord.ButtonStyle.primary)
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        op = random.choice(['+', '-', '*', '/'])
        if op == '/':
            b = random.randint(1, 10)
            a = b * random.randint(1, 10)
        else:
            a = random.randint(1, 50)
            b = random.randint(1, 50)
        
        question = f"{a} {op} {b}"
        # 実際にはここでModal等を使って答えを入力してもらう流れになります
        await interaction.response.send_message(f"認証問題: {question} の答えを入力してください（※現在は表示のみ）", ephemeral=True)

@bot.event
async def on_ready():
    # コマンド同期
    guild = discord.Object(id=GUILD_ID)
    bot.tree.copy_global_to(guild=guild)
    await bot.tree.sync(guild=guild)
    print(f"Botがログインし、コマンドを同期しました: {bot.user}")

# スラッシュコマンド（パネル呼び出し用）
@bot.tree.command(name="auth_panel", description="認証パネルを表示します")
async def auth_panel(interaction: discord.Interaction):
    await interaction.response.send_message("下のボタンを押して認証を開始してください。", view=AuthView())

# --- 起動 ---
if __name__ == "__main__":
    # Webサーバー起動
    t = threading.Thread(target=run_web_server)
    t.start()
    # Bot起動
    bot.run(os.environ['DISCORD_TOKEN'])
