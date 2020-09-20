# Plimmetry, made by https://github.com/TrackLab

from cv2 import imwrite, VideoCapture, CAP_PROP_FRAME_COUNT
import os
from tqdm import tqdm

def find_videos():
    found_videos = []
    for i in os.listdir():
        if i.endswith(".mp4"):
            found_videos.append(i)
            
    video_ids = range(len(found_videos))
    print('I found the following videos:')
    for video, ID in zip(found_videos, video_ids):
        print(ID, ":", video)

    return found_videos

def select_video(found_videos):

    selected_vid = None
    while type(selected_vid) != int:
        try:
            selected_vid = int(input("Please type the number of the correspondending video you wish to use: "))
            if not selected_vid in range(len(found_videos)):
                print("That video ID does not exist!")
                selected_vid = None
            else:
                return selected_vid
        except:
            print("That is not a number!")

def extract_mp4(video, frames_num):
    #for frame identity
    for i in tqdm(range(frames_count), desc="Extracting Frames from Video"):
        # Extract images
        ret, frame = vid.read()
        # end of frames
        if not ret: 
            break
        # Saves images
        name = './images/frame' + str(i) + '.jpg'
        imwrite(name, frame)

def delete_every_k_image(k, images):

    deleted_imgs = 0
    for image, i in zip(tqdm(images, desc=f"Stripping every {k}. image"), range(len(images))):
        # IF IMAGE COUNT IS DIVIDIBLE BY K, DELETE IT
        if i % k == 0:
            os.remove("images/"+image)
            deleted_imgs += 1

    return deleted_imgs

def make_int(frames_count):
    try:
        min_imgs = int(input(f"{frames_count} Images are available. How many images do you want to keep at minimum? "))
        if min_imgs <= 0:
            print(f"{min_imgs} Images are not possible. Please choose atleast a few.")
            make_int(frames_count)
        else:
            return min_imgs
    except:
        print("That is not a number!")
        make_int(frames_count)

found_videos = find_videos()
selected_vid = select_video(found_videos)
selected_vid = found_videos[selected_vid]

print('Let me count the frames in this video...')
vid = VideoCapture(selected_vid)
frames_count = int(vid.get(CAP_PROP_FRAME_COUNT))
min_imgs = make_int(frames_count)

# CHECKING FOR IMAGES FOLDER
if not os.path.exists('images'):
    os.makedirs('images')

extract_mp4(vid, frames_count)
images = os.listdir("images/")

while len(images) > min_imgs:

    delete_every = 16
    images = os.listdir("images/")
    # SKIP THE IMAGE SPLITTING IF LESS IMAGES THAN SPECIFIED ARE AVAILABLE
    if len(images) < min_imgs or len(images)-(len(images)/delete_every) < min_imgs:
        break
    else:
        deleted_imgs = delete_every_k_image(delete_every, images)

final_amount = len(os.listdir("images/"))


print(f"Out of {frames_count} images were {final_amount} images kept")