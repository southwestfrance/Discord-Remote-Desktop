import discord
from config import TOKEN
from commands.desktop_commands import DesktopCommands

class MyClient(discord.Client):
    def __init__(self, intents, commands_handler):
        super().__init__(intents=intents)
        self.commands_handler = commands_handler
    
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        
    async def on_message(self, message):
        print(f'Message from {message.author}({message.author.id}): {message.content}')
        
        if message.author == self.user:
            return
        
        await self.commands_handler.handle_command(message)
        
intents = discord.Intents.default()
intents.message_content = True

commands_handler = DesktopCommands()

client = MyClient(intents=intents, commands_handler=commands_handler)
client.run(TOKEN)