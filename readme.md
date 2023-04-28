Author: Bryce Patterson
Due February 13, 2023


Brief Overview
This program is designed to detect whether a particular point is present 
within a polygon. It takes a file as input from the command line and 
outputs whether the point is inside, outside, or on the edge of a polygon. This
is done by drawing a ray in the right horizontal direction from the point, 
and if the ray intersects with the edges an odd total amount of times it is
considered inside, and outside if it is an even amount of times. Only in special
cases is it considered on the edge.
It should be noted that such a program can only calculate to a degree of
certainty whether a point is inside or outside when the point and edge are
substantially close together. To give the user more control, at the top of
the program is a function called approx. To calculate points with a finer
degree of certainty simply change the threshold variable to a smaller amount,
and larger for a higher degree of ambiguity.

Instructions on how to Compile and Run the Point In Polygon Program
1. Create an input file that the program can run in the following manner:
[Insert number of polygon edges here]
[Insert each polygon edge on its own line, no more or less than the previous 
number]
[Insert each query point to be tested, also on its own line]
An example can be found in testfile.txt
2. Run the program
Using your operating system's command line, go to the directory that holds the 
program and type the following, then press enter:
python3 PointInPolygon.py
3. Input the desired file
You will be prompted for the input file. Make sure it is in the same directory
that the program is in, and type in the name with the file extension. Be advised
that this may not support all file types, .txt extensions are ideal. Press enter
when finished, and the program will output the point's position in relation to
the polygon.
