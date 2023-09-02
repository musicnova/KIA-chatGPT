import os

def read_titles_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def get_folder_names(directory_path):
    return [name for name in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, name))]

def find_matching_folders(video_titles, folder_names):
    matching_folders = []
    for title in video_titles:
        if title in folder_names:
            matching_folders.append(title)
    return matching_folders

if __name__ == "__main__":
    video_titles = read_titles_from_file("video_titles.txt")
    directory_path = "/home/bunta/ARCHIVE/Projects.Python/4.Kia.ChatGPT/000/trans/"
    folder_names = get_folder_names(directory_path)

    matching_folders = find_matching_folders(video_titles, folder_names)

    if matching_folders:
        print("Совпадающие папки:")
        for folder in matching_folders:
            print(folder)
    else:
        print("Совпадающих папок не найдено.")
