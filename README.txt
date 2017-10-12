{\rtf1\ansi\ansicpg1252\cocoartf1348\cocoasubrtf170
{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;\f1\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red67\green67\blue67;\red40\green145\blue225;\red38\green38\blue38;
\red242\green242\blue242;}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid1\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid1}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sa200

\f0\b\fs28 \cf2 \expnd0\expndtw0\kerning0
Scraping Numbers from HTML using BeautifulSoup
\b0 \expnd0\expndtw0\kerning0
\'a0In this assignment you will write a Python program similar to\'a0{\field{\*\fldinst{HYPERLINK "http://www.py4e.com/code3/urllink2.py"}}{\fldrslt \cf3 \expnd0\expndtw0\kerning0
http://www.py4e.com/code3/urllink2.py}}. The program will use\'a0
\b \expnd0\expndtw0\kerning0
urllib
\b0 \expnd0\expndtw0\kerning0
\'a0to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.\
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.\
\pard\tx220\tx720\pardeftab720\li720\fi-720
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 {\listtext	\'95	}\expnd0\expndtw0\kerning0
Sample data:\'a0{\field{\*\fldinst{HYPERLINK "http://py4e-data.dr-chuck.net/comments_42.html"}}{\fldrslt \cf3 \expnd0\expndtw0\kerning0
http://py4e-data.dr-chuck.net/comments_42.html}}\'a0(Sum=2553)\
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	\'95	}\expnd0\expndtw0\kerning0
Actual data:\'a0{\field{\*\fldinst{HYPERLINK "http://py4e-data.dr-chuck.net/comments_38751.html"}}{\fldrslt \cf3 \expnd0\expndtw0\kerning0
http://py4e-data.dr-chuck.net/comments_38751.html}}\'a0(Sum ends with 28)\uc0\u8232 \
\pard\pardeftab720
\cf2 \expnd0\expndtw0\kerning0
You do not need to save these files to your folder since your program will read the data directly from the URL.\'a0
\b \expnd0\expndtw0\kerning0
Note:
\b0 \expnd0\expndtw0\kerning0
\'a0Each student will have a distinct data url for the assignment - so only use your own data url for analysis.\
\pard\pardeftab720\sa200
\cf2 \expnd0\expndtw0\kerning0
\
\pard\pardeftab720

\b \cf2 \expnd0\expndtw0\kerning0
Data Format\
\pard\pardeftab720\sa200

\b0 \cf2 \expnd0\expndtw0\kerning0
The file is a table of names and comment counts. You can ignore most of the data in the file except for lines like the following:\
\pard\pardeftab720\sl360

\f1\fs26 \cf4 \cb5 \expnd0\expndtw0\kerning0
<tr><td>Modu</td><td><span class="comments">90</span></td></tr>\
<tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>\
<tr><td>Hubert</td><td><span class="comments">87</span></td></tr>\
\pard\pardeftab720

\f0\fs28 \cf2 \cb1 \expnd0\expndtw0\kerning0
You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.\
\pard\pardeftab720\sa200
\cf2 \expnd0\expndtw0\kerning0
Look at the\'a0{\field{\*\fldinst{HYPERLINK "http://www.py4e.com/code3/urllink2.py"}}{\fldrslt \cf3 \expnd0\expndtw0\kerning0
sample code}}\'a0provided. It shows how to find all of a certain kind of tag, loop through the tags and extract the various aspects of the tags.\
\pard\pardeftab720\sl360

\f1\fs26 \cf4 \cb5 \expnd0\expndtw0\kerning0
...\
# Retrieve all of the anchor tags\
tags = soup('a')\
for tag in tags:\
   # Look at the parts of a tag\
   print 'TAG:',tag\
   print 'URL:',tag.get('href', None)\
   print 'Contents:',tag.contents[0]\
   print 'Attrs:',tag.attrs\
\pard\pardeftab720

\f0\fs28 \cf2 \cb1 \expnd0\expndtw0\kerning0
You need to adjust this code to look for\'a0
\b \expnd0\expndtw0\kerning0
span
\b0 \expnd0\expndtw0\kerning0
\'a0tags and pull out the text content of the span tag, convert them to integers and add them up to complete the assignment.\
\pard\pardeftab720\sa200
\cf2 \expnd0\expndtw0\kerning0
\

\b \expnd0\expndtw0\kerning0
Sample Execution
\b0 \expnd0\expndtw0\kerning0
\
\
\pard\pardeftab720\sl360

\f1\fs26 \cf4 \cb5 \expnd0\expndtw0\kerning0
$ python3 solution.py\
Enter - http://py4e-data.dr-chuck.net/comments_42.html\
Count 50\
Sum 2...\
}