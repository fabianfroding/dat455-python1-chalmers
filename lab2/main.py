# Imports everything from both model and graphics
from gamemodel import *
from gamegraphics import *

# Here is a nice little method you get for free
# It fires a shot for the current player and animates it until it stops
def graphicFire(game, angle, vel):
    player = game.getCurrentPlayer()
    # create a shot and track until it hits ground or leaves window
    gproj = player.fire(angle, vel)
    while gproj.isMoving():
        gproj.update(1/50)
        update(50)
    return gproj

def graphicPlay():
    # TODO: This is where you implement the game loop
    # HINT: Creating a GraphicGame is a good start. 
    # HINT: You can look at the text interface for some inspiration
    # Note that this code should not directly work with any drawing or such, all that is done by the methods in the classes
    game = GraphicGame(Game(10, 3))
    game.newRound()

    inputDialog = InputDialog(0, 0, game.getCurrentWind())

    while(True):
        choice = inputDialog.interact()

        if choice == "Quit":
            inputDialog.close()
            game.getWindow().close()
            break
        else:
            (ang, vel) = inputDialog.getValues()
            print(ang)
            print(vel)
            graphicFire(game, ang, vel)



# Run the game with graphical interface
graphicPlay()