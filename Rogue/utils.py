def getch():
    """Entrée de caractère unique, ne fonctionne que sur les terminaux mac/linux/windows OS"""
    try:
        import termios
        # Système POSIX. Créez et retournez un getch qui manipule le tty.
        import sys, tty
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    except ImportError:
        # Non POSIX. Renvoie le getch de msvcrt (Windows).
        import msvcrt
        return msvcrt.getch().decode('utf-8')

def _find_getch():
   """Entrée de caractère unique, ne fonctionne que sur les terminaux mac/linux/windows OS"""
   try:
       import termios
   except ImportError:
       # Non POSIX. Renvoie le getch de msvcrt (Windows).
       import msvcrt
       return lambda: msvcrt.getch().decode('utf-8')
   # POSIX system. Create and return a getch that manipulates the tty.
   import sys, tty

   def _getch():
       fd = sys.stdin.fileno()
       old_settings = termios.tcgetattr(fd)
       try:
           tty.setraw(fd)
           ch = sys.stdin.read(1)
       finally:
           termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
       return ch
   return _getch

def sign(x):
    if x > 0:
        return 1
    return -1
