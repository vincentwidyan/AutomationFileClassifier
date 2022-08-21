import os
import shutil

def moveto(dst):
    return lambda src: shutil.move(src, dst)

def main():
	print("-------Welcome to Automation File Management----------")
	print("Created by : @vincentwwidyan")
	print("Date : 2022-08-21")
	print("----------------------------------------------------")
	
	
	dir_dict ={
		'app' :'Application',
		'files' : 'File',
		'document' : 'Documents',
		'arch' : 'Archieve',
		'attach' : 'Attachment',
		'picture' :  'Picture',
		'video' : 'Video',
		'music' : 'Music',
		'data' : 'Data',
		'font' : 'Font'
	}
	src_dir = input("\nYour Directory :")
	final_dir = {}

	for name, nameFile in dir_dict.items():
		finaldir = src_dir + r"/" + nameFile
		final_dir[name] = finaldir
		if not os.path.exists(finaldir):
			os.mkdir(finaldir)
		print("Folder ", nameFile, " is created!")

	action = {
		'pdf' : moveto(final_dir['files']),
		'PDF' : moveto(final_dir['files']),
		'txt' : moveto(final_dir['document']),
		'htm' : moveto(final_dir['document']),
		'cdr' : moveto(final_dir['files']),
		'psd' : moveto(final_dir['files']),
		'html' : moveto(final_dir['document']),
		'xlsx' : moveto(final_dir['data']),
		'xlsm' : moveto(final_dir['data']),
		'XLSX' : moveto(final_dir['data']),
		'xls' : moveto(final_dir['data']),
		'csv' : moveto(final_dir['data']),
		'CSV' : moveto(final_dir['data']),
		'doc' : moveto(final_dir['data']),
		'DOC' : moveto(final_dir['data']),
		'docx' : moveto(final_dir['data']),
		'pptx' : moveto(final_dir['data']),
		'ppt' : moveto(final_dir['data']),
		'PPTX' : moveto(final_dir['data']),
		'zip' : moveto(final_dir['arch']),
		'rar' : moveto(final_dir['arch']),
		'tar' : moveto(final_dir['arch']),
		'msg' : moveto(final_dir['attach']),
		'jpg' : moveto(final_dir['picture']),
		'jpeg' : moveto(final_dir['picture']),
		'PNG' : moveto(final_dir['picture']),
		'png' : moveto(final_dir['picture']),
		'jfif' : moveto(final_dir['picture']),
		'svg' : moveto(final_dir['picture']),
		'mp3' : moveto(final_dir['music']),
		'mp4' : moveto(final_dir['video']),
		'mkv' : moveto(final_dir['video']),
		'mov' : moveto(final_dir['video']),
		'MOV' : moveto(final_dir['video']),
		'gif' : moveto(final_dir['video']),
		'exe' : moveto(final_dir['app']),
		'dmg' : moveto(final_dir['app']),
		'pkg' : moveto(final_dir['app']),
		'ttf' : moveto(final_dir['font'])
	}

	for file in os.listdir(src_dir):
	    ext = os.path.splitext(file)[1][1:]
	    if ext in action:
	        action[ext](os.path.join(src_dir, file))
	print("All Known Extenstion are Moved!")
	print("----------------Program is Finished-------------------")

if __name__ == '__main__':
	main()


