import requests
import subprocess,sys

title_art=r""" _____              ______ _ _
|_   _|             |  ___| (_)
  | | ___  _ __ _ __| |_  | |___  __
  | |/ _ \| '__| '__|  _| | | \ \/ /
  | | (_) | |  | |  | |   | | |>  <
  \_/\___/|_|  |_|  \_|   |_|_/_/\_\
                                    """
print(title_art+'\n')
def main():
    movie_name = input("Enter the movie name:\n")
    print(f"Searching for {movie_name}")
    base_url = f"https://api.sumanjay.cf/torrent/?query={movie_name}"
    torrent_results = requests.get(url=base_url).json()
    index = 1
    magnet= []
    for result in torrent_results:
        if 'movie' in result['type'].lower():
            print(index,") ",result['name'],"-->",result['size'])
            index+=1
            magnet.append(result['magnet'])
    if magnet:
        choice = int(input("Enter the index of the movie which you want to stream\n"))
        try:
            magnet_link = magnet[choice-1]
            download = False # Default is streaming
            stream_choice = int(input("Press 1 to stream or Press 2 to download the movie\n"))
            if stream_choice == 2:
                download = True
                
            webtorrent_stream(magnet_link,download)
        except IndexError:
            print("Incorrect Index entered")
    else:
        print(f"No results found for {movie_name}")

# Handle Streaming
def webtorrent_stream(magnet_link:str,download:bool):
    cmd = []
    cmd.append("webtorrent")
    cmd.append(magnet_link)
    if not download:
        cmd.append('--vlc')
    
    if sys.platform.startswith('linux'):
        subprocess.call(cmd)
    elif sys.platform.startswith('win32'):
        subprocess.call(cmd,shell=True)

if __name__ == "__main__":
    main()