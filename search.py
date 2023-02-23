from googlesearch import search
import random
try:
    hancok2 ="""
\33[31;1m
            .--,       .--,
           ( (  \.---./  ) )
            '.__/o   o\__.'
               {=  ^  =}
                >  -  <
 ___________.""`-------`"".____________
/  o                            O      |          \33[37;1mAuthor  : HedyFake \33[0;36m   
\                      o               /          \33[37;1mYoutube : CatatanNewbie \33[0;36m
/  O           \033[32;1mGoogle-Dork\33[31;1m          o  |          \33[37;1mTwiter  : @iAmHere96509046 \33[31;1m
\                                      /         __
/                                      \     _.-'  `.
\______________o__________o____________/ .-~^        `~--'
              ___)( )(___        `-.___.'
      Mhw    (((__) (__)))
"""
    print(hancok2)

except ImportError:
    hancok2 ="""
\33[32;1m
    :::      :::::::      :::     
   :+:      :+:   :+:    :+:      
  +:+ +:+   +:+  :+:+   +:+ +:+   \033[35;1mImport google Not Found.!!\33[32;1m
 +#+  +:+   +#+ + +:+  +#+  +:+   
+#+#+#+#+#+ +#+#  +#+ +#+#+#+#+#+ 
      #+#   #+#   #+#       #+#   
      ###    #######        ###   

"""
    print(hancok2)



query = input('[\33[37;1m>\33[31;1m]\033[34;1mQuery:\033[37;1m')




hedy = open('site.txt', 'w')

for j in search(query, num_results=10, lang="en"):
    print('\033[32;1m[\033[33;1m+\033[32;1m]Found\033[35;1m-->\033[37;1m'+ j)
    hedy.write('   ' + j)

print('\x1b[6;30;42m' + '[+]Success!' + '\x1b[0m')
