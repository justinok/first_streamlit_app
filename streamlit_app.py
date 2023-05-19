import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title('Hola viajero 🥣 🥗 🐔 🥑🍞')

streamlit.header('te deseo')
streamlit.text('un maravilloso dia')
streamlit.header('🍌🥭 Recuerda alimentarte bien - Creador de smoothies 🥝🍇')
# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
