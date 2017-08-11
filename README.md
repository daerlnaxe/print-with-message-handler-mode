# print-with-message-handler-mode
A function print with 2 modes, a normal mode to act like the old and a mode to work with a message handler, to inject code
directly in the message, to struct it differently in order to manage it more easyly when intercepted after.


    Can Work with another script i did: intercepteur.py if you don't want to develop your own.

    A function print with 2 modes, a normal mode to act like the old and a mode to work with a message handler, to inject code
    directly in the message, to struct it differently in order to manage it more easyly when intercepted after.

    Can Work with another script i did: intercepteur.py if you don't want to develop your own

    Sorry for my english, i'm french

    Just a word: Seriously i don't know at all if something like this exists, i'm a great noob.
    Just 1 month with Python. I made it that for me, i said to myself, perhaps it can be useful for others, so....

    This function can act as the normal printing and permit to interface in the other mode with a message handler
    For the second part: it write at the end the message for the part councerning the interfacing with a handler because i think '\n' parasite them.)

    To interface with a message handler, you must intercept 'write' like this: sys.stdout = 'yourclass'
    (to return to the normal writing: sys.stdout = sys.__stdout__ )
    In this mode the message is prefixed with a name of handler and a level of message (so you can redirect flux as
    by the handler, than by the level message or both.

    Your message handler must manage by itself the writing.

    Here a little code to help you, you can create a terminal mode at the ini of your message handler to redirect to the
    terminal, and redirect to another file in same time, like this:

    def__init__self():
        self.terminal = sys.stdout
        self.logger = open('./retest', mode='a')

    And, in your managing function you will call this to redirect your output to the terminal AND a file.
    There is no limit to redirect your flux if like me you pass in your manager a dialogue module with all the informations needed.

    I hope you will enjoy it

    normal mode can have, like print:
        - sep: separator between value
        - end: what you want to ending your messager
        - file: to redirect the output to a file

    mode with handler:
        - mHandler: handler's name
        - lvlMess: level of your message (you can use what you want, numbers, string...)
        - sepInfo: The separator string you want to use to adapt this to your needs
        - start: No common thing with a handler message, but i use it to begin a message by what i want. Sometimes a '\n'
