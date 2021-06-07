# Getting the audio file out of Video
import moviepy.editor as mp
newsfilename= input("enter the name of your news video file (Eg.: MyNewsVideo.mp4): ")
try:
    news_clip = mp.VideoFileClip(newsfilename)
except:
    print(f"\033[1;31mNo file found named as '{newsfilename}'. Make sure that you dont forgot to add extension of your video file.")
    exit()
audioformat = '.wav'
audiofile = newsfilename+audioformat
# print(news_clip)
news_clip.audio.write_audiofile(audiofile)


# ================================================================#


# Getting text out of audio file
import speech_recognition as sr
filename = audiofile
r = sr.Recognizer()
# open the file
with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    ex = r.recognize_google(audio_data)
    # print(ex)


# ================================================================#

# Fetching Entities
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

sent = preprocess(ex)
pattern = 'NP: {<DT>?<JJ>*<NN>}'
cp = nltk.RegexpParser(pattern)
cs = cp.parse(sent)
# print(cs)
from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint
iob_tagged = tree2conlltags(cs)
# pprint(iob_tagged)
listOfEntities = list()
for i in iob_tagged:
    if ((i[1]=='NNP') or (i[1]=='NN') ):
        listOfEntities.append(i[0])

# Removing the dublicates from list of entities 
listOfEntities = list(dict.fromkeys(listOfEntities))
print(listOfEntities)