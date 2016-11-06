import bpy

context = bpy.context
scene = context.scene
vse = scene.sequence_editor

def hhmmss(frames):
	sec = int(frames / 59.94)
	min = int(sec /60)
	hour = int(sec /60)
	sec = sec % 60
	return "{:02d}:{:02d}:{:02d},000".format(hour, min, sec)

strips = []
for strip in vse.sequences_all:
	if strip.type == "COLOR" and strip.channel == 7:
		print(strip.frame_start)
		strips.append(strip)
		
strips.sort()
with open("test.srt", "w+") as f:
	i = 1
	for strip in strips:	
		f.writelines("%s\n"%i)
		f.writelines("{} --> {}\n".format(hhmmss(strip.frame_start), hhmmss(strip.frame_start + strip.frame_final_duration)))
		f.writelines("{}\n".format(strip.get("English", "not available")))
		f.writelines("\n")
		i = i + 1



#1
#00:02:17,440 --> 00:02:20,375
#Senator, we're making
#our final approach into Coruscant.
#
#2
#00:02:20,476 --> 00:02:22,501
#Very good, Lieutenant.