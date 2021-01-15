#--IMPORTS--
import arcade
import os
import random
import time
import math
import rooms
#-----------
#Dictionary containing directories of tiles that don't have collision
static_no_collision = {"f1":"images/floors/floor 1.png", "f2":"images/floors/floor 2.png", "f3":"images/floors/floor 3.png", "f4":"images/floors/floor 4.png", "f5":"images/floors/floor 5.png"}
#Dictionary containing directories of tiles that have collision
static_collision = {"wh1":"images/walls/wall horizontal 1.png", "wv1":"images/walls/wall vertical 1.png", "cbl1":"images/walls/corner bottom left 1.png", "cbr1":"images/walls/corner bottom right 1.png", "ctl1":"images/walls/corner top left 1.png", "ctr1":"images/walls/corner top right 1.png","c1":"images/walls/connector 1.png"}
#Dictionary containing directories of exits
exits = {"ex1":"images/misc/exit 1.png"}
#Dictionary containing directories of entrances
entrances = {"en1":"images/misc/entrance 1.png"}
#List of tile corresponding strings in order of render priority, for example 'wh1' will be rendered on top of the following items
static_render_priorities = ["wh1", "wv1", "cbl1", "cbr1", "ctl1", "ctr1", "c1", "f1", "f2", "f3", "f4", "f5", "ex1", "en1", ""]
#List containing all the directories for player 1 textures, in the following order;
#standing left folder, standing right folder, walking left folder, walking right folder, walking up folder, walking down folder.
#It automatically incorperates the files in these folders for player 1 animations.
player_1_texture_directories = ["images/player_1_anims/stand left textures", "images/player_1_anims/stand right textures", "images/player_1_anims/walk left textures", "images/player_1_anims/walk right textures", "images/player_1_anims/walk up textures", "images/player_1_anims/walk down textures"]

#List containing all the directories for player 2 textures, in the following order; 
#standing left folder, standing right folder, walking left folder, walking right folder, walking up folder, walking down folder.
#It automatically incorperates the files in these folders for player 2 animations
player_2_texture_directories = ["images/player_2_anims/stand left textures", "images/player_2_anims/stand right textures", "images/player_2_anims/walk left textures", "images/player_2_anims/walk right textures", "images/player_2_anims/walk up textures", "images/player_2_anims/walk down textures"]

#List containing all the directories for the guard textures, in the following order;
#standing left folder, standing right folder, walking left folder, walking right folder, walking up folder, walking down folder, alerted standing left folder, alerted standing right folder, alerted walking left folder, alerted walking right folder, alerted walking up folder, alerted walking down folder.
#It automatically incorperates the files in these folders for the guard animations
guard_texture_directories = ["images/guard/walk left textures", "images/guard/walk right textures", "images/guard/walk left textures", "images/guard/walk right textures", "images/guard/walk up textures", "images/guard/walk down textures", "images/guard/alerted walk left textures", "images/guard/alerted walk right textures", "images/guard/alerted walk left textures", "images/guard/alerted walk right textures", "images/guard/alerted walk up textures", "images/guard/alerted walk down textures"]

#Dictionary containing directories of coins
special = {"coin 1":"images/misc/coin 1.png"}

#A patrol controls a guard, each item is a instruction, with the items within representing;
#X direction, Y direction, time until next instruction,
#It loops through the patrol
#For example the first patrol makes him walk up for 3 seconds, walk right for 3 seconds, walk down for 3 seconds, walk left for 3 seconds, and then back to the begining and so on.
patrol_1 = [[0, 1, 0.8], [1, 0, 12], [0, -1, 0.8], [-1, 0, 12]]
patrol_2 = [[1, 0, 1.5], [0,1, 1.5],[-1, 0,1.5],[0,-1, 1.5]]
patrol_3 = [[1,0, 4], [-1, 0, 4]]
patrol_4 = [[0, 1, 4], [0, -1, 4]]
patrol_5 = [[0, 1, 2], [0, -1, 2]]
patrol_6 = [[-1, 0, 12],[1,0, 12]]
patrol_7 = [[1, 0, 12], [-1, 0, 12]]

#Loads the textures into a 2D list from the directories in the list on line 30 in the same order
player_1_textures = []
for a in range(len(player_1_texture_directories)):
  #Gets the filenames of the files in the directory
  files = os.listdir(player_1_texture_directories[a])
  textures = [] #This will be the second dimension to the 2D list
  #Loops through each filename in the directory
  for b in range(len(files)):
    #Adds a loaded from the directory made by concatinating "/" and the filename to the original directory
    textures.append(arcade.load_texture(player_1_texture_directories[a] + "/" + files[b]))
  #Adds all the directories textures to the original list hence a 2D list
  player_1_textures.append(textures)

#Loads the textures into a 2D list from the directories in the same way as for player 1
player_2_textures = []
for a in range(len(player_2_texture_directories)):
  files = os.listdir(player_2_texture_directories[a])
  textures = []
  for b in range(len(files)):
    textures.append(arcade.load_texture(player_2_texture_directories[a] + "/" + files[b]))
  player_2_textures.append(textures)

#Loads the textures into a 2D list from the directories in the same way as for player 1 and player 2
guard_textures = []
for a in range(len(guard_texture_directories)):
  files = os.listdir(guard_texture_directories[a])
  textures = []
  for b in range(len(files)):
    textures.append(arcade.load_texture(guard_texture_directories[a] + "/" + files[b]))
  guard_textures.append(textures)

#Class for any character with animations such as the players and guards
class Character(arcade.AnimatedWalkingSprite):
  def __init__(self, scale, stand_left_textures, stand_right_textures, walk_left_textures, walk_right_textures, walk_up_textures, walk_down_textures, texture_change_distance, collisions, speed):
    super().__init__(scale)
    #For some reason although in arcade it sets the _texture in initialization sometimes it requires some help
    self._texture = stand_right_textures[0]
    #Set the parent classes textures allowing it to proccess animations
    self.stand_left_textures = stand_left_textures
    self.stand_right_textures = stand_right_textures
    self.walk_left_textures = walk_left_textures
    self.walk_right_textures = walk_right_textures
    self.walk_up_textures = walk_up_textures
    self.walk_down_textures = walk_down_textures
    #Set the parent classes texture change distance, this determins how much distance before a the current texture should be switched
    self.texture_change_distance = texture_change_distance
    #Create physics (collision and movement) for the character
    self.physics = arcade.PhysicsEngineSimple(self, collisions)
    #Set the classes speed
    self.speed = speed
    self.game_over_collision = False
    self.game_over_time = 0
  def setup(self, x, y):
    #Place the character at specified coordinates
    self.center_x = x
    self.center_y = y
  #Updates the character however needs to be externally called
  def update(self):
    self.update_animation()
    self.physics.update()
   

#Class for a guard, a fairly complex 'AI' although it is just a algorithm, no deep learning
class Guard(Character):
  def __init__(self, scale, stand_left_textures, stand_right_textures, walk_left_textures, walk_right_textures, walk_up_textures, walk_down_textures, alerted_stand_left_textures, alerted_stand_right_textures, alerted_walk_left_textures, alerted_walk_right_textures, alerted_walk_up_textures, alerted_walk_down_textures, texture_change_distance, collisions, speed, patrol, alert_timer):
    super().__init__(scale, stand_left_textures, stand_right_textures, walk_left_textures, walk_right_textures, walk_up_textures, walk_down_textures, texture_change_distance, collisions, speed)
    #Store textures as they will need to be used again, the underscore (_) is required to differentiate it from the parent classes textures
    self._stand_left_textures = stand_left_textures
    self._stand_right_textures = stand_right_textures
    self._walk_left_textures = walk_left_textures
    self._walk_right_textures = walk_right_textures
    self._walk_up_textures = walk_up_textures
    self._walk_down_textures = walk_down_textures
    #Store alerted textures as they will need to be used again
    self.alerted_stand_left_textures = alerted_stand_left_textures
    self.alerted_stand_right_textures = alerted_stand_right_textures
    self.alerted_walk_left_textures = alerted_walk_left_textures
    self.alerted_walk_right_textures = alerted_walk_right_textures
    self.alerted_walk_up_textures = alerted_walk_up_textures
    self.alerted_walk_down_textures = alerted_walk_down_textures
    #Set the classes patrol
    self.patrol = patrol
    #Set the classes alert_timer, this is how long the guard will maintain alerted before losing interest
    self.alert_timer = alert_timer

  def guard_setup(self, x, y):
    #Call the parent classes setup to place the guard
    self.setup(x, y)
    #Set the direction of movement to be still
    self.dir_x = 0
    self.dir_y = 0
    #Set the patrol index, the patrol index is the index determining which instruction within the patrol is in use
    self.patrol_index = 0
    #Set the change time, change time is the exact time at which the guard should switch instruction within the patrol
    self.change_time = time.time() + self.patrol[0][2]
    #Set the alert, determines whether the guard is alerted
    self.alerted = False
    #Alert time is the exact time in which the guard should become un-alert
    self.alert_time = 0
    #Set the target, target is the point the guard will target when alterted, this is most likely a players position
    self.target = [0, 0]
  
  def guard_update(self):
    #If alerted then check whether alert is still valid, if true follow target, if false them become un-alert
    if(self.alerted):
      if(time.time() >= self.alert_time):
        self.un_alert()
      else:
        #Target is set externally to the nearest player
        dest_x = self.target[0]
        dest_y = self.target[1]
        #Calculate the angle the from the from the target to the guard 
        x_diff = dest_x - self.center_x
        y_diff = dest_y - self.center_y
        angle = math.atan2(y_diff, x_diff)
        #Then using the angle we can calculate the neccesary direction
        self.change_x = math.cos(angle) * self.speed
        self.change_y = math.sin(angle) * self.speed
    #If not alert then follow the patrol
    else:
      #If patrol instruction time has been reached then switch to next instruction
      if(time.time() >= self.change_time):
        if(self.patrol_index == len(self.patrol) - 1):
          self.patrol_index = 0
        else: 
          self.patrol_index += 1
        self.dir_x = self.patrol[self.patrol_index][0]
        self.dir_y = self.patrol[self.patrol_index][1]
        self.change_time = time.time() + self.patrol[self.patrol_index][2]
      #Move the guard
      self.change_x = self.dir_x * self.speed
      self.change_y = self.dir_y * self.speed
    #In the character class, this updates the characters animations and physics
    self.update()
  
  def alert(self):
    #Set to be alert
    self.alerted = True
    #Set alert termination time
    self.alert_time = time.time() + self.alert_timer
    #Switch textures to the alert variation
    self.stand_left_textures = self.alerted_stand_left_textures
    self.stand_right_textures = self.alerted_stand_right_textures
    self.walk_left_textures = self.alerted_walk_left_textures
    self.walk_right_textures = self.alerted_walk_right_textures
    self.walk_up_textures = self.alerted_walk_up_textures
    self.walk_down_textures = self.alerted_walk_down_textures
  
  def un_alert(self):
    #Set to be un-alert
    self.alerted = False
    #Set textures to the un-alert variation
    self.stand_left_textures = self._stand_left_textures
    self.stand_right_textures = self._stand_right_textures
    self.walk_left_textures = self._walk_left_textures
    self.walk_right_textures = self._walk_right_textures
    self.walk_up_textures = self._walk_up_textures
    self.walk_down_textures = self._walk_down_textures

#This is the main class, it controlls the levels, room generation, coins, controlls the players and handles input, logic, rendering for the game loop
class Game(arcade.Window):
  #Setup required for all levels
  def setup(self):
    #An arcade.SpriteList() is a list of sprites that has extra functionality and can be rendered easily and performantly
    #Setup all tiles that the characters can move through
    self.static_no_collision = arcade.SpriteList()
    #Setup all tiles that the characters cannot move through
    self.static_collision = arcade.SpriteList()
    #Setup all tiles that moves the characters to the next room/level
    self.exits = arcade.SpriteList()
    #Setup all tiles that moves the characters to the previous room
    self.entrances = arcade.SpriteList()

    self.coins = arcade.SpriteList()

    #Create a guard for each position passed in initialization and assign them the corresponding patrol passed in initialization
    self.guards = []
    for i in range(len(self.level_guard_positions[self.level_index])):
       guard = Guard(1, guard_textures[0], guard_textures[1], guard_textures[2], guard_textures[3], guard_textures[4], guard_textures[5], guard_textures[6], guard_textures[7], guard_textures[8], guard_textures[9], guard_textures[10], guard_textures[11], 5, self.static_collision, 1.25, self.level_guard_patrols[self.level_index][i], 6)
       guard.guard_setup(self.level_guard_positions[self.level_index][i][0], self.level_guard_positions[self.level_index][i][1])
       self.guards.append(guard)
    #Create a coins 
    for i in range(len(self.level_coin_positions[self.level_index])):
      self.coins.append(arcade.Sprite(special["coin 1"], center_x = self.level_coin_positions[self.level_index][i][0], center_y = self.level_coin_positions[self.level_index][i][1]))
    #sets up all the textures for player1
    self.player_1 = Character(1, player_1_textures[0], player_1_textures[1], player_1_textures[2], player_1_textures[3], player_1_textures[4], player_1_textures[5], 5, self.static_collision, 2)
    #sets up all the textures for player1
    self.player_2 = Character(1, player_2_textures[0], player_2_textures[1], player_2_textures[2], player_2_textures[3], player_2_textures[4], player_2_textures[5], 5, self.static_collision, 2)

  #Using fuctions to setup levels as a pose to classes although lengthy, its simpler and easier to cator to a specific level
  def level_1(self):
    #Sets the level index to allow the class the know the current level,
    #Its being set here instead of being added and subtracted to when colliding with entrances and exits to avoid misalignment
    self.level_index = 0
    #Calls the default setup
    self.setup()
    #Sets up the sprites for the room
    self.create_room(rooms.room_1, 0, 0, 24)
    #Sets up the players at specified coordinates
    self.player_1.setup(100, 100)
    self.player_2.setup(100, 100)

  def level_2(self):
    self.level_index = 1
    self.setup()
    self.create_room(rooms.room_2, 0, 0, 24)
    self.player_1.setup(100, 100)
    self.player_2.setup(100, 100)

  def level_3(self):
    self.level_index = 2
    self.setup()
    self.create_room(rooms.room_3, 0, 0, 24)
    self.player_1.setup(100, 100)
    self.player_2.setup(100, 100)
 
  def level_4(self):
    self.level_index = 3
    self.setup()
    self.create_room(rooms.room_4, 0, 0, 24)
    self.player_1.setup(100, 100)
    self.player_2.setup(100, 100)

  def level_5(self):
    self.level_index = 4
    self.setup()
    self.create_room(rooms.room_5, 0, 0, 24)
    self.player_1.setup(100, 100)
    self.player_2.setup(100, 100)

  def level_6(self):
    self.level_index = 5
    self.setup()
    self.create_room(rooms.room_6, 0, 0, 24)
    self.player_1.setup(100, 100)
    self.player_2.setup(100, 100)

  def level_7(self):
    self.level_index = 6
    self.setup()
    self.create_room(rooms.room_7, 0, 0, 24)
    self.player_1.setup(100, 100)
    self.player_2.setup(100, 100)



  def game_over(self):
    #Set all the variables to their null states
    self.static_no_collision = arcade.SpriteList()
    self.static_collision = arcade.SpriteList()
    self.exits = arcade.SpriteList()
    self.entrances = arcade.SpriteList()
    self.coins = arcade.SpriteList()
    self.guards = []

  def __init__(self, width, height, title, view, level_guard_positions, level_guard_patrols, coin_counts, level_dimensions):
    #Initialize the parent class (a window)
    super().__init__(width, height, title)
    #List of our level functions
    self.levels = [self.level_1, self.level_2, self.level_3, self.level_4, self.level_5, self.level_6, self.level_7]
    #Level index allows the class to determine the current level
    self.level_index = 0
    #The FOV around the midpoint of the players ontop of it being scaled to the distance between them
    self.view = view
    #3D List containing posistions of guards for specific levels
    self.level_guard_positions = level_guard_positions
    #2D List containing patrols of guards for specific levels
    self.level_guard_patrols = level_guard_patrols
    #3D List containing positions of coins for specific levels
    #The level coin positions are randomly generated here
    self.level_coin_positions = []
    for a in range(len(coin_counts)):
      coin_positions = []
      for b in range(coin_counts[a]):
        coin_positions.append([random.randint(0, level_dimensions[a][0]), random.randint(0, level_dimensions[a][1])])
      self.level_coin_positions.append(coin_positions)
    #This is each players cash, measure of your success!
    self.player_1_cash = 0
    self.player_2_cash = 0
    #Stored guard collisions used for game over functionality
    self.guard_collisions = 0
    #Queued time for game over if the player does not escape his grasp!
    self.game_over_time = 0
  
  def create_room(self, room, room_x, room_y, tile_size): #room_x and room_y should represent the bottom left of the room
    #Create the tilemapste 
    for y in range(0, len(room)):
      for x in range(0, len(room[0])):
        for i in range(len(static_render_priorities)):
          if(static_render_priorities.index(room[-y - 1][x]) == i):
            if(room[-y - 1][x] in static_no_collision):
              self.static_no_collision.append(arcade.Sprite(static_no_collision[room[-y - 1][x]], 1, center_x = x * tile_size + room_x, center_y = y * tile_size + room_y))
            elif(room[-y - 1][x] in static_collision):
              self.static_collision.append(arcade.Sprite(static_collision[room[-y - 1][x]], 1, center_x = x * tile_size + room_x, center_y = y * tile_size + room_y))
            elif(room[-y - 1][x] in exits):
                self.exits.append(arcade.Sprite(exits[room[-y - 1][x]], 1, center_x = x * tile_size + room_x, center_y = y * tile_size + room_y))
            elif(room[-y - 1][x] in entrances):
              self.entrances.append(arcade.Sprite(entrances[room[-y - 1][x]], 1, center_x = x * tile_size + room_x, center_y = y * tile_size + room_y))

#--INPUT--
  def on_key_press(self, key, modifiers):
    #Sets players direction and speed to its set speed in initialization depending on input
    #PLAYER 1
    if(key == arcade.key.W):
      self.player_1.change_y = self.player_1.speed
    elif(key == arcade.key.A):
      self.player_1.change_x = -self.player_1.speed
    elif(key == arcade.key.S):
      self.player_1.change_y = -self.player_1.speed
    elif(key == arcade.key.D):
      self.player_1.change_x = self.player_1.speed
    #PLAYER 2
    if(key == arcade.key.UP):
      self.player_2.change_y = self.player_1.speed
    elif(key == arcade.key.LEFT):
      self.player_2.change_x = -self.player_1.speed
    elif(key == arcade.key.DOWN):
      self.player_2.change_y = -self.player_1.speed
    elif(key == arcade.key.RIGHT):
      self.player_2.change_x = self.player_1.speed

  def on_key_release(self, key, modifiers):
    #Stops the players depending on keys released
    #PLAYER 1
    if(key == arcade.key.W or key == arcade.key.S):
      self.player_1.change_y = 0
    elif(key == arcade.key.A or key == arcade.key.D):
      self.player_1.change_x = 0
    #PLAYER 2
    if(key == arcade.key.UP or key == arcade.key.DOWN):
      self.player_2.change_y = 0
    elif(key == arcade.key.LEFT or key == arcade.key.RIGHT):
      self.player_2.change_x = 0
#---------

#--LOGIC--
  def update(self, delta_time):

    #Updates the characters
    self.player_1.update()
    self.player_2.update()
    
    #Sets the center of the viewport to be inbetween the players and scale to the distance between them creating a zoom effect
    
    midpoint = ((self.player_1.center_x + self.player_2.center_x) / 2, (self.player_1.center_y + self.player_2.center_y) / 2)
    distance = arcade.get_distance_between_sprites(self.player_1, self.player_2)
    arcade.set_viewport(midpoint[0] - distance - self.view, midpoint[0] + distance + self.view, midpoint[1] - distance - self.view, midpoint[1] + distance + self.view)
    
    
    #--COLLISIONS--
    #Checks if both players are colliding with any exits, if so, setup the next level
    if(arcade.check_for_collision_with_list(self.player_1, self.exits) and arcade.check_for_collision_with_list(self.player_2, self.exits)):
      print("Player 1 Cash:" + str(self.player_1_cash) + "\n" + "Player 2 Cash:"+ str(self.player_2_cash) + "\n")
      self.levels[self.level_index + 1]()
    #Checks if both players are colliding with any entrances, if so setup the previous level
    if(arcade.check_for_collision_with_list(self.player_1, self.entrances) and arcade.check_for_collision_with_list(self.player_2, self.entrances)):
      print("Player 1 Cash:" + str(self.player_1_cash-1) +"\n","Player 2 Cash:"+ str(self.player_2_cash) +"\n")
      self.levels[self.level_index - 1]()
    #Destroys any coins colliding with player_1 as well as adding to player_1's cash
    player_1_coin_collisions = arcade.check_for_collision_with_list(self.player_1, self.coins)
    for i in player_1_coin_collisions:
      self.level_coin_positions[self.level_index].remove([i.center_x, i.center_y])
      self.coins.remove(i)
      self.player_1_cash += 1
    #Destroys any coins colliding with player_2 as well as adding to player_2's cash
    player_2_coin_collisions = arcade.check_for_collision_with_list(self.player_2, self.coins)
    for i in player_2_coin_collisions:
      self.level_coin_positions[self.level_index].remove([i.center_x, i.center_y])
      self.coins.remove(i)
      self.player_2_cash += 1
    #Update Guards and detect collisions
    collision = False
    for i in self.guards:
      i.guard_update()
      if(i.alerted == True):
        if(arcade.get_distance_between_sprites(self.player_1, i) < arcade.get_distance_between_sprites(self.player_2, i)):
          i.target = [self.player_1.center_x, self.player_1.center_y]
        else:
          i.target = [self.player_2.center_x, self.player_2.center_y]

      if(arcade.check_for_collision(self.player_1, i)):
        i.alert()
        collision = True
      if(arcade.check_for_collision(self.player_2, i)):
        i.alert()
        collision = True

    if(collision == True):
      self.guard_collisions += 1
      if(self.guard_collisions == 1):
        self.game_over_time = time.time() + 2
    else:
      self.guard_collisions = 0
      self.game_over_time = 0

    if(self.game_over_time != 0):
      if(time.time() >= self.game_over_time):
        self.game_over()
#---------
#--RENDERING--
  def on_draw(self):
    arcade.start_render()
    self.static_no_collision.draw()
    self.static_collision.draw()
    self.exits.draw()
    self.entrances.draw()
    self.coins.draw()
    for i in self.guards:
      i.draw()
    self.player_1.draw()
    self.player_2.draw()
    
#-------------
#Creating the game, parameters: 
#window width, window height, window title, view around players, 3D list (1st dimension: levels, 2nd dimension: guard positions for the corrresponding level, 3rd dimension: the x and y component of the posistion), 2D list (1st dimension: levels, guard patrols for the corresponding level), list (coin coint for each level), 2D list (1st dimension: level, 2nd dimension: level x and y boundaries for the random coin positioning)
game = Game(800, 800, "Tower Heist", 100, 
[[[62, 268]],
 [[311, 384], [71.5, 456], [396, 302]], [[259.5, 146], [501.5, 178], [357.5, 266], [575.5, 344], [677.5, 296], [571.5, 520]],
[[77.5, 32], [260, 520], [251.5, 32], [349.5,520], [445.5, 32], [540.5,520], [638.5, 32],[732.5, 520]], [[192.5, 52], [71.5, 68], [71.5,180], [551, 44], [840.5, 208]], [[140, 48],[140, 72], [140, 96], [140, 120], [820, 48], [820, 72], [820, 96], [820, 120]], [[132, 40],[132, 88], [132, 136], [132,230], [132,278], [132,326]]],
[[patrol_1], 
[patrol_3, patrol_2, patrol_3], 
[patrol_2, patrol_2, patrol_2, patrol_2, patrol_2, patrol_2], 
[patrol_3, patrol_3, patrol_3, patrol_3, patrol_3, patrol_3, patrol_3, patrol_3], 
[patrol_1, patrol_4, patrol_4, patrol_4, patrol_5], 
[patrol_6, patrol_6, patrol_6, patrol_6, patrol_7, patrol_7, patrol_7, patrol_7], 
[patrol_6, patrol_6, patrol_6, patrol_6, patrol_6, patrol_6]],
[10, 10, 10, 10, 10, 10, 10], 
[[925, 550], [925, 550], [925, 550], [925, 550], [925, 550], [925, 550], [925, 550]])
game.levels[0]()
arcade.run()