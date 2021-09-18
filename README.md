# roBot

This is a Discord bot made with the purpose of responding to users with the course information of the course they requested.

***

# How To

Two commands:

1. `$help`: allows the bot to reply with an embed storing command informations for its usage.
  
2. `$find <course name> <course number>`: used to request the course information for the course specified.
  
 ***
 
 # Course Catalog
 
The course catalog was made through web scraping with [selenium](https://www.selenium.dev/) on the [aurora](https://aurora.umanitoba.ca/banprod/bwckctlg.p_disp_cat_term_date) website.

Courses.json consists of:

1. Keys in the form of course name. For this bot, the short hand name of the course is accepted.

+ Ex. instead of Computer Science, it uses COMP.

2. More Keys within the initial course name keys, that represent the course number.

3. And finally, under each course number key, the specific course title and info are stored.

***

# Run

roBot can be ran through any cloud services of your choosing or your own pc. You can find other ways.
I am currently running this bot on [Google Cloud Services](https://cloud.google.com/) for a couple private servers, but initially I used [replit](https://replit.com/~).

***

# Built With

+ [Python 3.9.7](https://www.python.org/downloads/)
+ [selenium 3.141](https://www.selenium.dev/documentation/)
+ [Discord 1.7.3](https://discordpy.readthedocs.io/en/stable/)
