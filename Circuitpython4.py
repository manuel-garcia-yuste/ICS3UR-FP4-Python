#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : November 2019
# Circuit python 4


def main():
    # this function is a scene

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 10, 8)

    # create a sprite
    # parameters (image_bank, image # in bank, x, y)
    alien = stage.Sprite(image_bank_1, 64, 56)
    sprites.append(alien)
    ship = stage.Sprite(image_bank_1, 5, 74, 56)
    sprites.insert(0, ship)  # insert at the top of sprites list

    # create a stage for the background to show up on
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers, items show up in order
    game.layers = sprites + [background]
    # render the background and initial location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        # print(keys)

        if keys & ugame, K_X:
            # prints("A")
            pass
        if keys & ugame, K_0:
            # print("B")
            pass
        if keys & ugame, K_START:
            # print("K_START")
            pass
        if keys & ugame, K_SELECT:
            # print("K_SELECT")
            pass
        if keys & ugame, K_RIGHT:
            ship.move(ship.x + 1, ship.y)
            pass
        if keys & ugame, K_LEFT:
            ship.move(ship.x - 1, ship)
            pass
        if keys & ugame, K_DOWN:
            ship.move(ship.x, ship.y + 1)
            pass

        # update game logic

        # redraw sprite list
        game.render_sprites(sprites)
        game.ticks()  # wait until refresh rate finishes


if __name__ == "__main__":
    main()
