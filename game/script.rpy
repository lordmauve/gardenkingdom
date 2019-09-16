# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Boy")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg sunny

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    "It's a hot and sunny day"

    "There's nothing to do..."

    "I'm so bored..."

    "What's that at the end of the garden?"

    scene bg toadstool

    "A little red toadstool, how strange.\nI don't remember seeing that before."

    # This ends the game.

    return
