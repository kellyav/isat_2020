When work is done on the remote repository (on github), 
those changes will not be automatically reflected on the local repositroy on your computer.
Thus, when trying to commit a new file to the remote repo, 
``` 
$ git init
```
```
$ git cd yourrepository
```
```
$ git add .
```

At this point, if both repositories arent up to date with each other, you'll get an error if you try to commit the local changes. 

So, you'll need to perform a pull request first...

```
$ git pull
```

This will list all the changes to the repository that were updated. Then all you have to do is push, so that the files from the local repository that were originally going to be updated.
```
$ git push
```
