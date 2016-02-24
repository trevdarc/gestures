###########################################
#
#   Gesture XML Parser
#   Written by Trevor D'Arcey
#   Last edited: 2/24/2016
#
###########################################

'''
This script reads all xml files in a directory and extracts information into a comma-delimited file.
It is made specifically to run on data with specific gestures, and will exit without completing the
data analysis, but will give a helpful error as to the problem with the data. It can detect two types
of errors: Mismatch in name, and mismatch in attribute. Following are a list of names that are
correctly recognized:
Names:
 - ?xml
 - Participant
    - id
 - Personality
    - ex, op, ag, ems / ne, co
 - Story
    - id, order, version
 - Part
    - number, agent_ex_lvl
 - Gesture
    - type, handedness, hold, prep, stroke, se_onset_height, se_onset_width, se_onset_radial,
    se_offset_height, se_offset_width, se_offset_radial, retract, agent_match_loc, agent_match_form

Items are collected until a gesture occurs. When a gesture occurs, the gesture information is read, and
the entire set of items is appended to a CSV file. Then the program continues parsing tags (and files)
until the next gesture.

All data is changed to lowercase prior to being written.
'''

import sys
import glob
import re

output = open('workfile.csv', 'a')

# Create column headers
output.write(
             "P_ID, Extra, Open, Agree, EMS, Cons, S_ID, S_Order, S_Version, P_Number, P_AgentExLvl, G_Type, G_Handedness, "
             "G_Stroke, G_Onset_Height, G_Onset_Width, G_Onset Radial, G_Offset_Height, G_Offset_Width, G_Offset Radial, "
             "G_Retract, Agent_Match_Loc, Agent_Match_Form\n")

# open the input file for reading
for filename in glob.glob('*.xml'):
    try:
        input_file = open(filename, "r")
    except IOError:
        print "Could not open file!"

    # Create all global variables to handle all the columns in excel. Note that this is inside
    # the for loop for each file, so that all variables are set to null each time a file is opened.
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
    g_hold = ""
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

    # creates a big string with all data from the file
    datafile = input_file.read()

    all_data = datafile.partition("<")[2]

    # Removes carriage returns and newline characters from the file
    all_data = all_data.replace('\n', ' ').replace('\r', '')
    all_data = re.sub(' +',' ',all_data)

    # This initializes the list
    all_tags = []

    # Splits the file into a list of tags
    while all_data != "":
        all_tags.append(all_data.partition(">")[0])
        all_data = all_data.partition("<")[2]

    # Main loop that parses each tag
    for tag in all_tags:

        # Get the tag name
        name = tag.partition(" ")[0]
        tag = tag.partition(" ")[2]

        while tag != "":
            # Get the next attribute and its value
            attribute = str.strip((tag.partition("=")[0]))
            tag = tag.partition("\"")[2]
            value = str.lower((tag.partition("\""))[0])
            tag = tag.partition("\"")[2]

            # Find the matching name and attribute, and populate global variables
            if name == "participant":
                if attribute == "id":
                    pid = value
                else:
                    print(filename)
                    sys.exit("ERROR! Participant has an undefined attribute: %s" % attribute)
            elif name == "personality":
                if attribute == "ex":
                    p_ex = value
                elif attribute == "op":
                    p_op = value
                elif attribute == "ag":
                    p_ag = value
                elif attribute == "ems":
                    p_ems = value
                elif attribute == "ne":
                    p_ems = value
                elif attribute == "co":
                    p_co = value
                else:
                    print(filename)
                    sys.exit("ERROR! Personality has an undefined attribute: %s" % attribute)
            elif name == "story":
                if attribute == "id":
                    s_id = value
                elif attribute == "order":
                    s_order = value
                elif attribute == "version":
                    s_version = value
                else:
                    print(filename)
                    sys.exit("ERROR! Story has an undefined attribute: %s" % attribute)
            elif name == "part":
                if attribute == "number":
                    part_number = value
                elif attribute == "agentexlvl":
                    part_agentexlvl = value
                else:
                    print(filename)
                    sys.exit("ERROR! Part has an undefined attribute: %s" % attribute)
            elif name == "gesture":
                if attribute == "type":
                    g_type = value
                elif attribute == "handedness":
                    g_handedness = value
                elif attribute == "hold":
                    g_hold = value
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
                    print(filename)
                    sys.exit("ERROR! Gesture has an undefined attribute: %s" % attribute)
            elif name == "?xml":
                continue
            else:
                print(filename)
                sys.exit("ERROR! Undefined name: %s" % name)
        if name == "gesture":

            # Append all global variables to the output file, separated by commas
            output.write(
            pid + ", " + p_ex + ", " + p_op + ", " + p_ag + ", " + p_ems + ", " + p_co + ", " + s_id + ", " + s_order + ", " +
            s_version + ", " + part_number + ", " + part_agentexlvl + ", " + g_type + ", " + g_handedness + ", " + g_stroke +
            ", " + g_se_onset_height + ", " + g_se_onset_width + ", " + g_se_onset_radial + ", " + g_se_offset_height + ", " +
            g_se_offset_width + ", " + g_se_offset_radial + ", " + g_retract + ", " + g_agent_match_loc + ", " + g_agent_match_form + "\n")

            # Reset all gesture values to null, so information doesn't carry over into the next gesture if it is missing information
            g_type = ""
            g_handedness = ""
            g_hold = ""
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
