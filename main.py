import streamlit as st


st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<h1 align="center">  BA Grade Calculator </h1>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
<h2 align="center"> "Education is the most powerful weapon which you can use to change the world." - Nelson Mandela</h2>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
<h3 align="center"> Welcome to the BA Grade Calculator app, this app is created  for calculating the final grade for BA of september-2023 term, a Diploma level course for  BS IN DATA SCIENCE COURSE OFFERED BY IIT MADRAS 
""", unsafe_allow_html=True)



st.markdown("<hr>", unsafe_allow_html=True)




def score_calculator(a,b,c,d,e):

  assignment = 0.4*a

  
  # Quiz Marks = 0.7*Max(Qz1, Qz2) + 0*3Min(Qz1, Qz2)
  
  quiz = 0.14*max(b,c) + 0.06*min(b,c)
  
  end_term = e*.4
  
  total_score = quiz+assignment+end_term+d
  if total_score >100:
    total_score = 100
  return total_score




def Grade_calculator(total_score,e):

  end_term = e*.40

  if end_term >10:
    
  
    if total_score >= 90:
      return 'S'
    
    elif total_score >= 80:
      return 'A'
  
    elif total_score >= 70:
      return 'B'
  
    elif total_score >= 60:
      return 'C'
  
    elif total_score >= 50:
      return 'D'
  
    elif total_score >= 40:
      return 'E'
  
    else:
      return 'F'

  else:
    return 'F'

st.markdown(""" <h3 align = "center"> Enter all the scores as visible in the dashboard </h3> """, unsafe_allow_html=True)

st.markdown(""" <h5 align = "center">Enter the Average  assignment for final score :</h5>""", unsafe_allow_html=True)
a = st.number_input(label = " " , key="first_digit_input") 

st.markdown(""" <h5 align = "center">Enter the quiz one score , enter zero if absent:</h5>""", unsafe_allow_html=True)
b = st.number_input(label = " " , key="second_digit_input")  # Using an empty string as label

st.markdown(""" <h5 align = "center">Enter the quiz two score, enter zero with absent:</h5>""", unsafe_allow_html=True)
c = st.number_input(label = " " , key="third_digit_input")  # Using an empty string as label

st.markdown(""" <h5 align = "center">Enter the bonus marks :</h5>""", unsafe_allow_html=True)
d = st.number_input(label = " " , key="fourth_digit_input")  # Using an empty string as label

st.markdown(""" <h5 align = "center">Enter the Endterm Exam score:</h5>""", unsafe_allow_html=True)
e = st.number_input(label = " " , key="fifth_digit_input")  # Using an empty string as label

Total_score = score_calculator(a,b,c,d,e)

grade = Grade_calculator(Total_score,e)

end_term = e*.4
assignment = 0.4*a

quiz = .14*max(b,c)+.06*min(b,c)

if st.button('Start Calculating!'):

  st.markdown(f"""
  <h3 align="center">Your quiz score out of 20 : {quiz:.2f}
  """, unsafe_allow_html=True)


  st.markdown(f"""
  <h3 align="center">Your assignmnet score out of 40 : {assignment:.2f}
  """, unsafe_allow_html=True)
  
  
  st.markdown(f"""
  <h3 align="center">Your End Term Score out of 40 capped to 40: {end_term:.2f} 
  """, unsafe_allow_html=True)

  st.markdown(f"""
  <h3 align="center">Your Bonus score : {d}
   """, unsafe_allow_html=True)


  st.markdown(f"""
  <h3 align="center">Your Total Score : {Total_score:.2f} 
  """, unsafe_allow_html=True)
  
  st.markdown(f"""
  <h3 align="center">Your Grade for BA is : {grade} 
  """, unsafe_allow_html=True)

  st.markdown("<hr>", unsafe_allow_html=True)
  
  
  st.markdown(f"""
    <h3 align="center">No Score rounding off is done in the above calculations, Your grades or Total Score may vary based on Score Rounding off by IITM
     """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
<h2 align="center"> Created by N.Tamilselvan - 21f2001270</h2>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
<h4 align="center"> Dedicating this app to KALPITA the course TA for BA , for her selfless dedication towards teaching us the concepts in depth and maintaining a record of all the live sessions recordings for the students for easy reference in the future and for the prompt reply in the discourse forum regarding any doubts we had in the subject. </h4>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

