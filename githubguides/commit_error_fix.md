# Handling this common commit error 
If youre not careful, this message will pop up after you tyr to commit something to your repository, 
if you git commit without a message (-m)

You can get out of it by:
Two options:
1. Type the message explanation of the commit to move foward with the commit.
2. Leave blank to abort the commit.

Then, Hit the 'esc' key, type **":wq"** and hit enter. 
If you chose option one, then the commit is cancelled and youll have to type 'git commit -m "message"' all over again.
If you chose option two, then the commit will occur and youre good to go for the next step of the upload process.

Example of the error:

\# Please enter the commit message for your changes. Lines starting

\# with '#' will be ignored, and an empty message aborts the commit.

\# On branch master

\# Your branch is ahead of 'origin/master' by 1 commit.

\#   (use "git push" to publish your local commits)

\#

\# Changes to be committed:

\#       modified:   README.md

\#

\# Untracked files:

\#       README.workingd

\#

\~               

\~        

\~    

\~  

\~   

~  

~ 

~ 

~   

~     

-- INSERT --
