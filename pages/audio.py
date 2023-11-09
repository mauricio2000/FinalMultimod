import os
import streamlit as st
import time
import glob
import numpy as np
import pytesseract
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
from PIL import Image
from gtts import gTTS
from googletrans import Translator

if 5==5:

        st.subheader("Has elegido AUDIO")
        stt_button = Button(label=" Inicio ", width=200)
        st.write("Toca el Botón y habla lo que quires traducir")
        
        stt_button.js_on_event("button_click", CustomJS(code="""
            var recognition = new webkitSpeechRecognition();
            recognition.continuous = true;
            recognition.interimResults = true;
         
            recognition.onresult = function (e) {
                var value = "";
                for (var i = e.resultIndex; i < e.results.length; ++i) {
                    if (e.results[i].isFinal) {
                        value += e.results[i][0].transcript;
                    }
                }
                if ( value != "") {
                    document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: value}));
                }
            }
            recognition.start();
            """))
        
        result = streamlit_bokeh_events(
            stt_button,
            events="GET_TEXT",
            key="listen",
            refresh_on_update=False,
            override_height=75,
            debounce_time=0)
        
        if result:
            if "GET_TEXT" in result:
                st.write(result.get("GET_TEXT"))
            try:
                os.mkdir("temp")
            except:
                pass
            st.title("Texto a Audio")
            translator = Translator()
            
            text = str(result.get("GET_TEXT"))
            print(text)

