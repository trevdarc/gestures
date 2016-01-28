# python code
# Look for an XML parser in python. There may be one that can make our lives easier.


# Create all global variables to handle all the columns in excel
var id
var pid
var sid
var duration
var whatever_else

# Iterate through XML tags in the file
# For each tag, get the first word, directly after the open bracket
switch {
  case participant
    do this stuff
  case another thing
    do other stuff
  case yet another thing
    do another bunch of stuff
  case gesture
    grab the rest of the data into relevant variables
    spit out all the variables, in order, into the csv file separated by commas, and then add a line break.
}
Iterate until no more xml tags exist in the file.
