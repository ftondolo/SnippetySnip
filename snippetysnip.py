# Federico Tondolo
# Summer 2019 at the Columbia University Medical Center
import numpy as np
import ffmpy
import cv2
import os
import subprocess

def main():
    # Creating temporary directory
    file_count=0
    os.mkdir('TEMP')
    # Loops for every file inside current dir
    for filename in sorted(os.listdir('.')):
        # If file is a video file
        if (filename.endswith(".wmv")):
            cap = cv2.VideoCapture(filename)
            # Number of clips found
            file_count+=1
            count = 0
            # No repetitions
            safe = 0
            # Start initialisation
            start = 0
            # Initialisation of frame_counting variable
            frame_count= 0
            # Loop as long as there's a frame to analyze
            while cap.grab():
                flag, frame = cap.retrieve()
                # Adding current frame to frame counter
                frame_count+=1
                # define the acceptable blues
                boundaries = [
                        ([0, 0, 0], [255, 0, 0])
                ]
                # loop over the boundaries
                for (minblue, maxblue) in boundaries:
                        # create NumPy arrays from the blue rangee
                        minblue = np.array(minblue, dtype = "uint8")
                        maxblue = np.array(maxblue, dtype = "uint8")
                        # find the blue and mask it
                        mask = cv2.inRange(frame, minblue, maxblue)
                        # Makes it so that image can be greyscaled
                        output = cv2.bitwise_and(frame, frame, mask = mask)
                        # Image is turned to greyscale
                        gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
                        # All greys are turned to 255 white for countNonZero
                        brightest = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)[1]
                        # If white pixel found, do stuff
                        if cv2.countNonZero(brightest):
                            if (frame_count >= safe):
                                # Increase count to then direct filenaming
                                count+=1
                                # Current playback time
                                end = ((frame_count-1)/30)
                                # Do the dirty work
                                safe=30+frame_count
                                subprocess.call(['ffmpeg', '-i', filename, '-ss', str(start), '-t', str(end-start), ('./TEMP/'+str(count)+'.wmv')])
                                start = (safe/30)
            # Write/Add file to list
            f= open("./TEMP/list.txt","w+")
            # Add all files to list
            q=1
            while count >= q:
                # Write corresponding file
                f.write("file '%i.wmv'\n" % (q))
                # Subtract from counter
                q+=1
            # Close list txt
            f.close()
            # Do the leftover laundry
            subprocess.call(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', './TEMP/list.txt', '-c', 'copy', ('./final'+str(file_count)+'.wmv')])
            os.system('rm -R TEMP')
         # If file is not a video
        else:
            continue


main()
