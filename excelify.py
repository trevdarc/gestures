# python code
# Look for an XML parser in python. There may be one that can make our lives easier.


# Create all global variables to handle all the columns in excel
# Participant
id = 0
# Personality
p_ex = 0
p_op = 0
p_ag = 0
p_ems = 0
p_co = 0
# Story
s_id = 0
s_order = 0
s_version = 0
# Part
number = 0
agentexlvl = 0
# Gesture
g_type = "none"
g_handedness = "NONE"
g_stroke = 0
g_se_onset_height = 0
g_se_onset_width = 0
g_se_onset_radial = 0
g_se_offset_height = 0
g_se_offset_width = 0
g_se_offset_radial = 0
g_retract = 0
g_agent_match_loc = FALSE
g_agent_match_form = FALSE


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
