import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw
from PIL import Image

compound_smiles = 'c1cc(C(=O)O)c(OC(=O)C)cc1'
m = Chem.MolFromSmiles(compound_smiles)
im=Draw.MolToImage(m)

st.image(im)
