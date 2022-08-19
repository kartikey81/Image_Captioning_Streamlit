%%writefile app.py
import streamlit as st
import pandas as pd
import os
import numpy as np
from  PIL import Image, ImageOps
import caption_web
html_temp = """
    <div class="" style="background-color:#3399ff;">
    <div class="clearfix">
    <div class="col-md-12">
    <center><p style="font-size:40px;color:white;margin-top:10px;">Major Project on </p></center>
    <center><p style="font-size:40px;color:white;margin-top:10px;">Artificial Intelligence & Data Science </p></center>
    </div>
    </div>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)
st.title("""
         Image_Captioning Project
         """
         )
file= st.file_uploader("Please upload image", type=("jpg", "png"))

if file is None:
  st.text("Please upload an Image file")
else:
  image=Image.open(file)
  path = "static/{}".format(file.name)
  image.save(path)
  image1=np.array(image)
  #file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
  #image = cv2.imdecode(file_bytes, 1)
  st.image(image1,caption='Uploaded Image.', use_column_width=True)
    
if st.button("Predict Caption"):
  path = "static/{}".format(file.name)
  
  

 
  caption = caption_web.image_caption(path)
  result_dic = {
            'image' : path,
            'caption' : caption
        }
  st.success('The image Caption is  """  {}  """'.format(result_dic['caption']))
if st.button("About"):
  st.header("Kartikey Sharma")
  st.subheader("Student, Department of Computer Engineering")
  
html_temp = """
   <div class="" style="background-color:#993333;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:20px;color:white;margin-top:10px;">Department of Computer Engineering</p></center> 
   <center><p style="font-size:20px;color:white;margin-top:10px;">Poornima Institute of Engineering & Technology</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)
