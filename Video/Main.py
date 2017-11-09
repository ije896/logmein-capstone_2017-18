from HeatMap import *
from VideoAnalysis import *
import sys

try:
    video_src = sys.argv[1]
except:s
    print("You need to pass a video_file path")

print(__doc__)
app = VideoAnalysis(video_src)
app.run()
app.to_json()

cv2.destroyAllWindows()
