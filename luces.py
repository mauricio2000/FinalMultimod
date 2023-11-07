import paho.mqtt.client as paho
import time
import streamlit as st
import json
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
    message =json.dumps({"Analog": act2})
    ret= client1.publish("mauri2", message)
    
 
else:
    st.write('')

if st.button('Cerrar'):
    act2="Cerrao"
    client1= paho.Client("ESTE_ES_MAURI2")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)   
    message =json.dumps({"Analog": act2})
    ret= client1.publish("mauri2", message)
    
 
else:
    st.write('')
