import streamlit as st
import pandas as pd
import numpy as np
import joblib

model =  joblib.load('model/model_rl (1).pkl')

st.title ("Application inclusion Financiere Afrique")

contry = st.selectbox( "Quels est votre pays",("Kenya", "Rwanda", "Tanzanie", "Uganda"))
annee = st.number_input ("Année au cours de laquelle l'enquête a été réalisée.")
localisation = st.selectbox( "Quels est votre localisation",("Rural", "Urban"))
acces_tel = st.selectbox("Si la personne interrogée a accès à un téléphone portable", ("Yes","No"))
hab = st.number_input ("Nombre de personnes vvant dans la maison")
age_repon = st.number_input ("Age des repondants")
genre_repon = st.selectbox ("Genre des repondants", ("Masculin","Feminin"))
lien_paren = st.selectbox ("Lien de parenté de la personne interrogée avec le chef de famille", ("Head of Household",
    "Spouse",
    "Child",
    "Parent",
    "Other relative",
    "Other non-relatives"))

sta_mar = st.selectbox ("Situation matrimonale :",("Married/Living together",
    "Divorced/Seperated",
    "Widowed",
    "Single/Never Married",
    "Dont know" ))

educ = st.selectbox ("Niveau d'études le plus élevé",("No formal education",
    "Primary education",
    "Secondary education",
    "Vocational/Specialised training",
    "Tertiary education",
    "Other/Dont know/RTA"))

travail = st.selectbox ("Travail de la personne interviewer ",("Self employed",
    "Government Dependent",
     "Formally employed Private",
    "Informally employed",
      "Formally employed Government",
     "Farming and Fishing",
      "Remittance Dependent",
     "Other Income",
      "Dont Know/Refuse to answer",
     "No Income"))

# Encodage
if contry == "Kenya":
    contry = 1
elif contry == "Rwanda":    contry = 2
elif contry == "Tanzania":  contry = 3
elif contry == "Uganda":    contry = 4

loc_dict = {
    'Urban': 1,
    'Rural': 0
}
localisation_num = loc_dict[localisation]

bank_dict = {
    'Yes': 1,
    'No': 0
}
acces_tel_mum = bank_dict[acces_tel]

gender_dict = {
    'Masculin': 1,
    'Feminin': 0
}

genr_num = gender_dict[genre_repon]

lien_dic = {
    'Head of Household': 1,
    'Spouse': 2,
    'Child': 3,
    'Parent':4,
    'Other relative' : 5,
    'Other non-relatives' : 6
}

lien_num = lien_dic[lien_paren]

marital_dict = {
    'Married/Living together': 1,
    'Divorced/Seperated': 2,
    'Widowed': 3,
    'Single/Never Married': 4,
    'Dont know' : 5
}

sta_mar_num = marital_dict[sta_mar]

educa_dict = {
    'No formal education':1,
    'Primary education':2,
    'Secondary education':3,
    'Vocational/Specialised training':4,
    'Tertiary education':5,
    'Other/Dont know/RTA':6
}

edu_num = educa_dict[educ]

job_dic = {
    'Self employed': 1,
    'Government Dependent': 2,
       'Formally employed Private': 3,
    'Informally employed':4,
       'Formally employed Government' : 5,
     'Farming and Fishing' : 6,
       'Remittance Dependent' : 7,
     'Other Income' : 8,
       'Dont Know/Refuse to answer' : 9,
     'No Income': 10
}
travail_num = job_dic[travail]


df_pred = pd.DataFrame([[contry,annee,localisation_num,acces_tel_mum,hab,age_repon
                           ,genr_num,lien_num,sta_mar_num,edu_num,travail_num]])


if st.button ("Predire :"):
    pred = model.predict(df_pred)
    st.success(f"Resultat de la prediction: {pred[0]}")