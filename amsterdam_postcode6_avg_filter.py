import streamlit as st
import pandas as pd

st.title('AVG Gevoeligheid van Postcode6 gebieden in Amsterdam')

st.text('Lijst is scrollbaar en doorzoekbaar (klik op lijst & druk op ctrl+F/cmd+f).')

# Read prepared Amsterdam Postcode6 file.
df = pd.read_csv('pc6_amsterdam.csv')

df

st.subheader('Enkele gegevens:')
st.text(f'Aantal postcode6 gebieden in gemeente Amsterdam: {len(df)}')
st.text(f'Aantal postcode6 gebieden dat avg gevoelig is: {df.AVG_GEVOELIG.sum()}')
st.text(f'Aantal postcode6 gebieden dat niet avg gevoelig is: {(~df.AVG_GEVOELIG).sum()}')
st.text('De AVG gevoeligheid is bepaald op basis van het aantal huishoudens per postcode6 gebied.')
st.text('Bij 15 of minder huishoudens wordt het postcode6 gebied als AVG_GEVOELIG aangemerkt.')
st.text('')
st.text('Deze informatie is gebaseerd op de CBS kerncijfers naar volledige postcode (PC6), 2020.')
st.text('Databron link: https://www.cbs.nl/nl-nl/dossier/nederland-regionaal/geografische-data/gegevens-per-postcode')
st.text('')
st.text('Gemaakt door Thomas Jongstra in 2022')
st.text('Contact: jongstra@gmail.com')