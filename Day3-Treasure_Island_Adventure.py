#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Day 3 Project: Treasure Island Adventure
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is a funny Choose-your-own-Adventure Game.
#Here, the player advances to different situations depending on what choices he/she makes.
#This was designed with puns intended for the coder's best friends.
#Do not try to misinput any choice ;)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Game_Over():
  print("""\n\n\n\n\n
                          ________________
                          \      __      /         __
                           \_____()_____/         /  )
                           '============`        /  /
                            #---\  /---#        /  /
                           (# @\| |/@  #)      /  /
                            \   (_)   /       /  /
                            |\ '---` /|      /  /
                    _______/ ||_____// \____/ o_|
                   /       \  /     \  /   / o_|
                  / |           o|        / o_| \
                 /  |  _____     |       / /   \ \
                /   |  |===|    o|      / /\    \ \
               |    |   \@/      |     / /  \    \ \
               |    |___________o|__/----)   \    \/
               |    '              ||  --)    \     |
               |___________________||  --)     \    /
                    |           o|   ''''   |   \__/
                    |            |          |
  """)
  print("You struggle with a mental breakdown trying to decide which road to take. \nPolice officers catch you and deport you to VENEZUELA.")

  print("\nGAME OVER")

print('''
*******************************************************************************
                    ____            ____            ____
                   /....\          /....\          /....\
           .-.    |::::::|    .-. |::::::|    .-. |::::::|
           | |    |::::::|    | | |::::::|    | | |::::::|
           | |    (`:'':')    | | (`:'':')    | | (`:'':')
           | |   _--|__|--__  | |.--|__|--__  | |_--|__|--__
           | |  |   ________|_|_|_  ________|_|_|_  ________|_____
           | | /    |            |  |            |  |            |
           | |/  /  |            |  |            |  |            |
           |_| |/|  |            |  |            |  |            |
          (===)| |  |  M  U  P   |  |  M  U  P   |  |  M  U  P   |
          `==='  |`-|            |`-|            |`-|            |
           | |   |`-|            |`-|            |`-|            |
           |_|   |  |            |  |            |  |            |
                 |  |            |  |            |  |            |
                 |  |            |  |            |  |            |
                 |`-|            |`-|            |`-|            |
                 |__|            |__|            |__|            |
                 /_ |            |_ |            |_ |            |
                |___`-__________-'__`-__________-'__`-__________-'
*******************************************************************************
''')
print("You are drunk and past COVID lockdown, running away from police officers.\n")
score = 0
choice = input("You arrive at a cross road. To the left you see a plain, long road. To the right, a forest which may give you an advantage. \n\nWhere do you want to go? Type \"left\" or \"right\": ").lower()

if choice == "left":
  print("\n\n\n\n\nYou run as fast as you can and come across a lake with an island in the middle of it.")
  print('''
                    _
             .''.' \    _  __
 ___         './    '. ' `'  `
    '._______.'       \
                       '.__________
                                   '-.____________
 _________________________________________________'.__________________
                                      ____________.'
                         __________.-'
      _______          .'                      
 ___.'       '.       /               '-._         
             .'\    .' ._,.__,        ____\____.o.
             '..'._/                 '-._______.-'
                                     .-'_______'-.
                                         _/    'o'
                                      .-'
                                      ''')
  score += 1

elif choice == "right":
  print('''\n\n\n\n\n
                         `;.`;'.
                     `;);.(~;(`;
                   `(;);;;;;);(::`
                    ;)(; ; ;;~;;;(;
                  `(`;;~-  -~(;~;)`)
                  ;(`;)      ;);;; ;
                `;);;(;`\ ^_/(;)~;;);
                  (;);.;)   ':);( ..(;
                  `'((;);   )(.');`:
                   |.' );)`   ); ;`.)
                   |  |( , ) ( ,;);:
                *  \  \ \WWWwWWW/;`'
                    \  \ ) .X. (
                 )   \  /  .X.  \   )
                ( (  )`/   /^\   | ( (
                 ) )   |\_/WWW\_/|  ) )
                (   )  | : |\   :\ ( ( *
                 ) ( ( wwwww wwwwww )  )
             * (    )) :::::  :::::(   (
                ) )((  ::::'   ::::. (  )
               ) (   ) ::::'(  ::::( ))   )
              ((    ( ::::' ))::::') )( (
            ( ) ) (  )  )  (( )(  ( (  ) )TS
          ((()))())((()())()()((())()())()())))
          ''')
  print("You come across CARMEN. \nHer regretful stare of deception and disappointment ultimately puts you in a coma. You wake up deported to VENEZUELA.")
  print("\nGAME OVER")

else:
  Game_Over()

if score == 1:
  choice = input("You see a friendly old lady coming on a boat. \n\nType \"wait\" to grab the boat, or \"swim\" to try swimming to the island: ").lower()

  if choice == "swim":
    print("\n\n\n\n\nYou struggle trying not to drown but somehow manage to reach the island with a cave on it.")
    score += 1

  elif choice == "wait":
    print('''\n\n\n\n\n
                            (
                          )     (
                   ___...(-------)-....___
               .-""       )    (          ""-.
         .-'``'|-._             )         _.-|
        /  .--.|   `""---...........---""`   |
       /  /    |                             |
       |  |    |                             |
        \  \   |                             |
         `\ `\ |                             |
           `\ `|                             |
           _/ /\                             /
          (__/  \                           /
       _..---""` \                         /`""---.._
    .-'           \                       /          '-.
   :               `-.__             __.-'              :
   :                  ) ""---...---"" (                 :
    '._               `"--...___...--"`              _.'
      \""--..__                              __..--""/
       '._     """----.....______.....----"""     _.'
          `""--..,,_____            _____,,..--""`
                        `"""----"""`
    ''')
    print("The old lady MARIA EUGENIA takes you on her boat. \n\nYou can't refuse her unlimited coffee offers and you end up intoxicated. You wake up deported to VENEZUELA.")
    print("\nGAME OVER")

  else:
    Game_Over()

if score == 2:
  print('''
      ______
   ,-' ;  ! `-.
  / :  !  :  . \
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|
  ''')
  choice = input("You enter the cave and you find three doors inside. \n\nType \"blue\", \"yellow\", or \"red\" to open the blue, yellow, or red door, respectively: \n").lower()

  if choice == "yellow":
    print('''\n\n\n\n\n
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
      ''')
    print("You discover a room full of GOLD BARS. You use them to convince the police officers of turning a blind eye on you.\n\nYou then carry on to win the presidency!")
    print("\nCongratulations! You did it!!")

  elif choice == "red":
    print("""\n\n\n\n\n
                      ...........     ............
                 ,..,'           ',.,'            ',..,
               ,' ,'   ~ ~~ ~~     :                ', ',
             ,' ,'    CHILE        :                  ', ',
           ,' ,'   ~~ ~~~~ ~~      :                    ', ',
         ,' ,'      VISA           :                      ', ',
       ,' ,'    ~~ ~~~~ ~~~~ ~~    :                     ~  ', ',
     ,' ,'.......................  :  ........................', ',
   ,' ,'                         ',:,'                          ', ',
 ,'  '........................     '     .........................'  ',
  ''''''''''''''''''''''''''''';''''''';''''''''''''''''''''''''''''''
                                '''''''
    """)
    print("You discover a passport with an unused and expired VISA TO CHILE. You die from depression.")
    print("\nGAME OVER")

  elif choice == "blue":
    print("""\n\n\n\n\n
                       .
                       M
                      dM
                      MMr
                     4MMML                  .
                     MMMMM.                xf
     .              "MMMMM               .MM-
      Mh..          +MMMMMM            .MMMM
      .MMM.         .MMMMML.          MMMMMh
       )MMMh.        MMMMMM         MMMMMMM
        3MMMMx.     'MMMMMMf      xnMMMMMM"
        '*MMMMM      MMMMMM.     nMMMMMMP"
          *MMMMMx    "MMMMM\    .MMMMMMM=
           *MMMMMh   "MMMMM"   JMMMMMMP
             MMMMMM   3MMMM.  dMMMMMM            .
              MMMMMM  "MMMM  .MMMMM(        .nnMP"
  =..          *MMMMx  MMM"  dMMMM"    .nnMMMMM*
    "MMn...     'MMMMr 'MM   MMM"   .nMMMMMMM*"
     "4MMMMnn..   *MMM  MM  MMP"  .dMMMMMMM""
       ^MMMMMMMMx.  *ML "M .M*  .MMMMMM**"
          *PMMMMMMhn. *x > M  .MMMM**""
             ""**MMMMhx/.h/ .=*"
                      .3P"%....
                    nP"     "*MMnx                
    """)
    print("You discover a room with an unlimited supply of MARIHUANA. You become addicted, struggle with a white-out pálida, and suddenly trip on a sidewalk and pass away.")
    print("\nGAME OVER")
  
  else:
    Game_Over()
