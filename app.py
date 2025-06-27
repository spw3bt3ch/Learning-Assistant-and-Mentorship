import streamlit as st 
import openai
import requests

st.header('Learning Assistant & Mentorship')
st.write('Powered by openAi')

tab1, tab2, tab3 = st.tabs(['Home', 'Learning Assistant', 'Mentor'])

text = """Welcome to Your Personal Growth Companion
AI-Powered Learning Assistant & Mentor App

Whether you're aiming to master a new skill, understand complex topics, or navigate your personal or career journey — you're in the right place.

1. Learn Smarter with your AI Learning Assistant
Step-by-step lessons, interactive quizzes, and real-time feedback tailored to your pace and level — from beginner to expert.

2. Grow Wiser with your AI Mentor
Get thoughtful guidance, personalized advice, and a growth roadmap shaped around your goals, strengths, and challenges.

Start your journey today — because knowledge is power, and wisdom is direction.

🚀 Learn. Grow. Succeed.


"""

with tab1:
  st.write(text)

with tab2:
  with st.form('learning'):
    st.subheader('This is a Learning Assistance page')
    user_input = st.text_input('What would you like to learn today? Type the topic, I\'ve got your back')
    submitted = st.form_submit_button('Start Learning')

    if submitted:
      if user_input:
        url = "https://open-ai21.p.rapidapi.com/conversationllama"

        payload = {
          "messages": [
            {
              "role": "user",
              "content": f"Act as my AI Learning Assistant. Help me learn {user_input} from beginner to advanced level. Start with the basics, explain each concept clearly, give me examples, and ask me short questions to test my understanding after each step. Only move to the next topic after I answer correctly; Also help with concept, exercises, errors, platform navigation;Friendly, adaptive, real-time, personalized based on learning style. Explain topics step-by-step, Answer technical/coding questions - Debug code, provide learning resources - Adapt explanations to student level; When referred."
            }
          ],
          "web_access": False
        }
        headers = {
          "x-rapidapi-key": "a67d2a453emsh4d691d4dacd48efp13df79jsned94b02796f0",
          "x-rapidapi-host": "open-ai21.p.rapidapi.com",
          "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        resp = dict(response.json())

        st.write(resp['result'])

with tab3:
  with st.form('mentor'):
    st.subheader('This is Mentor page')
    goal = st.text_input('What would you like me to mentor you about? Type-in your Field or Goal')
    submitted = st.form_submit_button('Get Mentorship')

    if submitted:
      if goal:

        url = "https://open-ai21.p.rapidapi.com/conversationllama"

        payload = {
          "messages": [
            {
              "role": "user",
              "content": f"Act as my mentor in {goal}. Help me clarify my goals, identify my strengths and weaknesses, create a personal development plan, and offer advice based on real-world experience. Ask reflective questions to challenge my thinking and guide me to make informed decisions. Also give long-term career growth and track specific technical mentorship, periodic(sessions/check-ins/project reviews); guide project quality, career goals, learning path, professional dev; expert-level, persona-based, professional yet supportive mentorship; review projects - give portfolio advice, monitor progress, provide job market insight, recommend specializations; engaged when the student requests mentorship or reaches key milestones."
            }
          ],
          "web_access": False
        }
        headers = {
          "x-rapidapi-key": "a67d2a453emsh4d691d4dacd48efp13df79jsned94b02796f0",
          "x-rapidapi-host": "open-ai21.p.rapidapi.com",
          "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        resp = dict(response.json())

        st.write(resp['result'])
