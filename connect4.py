
O = """ .----------------. 
| .--------------. |
| | \033[34m    ____ \033[0m    | |
| | \033[34m  .'    `. \033[0m  | |
| | \033[34m /  .--.  \\ \033[0m | |
| | \033[34m | |    | | \033[0m | |
| | \033[34m \\  `--'  / \033[0m | |
| |  \033[34m `.____.'  \033[0m | |
| |              | |
| '--------------' |
 '----------------' """

X = """ .----------------. 
| .--------------. |
| | \033[31m    ____ \033[0m    | |
| | \033[31m  .'    `. \033[0m  | |
| | \033[31m /  .--.  \\ \033[0m | |
| | \033[31m | |    | | \033[0m | |
| | \033[31m \\  `--'  / \033[0m | |
| |  \033[31m `.____.'  \033[0m | |
| |              | |
| '--------------' |
 '----------------' """

B = r""" .----------------. 
| .--------------. |
| |              | |
| |              | |
| |              | |
| |              | |
| |              | |
| |              | |
| |              | |
| '--------------' |
 '----------------' """

NUMS = [
r"""
 .----------------. 
| .--------------. |
| |     __       | |
| |    /  |      | |
| |    `| |      | |
| |     | |      | |
| |    _| |_     | |
| |   |_____|    | |
| |              | |
| '--------------' |
 '----------------' 
""",
r"""
 .----------------. 
| .--------------. |
| |    _____     | |
| |   / ___ `.   | |
| |  |_/___) |   | |
| |   .'____.'   | |
| |  / /____     | |
| |  |_______|   | |
| |              | |
| '--------------' |
 '----------------' 
""",
r"""
 .----------------. 
| .--------------. |
| |    ______    | |
| |   / ____ `.  | |
| |   `'  __) |  | |
| |   _  |__ '.  | |
| |  | \____) |  | |
| |   \______.'  | |
| |              | |
| '--------------' |
 '----------------' 
""",
r"""
 .----------------. 
| .--------------. |
| |   _    _     | |
| |  | |  | |    | |
| |  | |__| |_   | |
| |  |____   _|  | |
| |      _| |_   | |
| |     |_____|  | |
| |              | |
| '--------------' |
 '----------------' 
""",
r"""
 .----------------. 
| .--------------. |
| |   _______    | |
| |  |  _____|   | |
| |  | |____     | |
| |  '_.____''.  | |
| |  | \____) |  | |
| |   \______.'  | |
| |              | |
| '--------------' |
 '----------------' 
""",
r"""
 .----------------. 
| .--------------. |
| |    ______    | |
| |  .' ____ \   | |
| |  | |____\_|  | |
| |  | '____`'.  | |
| |  | (____) |  | |
| |  '.______.'  | |
| |              | |
| '--------------' |
 '----------------' 
""",
r"""
 .----------------. 
| .--------------. |
| |   _______    | |
| |  |  ___  |   | |
| |  |_/  / /    | |
| |      / /     | |
| |     / /      | |
| |    /_/       | |
| |              | |
| '--------------' |
 '----------------' 
""",
r"""
 .----------------. 
| .--------------. |
| |     ____     | |
| |   .' __ '.   | |
| |   | (__) |   | |
| |   .`____'.   | |
| |  | (____) |  | |
| |  `.______.'  | |
| |              | |
| '--------------' |
 '----------------' 
""",
r"""
 .----------------. 
| .--------------. |
| |    ______    | |
| |  .' ____ '.  | |
| |  | (____) |  | |
| |  '_.____. |  | |
| |  | \____| |  | |
| |   \______,'  | |
| |              | |
| '--------------' |
 '----------------' 
"""

]


NUMS = [num[1:] for num in NUMS]

GAME_OVER = r"""
                                                                                                             
                                     ____                        ,----..                                     
  ,----..      ,---,               ,'  , `.    ,---,.           /   /   \                  ,---,.,-.----.    
 /   /   \    '  .' \           ,-+-,.' _ |  ,'  .' |          /   .     :        ,---.  ,'  .' |\    /  \   
|   :     :  /  ;    '.      ,-+-. ;   , ||,---.'   |         .   /   ;.  \      /__./|,---.'   |;   :    \  
.   |  ;. / :  :       \    ,--.'|'   |  ;||   |   .'        .   ;   /  ` ; ,---.;  ; ||   |   .'|   | .\ :  
.   ; /--`  :  |   /\   \  |   |  ,', |  '::   :  |-,        ;   |  ; \ ; |/___/ \  | |:   :  |-,.   : |: |  
;   | ;  __ |  :  ' ;.   : |   | /  | |  ||:   |  ;/|        |   :  | ; | '\   ;  \ ' |:   |  ;/||   |  \ :  
|   : |.' .'|  |  ;/  \   \'   | :  | :  |,|   :   .'        .   |  ' ' ' : \   \  \: ||   :   .'|   : .  /  
.   | '_.' :'  :  | \  \ ,';   . |  ; |--' |   |  |-,        '   ;  \; /  |  ;   \  ' .|   |  |-,;   | |  \  
'   ; : \  ||  |  '  '--'  |   : |  | ,    '   :  ;/|         \   \  ',  /    \   \   ''   :  ;/||   | ;\  \ 
'   | '/  .'|  :  :        |   : '  |/     |   |    \          ;   :    /      \   `  ;|   |    \:   ' | \.' 
|   :    /  |  | ,'        ;   | |`-'      |   :   .'           \   \ .'        :   \ ||   :   .':   : :-'   
 \   \ .'   `--''          |   ;/          |   | ,'              `---`           '---" |   | ,'  |   |.'     
  `---`                    '---'           `----'                                      `----'    `---'       
                                                                                                             
"""

O_WIN = """\033[34m
  /$$$$$$        /$$      /$$ /$$$$$$ /$$   /$$  /$$$$$$ 
 /$$__  $$      | $$  /$ | $$|_  $$_/| $$$ | $$ /$$__  $$
| $$  \\ $$      | $$ /$$$| $$  | $$  | $$$$| $$| $$  \\__/
| $$  | $$      | $$/$$ $$ $$  | $$  | $$ $$ $$|  $$$$$$ 
| $$  | $$      | $$$$_  $$$$  | $$  | $$  $$$$ \\____  $$
| $$  | $$      | $$$/ \\  $$$  | $$  | $$\\  $$$ /$$  \\ $$
|  $$$$$$/      | $$/   \\  $$ /$$$$$$| $$ \\  $$|  $$$$$$/
 \\______/       |__/     \\__/|______/|__/  \\__/ \\______/ 
\033[0m
                                                          
"""
X_WIN = """\033[31m
  /$$$$$$        /$$      /$$ /$$$$$$ /$$   /$$  /$$$$$$ 
 /$$__  $$      | $$  /$ | $$|_  $$_/| $$$ | $$ /$$__  $$
| $$  \\ $$      | $$ /$$$| $$  | $$  | $$$$| $$| $$  \\__/
| $$  | $$      | $$/$$ $$ $$  | $$  | $$ $$ $$|  $$$$$$ 
| $$  | $$      | $$$$_  $$$$  | $$  | $$  $$$$ \\____  $$
| $$  | $$      | $$$/ \\  $$$  | $$  | $$\\  $$$ /$$  \\ $$
|  $$$$$$/      | $$/   \\  $$ /$$$$$$| $$ \\  $$|  $$$$$$/
 \\______/       |__/     \\__/|______/|__/  \\__/ \\______/ 
\033[0m
                                                          
"""

DRAW = """
 /$$$$$$$$ /$$$$$$ /$$$$$$$$ /$$
|__  $$__/|_  $$_/| $$_____/| $$
   | $$     | $$  | $$      | $$
   | $$     | $$  | $$$$$   | $$
   | $$     | $$  | $$__/   |__/
   | $$     | $$  | $$          
   | $$    /$$$$$$| $$$$$$$$ /$$
   |__/   |______/|________/|__/
                                                               
                                
"""

class Connect4:
    def __init__(self, width, height, O, X, B, nums):
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        self.O = O
        self.X = X
        self.B = B
        self.width = width
        self.height = height
        self.nums = nums


    def __str__(self):
        out = ""
       
        for j,row in enumerate(self.board):
            for i in range(len(self.B.split("\n"))):
                for k,cell in enumerate(row):
                    if cell == 0:
                        if j == 0:
                            out += self.nums[k].split("\n")[i]
                        else:
                            out += self.B.split("\n")[i]
                    elif cell == 1:
                        out += self.X.split("\n")[i]
                    elif cell == 2:
                        out += self.O.split("\n")[i]
                out += "\n"
            out += '-' * len(self.B.split("\n")[0]) * self.width + "\n"
        return out

    def place_token(self, col, player):
        if col > self.width or col < 1:
            return False
        for j in range(self.height):
            i = self.height - j - 1
            if self.board[i][col - 1] == 0:
                self.board[i][col - 1] = player
                return True
        return False

board = Connect4(6,7, O, X, B, NUMS)
print(board)
while True:
    while board.place_token(int(input("Enter column Player 1: ")), 1) == False:
        print("Invalid move")
    print(board)

    while board.place_token(int(input("Enter column Player 2: ")), 2) == False:
        print("Invalid move")
    print(board)

#Actual flow of game here
