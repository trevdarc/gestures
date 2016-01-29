# python code
# Look for an XML parser in python. There may be one that can make our lives easier.


# Create all global variables to handle all the columns in excel
# Participant
pid = 0
# Personality
ex = 0
op = 0
ag = 0
ems = 0
co = 0
# Story
s_id = 0
order = 0
version = 0
# Part
number = 0
agentexlvl = 0
# Gesture
g_type = "none"
handedness = "NONE"
stroke = 0
se_onset_height = 0
se_onset_width = 0
se_onset_radial = 0
se_offset_height = 0
se_offset_width = 0
se_offset_radial = 0
retract = 0
agent_match_loc = FALSE
agent_match_form = FALSE


# Iterate through XML tags in the file
# For each tag, get the first word, directly after the open bracket
if(tag_label == "participant")
  do this stuff
elif(tag_label == "personality")
  do this stuff
elif(tag_label == "story")
  do this stuff
elif(tag_label == "part")
  do this stuff
elif(tag_label == "gesture")
  grab the rest of the data into relevant variables
  spit out all the variables, in order, into the csv file separated by commas, and then add a line break.
}
Iterate until no more xml tags exist in the file.
