import sys
# Create all global variables to handle all the columns in excel
# Participant
pid = 0
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
part_number = 0
part_agentexlvl = 0
# Gesture
g_type = "NONE"
g_handedness = "NONE"
g_prep = 0
g_stroke = 0
g_se_onset_height = 0
g_se_onset_width = 0
g_se_onset_radial = 0
g_se_offset_height = 0
g_se_offset_width = 0
g_se_offset_radial = 0
g_retract = 0
g_agent_match_loc = "FALSE"
g_agent_match_form = "FALSE"

# open the input file for reading
try:
    input_file = open("P107.xml", "r")
except IOError:
    print "Could not open file!"

# creates a big string with all data from the file
datafile = input_file.read()

all_data = datafile.partition("<")[2]
# This initializes the list
all_tags = []
while all_data != "":
    all_tags.append(all_data.partition(">")[0])
    all_data = all_data.partition("<")[2]

for tag in all_tags:
    name = tag.partition(" ")[0]
    tag = tag.partition(" ")[2]

    # Get attributes
    while tag != "":
        attribute = str.strip((tag.partition("=")[0]))
        tag = tag.partition("\"")[2]
        value = (tag.partition("\""))[0]
        tag = tag.partition("\"")[2]
        if name == "participant":
            if attribute == "id":
                pid = value
            else:
                sys.exit("ERROR! Participant has an undefined attribute: %s" % attribute)
        if name == "personality":
            if attribute == "ex":
                p_ex = value
            elif attribute == "op":
                p_op = value
            elif attribute == "ag":
                p_ag = value
            elif attribute == "ems":
                p_ems = value
            elif attribute == "co":
                p_co = value
            else:
                sys.exit("ERROR! Personality has an undefined attribute: %s" % attribute)
        if name == "story":
            if attribute == "id":
                s_id = value
            elif attribute == "order":
                s_order = value
            elif attribute == "version":
                s_version = value
            else:
                sys.exit("ERROR! Story has an undefined attribute: %s" % attribute)
        if name == "part":
            if attribute == "number":
                part_number = value
            elif attribute == "agentexlvl":
                part_agentexlvl = value
            else:
                sys.exit("ERROR! Part has an undefined attribute: %s" % attribute)
        if name == "gesture":
            if attribute == "type":
                g_type = value
            elif attribute == "handedness":
                g_handedness = value
            elif attribute == "prep":
                g_prep = value
            elif attribute == "stroke":
                g_stroke = value
            elif attribute == "se_onset_height":
                g_se_onset_height = value
            elif attribute == "se_onset_width":
                g_se_onset_width = value
            elif attribute == "se_onset_radial":
                g_se_onset_radial = value
            elif attribute == "se_offset_height":
                g_se_offset_height = value
            elif attribute == "se_offset_width":
                g_se_offset_width = value
            elif attribute == "se_offset_radial":
                g_se_offset_radial = value
            elif attribute == "retract":
                g_retract = value
            elif attribute == "agent_match_loc":
                g_agent_match_loc = value
            elif attribute == "agent_match_form":
                g_agent_match_form = value
            else:
                sys.exit("ERROR! Gesture has an undefined attribute: %s" % attribute)
            print pid, p_ex, p_op, p_ag, p_ems, p_co, s_id, s_order, s_version, part_number, part_agentexlvl
            print "Gesture Information: "
            print g_type, g_handedness, g_stroke, g_se_onset_height, g_se_onset_width, g_se_onset_radial, g_se_offset_height, g_se_offset_width, g_se_offset_radial, g_retract, g_agent_match_loc, g_agent_match_form
