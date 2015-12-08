# MediaKeys

## Description
This script sends Windows media key event to the system based on first parameter to the script that gets looked up in
a dictionary and mapped to an appropriate command

It is a python script, so you have to have Python3 installed

## Usage
I use it by having created following shortcuts (.lnk) in my system path

<table>
<tr><th>location of the item</th><th>name</th></tr>
<tr><td>"C:\Python34\python.exe c:\projects\personal\source\MediaKeys.py p"</td><td>p</td></tr>
<tr><td>"C:\Python34\python.exe c:\projects\personal\source\MediaKeys.py n"</td><td>n</td></tr>
<tr><td>"C:\Python34\python.exe c:\projects\personal\source\MediaKeys.py pp"</td><td>pp</td></tr>
<tr><td>"C:\Python34\python.exe c:\projects\personal\source\MediaKeys.py u"</td><td>u</td></tr>
<tr><td>"C:\Python34\python.exe c:\projects\personal\source\MediaKeys.py d"</td><td>d</td></tr>
</table>


Now I can control music from my non Media Key enabled keyboard by:
To play/pause
Win+r, p, Enter 

To move to next song
Win+r, n, Enter

To move to previous/beginning of song
Win+r, pp, Enter

Volume Up/Down the same with u & d,

to repeat the command, just do: Win+r, Enter
I use it with MS Groove music, but is should work with any decent media player

## License
This is pretty much all taken from http://stackoverflow.com/questions/11906925/python-simulate-keydown
