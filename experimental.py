#guard dog textures
guard_dog_directories = {"guard_dog_left":"images/other_enemies/guard_dog_left.png", "guard_dog_right":"images/other_enemies/guard_dog_right.png"} ]

#there are 2 textures when the nearest player's center x is less than the guard dog and when the nearest players center x is greater than the guard dogs ie to the left and right of the guard dog
#class for the guard dog because he is weird
  class guard_dog(Character):
    def __init__(self, scale, center_x, center_y, guard_dog_right, guard_dog_left ):
      super(). __init__(scale)
      self.guard_dog_right = guard_dog_right
      self.guard_dog_left = guard_dog_left
    def setup(self, x, y):
      self.setup()
      #the guard dog does not move only rotate towards the nearest player in update
    
    
    #----------------------------------------



      '''
      #----------------guard dog TEST---------
      start_x = guard_dog.center_x
      start_y = guard_dog.center_y
      
      # Get the destination location for the guard dog
      player = arcade.get_closest_sprite(guard_dog, player_1, player_2)
      dest_x = self.player.center_x
      dest_y = self.player.center_y

      # Do math to calculate how to get the head of the dog towards the destination.
      # Calculation the angle in degrees between the start points
      # and end points. This is the angle the head of the dog will travel.
      x_diff = dest_x - start_x
      y_diff = dest_y - start_y
      angle = math.atan2(y_diff, x_diff)

      # Set the enemy to face the player.
      guard_dog.angle = math.degrees(angle)-90
      #set the dog to not look upside down when he looks at you 
      if guard_dog.center_x>player.center_x:
        #change texture to guard_dog_left
      if guard_dog.center_x<player.center_x:
        #change texture to guard_dog_right
      #-----------------------------
    '''

    #sets up all the textures for the guard dog
    #self.guard_dog = guard_dog(1, 2, 5,  guard_dog_directories["guard_dog_right"], #guard_dog_directories["guard_dog_left"])

    #Input = input("")
#if Input == "Direct Acceleration":
#   print("you have found the easter egg")#guard dog textures
guard_dog_directories = {"guard_dog_left":"images/other_enemies/guard_dog_left.png", "guard_dog_right":"images/other_enemies/guard_dog_right.png"} ]

#there are 2 textures when the nearest player's center x is less than the guard dog and when the nearest players center x is greater than the guard dogs ie to the left and right of the guard dog
#class for the guard dog because he is weird
  class guard_dog(Character):
    def __init__(self, scale, center_x, center_y, guard_dog_right, guard_dog_left ):
      super(). __init__(scale)
      self.guard_dog_right = guard_dog_right
      self.guard_dog_left = guard_dog_left
    def setup(self, x, y):
      self.setup()
      #the guard dog does not move only rotate towards the nearest player in update
    
    
    #----------------------------------------



      '''
      #----------------guard dog TEST---------
      start_x = guard_dog.center_x
      start_y = guard_dog.center_y
      
      # Get the destination location for the guard dog
      player = arcade.get_closest_sprite(guard_dog, player_1, player_2)
      dest_x = self.player.center_x
      dest_y = self.player.center_y

      # Do math to calculate how to get the head of the dog towards the destination.
      # Calculation the angle in degrees between the start points
      # and end points. This is the angle the head of the dog will travel.
      x_diff = dest_x - start_x
      y_diff = dest_y - start_y
      angle = math.atan2(y_diff, x_diff)

      # Set the enemy to face the player.
      guard_dog.angle = math.degrees(angle)-90
      #set the dog to not look upside down when he looks at you 
      if guard_dog.center_x>player.center_x:
        #change texture to guard_dog_left
      if guard_dog.center_x<player.center_x:
        #change texture to guard_dog_right
      #-----------------------------
    '''

    #sets up all the textures for the guard dog
    #self.guard_dog = guard_dog(1, 2, 5,  guard_dog_directories["guard_dog_right"], #guard_dog_directories["guard_dog_left"])

    #Input = input("")
#if Input == "Direct Acceleration":
#   print("you have found the easter egg")