import paho.mqtt.client as paho
import time
import streamlit as st
import json
import os
import cv2
import time
import glob
import pytesseract
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
values = 0.0
act1="OFF"
act2="Cerrao"

def on_publish(client,userdata,result):             #create function for callback
    print("el dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received=str(message.payload.decode("utf-8"))
    st.write(message_received)

        


broker="157.230.214.127"
port=1883
client1= paho.Client("ESTE_ES_MAURI2")
client1.on_message = on_message



st.title("Casa Inteligente cmqtt")
st.write("Control de luces")
if st.button('Encender luces'):
    act1="Encendido"
    client1= paho.Client("ESTE_ES_MAURI2")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("mauri1", message)
 
    #client1.subscribe("Sensores")
    
    
else:
    st.write('')

if st.button('Apagar Luces'):
    act1="Apagado"
    client1= paho.Client("ESTE_ES_MAURI2")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("mauri1", message)
  
    
else:
    st.write('')

st.write("Control puerta")

if st.button('Abrir'):
    act2="Abrido"
    client1= paho.Client("ESTE_ES_MAURI2")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)   
    message =json.dumps({"Act2": act2})
    ret= client1.publish("mauri1", message)
    
 
else:
    st.write('')

if st.button('Cerrar'):
    act2="Cerrao"
    client1= paho.Client("ESTE_ES_MAURI2")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)   
    message =json.dumps({"Act2": act2})
    ret= client1.publish("mauri1", message)
    
 
else:
    st.write('')

st.write("Toca el Botón y habla lo que quires traducir")
stt_button = Button(label=" Inicio ", width=200)       
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
