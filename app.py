import streamlit as st
st.title("Text Summarizer")
options=['Paste the url',"Paste the raw article"]
select=st.radio("Options",options)
if select == "Paste the url":
    import newspaper
    from newspaper import Article
    import nltk
    nltk.download('punkt')
    url =st.text_input('Paste the article link below',"")
    language={"English":"en","Hindi":"hi"}
    selected_lang=st.selectbox("Language of the article", language)
    if st.button("Summarize"):
        my_article = Article(url, selected_lang)
        my_article.download()
        my_article.parse()
        st.header(my_article.title)
        # NLP on the article
        
        my_article.nlp()
        # Extract summary
        st.markdown(my_article.summary)
        # Extract keywords
        st.markdown('Keywords: '+','.join([i for i in (my_article.keywords)]))
else:
    from transformers import PegasusForConditionalGeneration
    from transformers import PegasusTokenizer
    from transformers import pipeline
    model_name = "google/pegasus-xsum"
    pegasus_tokenizer = PegasusTokenizer.from_pretrained(model_name)
    input_text=st.text_area("Input the text to summarize","")
    if st.button("Summarize"):
        st.text("It may take a minute or two.")
        nwords=len(input_text.split(" "))
        summarizer = pipeline("summarization", model=model_name, tokenizer=pegasus_tokenizer,min_length=int(nwords/10)+20, max_length=int(nwords/5+20), framework="pt")
        summary=summarizer(input_text)[0]['summary_text']
        st.header("Summary")
        st.markdown(summary)
