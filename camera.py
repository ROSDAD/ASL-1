#import libs
import uvicorn
from vidgear.gears import WebGear

# various performance tweaks
options = {"frame_size_reduction": 40, "frame_jpeg_quality": 80,
           "frame_jpeg_optimize": True, "frame_jpeg_progressive": False}

# initialize WebGear app with suitable video file (for e.g `foo.mp4`)
web = WebGear(source="foo.mp4", logging=True, **options)

# run this app on Uvicorn server at address http://0.0.0.0:8000/
uvicorn.run(web(), host='0.0.0.0', port=8000)

# close app safely
web.shutdown()
