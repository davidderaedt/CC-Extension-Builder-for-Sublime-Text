#!/bin/bash

CEPDIR=CEP
EXTDIR=~/Library/Application\ Support/Adobe/$CEPDIR/extensions

#create extensions folder if does not exist
mkdir -p "$EXTDIR"

#copy source folder to destination with specified ID
cp -r -X "$1" "$EXTDIR"/$2

#return resulting path
echo "$EXTDIR"/$2