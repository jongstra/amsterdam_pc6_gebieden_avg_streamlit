import streamlit as st
import pandas as pd

# Title and info about dataframe.
st.title('AVG Gevoeligheid van Postcode6 gebieden in Amsterdam')
st.text('Lijst is scrollbaar en doorzoekbaar (klik op lijst & druk op ctrl+F/cmd+f).')

# Read prepared Amsterdam Postcode6 file.
df = pd.read_csv('pc6_amsterdam.csv')

# Show full dataframe.
df

# Show additional info about data.
st.subheader('Enkele gegevens')
st.text(f'Aantal postcode6 gebieden in gemeente Amsterdam: {len(df)}')
st.text(f'Aantal postcode6 gebieden dat avg gevoelig is: {df.AVG_GEVOELIG.sum()}')
st.text(f'Aantal postcode6 gebieden dat niet avg gevoelig is: {(~df.AVG_GEVOELIG).sum()}')
st.text('')
st.text('De AVG gevoeligheid is bepaald o.b.v. het aantal huishoudens per postcode6 gebied.')
st.text('Definitie AVG_GEVOELIG: minder dan 15 huishoudens of onbekend aantal huishoudens.')
st.text('')


st.write('Deze informatie is gebaseerd op de CBS kerncijfers naar volledige postcode (PC6), 2020. [Zie link](https://www.cbs.nl/nl-nl/dossier/nederland-regionaal/geografische-data/gegevens-per-postcode).')
st.text('')

st.text('Gemaakt door Thomas Jongstra in 2022')
st.text('Contact: jongstra@gmail.com')