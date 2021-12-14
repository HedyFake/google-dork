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

TLD = ["com","com.tw","co.in","be","de","co.uk","co.ma","dz","ru","ca"]

query = input('[\33[37;1m>\33[31;1m]\033[34;1mQuery:\033[37;1m')

site = input('\033[36;1m[\033[1;38;5;208m>\033[36;1m]\033[32;1mSite:\033[37;1m')

tld = site

hedy = open('site.txt', 'w')

for j in search(query, tld, num=10, stop=95, pause=2):
    print('\033[32;1m[\033[33;1m+\033[32;1m]Found\033[35;1m-->\033[37;1m'+ j)
    print('\x1b[6;30;42m' + '[+]Success!' + '\x1b[0m')
    hedy.write('_',+ j)