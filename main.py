import gradio as gr
import google.generativeai as genai
import json

genai.configure(api_key="AIzaSyDPXUpQ-q68wFXESYaR6EOIWREs9N2TqNY")

with open("core.json", "r") as f:
    knowledge_data = json.load(f)

def main(user_input):
    prompt = f"You are the digital avatar of Muhammad Hassan, an AI Engineer \n Instructions: Keep your tone decent and elegant. Use emojis on every output based on tone. Do not say anything from yourself. Extract information logically. IMP: Confess that you don't know the relevant infrormation if you don't know \n Based on the information {knowledge_data}, answer the question:\n User: {user_input}\n AI:"
    response = genai.GenerativeModel("gemini-pro").generate_content(prompt)
    return response.text if response else "I couldn't find a relevant answer."

interface = gr.Interface(
    fn=main,
    inputs=gr.Textbox(label="Ask me a question"),
    outputs=gr.Textbox(label="Answer"),
    title="Talk to Me"
)

interface.launch()
