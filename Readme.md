Problem - Word Paths

Outline

The problem is to find “word paths”. What this means is that you find a path from one word to

another word, changing one letter each step, and each intermediate word must be in the

dictionary.

We tend to use the dictionary file on a unix/linux/mac in /usr/share/dict/words. If you do not

have a copy of this file, please let us know.

Some example solutions:

rial ­> real ­> feal ­> foal ­> foul ­> foud

dung ­> dunt ­> dent ­> gent ­> geet ­> geez

jehu ­> jesu ­> jest ­> gest ­> gent ­> gena ­> guna ­> guha

yagi ­> yali ­> pali ­> palp ­> paup ­> plup ­> blup

bitt ­> butt ­> burt ­> bert ­> berm ­> berm ­> germ ­> geum ­> meum

jina ­> pina ­> pint ­> pent ­> peat ­> prat ­> pray

fike ­> fire ­> fare ­> care ­> carp ­> camp

The program should take as input the path to the word file, a start word and an end word and

print out at least one path from start to end, or something indicating there is no possible path if

appropiate.

e.g.

$ python ./wordpaths.py /usr/share/dict/words flux alem

cat ­> cog ­> cog ­> dog

Requirements

● Please send your output as one .tar.gz file to your recruitment contact

● Your software should have an appropiate basic command line utility to run

● Try to demonstrate OO methodologies where possible (e.g. encapsulation)

● Where your program is written in an interpreted language like ruby or python, please

say which version you’ve used

● Include appropriate testing routines.

● No use of third party libraries for the main code. The intent of the problem is to

demonstrate the ability to write the particular data structures & algorithms that are

most applicable to solve this problem.