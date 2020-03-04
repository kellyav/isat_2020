""" A guide I have written on 
How to upload files using mac terminal command line
"""

1. Create the respository and/ or clone it. 
Create a (remote) repository on Github's webstie, and click clone or download. Then, copy the link this provides.

2. Open terminal, and change the current working directory to the location where you want the cloned directory to be made.
to do this, type
```
$ git init
```
then 
```
$ git clone https://hostname/YOUR-GITHUB-USERNAME/THE-REPOSITORY 
```
This will create a folder in your computer exactly like the respository on Github. 

Add the folder/ files you want to upload to the repository on Github to this local version of the repository on your computer. 
```
$ git add .
```
You can also type 'git add filename', but the "." will add any changes made to the remote folder.

Check that the files were added, before commiting the changes:
```
$ git status
```

If the git status shows exactly what was intended to happen, commit the changes:
```
$ git commit -m "add a message here about the commit for github to display"
```

When work is done on the remote repository (on github), those changes will not be automatically reflected on the local repositroy on your computer. This may not be reflected in the output of git status
Thus, when trying to commit a new file to the remote repo.
You need to update the changes so that it is up to date on the local branch. This means that we have to pull the changes before commiting:

So, you'll need to perform a pull request first...

```
$ git pull
```
This will list all the changes to the repository that were updated. 
Then all you have to do is push, so that the files from the local repository that were originally going to be updated. push the changes onto the remote repository
```
$ git push
```
Now, the file(s) you wanted to add will show up on your GitHub repository!
