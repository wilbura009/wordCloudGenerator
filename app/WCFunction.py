import os
import re
import sys

from os import path
from wordcloud import WordCloud

def generateWordCloud(fileIn):
    absPath = os.path.abspath(__file__)
    prjRoot = os.path.dirname(absPath)
    imgPath = os.path.dirname(absPath) + "/img"

    textFile = "temp.txt"
    os.rename( fileIn, textFile )

    outputFile = re.sub( r"(^.*)(\..*)", r"\1", textFile ) # strip extension from file name
    outputFile = outputFile + ".png" # append extension
    outputFile = path.join(imgPath, outputFile) # Full path to output file
    
    # Read the whole text.
    text = open( textFile ).read()

    wordcloud = WordCloud( scale=5, max_font_size=30).generate(text)

    wordcloud.to_file(outputFile) # output the wordcloud to .png

    os.remove( os.path.abspath(textFile) ) #remove to uploaded text file

    # Display the generated image:
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    return
