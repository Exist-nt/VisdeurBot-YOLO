from ultralytics import YOLO
#import sys
#import argparse

model = YOLO("visdeurbot-yolo.pt")

#parser = argparse.ArgumentParser()

#parser.add_argument("input", type=str, default="", nargs="?", help="Location of the input file")
#parser.add_argument("output", type=str, default="images/runs", nargs="?", help="Location of the output folder")

#try:
#	args = parser.parse_known_args()[0]
#except:
#	print("")
#	parser.print_help()
#	sys.exit(0)

model.predict("https://visdeurbel.videostreams.nl/hls/visdeurbel/index.m3u8", conf=0.55, device="mps", show=True)
