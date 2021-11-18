# race.py
import os
import discord
import csv
import random
from datetime import datetime, timedelta
import pandas as pd


attributes_file = "attributes.csv"
attributes_fields = []
attributes = []

# reading csv file
with open(attributes_file, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    attributes_fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        attributes.append(row)

    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))


# IMPORT COMMANDS FROM THE DISCORD.EXT MODULE.
from discord.ext import commands

from dotenv import load_dotenv

filename = "log.csv"
fields = []
rows = []


def maximum(a, b):
    if a >= b:
        return a
    else:
        return b

def fullname(id):
    if id > 1000:
        return "#"+str(id)
    if id > 100:
        return "#0"+str(id)
    if id > 10:
        return "#00"+str(id)
    if id > -1:
        return "#000"+str(id)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
bot = commands.Bot(command_prefix="%")


@bot.command(name="roll")
async def race_function(ctx, *args):


    rows = []

        # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

        # get total number of rows
        print("Total no. of rows: %d"%(csvreader.line_num))



    x=0
    for arg in args:
        if x == 0:
            player1 = int(arg)
        x+=1

    print("rows:")
    print(rows)
    print("player1:")
    print(player1)
    bestfriend = attributes[player1-1][6]
    nemesis = attributes[player1-1][7]
    strength = int(attributes[player1-1][8])
    speed = int(attributes[player1-1][9])
    endurance = int(attributes[player1-1][10])
    intelligence = int(attributes[player1-1][11])
    wisdom = int(attributes[player1-1][12])
    charisma = int(attributes[player1-1][13])
    class_attribute = attributes[player1-1][14]
    element = attributes[player1-1][15]
    habitat = attributes[player1-1][16]
    attribute_x = int(attributes[player1-1][17])
    attribute_y = int(attributes[player1-1][18])
    attribute_z = int(attributes[player1-1][19])
    print("strength: "+str(strength)+". speed: "+str(speed)+". endurance: "+str(endurance)+". intelligence: "+str(intelligence)+". wisdom: "+str(wisdom)+". charisma: "+str(charisma)+".")
    print("bestfriend: "+bestfriend+". nemesis: "+nemesis+". class_attribute: "+class_attribute+". element: "+element+". habitat: "+habitat+".")

    m = [i for i in rows if str(player1) == i[1]]
    position = 0
    for moves in m:
        position = position + int(moves[2])
    if len(m) > 0:
        position = int(m[-1][5])

    numrows = len(m)
    now = datetime.now()
    if numrows > 0:
        lastrolldate = m[-1][3]
        lastrolltime = m[-1][4]
        lastroll = datetime.strptime(lastrolldate+" "+lastrolltime,"%m/%d/%Y %H:%M:%S" )
        rest_time = timedelta(hours=(24-endurance/2))
        print("rest_time:")
        print(rest_time)
        ready_time = lastroll+rest_time
        if now > ready_time:
            ready = 1
        if ready_time > now:
            ready = 0
    if numrows == 0:
        ready = 1
    if ready == 1:
        await ctx.channel.send("player "+fullname(player1)+" is at "+str(position)+", will roll now.")
        move = random.randint(1, (3+round(speed/3)))
        new_position = position + move

        now = datetime.now()
        date = now.strftime("%m/%d/%Y")
        time = now.strftime("%H:%M:%S")

        valhalla = 100

        if new_position == valhalla:
            await ctx.channel.send(fullname(player1)+" rolled a "+str(move)+" and is now at "+str(new_position)+".")
            await ctx.channel.send(fullname(player1)+" wins!!!!")
            perms = ctx.channel.overwrites_for(ctx.guild.default_role)
            perms.send_messages=False
            await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=perms)

        elif new_position < valhalla:
            await ctx.channel.send(fullname(player1)+" rolled a "+str(move)+" and is now at "+str(new_position)+".")
        elif new_position > valhalla:
            diff = new_position-valhalla
            new_position = valhalla-diff
            await ctx.channel.send("["+fullname(player1)+"] You must land exactly on "+str(valhalla)+" or bounce back the remaining amount of your roll. "+fullname(player1)+" rolled a "+str(move)+" and is now at "+str(new_position)+".")

        if new_position == 1:
            await ctx.channel.send("["+fullname(player1)+"] Life is all about baby steps. Let's give you a boost of 1.")
            new_position = new_position + 1
        elif new_position == 2:
            await ctx.channel.send("["+fullname(player1)+"] Two is a lucky number, how's 2 more.")
            new_position = new_position + 2
        elif new_position == 3:
            await ctx.channel.send("["+fullname(player1)+"] You were mean. Go back 2 spaces.")
            new_position = new_position + (-2)
        elif new_position == 4:
            await ctx.channel.send("["+fullname(player1)+"] You saw a shooting star. Move forward 4 spaces.")
            new_position = new_position + 4
        elif new_position == 5:
            await ctx.channel.send("["+fullname(player1)+"] A butterfly landed on your shoulder. Move forward 6 spaces")
            new_position = new_position + 6
        elif new_position == 6 or new_position == 22 or new_position == 33 or new_position == 42 or new_position == 61:
            await ctx.channel.send("["+fullname(player1)+"] A wagon is passing by, let's convince them to give you a ride. Your charsima is "+str(charisma)+", so you'll roll a "+str(charisma)+" sided dice...")
            quickroll = random.randint(1, charisma)
            await ctx.channel.send("["+fullname(player1)+"] You rolled a "+str(quickroll)+", and hitced a ride for "+str(quickroll)+" spaces.")
            new_position = new_position + quickroll
        elif new_position == 7 or new_position == 13 or new_position == 28 or new_position == 36 or new_position == 43 or new_position == 53:
            await ctx.channel.send("["+fullname(player1)+"] You found a short cut, but it's a bit tricky to navigate. Roll a "+str(intelligence)+" (your intelligence) sided dice to see how far it took you.")
            quickroll = random.randint(1, intelligence)
            await ctx.channel.send("["+fullname(player1)+"] You rolled a "+str(quickroll)+", and found your way up "+str(quickroll)+" spaces.")
            new_position = new_position + quickroll
        elif new_position == 32 or new_position == 63 or new_position == 82:
            await ctx.channel.send("["+fullname(player1)+"] A huge gust of wind is blowing you back. Roll a "+str(strength)+" (your strength) sided dice to see how much you got pushed back. (20-roll)")
            randroll = random.randint(1, strength)
            quickroll = 20-randroll
            await ctx.channel.send("["+fullname(player1)+"] You rolled a "+str(randroll)+", and was blown back "+str(quickroll)+" spaces.")
            new_position = new_position - quickroll
        elif new_position == 61 or new_position == 86 or new_position == 93:
            await ctx.channel.send("["+fullname(player1)+"] You are faced with an impossible and difficult choice (it happens). Roll a "+str(wisdom)+" (your wisdom) sided dice to see how far this held you back. (40-2*roll)")
            randroll = random.randint(1, wisdom)
            quickroll = 40-2*randroll
            await ctx.channel.send("["+fullname(player1)+"] You rolled a "+str(randroll)+", and will now move back "+str(quickroll)+" spaces.")
            new_position = new_position - quickroll
        elif new_position == 12:
            await ctx.channel.send("["+fullname(player1)+"] You rescued an injured bird and nursed it back to health. Move forward 32 spaces.")
            new_position = new_position + 32
        elif new_position == 41:
            await ctx.channel.send("["+fullname(player1)+"] You littered in the forest. Go back 30 spaces.")
            new_position = new_position + (-30)
        elif new_position == 44:
            await ctx.channel.send("["+fullname(player1)+"] You collected way more berries than you need for yourself. Poor form. Go back 10 spaces.")
            new_position = new_position + (-10)
        elif new_position == 49:
            await ctx.channel.send("["+fullname(player1)+"] You graffiti'd a beautiful boulder on the hiking trail. Why? Go back 23 spaces.")
            new_position = new_position + (-23)
        elif new_position == 51:
            await ctx.channel.send("["+fullname(player1)+"] You were there for a friend in need. Move forward 23 spaces.")
            new_position = new_position + 23
        elif new_position == 52:
            await ctx.channel.send("["+fullname(player1)+"] You stole berries from a neighbor's garden. Go back 32 spaces.")
            new_position = new_position + (-32)
        elif new_position == 57:
            await ctx.channel.send("["+fullname(player1)+"] You made cookies and shared it with all the neighbors. Move forward 15 spaces.")
            new_position = new_position + 15
        elif new_position == 58:
            await ctx.channel.send("["+fullname(player1)+"] You didn't make sure to put out a campfire. Nothing happened, but still, poor form. Go back 12 spaces.")
            new_position = new_position + (-12)
        elif new_position == 62:
            await ctx.channel.send("["+fullname(player1)+"] Had too much aged nectar last night. Go back 15 spaces.")
            new_position = new_position + (-15)
        elif new_position == 69:
            await ctx.channel.send("["+fullname(player1)+"] You borrow honey from a neighbor and never returned it. Go back 17 spaces.")
            new_position = new_position + (-17)
        elif new_position == 73:
            await ctx.channel.send("["+fullname(player1)+"] You laid on a field of flowers for a selfie. Do better. Go back 34 spaces.")
            new_position = new_position + (-34)
        elif new_position == 76:
            await ctx.channel.send("["+fullname(player1)+"] You wrote a book about your adventures. Move forward 18 spaces.")
            new_position = new_position + 18
        elif new_position == 78:
            await ctx.channel.send("["+fullname(player1)+"] You resisted temptation. Move forward 16 spaces.")
            new_position = new_position + 16
        elif new_position == 84:
            await ctx.channel.send("["+fullname(player1)+"] You yelled at somebody who didn't deserve it. Go back 28 spaces.")
            new_position = new_position + (-28)
        elif new_position == 95:
            await ctx.channel.send("["+fullname(player1)+"] You were mean to someone new to Beastopia. Go back 43 spaces.")
            new_position = new_position + (-43)
        elif new_position == 99:
            await ctx.channel.send("["+fullname(player1)+"] You did something unspeakably naughty.. go back 75 spaces!")
            new_position = new_position + (-75)

        await ctx.channel.send(fullname(player1)+" is now at "+str(new_position)+".")

        row = [0,player1,move,date,time,new_position]
        rows.append(row)

    if ready == 0:
        print("not ready")
        remaining_rest_time = ready_time - now
        print(remaining_rest_time)
        print("You're not ready, you must rest this much longer:"+str(remaining_rest_time))
        await ctx.channel.send(fullname(player1)+" is not ready and must rest this much longer: "+str(remaining_rest_time))


    #print results in csv
    out=open("log.csv","w")
    output=csv.writer(out)
    for row in rows:
	    output.writerow(row)
    out.close()

bot.run(TOKEN)

