#!/bin/bash
export PATH=$PATH:/home/ash/bin
cd ~
game=zelda

python ~/randinput.py &
PYTHON_PID=$!

mednafen ~/$game.gb*

# block until mednafen dies
kill $PYTHON_PID
for key in 36 116 111 113 114 56 61; do xdo keyrelease -k $key; done
