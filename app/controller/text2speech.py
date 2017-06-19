from watson_developer_cloud import TextToSpeechV1

username = "78c9c3f1-1251-414e-b507-618b3550f78d"
password = "6R1z00D82B0U"

def test2speech(text,filename):
    watson_speech = TextToSpeechV1(username=username,password=password)
    with open(filename,'wb') as file:
        file.write(watson_speech.synthesize(text=text,
                                            voice='en-US_AllisonVoice'))


