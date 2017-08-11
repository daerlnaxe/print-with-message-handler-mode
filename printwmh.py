#!/usr/bin/python3.6
# -*- coding: utf-8 -*-


"""
    Author: Alexandre CODOUL aka Daerlnaxe

    Version alpha 1
    créé le: 2017-08-10
    modifié le: 2017-08-10

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

"""


import sys

def printp(*args, **kwargs):
    defVal={'bwnl':'\n', 'end':'\n', 'sep':' '}
    uOkVal = { 'newline':'\u000A',}
    strOkVal = { 'newline':'\n', }


# ================== functions ==================

    def valid_str(value, name):
        if value is None: return
        if isinstance(value, str):
            return True
        else:
            raise TypeError( f'{name} must be str or None' )

# --- Check if the value is ok, need an unicode or is bad
    # deprecated in python3
    #def need_unicode(value, name):
    #    if value is None: return
    #    if isinstance(value, unicode):
    #        return 1
    #    elif isinstance(value, str):
    #        return 2
    #    else:
    #        raise TypeError(f'{name} must be None or a string')

# --- Normal mode
    def normal_mode(args):
        for i, arg in enumerate(args):
            if i:
                write(sep)
            write(arg)
        write(end)

# --- Common part
    def write(data):
        # Conversion to str if necessary
        if not isinstance(data, str):
            data = str(data)

        fp.write(data)

# --- mode with handler

    def mode_wh( args, mHandler, lvlMess, sepInfo):
        chaine = f'mHandler={mHandler}{sepInfo}'
        chaine += f'lvlMess={lvlMess}{sepInfo}'
        chaine += f'start={start}{sepInfo}'

        message = ''
        for i, arg in enumerate(args):
            if i:
                message += sep
            message += arg

        chaine += f'message={message}{sepInfo}'
        chaine += f'end={end}'

        fp.write( chaine )


# ================== Mode With Handler ==================
# --- if somebody want to redirect output
    mHandler = kwargs.pop('mHandler', None)
    valid_str( 'mHandler', mHandler )
# --- level of the message for the message handler
    lvlMess = kwargs.pop('lvlMess', None)
    valid_str( 'lvlMess', lvlMess )

# --- separator for the message handler to personnalize what you want
    sepInfo = kwargs.pop('sepInfo','::')
    valid_str( 'sepInfo', sepInfo )

# --- starting of the line
    start = kwargs.pop('start', '')
    #startNU = need_unicode(start, 'start')
    valid_str( 'start', start )

# ================== Normal ==================
# --- fp, simple rediction to a file
    fp = kwargs.pop('file', sys.stdout)         # in case of no file => redirect on terminal
    if fp is None: return                       # in case the file don't exist

# --- separator
    sep = kwargs.pop('sep', ' ')
    #sepNU = need_unicode(sep, 'sep')
    valid_str( 'sep', sep )
# --- ending of the line
    end = kwargs.pop('end', '\n')
    #endNU = need_unicode(end, 'end')
    valid_str( 'end', end )

# === No more
    if kwargs:
        raise TypeError("invalid keyword arguments to print()")
# ===
    #deprecated in python3 ?
    #if sepNU == 1 or endNU == 1:
    #    newline = u'\n'
    #    espace = u' '       'a little bit of French, omelette du/AU fromage'
    #else:
    #    newline = '\n'
    #    espace = ' '

# --- In case of nothing for sep and end
    #if sep == None:
    #    sep = ' '
    #if end == None:
    #end = '\n'


# ================== Switch =============
# --- In normal mode
    if mHandler is None:
        normal_mode( args )
# --- In case of interface with a message handler
    else:
        mode_wh( args, mHandler, lvlMess, sepInfo)
