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

