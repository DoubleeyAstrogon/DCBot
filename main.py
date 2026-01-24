import discord
from discord import app_commands
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

class selection(discord.ui.View):
    @discord.ui.select(
        placeholder="Wybierz opcję...",
        min_values=1,  # minimalna liczba wybranych opcji
        max_values=2,  # maksymalna liczba wybranych opcji
        options=[
            discord.SelectOption(label="Opcja 1", description="To jest pierwsza opcja", emoji="🍎"),
            discord.SelectOption(label="Opcja 2", description="To jest druga opcja", emoji="🍌"),
            discord.SelectOption(label="Opcja 3", description="To jest trzecia opcja", emoji="🍇"),
        ]
    )
    async def select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        selected = ", ".join(select.values)
        await interaction.response.send_message(f'Wybrałeś: {selected}', ephemeral=True)

class catbutton(discord.ui.View):
    @discord.ui.button(
        style=discord.ButtonStyle.primary,
        label="cats!!",
        emoji="🍎"
    )
    async def callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("one cat... two cats... three cats...", ephemeral=True)

class otherCatButton(discord.ui.View):
    @discord.ui.button(
        style=discord.ButtonStyle.danger,
        label="cats!!!!!!!!!!!!!!!!!!!1 ",
    )
    async def callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("other cat moments!!!!!!!!!!!!!!!", ephemeral=True)

@bot.command()
async def wybierz(ctx):
    view = selection()
    await ctx.send(view=view)

@bot.command()
async def catthing(ctx):
    view = catbutton()
    await ctx.send(view=view)

@bot.command()
async def cats(ctx):
    view = otherCatButton()
    await ctx.send(view=view)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
