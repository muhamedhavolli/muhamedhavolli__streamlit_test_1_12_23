import streamlit as st

the_input = st.text_input('')


def convert_list(the_input):
    lista = the_input.split()
    return lista

if st.button('Return List'):
    var1 = convert_list(the_input)
    st.write(var1)

#########################

empty_list = []
alfa = convert_list(the_input)

def convert_lower(empty_list):
    for i in alfa:
        i = i.lower()
        empty_list.append(i)
    return empty_list
            
    
    
if st.button('Lower'):
    var2 = convert_lower(empty_list)
    st.write(var2)
    



    
##########################


def count():
    counteri = 0
    beta = convert_list(the_input)
    for i in beta:
        counteri += 1
    return(counteri)


if st.button('PRINT_COUNT'):
    var3 = str(count())
    st.write('THERE ARE ' + var3 + ' ELEMENTS.')
    
    
    
    