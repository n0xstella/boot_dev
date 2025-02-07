def list_files(parent_directory, current_filepath=""):
    file_paths = []

    for key in parent_directory:
        new_path = current_filepath + '/' + key
        if parent_directory[key] == None:
            file_paths.append(new_path) 
        else:
            new_dict = list_files(parent_directory[key], new_path)
            file_paths.extend(new_dict)
    
    return file_paths