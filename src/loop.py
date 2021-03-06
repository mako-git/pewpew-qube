import pew

"""
THIS IS THE GENERAL STRUCTURE OF AN INSTRUCTION SET
class instruction_set_H_CX:
   def __init__(self):
       self.state = <initial_state>

   def key_pressed(self, key):
       # Update self.state here
       
   def get_current_screen(self):
       # Calculate screen using current self.state
       return screen
"""

start_screens = ((
                         (0, 0, 0, 0, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 0, 0, 0),
                         (0, 0, 0, 3, 3, 0, 0, 0),
                         (0, 0, 0, 3, 3, 0, 0, 0),
                         (0, 0, 0, 0, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 0, 0, 0)
                     ),
                     (
                         (0, 0, 0, 0, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 0, 0, 0),
                         (0, 0, 3, 3, 3, 3, 0, 0),
                         (0, 0, 3, 2, 2, 3, 0, 0),
                         (0, 0, 3, 2, 2, 3, 0, 0),
                         (0, 0, 3, 3, 3, 3, 0, 0),
                         (0, 0, 0, 0, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 0, 0, 0)
                     ),
                     (
                         (0, 0, 0, 0, 0, 0, 0, 0),
                         (0, 3, 3, 3, 3, 3, 3, 0),
                         (0, 3, 2, 2, 2, 2, 3, 0),
                         (0, 3, 2, 1, 1, 2, 3, 0),
                         (0, 3, 2, 1, 1, 2, 3, 0),
                         (0, 3, 2, 2, 2, 2, 3, 0),
                         (0, 3, 3, 3, 3, 3, 3, 0),
                         (0, 0, 0, 0, 0, 0, 0, 0)
                     ),
                     (
                         (3, 3, 3, 3, 3, 3, 3, 3),
                         (3, 2, 2, 2, 2, 2, 2, 3),
                         (3, 2, 1, 1, 1, 1, 2, 3),
                         (3, 2, 1, 0, 0, 1, 2, 3),
                         (3, 2, 1, 0, 0, 1, 2, 3),
                         (3, 2, 1, 1, 1, 1, 2, 3),
                         (3, 2, 2, 2, 2, 2, 2, 3),
                         (3, 3, 3, 3, 3, 3, 3, 3)
                     ))

final_screens = ((
                     (1, 0, 0, 0, 0, 0, 0, 1),
                     (0, 2, 0, 0, 0, 0, 2, 0),
                     (0, 0, 3, 0, 0, 3, 0, 0),
                     (0, 0, 0, 3, 3, 0, 0, 0),
                     (0, 0, 0, 3, 3, 0, 0, 0),
                     (0, 0, 3, 0, 0, 3, 0, 0),
                     (0, 2, 0, 0, 0, 0, 2, 0),
                     (1, 0, 0, 0, 0, 0, 0, 1),
),
                 (
                     (0, 0, 0, 0, 0, 0, 0, 0),
                     (0, 1, 0, 0, 0, 0, 1, 0),
                     (0, 0, 2, 0, 0, 2, 0, 0),
                     (0, 0, 0, 3, 3, 0, 0, 0),
                     (0, 0, 0, 3, 3, 0, 0, 0),
                     (0, 0, 2, 0, 0, 2, 0, 0),
                     (0, 1, 0, 0, 0, 0, 1, 0),
                     (0, 0, 0, 0, 0, 0, 0, 0),
),
                 (
                     (0, 0, 0, 0, 0, 0, 0, 0),
                     (0, 0, 0, 0, 0, 0, 0, 0),
                     (0, 0, 1, 0, 0, 1, 0, 0),
                     (0, 0, 0, 2, 2, 0, 0, 0),
                     (0, 0, 0, 2, 2, 0, 0, 0),
                     (0, 0, 1, 0, 0, 1, 0, 0),
                     (0, 0, 0, 0, 0, 0, 0, 0),
                     (0, 0, 0, 0, 0, 0, 0, 0),
),
                 (
                     (0, 0, 0, 0, 0, 0, 0, 0),
                     (0, 0, 0, 0, 0, 0, 0, 0),
                     (0, 0, 0, 0, 0, 0, 0, 0),
                     (0, 0, 0, 1, 1, 0, 0, 0),
                     (0, 0, 0, 1, 1, 0, 0, 0),
                     (0, 0, 0, 0, 0, 0, 0, 0),
                     (0, 0, 0, 0, 0, 0, 0, 0),
                     (0, 0, 0, 0, 0, 0, 0, 0),
))

blank_screen = (
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
)


def main_loop(ins):
    """
    main loop of the program. Takes an instruction
    set and calls it iteratively to process the
    pushed buttons and update the display.
    Button 'O' exits the loop
    """
    # initialize PewPew console
    pew.init()

    # Load start screens
    for start_screen in start_screens:
        pew.show(pew.Pix.from_iter(start_screen))
        pew.tick(0.2)
    pew.show(pew.Pix.from_iter(blank_screen))
    pew.tick(0.5)
    
    # initialization stage
    pew.show(ins.get_current_screen())

    # flags used throughout the loop
    bool_loop = True
    old_keys = 0
    
    while bool_loop:
        keys = pew.keys()
    
        if keys != 0 and keys != old_keys:
            old_keys = keys
    
            # dispatch the pushed buttons
            if keys & pew.K_X:
                value = pew.K_X
            elif keys & pew.K_DOWN:
                value = pew.K_DOWN
            elif keys & pew.K_LEFT:
                value = pew.K_LEFT
            elif keys & pew.K_RIGHT:
                value = pew.K_RIGHT
            elif keys & pew.K_UP:
                value = pew.K_UP
            elif keys & pew.K_O:
                value = pew.K_O
                bool_loop = False
            else:
                value = 0

            ins.key_pressed(value)
    
        elif keys == 0:
            # this is necessary to be able to push 
            # a button twice in a row
            old_keys = keys
    
        # update the screen and wait for 20ms
        pew.show(ins.get_current_screen())
        pew.tick(0.02)
        
    # the program has been terminated. 
    # display the final sequence
    for final_screen in final_screens:
        pew.show(pew.Pix.from_iter(final_screen))
        pew.tick(0.2)
    pew.show(pew.Pix.from_iter(blank_screen))
    pew.tick(0.2)
