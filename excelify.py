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
    attribute = (tag.partition("=")[0])
    tag = tag.partition("\"")[2]
    value = (tag.partition("\""))[0]
    print attribute, value
