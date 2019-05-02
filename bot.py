# -----------------------------------------
#                IMPORTS
# -----------------------------------------
import discord
import asyncio
import random
import requests
import os

# -----------------------------------------
#               VARIAVEIS
# -----------------------------------------
COR = 0x9b00fc
client = discord.Client()
#token = "TOKEN SEU AQUI"
#
cargo = "."

# -----------------------------------------
#                  CODE
# -----------------------------------------
@client.event
async def on_ready():
    print('Logado como:\n{0} (ID: {0.id})'.format(client.user))
    await client.change_presence(game=discord.Game(name='Night Core', type=1, url='https://www.twitch.tv/hmmmm'), status='streaming')
# -----------------------------------------
@client.event
async def on_message(message):
    if message.content.startswith(f'{bot.user.mention}'):
        await bot.send_message(message.channel, f'para ajuda use =ajuda :D ')
@client.event
async def on_message(message):
    if message.content.startswith('=ajuda'):
        embed = discord.Embed(title='Informações',description='**Sou um bot criado para enviar mensagens no DM de todos membros do servidor**\n\nPara me utilizar é facil, digite (=setar [url].png) a url da imagem que deve ser terminada em .png é deve ser exibida no chat do discord.\n\nQuando setar a imagem digite (c!anuncio [msg]), muito facil não acha ?',color=COR)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/460869727129174027/461766170127892480/bot_png.png')
        await client.send_message(message.channel, embed=embed)
    if message.content.lower().startswith('=deletar'):
        role = discord.utils.get(message.server.roles, name=cargo)
        if not role in message.author.roles:
            embed1 = discord.Embed(title='Hmmm tem algo de errado...', description="Infelizmente você precisa do cargo `{}` para utilizar este comando.".format(cargo), color=COR)
            embed1.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            return await client.send_message(message.channel, embed=embed1)
        qntdd = message.content.strip('=deletar')
        qntdd = int(qntdd)
        if qntdd <= 100:
            msg_author = message.author.mention
            await client.delete_message(message)
            deleted = await client.purge_from(message.channel, limit=qntdd)
            botmsgdelete = await client.send_message(message.channel,'Escolhidas (**{}**) Deletadas (**{}**). \nPedido feito por **{}** '.format(len(deleted), qntdd, msg_author))
            await asyncio.sleep(10)
            await client.delete_message(botmsgdelete)
    if message.content.startswith('=setar'):
        role = discord.utils.get(message.server.roles, name=cargo)
        if not role in message.author.roles:
            embed1 = discord.Embed(title='Hmmm tem algo de errado...', description="Infelizmente você precisa do cargo `{}` para utilizar este comando.".format(cargo), color=COR)
            embed1.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            return await client.send_message(message.channel, embed=embed1)
        await client.delete_message(message)
        set1 = message.content.strip('=setar')
        global setar
        setar = set1
        embed1 = discord.Embed(color=COR)
        embed1.set_image(url=setar)
        embed1.add_field(name=f"{message.author.name}", value="Pronto, senhor(a) coloquei a imagem que você pediu para ser enviada no DM dos membros 🖤", inline=False)
        await client.send_message(message.channel, embed=embed1)

    if message.content.startswith('=anuncio'):
        msg = message.content[10:]
        role = discord.utils.get(message.server.roles, name=cargo)
        if not role in message.author.roles:
            embed1 = discord.Embed(title='Hmmm tem algo de errado...', description="Infelizmente você precisa do cargo `{}` para utilizar este comando.".format(cargo), color=COR)
            embed1.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            return await client.send_message(message.channel, embed=embed1)
        x = list(message.server.members)
        s = 0
        embed2 = discord.Embed(title='Pronto senhor(a)',description='Estou enviando a mensagem que você pediu no DM de todos membros 🖤\n' + "Foi esta mensagem que você pediu não foi ?\n\n" + "{}".format(msg) + '\n\nSe foi eu irei enviar ela para {} membros'.format(len(x)), color=COR)
        embed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
        await client.send_message(message.channel, embed=embed2)
        for member in x:
            embed1 = discord.Embed(color=COR, description="{}\n".format(msg))
            embed1.set_image(url=setar)
            embed1.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            try:
                await client.send_message(member, embed=embed1)
                print(member.name)
                s += 1
            except:
                pass
client.run(str(os.environ.get('BOT_TOKEN')))
