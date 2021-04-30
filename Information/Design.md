
######CEG 4110 Spring 2021  Design.md documentation 

###### Kyle Sturdevant, Trenton Brown, Joshua Rupp --> Group 12


#Frontend


######Design REQ 010  by Kyle 

**REQ: 010**

- Command: `-overview`
- Return: A paragraph explaining the game Monster Hunter World

######REQ 020 Design:  by  Kyle

**REQ: 020**

- Command: `-monsters <id>|<name> (page)` 
  - The required field will be either a number (id) or a string (name).
  - There is then an optional field that provides a page number if previous results went past current page limit.
- Return: 
    - If no input is provided then display instructions on how to use the command
    - If none returned then say no monster found
    - If returns one monster it will list:
        - Name
        - Type
        - Species
        - Description
        - Aliments (if exist)
        - Locations
        - Resistances (if exist)
        - Weaknesses (if exits)
        - Rewards
    - If returns more than one monster it will list in a table:
        - ID
        - Name
        - Type
        - Description

######REQ 030 Design:  by  Kyle

**REQ: 030**

- Command: `-weapons <id>|<name> (page)`
    - The required field will be either a number (id) or a string (name).
    - There is then an optional field that provides a page number if previous results went past current page limit.
- Return:
    - If no input is provided then display instructions on how to use the command
    - If none returned then say no monster found
    - If returns one weapon it will list:
        - Name
        - Type
        - Attack
        - Attributes
        - Damage Type
        - Durability
        - Elements
        - Crafting
        - Elderseal
    - If returns more than one weapon it will list in a table:
        - ID
        - Name
        - Type
        - Attack

######REQ 040 Design:  by  Kyle

**REQ: 040**


- Command: `-material <id>|<name> (page)`
    - The required field will be either a number (id) or a string (name).
    - There is then an optional field that provides a page number if previous results went past current page limit.
- Return:
    - If no input is provided then display instructions on how to use the command
    - If none returned then say no material found
    - If returns one material it will list:
        - Name
        - Type
        - Description
        - Usages
        - Crafting
        - Locations
    - If returns more than one material it will list in a table:
        - ID
        - Name
        - Description

######REQ 050 Design:  by  Kyle

**REQ: 050**

- Command: `-kit {<weapon>, <armor>, <decorations>}`
    - The required field will be some combination of a weapon, armor, and decorations
- Return:
    - If no input is provided then it will display the current user's kit.
        - If the current user does not have a kit, it will display how to use the command
    - If any input is provided, it will save this data for the specific user
        - Output message saying kit was saved.


######REQ 060 Design:  by  Kyle

**REQ: 060**

- Command: `-vendors (page)`
    - There is then an optional field that provides a page number if previous results went past current page limit.
- Return:
    - If no input is provided then display the first 5 vendors information:
        - Id
        - Name
        - Location
    - If a page number is specified, it will lists the 5 vendors for that page
        - If the page number mulitiplied by 5 is greater then the number of vendors, display page error
   
   
######REQ 070 Design:  by  Kyle

**REQ: 070**

- Command: `-soldby <id>|<name> (page)`
    - The required field will be either a number (id) or a string (name).
    - There is then an optional field that provides a page number if previous results went past current page limit.
- Return:
    - If no input is provided then display instructions on how to use the command
    - If none returned then say no products found
    - If returns one product it will list:
        - Name
        - Type
        - Description
    - If returns more than one product it will list in a table:
        - ID
        - Name
        - Type
        - Description


######REQ 080 Design:  by  Trent

**Requirement 080**  

This design was chosen because it will get the user the list of events, and they would
then be able to look up the individual event so that they could learn what the event entails.
- Command: `-events [id]` 
    - Parameter is optional 
- Return:
    - If no input, returns a list of events:
      - id
      - Name
    - If id is given:
        - Name
        - description
        - startTimeStamp
        - endTimeStamp
  
  
######REQ 090 Design:  by  Trent


**Requirement 090**  

This design choice was made because if the user failed to define either or the parameters,
"ecosystem" or "rank", there would be too much information to display.
- Command: `-location [ecosystem] [rank]`  
    - parameters are required 
- Return: 
    - If no parameters are passed, return a message about how to use the command
    - If only the ecosystem is passed, nothing should be returned as the result could give inaccurate information
    - If ecosystem and rank are passed, return a list of monsters in that ecosystem at that rank
        - id
        - Name
        
        
######REQ 100 Design:  by  Trent  

 
**Requirement 100**  

This design choice was made because there are only a few tools with small descriptions. So a list
of the tools being output should pose no problem and should reduce the number of chances a user
has to try and use the command and not get the desired results.
- Command: `-hunter tools`
- Return:  
    - Name
    - Description


######REQ 110 Design:  by  Trent


**Requirement 110**

Not every aspect of the game will have a tip to go with it. So the choice was made to provide
a random tip rather than have the user guess at which aspect has a tip by passing a parameter.
- Command: `-tip`  
- Return: A random tip about gameplay  

######REQ 120 Design:  by  Trent

**Requirement 120**  

The choice made for this requirement is for the same reason as requirement 90, if either
one of the parameters there would be too much information to output.
- Command: `-Guiding [area] [level]`
  - Parameters are required 
- Return:  
    - If no argument is passed, return how to use the command
    - If only one parameter is passed, return nothing to avoid giving incorrect information
    - If both parameters are passed return a list of monsters in the area at that level
        - id
        - Name
------------------------------------------------------------------------------------------


######REQ 130 Design: By Josh


Command name: _-item_recipe_

Parameters: _name_, _id_

**Design of _-item_recipe_command**:

The name for the command, _-item_recipe_ ,was a straight forward process. I needed a name that would 
be non ambiguous.  In contrast, if the command name was _-i_ or _-itm_. There leaves a level of 
decoding from the users perspective, on trying to figure out the function of the command. 
Where as _-item_recipe_ does not require a significant amount more typing. Yet leaves no ambiguity
as to the function of the command.

The parameters of the _-item_recipe_ command are a way to provide a convenient way to search for a 
item recipe. The user need not know exactly what he/she wishes to search for. However,
this command does require that the user needs to know some part of the name. 
Providing no parameters, returns nothing, except a message telling the user to input a name. 
Not all items in the Monster Hunter World game are craftable. Thus if the item searched for 
is non-craftable then the bot will return a message to that affect.  This design provides 
flexibility and robustness from an functionality standpoint. Moreover, makes it a convenient 
user friendly design so that the user does not need to be an expert in all things related to 
craft-able items in Monster Hunter World. In order to find out useful information about items 
and craftabililty.  



examples of _item make_ command usage: 

`-item_recipe Mega Potion`  -- example with _name_ parameter 

`-item_recipe 12`           -- example with _id_ parameter 

example of _item make_ command return value(s):

`crafting item: Mega Potion`   -- outputs _name_ of searched item

`Items needed: Potion, Honey`  -- outputs _comma separated list_ of items needed 
 

------------------------------------------------------------------------------------------


######REQ 140 Design: By Josh


Command name: _-add_ 

Parameters: None

**Design of _-add_  command**:

A privilege user is define by roles in Discord. Each Discord user account has a role 
on a server that the user's account is a member of. Therefore, if the role is of type 
"privileged" then the bot will allow that user account to adjust data or edit it in the 
database of Monster Hunter World video game. 

This command _-add_ needs no parameters to function properly. The discord bot will only 
allow this command to work IF.F the user account on discord has the appropriate role or 
privileges to execute such as command. If a user count on discord does not have the role 
of a privileged user and attempts to execute this command. A message will be printed out 
accordingly. 

If however, the bot allows the command to execute. Then the bot shall ask for what type 
of action the user wishes to add to the Monster Hunter World database. Such as item, weapon, 
location, Armor, ect. The Bot will then prompt sequentially, all fields of that item type to 
the user. The user will input the data desired for that field. Once all fields have been
satisfied the bot will write it to the database. Of course if the user inputs a wrong type 
for an item, (i.e. something other than a weapon, location,item, armor) than the bot present 
an error message to that effect. The bot will only prompt an error message about inputting wrong
or misguided data up to three times. After this condition the command will exit, and all data 
typed prior will be lost. 


The design for the _add_ command is much bigger in terms of overall scope. Both in Design 
and implementation. Thus this feature will be held off until the second phase of development. 
If the backend is change. Thus currently speaking this is a requirement to design hiccup that
comes as an inevitable consequence form the waterfall process.  


examples of _-add_ command usage:

`-add`



------------------------------------------------------------------------------------------


######REQ 150 Design: By Josh


Command name: _-edit_ 

Parameters: None

**Design of _edit_ command**:


This command is very similar to **REQ 140** command.very similar functionality. The only
distinction is that this command does not add new weapons, items, locations, armor or other
aspects to the Monster Hunter World database. It simply allows a privileged use to edit 
currently existing information about an item, weapon, location, armour, or other. The program 
will prompt the user for to enter the type of data they wish to edit. If the user inputs an 
invalid type; other than items, weapons, locations or other, that is not apart of the game. 
The bot will print an appropriate message, and prompt for editing input again. However,
if the user again, provides misguided input then the _edit_ command exits. However, if the 
user inputs valid input that references a specific type of item in the game. Then the Bot 
will find that item and provide a list of all fields available to edit. This way it creates
no ambiguity on the users perspective, for what can and cannot be edited in the Monster Hunter 
World game via the Discord bot.


A privilege user is define by roles in Discord. Each Discord user account has a role 
on a server that the user's account is a member of. This is given by the Admin of the server.
Therefore, if the role is of type "privileged" then the bot will allow that user account 
to adjust data or edit it in the database of Monster Hunter World video game. 


As with **REQ 140**; **REQ 150** is considered more of a bonus feature and therefore is 
held off until the second phase of development. If the backend is change. Thus, currently 
speaking this is a requirement to design hiccup that comes as an inevitable consequence 
form the waterfall process.  



examples of _-edit_  command usage:

`-edit`  






------------------------------------------------------------------------------------------


######REQ 160 Design:  Josh


Command name: _-my_victims_ 

Parameters: _name_ 

**Design of _-my_victims_  command**:

The command _my_victims_ takes in the name of a monster in the monster hunter world video
game, as its only parameter. It installs it into a list of monsters, and then displays 
the list to the user via discord. If the name of the monster is not a monster in the 
Monster Hunter World game. Then the Bot prints out an appropriate message to the user. IF
the command is entered without any name, or parameter. Then the command will print out the correct 
syntax for how the command should operate. 

To ensure that each user of the Monster Hunter World Bot has its own list of monsters killed. 
This command creates and installs victimized monsters under the user's discord name. 
So that each user can track their killed monsters.

There are 48 total monsters in the Monster Hunter World video game. Thus the maximum size 
of any monster list will be 48. _Currently, as of 4/20/21, this number of monsters is correct. 
However, due to updates, or Monster Hunter World game designers wanting to add or remove 
monster content. This total number of monsters is subject to change_.The smallest size of
course would be if there were no monsters killed, thus size = 0. Being how the upper
bound of a monster list is 48. printing out to discord should not cause any significant
undefined bandwidth issues. 

Potentially I could have returned a dictionary here instead of a list, however,
you would have to utilize a value, or key field per cell in a dictionary in the python 
programming language. Since it is not needed and would only cause of more unneeded data 
to the user, and in code. It simply is complexity that is not needed. Thus a list or array 
in the python language is best for this design.  


examples of _my_victims_ command usage:

`-my victims Kulu-Ya-Ku`  -- example with _name_ parameter 



------------------------------------------------------------------------------------------


######REQ 170 Design:  by Josh


Command name: _-victimized_ 

Parameters: _name_ 

**Design of _victimized_ command**:


This command is the exact same design as the **REQ 160**. In every way; the only difference
is the command name is different. The design and implementation will be identical.
Therefore, refer to **REQ 160** to find out the details. 


examples of _-victimized_  command usage:

`-gone to soon Kulu-Ya-Ku`  -- example with _name_ parameter 



######REQ 250 Design:   by Josh


Command name: _-help_ 

Parameters: None

**Design of _help_ command**:

The _help_ command will list all available commands supported by the bot. Moreover will 
print a brief description of each command. It will do this by printing a dictionary to 
Discord Server. The key in the dictionary is the command name, the value shall be a brief 
description or purpose of the command.  


I decided to go with a dictionary for this data structure instead of an array or list for 
one major reason; complexity. To achieve the same functionality that a dictionary in python
gives you. You would either need a nested list structure. Which is two lists. Furthermore,
you could use two parallel lists with indices matching up for command and description. 
Either way two separate but related lists would be needed. However, using a dictionary 
only one structure is needed. 


examples of _help_ command usage:

`-help`

######REQ 260 Design: By Josh

**Design of format table**:

The table will output the data obtained by the Monster Hunter World bot, in a nice organized 
column, row matrix style table. The headers of the table will organize the different types of 
data in each column so that the user has a nice, formatted, organized visual of the searched 
results. That way this avoids any cryptic confusing output. More importantly however, the 
user does not feel annoyed by the unprofessional presentation of the data, and not want to use 
the bot. 

Considering the case that some lines or rows might have more data than others. I feel that 
text wrapping per column is a must for this table. We do not want to consider the possibility 
that all data in every row is going to be the same size or same length. More importantly, 
we do not want to have to truncate strings, in order to make the data all fit. This is a bad 
design for a table, and would look very unprofessional. Therefore, I would have to say that 
text wrapping needs to be at the center of the tables functionality. 

The table will have the ability to delete a row if needed, or clear the whole table in case 
of extengient circumstances. I mean why not, have that ability. Moreover, the table should be 
able to calculate the maximum length for each column.Then devise a solution in case 
one column takes up the whole length of the table, or the summations of each column's width 
is greater or equal to a maximum specified width.  The reason for this is there is implicit text 
wrapping in discord after 80 characters are entered on a line. So the table will need to 
have the ability to compute the total width of every column and ensure that it is less than 80
characters. 

There are some nice python libraries for formatted tables. I choose to go with prettytables. 
Although there many others to choose from. I simply feel that an ACSII character boarder and 
formatted table is best for this design, because the table needs to be able to be printed on 
discord. I think that a more simple text formatted table should have a very low probability of  
compatibility issues with Discord. 


#Backend

**REQ: 240**

- Option 1: https://github.com/MattJarman/mhw-api
    - Pro: Database in sqlite, so entire database is in repo
    - Con: API only provides 3 endpoints with very limited information
    - Summary: After installing Docker and getting this running, the limits in the REST API 
      make using this backend difficult. It doesn't support all the end points the other API 
      supports, and appears to have fewer categories of data. I would not recommend for this project.
- Option 2: https://github.com/LartTyler/MHWDB-API
    - Pro: Many endpoints with good documentation [here](https://docs.mhw-db.com/)
    - Con: MySql database which doesn't appear to be provided
    - Summary: After installing Vagrant and getting this API up, I found the README instructions impossible to complete. 
      The instructions said to run "./db-reset.sh latest", but this 'db-reset.sh' file doesn't exist in the repo. 
      So, when making calls to the API running locally, it fails with a database error as the database isn't 
      configured correctly. This could be an alternative solution, if the database was populated.
- Option 3: Use https://mhw-db.com directly
    - Pro: We don't need to run and host our own REST API
    - Pro: All the endpoints documented [here](https://docs.mhw-db.com/) are available. 
    - Con: We are unable to change the backend if needed. 
    - Summary: The documentation shows this REST API should provide all the features we require 
      and is publicly accessible. Using the already provided API and hosting, this option would require less resources 
      than if we were to run our own REST API backend. At this time, this is the suggested backend.
