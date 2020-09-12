
import streamlit as st
PAGE_CONFIG = {"page_title":"colab.io","layout":"centered"}




st.title("neural network visualizer")
st.subheader("App in progress")
  #URI = 'url for the server'
if st.button('predict'):
   #response = requests.post(URI, data{})
   response = json.loads(response.text)
   image = response.get('image')
   prediction = response.get('prediction')
   image = np.reshape(image, (28,28))
   st.image(image, width=150)
menu = ["Image","About"]
choice = st.sidebar.selectbox('Menu',menu)
if choice == 'Image':
		st.subheader("Showing image")	
