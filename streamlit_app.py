import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title('Hola viajero 🥣 🥗 🐔 🥑🍞')

streamlit.header('te deseo')
streamlit.text('un maravilloso dia')
streamlit.header('🍌🥭 Recuerda alimentarte bien 🥝🍇')

streamlit.dataframe(my_fruit_list)
