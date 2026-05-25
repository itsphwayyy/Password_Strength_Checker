# -*- coding: utf-8 -*-
"""
Created on Mon May 25 09:49:15 2026

@author: ACER
"""

import streamlit as st
import string 


st.title("Password Strength Checker")
st.write("Let's see how strong your password is")

pw = st.text_input("Enter your password", type="password")

if st.button("Check my password"):
    
    score = 0
    sc = 0
    character = 0
    digit = 0
    
    
    if any(char.isalpha() for char in pw):
        Len = sum(1 for char in pw if char.isalpha())
        character += Len
        
    if any(d.isdigit() for d in pw):
        num = sum(1 for d in pw if d.isdigit())
        digit += num
        
        
    if any(char in string.punctuation for char in pw):
        l = sum(1 for char in pw if char in string.punctuation)
        sc += l
    

    score += 2 if sc >= 2 else (1 if sc == 1 else 0)
    score += 2 if digit >= 2 else (1 if digit == 1 else 0)
    score += 2 if character >= 2 else (1 if character == 1 else 0)
         
    
    if score == 6:
        
        st.success("Perfect! Your password is really strong!") 
        
    elif score >= 3:
        
        st.warning("You are incredibly close! Just add a bit more and your password will be the strongest!")
        
    else:
        st.error("A Little weak")
        st.write("Don't worry! We can fix this together. Add a little more characters or digits.")
 

    