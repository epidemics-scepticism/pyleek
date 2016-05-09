# pyleek
turn an .onion address into a 5 word phrase and back again
```
$ ./leek.py e facebookcorewwwi.onion
redate sheilas lifesome dowable tontiners
$ ./leek.py d redate sheilas lifesome dowable tontiners
facebookcorewwwi.onion
```
compatible with C leekspeak
```
$ ./leek.py e facebookcorewwwi.onion
redate sheilas lifesome dowable tontiners
$ ./leekspeak d 'redate sheilas lifesome dowable tontiners'
facebookcorewwwi.onion
```
```
$ ./leekspeak e facebookcorewwwi.onion
redate sheilas lifesome dowable tontiners 
$ ./leek.py d redate sheilas lifesome dowable tontiners
facebookcorewwwi.onion
```
