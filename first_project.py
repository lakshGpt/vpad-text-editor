import os, shutil

dict_extension = {
	'audio_extensions' : ('.mp3','.mp4','.m4a','.wav','.flac'),
	'videos_extension' : ('.mp4','.mkv','.mkv','.flv','.mpeg','.3gp'),
	'document_extensions' : ('.pdf','.doc','.zip','.xls')
		}

folderPath = input('enter folder path :')

def file_finder(folder_path,file_extension):
#	files = []
#	for file in os.listdir(folder_path):
#		for extension in file_extension:
#			if file.endswith(extension):
#				files.append(file)
#	return files
	return [file for file in os.listdir(folder_path) for extendion in file_extensions if file.endswith(extension)]


for extension_type,extension_tuple in dict_extension.items():
	folder_name = extension_type.split('_')[0] + 'Files'
	folder_path = os.path.join(folderPath,folder_name)
	os.mkdir(folder_path)
	for item in file_finder(folderPath,extension_tuple):
		item_path = os.path.join(folderPath,item)
		item_new_path = os.path.join(folder_path,item)
		shutil.move(item_path,item_new_path)
#	print('calling file finder')
#	print(file_finder(folderPath,extension_tuple))