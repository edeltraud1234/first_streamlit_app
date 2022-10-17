import pandas
my_fruit_list = pandas.read_csv("dir/snowflake_Training/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
