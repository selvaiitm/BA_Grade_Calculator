import streamlit as st

st.text('')


st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<h1 align="center">  TDS Grade Calculator </h1>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
<h2 align="center"> "Education is the most powerful weapon which you can use to change the world." - Nelson Mandela</h2>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
<h3 align="center"> Welcome to the TDS Grade Calculator app, this app is created  for calculating the final grade for TDS of september-2023 term, a Diploma level course for  BS IN DATA SCIENCE COURSE OFFERED BY IIT MADRAS 
""", unsafe_allow_html=True)



st.markdown("<hr>", unsafe_allow_html=True)


# Final course score T = 0.1GAA + 0.2 ROE1 + 0.2 P1 + 0.2P2 + 0.3F

def score_calculator(a,b,c,d,e):
  return 0.1*a + 0.2*b + 0.2*c + 0.2*d + 0.3*e


def Grade_calculator(total_score):
  
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


st.markdown(""" <h5 align = "center">Enter the Graded assignment score:</h5>""", unsafe_allow_html=True)
a = st.number_input(label = " " , key="first_digit_input") 

st.markdown(""" <h5 align = "center">Enter the Programing quiz score:</h5>""", unsafe_allow_html=True)
b = st.number_input(label = " " , key="second_digit_input")  # Using an empty string as label

st.markdown(""" <h5 align = "center">Enter the Course project one score:</h5>""", unsafe_allow_html=True)
c = st.number_input(label = " " , key="third_digit_input")  # Using an empty string as label

st.markdown(""" <h5 align = "center">Enter the Course project two score:</h5>""", unsafe_allow_html=True)
d = st.number_input(label = " " , key="fourth_digit_input")  # Using an empty string as label

st.markdown(""" <h5 align = "center">Enter the Endterm Exam score:</h5>""", unsafe_allow_html=True)
e = st.number_input(label = " " , key="fifth_digit_input")  # Using an empty string as label

Total_score = score_calculator(a,b,c,d,e)

grade = Grade_calculator(Total_score)



if st.button('Start Calculating!'):
  
  st.markdown(f"""
  <h3 align="center">Your Total Score : {Total_score:.2f} 
  """, unsafe_allow_html=True)
  st.markdown(f"""
  <h3 align="center">Your Grade for TDS is : {grade} 
  """, unsafe_allow_html=True)

st.markdown("""
<h2 align="center"> Created by N.Tamilselvan - 21f2001270</h2>
""", unsafe_allow_html=True)
