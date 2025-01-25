import discord
import pyautogui
from PIL import Image, ImageDraw, ImageFont
import time
from discord.ext import commands

class DesktopCommands:
    def __init__(self):
        pyautogui.FAILSAFE = False
        pass
        
    def pos(self):
        x, y = pyautogui.position()
        pos = (x, y)
        return pos
    
    def screenshot_and_embed(self):
        # screenshot desktop with pyautogui
        desktop_img = pyautogui.screenshot("desktop.png")
        
        # open screenshot with pillow
        img = Image.open("desktop.png")
        draw = ImageDraw.Draw(img)
        
        # get mouse pos
        x, y = pyautogui.position()
        
        # draw circle to indicate mouse pos
        radius = 10
        draw.ellipse(
            (x - radius, y - radius, x + radius, y + radius),
            fill="white",  
            outline="black", 
            width=2  
        )
        
       
        # load a default font
        font = ImageFont.load_default()
        
        # Calculate text size using getbbox
        text = f"({x}, {y})"
        text_bbox = font.getbbox(text)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        # Draw the mouse coordinates above the ellipse
        text_offset = 15  # Distance above the circle
        draw.text(
            (x - text_width // 2, y - radius - text_offset - text_height),
            text,
            fill="cyan",
            font=font
        )
        # save changes
        img.save("desktop.png")
        
        file = discord.File("desktop.png", filename="desktop.png")
        embed = discord.Embed()
        
        x, y = self.pos()
        embed.description = f"mouse pos: {x}. {y}"
        
        embed.set_image(url="attachment://desktop.png")
        
        return file, embed
    
    def type_to_desktop(self, sentence):
        pyautogui.write(sentence)
        return
    
    def key_press(self, button):
        pyautogui.press(button)
        return
        
    def move_mouse(self, coords):
        pyautogui.moveTo(int(coords[0]), int(coords[1]))
        return
        
    async def handle_command(self, message):
        msg = message.content.lower()
        
        # handle screenshot command
        if msg == "!ss" or msg == "!screenshot":
            file, embed = self.screenshot_and_embed()
            await message.channel.send(embed=embed, file=file)
        
        # handle typing command
        if msg.startswith("!type"):
            content = msg[len("!type "):]
            self.type_to_desktop(content)

            file, embed = self.screenshot_and_embed()
            await message.channel.send(embed=embed, file=file)
            
        # handle keypress commmand    
        if msg.startswith("!press"):
            content = msg[len("!press "):]
            self.key_press(content)

            file, embed = self.screenshot_and_embed()
            await message.channel.send(embed=embed, file=file)
            
        if msg == "!click" or msg == "!c":
            pyautogui.click()

            file, embed = self.screenshot_and_embed()
            await message.channel.send(embed=embed, file=file)
        
        # handle mouse move command    
        if msg.startswith("!mouse"):
            content = msg[len("!mouse "):]
            coords = content.split(" ")
            print(coords)
            self.move_mouse(coords)

            file, embed = self.screenshot_and_embed()
            await message.channel.send(embed=embed, file=file)
    
