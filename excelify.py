import sys

# Create all global variables to handle all the columns in excel
# Participant
pid = ""
# Personality
p_ex = ""
p_op = ""
p_ag = ""
p_ems = ""
p_co = ""
# Story
s_id = ""
s_order = ""
s_version = ""
# Part
part_number = ""
part_agentexlvl = ""
# Gesture
g_type = ""
g_handedness = ""
g_prep = ""
g_stroke = ""
g_se_onset_height = ""
g_se_onset_width = ""
g_se_onset_radial = ""
g_se_offset_height = ""
g_se_offset_width = ""
g_se_offset_radial = ""
g_retract = ""
g_agent_match_loc = ""
g_agent_match_form = ""

# open the input file for reading
try:
    input_file = open("P107.xml", "r")
except IOError:
    print "Could not open file!"

output = open('workfile.csv', 'a')

# Create column headers
output.write(
             "P_ID, Extra, Open, Agree, EMS, Cons, S_ID, S_Order, S_Version, P_Number, P_AgentExLvl, G_Type, G_Handedness, "
             "G_Stroke, G_Onset_Height, G_Onset_Width, G_Onset Radial, G_Offset_Height, G_Offset_Width, G_Offset Radial, "
             "G_Retract, Agent_Match_Loc, Agent_Match_Form\n")
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
        value = str.lower((tag.partition("\""))[0])
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
    if name == "gesture":
        output.write(
        pid + ", " + p_ex + ", " + p_op + ", " + p_ag + ", " + p_ems + ", " + p_co + ", " + s_id + ", " + s_order + ", " +
        s_version + ", " + part_number + ", " + part_agentexlvl + ", " + g_type + ", " + g_handedness + ", " + g_stroke +
        ", " + g_se_onset_height + ", " + g_se_onset_width + ", " + g_se_onset_radial + ", " + g_se_offset_height + ", " +
        g_se_offset_width + ", " + g_se_offset_radial + ", " + g_retract + ", " + g_agent_match_loc + ", " + g_agent_match_form + "\n")
        g_type = ""
        g_handedness = ""
        g_prep = ""
        g_stroke = ""
        g_se_onset_height = ""
        g_se_onset_width = ""
        g_se_onset_radial = ""
        g_se_offset_height = ""
        g_se_offset_width = ""
        g_se_offset_radial = ""
        g_retract = ""
        g_agent_match_loc = ""
        g_agent_match_form = ""
