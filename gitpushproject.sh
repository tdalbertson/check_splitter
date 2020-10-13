#!/bin/bash

clear
printf "This is used to simplify the push process when using git.\n"
git add .
read -p "Enter commit comment: " comment
echo \"$comment\"
read -p "Are you sure this is the correct comment? (y)es (n)o: " confirmation
if [ $confirmation == 'y' ]
then
   clear
   git commit -m "$comment"
   git push
   tput cup 10 15
   echo Push done!
else
   clear
fi
