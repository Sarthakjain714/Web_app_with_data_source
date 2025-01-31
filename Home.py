import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
col1,col2=st.columns(2)

with col1:
    st.write("<br><br>",unsafe_allow_html=True)
    st.image("images/PassportSizePhoto.jpg",width=200)

with col2:
    st.header("Sarthak Jain")
    description='''<b style="font-size:0.7rem">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
     has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a 
     galley of type and scrambled it to make a type specimen book. It has survived not only five 
     centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
     It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
    and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem 
    Ipsum<b>'''
    st.write(description,unsafe_allow_html=True)

st.title("Projects :")

col3,emptycol,col4=st.columns(3)
df=pd.read_csv('data.csv',sep=';')


with col3:
    for index,rows in df[:10].iterrows():
        # print (rows)
        st.markdown(f"<b><p style='font-size:20px'>{rows['title']}</p></b>",unsafe_allow_html=True)
        st.image(f"images/{rows['image']}")
        st.write(rows['description'])
        st.write(f"[Source Code]({rows['url']})")

with col4:
    for index,rows in df[10:].iterrows():
        # print (rows)
        st.markdown(f"<b><p style='font-size:20px'>{rows['title']}</p></b>",unsafe_allow_html=True)
        # st.title(st.markdown(f"<p style='font-size:20px;{rows['title']}</p>",unsafe_allow_html=True))
        st.image(f"images/{rows['image']}")
        st.write(rows['description'])
        st.write(f"[Source Code]({rows['url']})")





