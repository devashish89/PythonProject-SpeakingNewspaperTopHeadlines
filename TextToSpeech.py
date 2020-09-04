

# Calling the Disptach method of the module which
# interact with Microsoft Speech SDK to speak
# the given input from the keyboard
def speak(val):
    import win32com.client
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(val)
