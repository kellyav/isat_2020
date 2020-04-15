# A guide on How to upload files using command line
I used mac terminal for this instruction. There may be a slight variation for windows computers. 

## Set up the local environment
### This requires you to have the necessary git packages beforehand. [Windows users may have to download Git and set it up first.](https://github.com/kellyav/isat_2020/blob/master/settingupgit.md "downloading Git for the first time")


Create a (remote) repository on Github's webstie, and click 'clone or download'. Then, copy the link this provides.

Open terminal, and change the current working directory to the location where you want the cloned directory to be made.
to do this, type
```
$ git init
```
then, using the copied repository url: 
```
$ git clone https://hostname/YOUR-GITHUB-USERNAME/THE-REPOSITORY 
```
This will create a folder in your computer exactly like the respository on Github. Only do this if you do not have a version of the repository on your local drive. 

*Then, edit the file locally as you please. Make sure changes are saved on the file that is saved in the local repository folder *


## Add the folder/ files you want to upload 
to the repository on Github from the local version of the repository on your computer. 
```
$ cd pathnameof/yourrepository
```

the "ls" command lists the file contents of a directory. 
the "-l" formats the output list a little more structured and the "-a" also lists "hidden" files (which is helpful when working with version control). Showing the contents of the current directory works as follows:
```
$ ls -la
```

'Add' the modified files:
```
$ git add .
```
*You can also type 'git add filename', but the "." will add any changes made to the remote folder.*


Check that the files were added, before commiting the changes:
```
$ git status
```

If the git status shows exactly what was intended to happen, commit the changes:
```
$ git commit -m "add a message here about the commit for github to display"
```

if you do not write '-m "message"' then there will be an error message:
``` 
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
```
type :wq and press enter 

*At this point, the commit might be succesful, or it might fail.*

When work is done on the remote repository (on github), those changes will not be automatically reflected on the local repositroy on your computer. This includes changes done by other contributors. This may not be reflected in the output of git status, and will make the commit fail.
Thus, when trying to commit a new file to the remote repo, you need to update the changes so that it is up to date on the local branch. This means that we have to pull the changes before commiting:

So, if you did not start by cloning the diretory, you'll need to perform a pull request first...
```
$ git pull
```
This will list all the changes to the repository that were updated. 

Then all you have to do is push, so that the files from the local repository that were originally going to be updated. push the changes onto the remote repository
```
$ git push
```
Now, the file(s) you wanted to add will show up on your GitHub repository!
