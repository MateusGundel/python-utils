from random import choice


def get_red_text(text):
    return f'\033[91m{text}\033[00m'
def get_green_text(text):
    return f'\033[92m{text}\033[00m'
def get_yellow_text(text):
    return f'\033[93m{text}\033[00m'
def get_light_purple_text(text):
    return f'\033[94m{text}\033[00m'
def get_purple_text(text):
    return f'\033[95m{text}\033[00m'
def get_cyan_text(text):
    return f'\033[96m{text}\033[00m'
def get_light_gray_text(text):
    return f'\033[97m{text}\033[00m'
def get_black_text(text):
    return f'\033[98m{text}\033[00m'


def get_siglas():
    alfabeto = "abcdefghijklmnopqrstuvwxyz0123456789áõãç"
    print(get_green_text("Alfabeto: "), get_yellow_text(alfabeto),
          get_green_text("\tTamanho: "), get_yellow_text(len(alfabeto)), sep=' ')
    x = 0
    siglas = []
    for char_f in alfabeto:
        for char_s in alfabeto:
            for char_t in alfabeto:
                sigla = f'{char_f}{char_s}{char_t}'
                # print(f'index:{x+1} sigla: {sigla}')
                siglas.append(sigla)
                x += 1
    print(f'\nAchou {get_yellow_text(str(x+1))} siglas...\n')
    return siglas


if __name__ == '__main__':
    siglas = get_siglas()
    confirm = 'S'
    while(confirm != 'N' and len(siglas) > 0):
        sigla = choice(siglas)
        siglas.remove(sigla)

        print(f'{get_green_text("Sigla:")} {get_yellow_text(sigla.upper())}', end='\t\t')
        print(
            f'{get_green_text("Restam:")} {get_yellow_text(str(len(siglas)))} siglas', end='\t\t')
        print(f'Digite {get_yellow_text("N")} para sair...', end='\n')

        confirm = input().upper()

    input('RIP')
