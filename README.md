# SnippetySnip
Program created with the purpose of analysing a video and removing occasional blue flashes which occur within it.  More specifically, when a blue flash (usually lasting around 500ms and in 30s intervals) these are removed and the two loose video ends are stitched back together.  The program works its magic on every single wmv file in its directory creating a TEMP folder in which files with the format  `<clip#>.wmv` are saved, these are the intervals of video between the blue screens.  After the program has traversed the video a text file is created with all the wmv filenames and then this file is used to concatenate all of the wmvs together.  The resultant file is then saved as final.wmv in the parent directory and at this point thee entirety of the TEMP directory is deleted.

  
## Notice
Due to the naming structure, __it is necessary that there are no folders named 'TEMP' in the program's directory__. Moreover, __this program was designed to work solely with greyscale video__. Lastly, if possible, place lightbulb in such a way as to eliminate extraneous light in its immediate vicinity whether it be caused by other lights or the lightbulb's own reflection <br>

## Windows Install
_Administrator Privileges Required_
1) Download and install all of the following files **in the order in which they appear:**<br>
    - Visual Studio 2019 : https://aka.ms/vs/16/release/vc_redist.x64.exe<br>
    - Python 3.7.3 : https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe<br> 
      > Custom->Next->Add Python to environment variables
   
    - NumPy : Open CMD and type `pip install numpy`<br>
    - ffmpy : Open CMD and type `pip install ffmpy`<br>
    - OpenCV : Open CMD and type `pip install opencv-python`<br>
    - ffmpeg : https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-20190620-86f04b9-win64-static.zip<br>
      - Follow instructions found here : https://www.wikihow.com/Install-FFmpeg-on-Windows
2) Download snippetysnip.py and position it in a folder with all of the .wmv files you want examined<br>
3) Open snippetysnip.py in IDLE (Python 3.7 64-bit)
   > File->Open...
  
4) Run snippetysnip.py
    > Run->Run Module
   
5) Wait for completion, should take about 40 seconds per 10-minute video <br>
**DO NOT MANIPULATE THE FILE STRUCTURE UNTIL THE PROGRAM FINISHES**


## Debian Install
_Administrator Privileges Required_
1) Download and install all of the following files **in the order in which they appear:**<br>
    - Pip : `sudo apt-get install python-pip`<br> 
    - ffmpeg : `sudo apt-get install ffmpeg`<br>
    - ffmpy :`pip install ffmpy`<br>
    - NumPy : `pip install  numpy`<br>
    - OpenCV : `pip install opencv-python`<br>
2) Download snippetysnip.py and position it in a folder with all of the .wmv files you want examined<br>
3) Open a Terminal window and navigate to the directory which you have selected
   > `cd /...`
  
4) Run snippetysnip.py
    > `python snippetysnip.py`
  
5) Wait for completion, should take about 40 seconds per 10-minute video <br>
**DO NOT MANIPULATE THE FILE STRUCTURE OR THE TERMINAL WINDOW UNTIL THE PROGRAM FINISHES**<br>
**IF YOU WISH TO PLAY THE .WMV FILES THEN YOU WILL NEED TO INSTALL UBUNTU RESTRICTED EXTRAS**
