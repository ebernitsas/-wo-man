#!/usr/bin/python

import random 


with open('/bin/trump_shit.txt') as fp:
	text = fp.read()

quote_num = random.randint(1,42)

#print text 
start = text.find(str(quote_num)+'.')


text = text[start:]
text = text[:text.find('--')]
quote = text



donkey = '''
___________________________________________________________

''' + quote + '''


___________________________________________________________
  \ /
   V


                          /\          /\.
                         ( \\        // )
                          \ \\      // /
                           \_\\||||//_/ 
                            \/ _  _ \ 
                           \/|(O)(O)|
                          \/ |      |  
      ___________________\/  \      /
     //                //     |____|      
    //                ||     /      \.
   //|                \|     \ 0  0 /
  // \       )         V    / \____/ 
 //   \     /        (     /
""     \   /_________|  |_/
       /  /\   /     |  ||
      /  / /  /      \  ||
      | |  | |        | ||
      | |  | |        | ||  
      |_|  |_|        |_||       
       \_\  \_\        \_\\ '''


print donkey