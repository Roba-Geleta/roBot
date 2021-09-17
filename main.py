import discord
import os
import json

client = discord.Client()

#access the json file storing the course info
course_Dict = {}
my_token = None
with open('Courses.json', 'r') as file:
  course_Dict = json.load(file)
with open('config.json', 'r') as file:
  my_token = json.load(file)

my_token = my_token.get("TOKEN")

print(my_token)


#used to verify user input is an integer
def is_Integer(num):
    check = True
    try:
        num = int(num)
    except ValueError:
        check = False
    return check

#used to return an embed storing information about the course requested
def msg_Return(course,desc):
  string = discord.Embed(
    title= course,
    description = desc["title"] +'\n' + desc["info"],
    colour = discord.Colour.red()
  )
  string.add_field(name ="Description:", value = desc["info"], inline = False)

  return string

#used to return an embed storing information about the help command
def help_Return():
  string = discord.Embed(
    title= "Command List",
    description = "All commands start with the symbol '$'",
    colour = discord.Colour.red()
  )

  string.set_author(name = "[roBot Help]", icon_url= client.user.avatar_url)
  string.add_field(name = "$find <short-hand course name> <course number>", value = "course name is not case sensitive.\n Command only takes in short-hand versions of the course name, so instead of chemistry, you would write CHEM/chem.\n Example command - $find comp 1012")
  string.set_thumbnail(url = client.user.avatar_url)
  string.set_footer(text = "Thanks for using this wacky bot.")
  
  return string 


#event - client is on
@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

#event - when client detects a message
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  #if the message is starts with the specified command
  if message.content.startswith("$find"):
    msg = message.content.split(" ") #split the message
    if(len(msg) < 3 or len(msg) > 3): #if the command is written correctly, it should hold 3 seperate words the find command, the course name, the course num
      return
    else:
      if(msg[1].upper() in course_Dict.keys()): #check if the course name is in the dictionary keys
        #check if the course num is within the course name key
        if(is_Integer(msg[2]) and (msg[2] in course_Dict[msg[1].upper()].keys())):
          #print out an embed of the course information
          await message.channel.send(embed = msg_Return(" ".join(msg[1:]).upper(),course_Dict[msg[1].upper()][msg[2]]))
  elif message.content == ("$help"): #if the message is a help command
    await message.channel.send(embed = help_Return())


#access the token from the environment and run the bot
#my_token = os.environ['TOKEN'] for when code was present in replit
client.run(my_token)