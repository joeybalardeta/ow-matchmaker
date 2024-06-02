from core import utils
import discord
from discord import app_commands

class Bot:
    def __init__(self):
        self.intents = discord.Intents.default()
        self.client = discord.Client(intents = self.intents)
        self.tree = app_commands.CommandTree(self.client)


    def register_commands(self):
        @self.tree.command(
            name = "help",
            description = "Get a list of all supported commands."
        )
        async def help(interaction):
            await interaction.response.send_message("```Available commands:\n- /help\n- /add <username>\n- /remove <username>```")
        
        @self.tree.command(
            name = "add",
            description = "Add a user to the player pool."
        )
        @app_commands.describe(player = "The user to add to the player pool.")
        async def add_player(interaction, player: str):
            await interaction.response.send_message("Adding %s to player pool." % (player))

        @self.tree.command(
            name = "remove",
            description = "Remove a user from the player pool."
        )
        @app_commands.describe(player = "The user to remove from the player pool.")
        async def remove_player(interaction: discord.Interaction, player: str):
            await interaction.response.send_message("Removing %s from player pool." % (player))


    def register_events(self):
        @self.client.event
        async def on_ready():
            await self.tree.sync()
            print(f"Overwatch Matchmaker online! ID: {self.client.user.id}")


    def run(self):
        token = utils.read_first_line("/config/token.txt")
        self.client.run(token)