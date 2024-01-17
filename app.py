import streamlit as st
import pickle
import pandas as pd
teams=['Rajasthan Royals',
 'Royal Challengers Bangalore',
 'Sunrisers Hyderabad',
 'Delhi Capitals',
 'Chennai Super Kings',
 'Gujarat Titans',
 'Lucknow Super Giants',
 'Kolkata Knight Riders',
 'Punjab Kings',
 'Mumbai Indians']

cities=['Ahmedabad', 'Kolkata', 'Mumbai', 'Navi Mumbai', 'Pune', 'Dubai',
       'Sharjah', 'Abu Dhabi', 'Delhi', 'Chennai', 'Hyderabad',
       'Visakhapatnam', 'Chandigarh', 'Bengaluru', 'Jaipur', 'Indore',
       'Bangalore', 'Raipur', 'Ranchi', 'Cuttack', 'Dharamsala', 'Nagpur',
       'Johannesburg', 'Centurion', 'Durban', 'Bloemfontein',
       'Port Elizabeth', 'Kimberley', 'East London', 'Cape Town']
st.title('IPL 2024 Win Predictor')
pipe=pickle.load(open('pipe .pkl','rb'))
c1,c2 = st.columns(2)
with c1:
 batting=st.selectbox('Select the Batting Team',teams)
with c2:
 bowling=st.selectbox('Select the Bowling Team',teams)

venue=st.selectbox('Select match venue ',cities)

target=st.number_input('Target Score')

c3,c4,c5=st.columns(3)

with c3:
    curr_score=st.number_input('Current Score')
with c4:
    wickets=st.number_input('Wickets out')
with c5:
    overs=st.number_input('Overs Completed')
if st.button('Predict Winning Probability'):
    runs_left=target-curr_score
    balls_left=120-(6*overs)
    wickets_left=10-wickets
    CRR=curr_score/overs
    RRR=(runs_left*6)/balls_left

    input_df=pd.DataFrame({'BattingTeam':[batting],'Bowling_team':[bowling],'City':[venue],'runs_left':[runs_left],'balls_left':[balls_left],'Wickets_left':[wickets_left],'total_run_x':[target],'CRR':[CRR],'RRR':[RRR]})

    prob=pipe.predict_proba(input_df)
    win=prob[0][1]*100
    loss=prob[0][0]*100
    st.header("Batting Team "+"- "+str(round(win))+"%")
    st.header("Bowling Team "+"- "+str(round(loss))+"%")