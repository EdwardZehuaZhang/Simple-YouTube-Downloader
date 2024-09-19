import os
import subprocess

def download_and_convert(video_url, counter):
    intermediate_output = f"C:\\Users\\yourname\\Downloads\\video_{counter}.mp4"
    final_output = f"C:\\Users\\yourname\\Downloads\\video_{counter}_premiere.mp4"
    
    yt_dlp_command = [
        "yt-dlp",
        "-f", "bestvideo+bestaudio",
        "-o", intermediate_output,
        video_url
    ]
    
    subprocess.run(yt_dlp_command, shell=True, check=True)
    
    ffmpeg_command = f'ffmpeg -y -i "{intermediate_output}" -c:v libx264 -pix_fmt yuv420p -c:a aac -b:a 192k "{final_output}"'
    subprocess.run(ffmpeg_command, shell=True, check=True)
    
    if os.path.exists(intermediate_output):
        os.remove(intermediate_output)
        print(f"Deleted intermediate file: {intermediate_output}")

if __name__ == "__main__":
    counter = 1
    while True:
        video_url = input("Enter the YouTube video URL (or 'exit' to quit): ")
        if video_url.lower() == 'exit':
            break
        
        download_and_convert(video_url, counter)
        counter += 1
