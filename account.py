import streamlit as st
from firebase_admin import credentials, auth

cred = credentials.Certificate('triveni-4bd92-aa17144d65f6.json')

#firebase_admin.initialize_app(cred)



def app():
    st.title('Welcome to :orange[Triveni]')
    
    #print(choice)


    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''    




    def failed():
        try:
            user = auth.get_user_by_email(email)
            #print(user.uid)
            st.write('Login Successful')

            st.session_state.username = user.uid
            st.session_state.useremail = user.email
        except:
            st.warning('Login failed')

    


    if 'signedout' not in st.session_state:
        st.session_state.signedout = False
    if 'signout' not in st.session_state:
        st.session_state.signout = False


    if not st.session_state['signedout']:
        choice = st.selectbox('Login/Signup', ['Login', "Signup"])
        if choice == 'Login':
            email = st.text_input('Employee ID')
            password = st.text_input('Password', type='password')
            st.button('Login', on_click=failed)
        else:
            
            email = st.text_input('Enter your Employee ID')
            password = st.text_input('Password', type='password')
            username = st.text_input('Enter your unique username')

            if st.button('Creat my account'):
                user = auth.create_user(email = email, password = password, uid = username) 
                st.success('Account created Successfully!')
                st.markdown('Please log in using email and password')
                st.balloons()

