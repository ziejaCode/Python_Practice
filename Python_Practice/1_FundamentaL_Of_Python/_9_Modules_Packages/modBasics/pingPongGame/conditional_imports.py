# game.py
# import the draw module
#import draw_textual
import game 

visual_mode = 0

if visual_mode:
    # in visual mode, we draw using graphics
    import draw_visual as draw
else:
    # in textual mode, we print out text
    import draw_textual as draw


def main():
    result = game.play_game()
    # this can either be visual or textual depending on visual_mode
    draw.draw_game(result)


# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()