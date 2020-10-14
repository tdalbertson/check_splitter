
#!/bin/bash

clear
printf "This is used to simplify the push process when using git.\n"
git add /Users/menma/Documents/Python\ Projects/Check\ Splitter/check_splitter.py
read -p "Enter commit comment: " comment
echo \"$comment\"
read -p "Are you sure this is the correct comment? (y)es (n)o: " confirmation
if [ $confirmation == 'y' ]
then
   clear
   git commit -m "$comment"
   git push
   clear
   tput cup 10 15
   tput setaf 5; tput bold; echo Push done!
else
   clear
fi
