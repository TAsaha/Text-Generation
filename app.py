import streamlit as st
from transformers import pipeline

def load_model():
  generator = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")
  return generator
st.image("feenix-lab-logo_use-on-black.png")
st.title("Text Generation")

prompt = st.text_input("Enter a prompt to start:")
temperature = st.slider("Temperature (Controls Randomness)", min_value=0.0, max_value=1.0, step=0.1, value=0.7)
max_length = st.number_input("Max Length of Generated Text", min_value=10, max_value=200, step=10, value=30)

if st.button("Generate Text"):
  # Load the model if not cached
  generator = load_model()
  
  # Generate text using the prompt, temperature, and max_length
  generated_text = generator(prompt, max_length=max_length, temperature=temperature)[0]["generated_text"]
  st.write("Generated Text:")
  st.write(generated_text)
