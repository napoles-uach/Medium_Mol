import streamlit as st
from stmol import showmol
import py3Dmol

def render_mol(xyz):
    xyzview = py3Dmol.view(width=400,height=400)
    xyzview.addModel(xyz,'xyz')
    xyzview.setStyle({'sphere':{}})
    xyzview.setBackgroundColor('white')#('0xeeeeee')
    xyzview.zoomTo()
    showmol(xyzview, height = 500,width=800)

uploaded_files = st.sidebar.file_uploader("Choose xyz files", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    xyz = uploaded_file.getvalue().decode("utf-8")
    render_mol(xyz)
