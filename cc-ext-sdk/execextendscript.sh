#!/bin/bash

appcode=$1

if [ "$appcode" = "ps" ]
then
    app="Adobe Photoshop CC"
    command="do javascript \"#include '$2'\""
elif [ "$appcode" = "ai" ]
then
    app="Adobe Illustrator"
    command="do javascript \"#include '$2'\""
elif [ "$appcode" = "id" ]
then 
    app="Adobe InDesign CC"
    command="do script \"#include '$2'\" language javascript" 
elif [ "$appcode" = "ae" ]
then
    app="Adobe After Effects CC"
    command="DoScriptFile \"$2\""
fi

osascript <<-AS
tell application "$app"
   $command
end tell
AS
