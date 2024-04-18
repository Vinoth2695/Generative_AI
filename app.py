import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import LLMChain

## Function to get response from LLAma 2 Model


def get_LLAMA_Response(input_text,no_words,blog_style):

    ## Calling LLAma Model
    llm = CTransformers(model='Models\llama-2-7b-chat.ggmlv3.q4_1.bin',
                        model_type='llama',
                        config={'max_new_tokens':2048,
                                                   'temperature':0.01,
                                                   'context_length':4096})
    
    ## prompt Template

    # template="""
    #             Write a blog for {blog_style} job profile for a topic {input_text} with code within {no_words} words.

    #             """
    # template="""
    #             Generate and write output for {blog_style} on a topic {input_text} with code more than or equal to {no_words} words.
    #             {input_text} for {blog_style} with more than or equal to {no_words} words.

    #             """
    
    template="""
                {input_text} for {blog_style} with more than or equal to {no_words} words.

                """

    prompt = PromptTemplate(input_variables=['blog_style','input_text','no_words'],
                            template=template)
    
    ## Generate the response from the LLAMA Model

    # response = llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    chain = LLMChain(llm=llm,prompt=prompt,verbose=True)
    response = chain.run({'blog_style':blog_style,"input_text":input_text,"no_words":no_words})
    print(response)

    return response
    
    



st.set_page_config(page_title="Generate Blogs",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Lets Check the Power of Generative AI 🤖")

input_text = st.text_input("Enter the Topic here to Search :")


## Creating Two more columns for additional two fields

col1,col2 = st.columns([5,5])

with col1:
    no_words = st.text_input("No of Words:")

with col2:
    blog_style = st.selectbox("Generate the Output for:",
                              ["Automation Engineer",'Manual Tester','Devloper'],index=0)
    
submit_btn = st.button("Generate")


## Final Response

if submit_btn:
    st.write(get_LLAMA_Response(input_text,no_words,blog_style))


