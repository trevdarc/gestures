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


datalist = []
# open the input file for reading
input_file = open("foo.txt", "wb")

# get the first line from the input file and put it in a string variable
xml_line = input_file.readline()

# split the line into array items by looking for open brackets. This should split up the XML tags on this line.
tag_array = xml_line.split("<")

# define the tag_label for the array items as the first word of the array item.
tag_label = tag_array[0].partition(" ")[0]

# Iterate through XML tags in the line
# For each array item, get the first word, directly after the open bracket
if(tag_label == "participant")
  # do stuff
  id = 
elif(tag_label == "personality")
  # do stuff  
  p_ex = 
  p_op = 
  p_ag = 
  p_ems = 
  p_co = 
  
elif(tag_label == "story")
  # do this stuff
  s_id = 
  s_order = 
  s_version = 
  
elif(tag_label == "part")
  # do this stuff
  number = 
  agentexlvl = 
  
elif(tag_label == "gesture")
  # grab the rest of the data into relevant variables
  g_type =
  g_handedness = 
  g_stroke = 
  g_se_onset_height = 
  g_se_onset_width = 
  g_se_onset_radial = 
  g_se_offset_height = 
  g_se_offset_width = 
  g_se_offset_radial = 
  g_retract = 
  g_agent_match_loc = FALSE
  g_agent_match_form = FALSE
  
  data_slice = (id, p_ex, p_op, p_ag, p_ems, p_co, s_id, s_order, s_version, number, agentexlvl, g_type, g_handedness, g_stroke, g_se_onset_height, g_se_onset_width, g_se_onset_radial, g_se_offset_height, g_se_offset_width, g_se_offset_radial, g_retract, g_agent_match_loc, g_agent_match_form)
  datalist.append(list_slice)
}

#write out csv file to desktop or wherever

Iterate until no more xml tags exist in the file.
