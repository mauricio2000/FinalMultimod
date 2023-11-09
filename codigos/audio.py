import os
import cv2
import streamlit as st
import time
import glob
import numpy as np
import pytesseract
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
from PIL import Image

st.subheader("Has elegido AUDIO")
stt_button = Button(label=" Inicio ", width=200)
        

