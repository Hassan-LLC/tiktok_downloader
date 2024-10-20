import argparse
import subprocess

def download_video(url, output_filename):
    command = ["yt-dlp", url, "-o", output_filename]
    try:
        subprocess.run(command, check=True)
        print(f"Video downloaded successfully as {output_filename}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Download TikTok videos without a watermark")
    parser.add_argument("url", help="TikTok video URL")
    parser.add_argument("-o", "--output", help="Output filename", default="tiktok_video.mp4")
    args = parser.parse_args()

    download_video(args.url, args.output)

if __name__ == "__main__":
    main()