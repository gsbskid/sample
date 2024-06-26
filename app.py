import base64
import json
import os
import re
import time
import uuid
from io import BytesIO
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st
from streamlit_drawable_canvas import st_canvas
from svgpathtools import parse_path

drawing_mode = st.sidebar.selectbox(
    'Drawing tool : ',
    (
        'freedraw' , 
        'line' , 
        'rect' , 
        'circle' , 
        'transform' , 
        'polygon' , 
        'point'
    )
)

stroke_width = st.sidebar.slider(
    'Stroke width : ', 
    1 , 25 , 3
)

if drawing_mode == 'point' : point_display_radius = st.sidebar.slider(
    'Point display radius : ', 
    1 , 25 , 3
)

stroke_color = st.sidebar.color_picker('Stroke color hex : ')
bg_color = st.sidebar.color_picker('Background color hex: ' , '#eee')
bg_image = st.sidebar.file_uploader('Background image : ' , type = ['png' , 'jpg'])
realtime_update = st.sidebar.checkbox('Update in realtime' , True)

canvas_result = st_canvas(
    fill_color = 'rgba(255, 165, 0, 0.3)' , 
    stroke_width = stroke_width , 
    stroke_color = stroke_color , 
    background_color = bg_color , 
    background_image = None , 
    update_streamlit = realtime_update , 
    height = 150 , 
    drawing_mode = drawing_mode , 
    point_display_radius = 0 , 
    display_toolbar = st.sidebar.checkbox('Display toolbar' , True) , 
    key = 'full_app'
)

if canvas_result.image_data is not None : st.image(canvas_result.image_data)
