# Automation File Classifier
Python Programming for Classify and Move Files based on their Extension 

----
### Usage
To use this code, use Python 3 and run the script. It will ask your directory that you want to apply, then all files will be classified based on extension

----
### Code Explanation

#### 1. Loop Directory Creation
Code below run looping a dict to create folder based on extention. You can edit the dict variable as your need

```
dir_dict ={
		'app' :'Application',
		'files' : 'File',
}

for name, nameFile in dir_dict.items():
		finaldir = src_dir + r"/" + nameFile
		final_dir[name] = finaldir
		if not os.path.exists(finaldir):
			os.mkdir(finaldir)
		print("Folder ", nameFile, " is created!")
```
#### 2. Assign Extension to Destination Folder
Assign each extension to certain destination folder. You can add more extension as your need

```
action = {
		'pdf' : moveto(final_dir['files']),
		'exe' : moveto(final_dir['app']),
		'txt' : moveto(final_dir['document']),
}
```

#### 3. Move Files
Function for moving file with destination as input

```
def moveto(dst):
    return lambda src: shutil.move(src, dst)
```    





