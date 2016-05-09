#!/usr/bin/env python2

#    Copyright (C) 2016 cacahuatl < cacahuatl at autistici dot org >
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import struct,base64
from sys import argv
class Leek():
    loaded = False
    def __init__(self, words="words"):
        words = open(words).read().strip().split('\n')
        self.w = {}
        self.v = {}
        c = 0
        for word in words:
            self.v[c] = word
            self.w[word] = c
            c = c + 1
        if len(self.w) != 65536:
            raise Exception('Invalid word list length: %d' % len(self.w))
        self.loaded = True
    def encode(self, onion):
        """Turn an onion address into a 5 word phrase"""
        if self.loaded == False:
            raise Exception('Leek class did not initialize.')
        onion = onion.split('.onion')[0]
        if len(onion) != 16:
            raise Exception('Invalid onion address: "%s"' % onion)
        blob = base64.b32decode(s=onion, casefold=True)
        phrase = []
        for i in range(0,5):
            c = struct.unpack("<H", blob[i*2:i*2+2])[0]
            w = self.v.get(c)
            if w == None:
                raise Exception('Invalid decoded value: "%d"' % c) # this shouldn't happen...
            phrase.append(w)
        return ' '.join(phrase)
    def decode(self, phrase):
        """Turn a 5 word phrase into an onion address"""
        if self.loaded == False:
            raise Exception('Leek class did not initialize.')
        phrase = phrase.split(' ')
        blob = ''
        for word in phrase:
            c = self.w.get(word)
            if c == None:
                raise Exception('Invalid word in phrase: "%s"' % word)
            blob += struct.pack("<H", c)
        onion = base64.b32encode(s=blob).lower() + ".onion"
        return onion
if __name__ == '__main__':
    l = Leek()
    argc = len(argv)
    if argc > 2:
        if argv[1][0] == 'e':
            print "%s" % l.encode(argv[2])
        if argv[1][0] == 'd':
            print "%s" % l.decode(' '.join(argv[2:]))
