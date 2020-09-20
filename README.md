# Plimmetry. An automated Program to extract and split images from videos, designed to be used for photogrammetry

Plimmetry is a fairly simple Program/Script to give you the opportunity to speed up photogrammetry workflows.

# Why was it made?
Typically, photogrammetry is being done by taking a lot of pictures around the object, from every angle.
This process can take quiet alot of time, depending on how many images you want.
With a recorded video around the object however, you quickly have hundrets to thousands of images around the object. The amount of images is way too high to use them for calculating a 3D Model though.

Extracting each frame would take extra steps, as well as clearing out the frames, since simply deleting a big section of all frames would take away alot of information. 

# How does it work?
Plimmetry automatically looks for all .mp4 files in its directory, giving you a list of them. You simply select the one you would like to extract.
It will then tell you how many frames the video has in total, and you only have to specify the amount of frames you want to keep at minimum. For a normal photoscan, 100-200 should be a good number, but you can choose whatever you like.
Plimmetry then extracts all the frames of the video into a folder called "images", that it will either create automatically, or use one if it already exist.
# WARNING: Make sure the folder "images" is empty if you already have one, otherwise Plimmetry will delete files out of it, and those files will be completley deleted, not put into the bin!
Once all frames have been extracted, every 16th image will be removed to decrease the amount of images, while keeping the information of all angles. Plimmetry will iterate through all images, deleting every 16th image, and it will repeat this process until it reached the amount of images you want to keep.
Should you have specified 200 Images to be kept, and 205 are left, Plimmetry will leave you with 205 images, since interating through them again and deleting every 16th would make it less than your 200 images. Thats why you are being asked how many images you want to keep at minimun.

