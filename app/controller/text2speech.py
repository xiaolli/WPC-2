from watson_developer_cloud import TextToSpeechV1

username = "!@#$%^&*()"   #替换
password = "(*&^%$#@!"    #替换

def test2speech(text,filename):
    watson_speech = TextToSpeechV1(username=username,password=password)
    with open(filename,'wb') as file:
        file.write(watson_speech.synthesize(text=text,
                                            voice='en-US_AllisonVoice'))


