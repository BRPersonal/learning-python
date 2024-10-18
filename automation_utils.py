import requests
from bs4 import BeautifulSoup
import os
import shutil

def get_todays_news() -> str:
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h2', class_='sc-4fedabc7-3')

    #collecting in a set to avoid duplicates
    news_summary = {headline.get_text() for headline in headlines} 

    return '\n'.join(news_summary)

def organize_files(directory:str) -> None:
    """
    Searches for files in the directory and organizes them by thier 
    file extension. Creates sub-directory for each unique file extension
    and moves the file to that corresponding sub-directory
    Recursively does it for sub-directories too

    Arguments:
    directory -- the absolute path to the directory to organize    
    """
    assert os.path.isabs(directory) #passed in directory must be an absolute path

    for file_name in os.listdir(directory):
        
        absolute_path = os.path.join(directory,file_name)

        print(f"fileName={absolute_path}")
        if os.path.isfile(absolute_path):

            file_extension = os.path.splitext(file_name)[1]
            if (file_extension == ""):
                continue  #ignore files without extension

            target_dir = os.path.join(directory,file_extension[1:])  #discard leading dot
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            shutil.move(absolute_path,os.path.join(target_dir,file_name))

        elif os.path.isdir(absolute_path):
            organize_files(absolute_path) #recursive call


