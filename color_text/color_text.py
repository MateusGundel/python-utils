'''Colors class: reset all colors with colors.reset;
two sub classes fg for foreground and bg for background;
use as colors.subclass.colorname.
i.e. colors.fg.red or colors.bg.green 
also, the generic bold, disable, underline, reverse, strike through, 
and invisible work with the main class i.e. colors.bold'''


class Colors: 

    @staticmethod
    def format_text(text, foreground='', background='', style=''):
       return f'{style}{background}{foreground}{text}'

    class Style:
        reset='\033[0m'
        bold='\033[01m'
        disable='\033[02m'
        underline='\033[04m'
        reverse='\033[07m'
        strikethrough='\033[09m'
        invisible='\033[08m'

    class Foreground: 
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'

    class Background: 
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'
  
if __name__ == "__main__":
    print(Colors.format_text('normal'))

    print(Colors.format_text('Fonte verde - Fundo normal', Colors.Foreground.green))
    print(Colors.Style.reset)

    print(Colors.format_text('Fonte normal - Fundo verde', Colors.Background.green))
    print(Colors.Style.reset)

    print(Colors.format_text('Fundo verde - Fonte verde',
                            Colors.Foreground.green, Colors.Background.green))
    print(Colors.Style.reset)

    print(Colors.format_text('Fundo verde - Fonte verde - Style Bold',
                            Colors.Foreground.green, Colors.Background.green, Colors.Style.bold))
    print(Colors.Style.reset)
    
    input()

