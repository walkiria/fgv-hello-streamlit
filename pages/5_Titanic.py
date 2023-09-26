from urllib.error import URLError

import altair as alt
import pandas as pd
import pickle

import streamlit as st
from streamlit.hello.utils import show_code

model=pickle.load(open(r"model/titanic_v0.pkl",'rb'))     ## Load pickeled ml model


def main():

    """ main() contains all UI structure elements; getting and storing user data can be done within it"""
    st.title("Titanic Survival Prediction")                                                                              ## Title/main heading
    # st.image(r"titanic_sinking.jpg", caption="Sinking of 'RMS Titanic' : 15 April 1912 in North Atlantic Ocean",use_column_width=True) ## image import
    st.write("""## Would you have survived From Titanic Disaster?""")                                                    ## Sub heading

    ## Side Bar Configurations
    st.sidebar.header("More Details:")
    st.sidebar.markdown("[For More facts about the Titanic here](https://www.telegraph.co.uk/travel/lists/titanic-fascinating-facts/#:~:text=1.,2.)")
    st.sidebar.markdown("[and here](https://titanicfacts.net/titanic-survivors/)")
    st.title("-----          Check Your Survival Chances          -----")

    ## Framing UI Structure
    Sex = st.selectbox("Select Gender:", ["Male","Female"])                         # select box for gender[Male|Female]
    if Sex == "Female":
        Sex_female = 1
        Sex_male   = 0
    else:
        Sex_female = 0
        Sex_male   = 1

    Pclass= st.selectbox("Select Passenger-Class:",[1,2,3])                        # Select box for passenger-class

    ## Getting & Framing Data: Collecting user-input into dictionary
    data={"Pclass":Pclass,"Sex_female":Sex_female,'Sex_male':Sex_male}

    df=pd.DataFrame(data,index=[0])      ## converting dictionary to Dataframe
    return df

data=main()                             ## calling Main()


## Prediction:
if st.button("Predict"):                                                                ## prediction button created,which returns predicted value from ml model(pickle file)
    result = model.predict(data)                                                        ## prediction of user-input
    proba=model.predict_proba(data)                                                     ## probabilty prediction of user-input
    #st.success('The output is {}'.format(result))

    if result[0] == 1:
        st.write("***congratulation !!!....*** **You probably would have made it!**")
        # st.image(r"lifeboat.jfif")
        # st.write("**Survival Probability Chances :** 'NO': {}%  'YES': {}% ".format(round((proba[0,0])*100,2),round((proba[0,1])*100,2)))
    else:
        st.write("***Better Luck Next time !!!!...*** **you're probably Ended up like 'Jack'**")
        # st.image(r"Rip.jfif")
        # st.write("**Survival Probability Chances :** 'NO': {}%  'YES': {}% ".format(round((proba[0,0])*100,2),round((proba[0,1])*100,2)))