#!/bin/sh
GAME=SDLPoP
GAME_LOCALDIR=$HOME/.$GAME
GAME_DATADIR=/usr/share/$GAME
GAME_EXECUTABLE=/usr/libexec/$GAME/prince
GAME_DOCDIR=/usr/share/doc/$GAME

mkdir -p $GAME_LOCALDIR
cd $GAME_LOCALDIR

# Create link to game file
ln -sf $GAME_EXECUTABLE 

# Link directories which are not modified by users
ln -nsf ${GAME_DATADIR}/data

# Copy directories which can be modified by users
test -d mods || cp -aR ${GAME_DATADIR}/mods mods

# Copy files which can be modified by users
test -e SDLPoP.ini || cp -a $GAME_DATADIR/SDLPoP.ini .

exec ./prince "$@"

