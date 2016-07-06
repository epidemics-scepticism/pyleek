# pyleek
turn an .onion address into a 5 word phrase and back again
```
$ ./leek.py encode facebookcorewwwi.onion
redate sheilas lifesome dowable tontiners
$ ./leek.py decode redate sheilas lifesome dowable tontiners
facebookcorewwwi.onion
```
compatible with C [leekspeak](https://github.com/epidemics-scepticism/leekspeak)
```
$ ./leek.py encode facebookcorewwwi.onion
redate sheilas lifesome dowable tontiners
$ ./leekspeak decode redate sheilas lifesome dowable tontiners
facebookcorewwwi.onion
```
```
$ ./leekspeak encode facebookcorewwwi.onion
redate sheilas lifesome dowable tontiners 
$ ./leek.py decode redate sheilas lifesome dowable tontiners
facebookcorewwwi.onion
```
