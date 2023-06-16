import streamlit as st
import openai

# Set OpenAI API key
openai.api_key = "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"
# Interface
st.title("CSM Call Analysis Dashboard")
# Define the input text
input_text = st.text_area("Enter the conversation transcript:", max_chars=60000)


# Define the functions
@st.cache
def content_understanding(transcript: str) -> str:
    conversation = [
        {
            "role": "system",
            "content": "You are a highly advanced AI with capabilities in understanding and summarizing the main themes discussed during a conversation. Your objective is to identify key topics, issues, and areas of interest mentioned in the dialogue.",
        },
        {"role": "user", "content": transcript},
        {"role": "user", "content": "Analyze the conversation and output a list or categorization of the main themes discussed."},
    ]
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=conversation,
    )
    return chat_completion.choices[0].message.content

@st.cache
def response_recommendation(transcript: str) -> str:
    conversation = [
        {
            "role": "system",
            "content": "You are an intelligent AI that can provide suggested responses or actions for a customer service manager based on the content of a call.",
        },
        {"role": "user", "content": transcript},
        {"role": "user", "content": "Based on the conversation, provide suggested responses or actions."},
    ]
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=conversation,
    )
    return chat_completion.choices[0].message.content

@st.cache
def urgency_detection(transcript: str) -> str:
    conversation = [
        {
            "role": "system",
            "content": "You are a sophisticated AI that can analyze the content of a conversation and generate a score or flag indicating the urgency of the issues discussed.",
        },
        {"role": "user", "content": transcript},
        {"role": "user", "content": "Analyze the conversation and indicate the urgency of the issues discussed."},
    ]
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=conversation,
    )
    return chat_completion.choices[0].message.content

@st.cache
def keyword_analysis(transcript: str) -> str:
    conversation = [
        {
            "role": "system",
            "content": "You are an AI that can perform keyword analysis on a conversation, outputting a list or visualization of the most frequently mentioned keywords and specific product or feature mentions.",
        },
        {"role": "user", "content": transcript},
        {"role": "user", "content": "Perform keyword analysis on the conversation."},
    ]
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=conversation,
    )
    return chat_completion.choices[0].message.content

@st.cache
def sentiment_and_satisfaction_analysis(transcript: str) -> str:
    conversation = [
        {
            "role": "system",
            "content": "You are an AI that can perform sentiment and satisfaction analysis on a conversation. You can provide a sentiment score for the call and predict the customer's likely Net Promoter Score (NPS).",
        },
        {"role": "user", "content": transcript},
        {"role": "user", "content": "Perform sentiment and satisfaction analysis on the conversation."},
    ]
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=conversation,
    )
    return chat_completion.choices[0].message.content

@st.cache
def competitor_mention_analysis(transcript: str) -> str:
    conversation = [
        {
            "role": "system",
            "content": "You are an AI that can analyze a conversation for mentions of competitors. You can generate a list of any competitor names mentioned during the call and provide some analysis around the context in which they were mentioned.",
        },
        {"role": "user", "content": transcript},
        {"role": "user", "content": "Analyze the conversation for mentions of competitors."},
    ]
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=conversation,
    )
    return chat_completion.choices[0].message.content

@st.cache
def sales_opportunity_detection(transcript: str) -> str:
    conversation = [
        {
            "role": "system",
            "content": "You are an AI that can detect sales opportunities in a conversation. You can identify potential upsell or cross-sell opportunities mentioned during the conversation.",
        },
        {"role": "user", "content": transcript},
        {"role": "user", "content": "Identify sales opportunities in the conversation."},
    ]
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=conversation,
    )
    return chat_completion.choices[0].message.content

@st.cache
def call_duration_analysis(transcript: str) -> str:
    conversation = [
        {
            "role": "system",
            "content": "You are an AI that can analyze the duration of a conversation. You can output an analysis of the call's duration in relation to its content and the customer's sentiment.",
        },
        {"role": "user", "content": transcript},
        {"role": "user", "content": "Analyze the duration of the conversation."},
    ]
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=conversation,
    )
    return chat_completion.choices[0].message.content

@st.cache
def action_item_extraction(transcript: str) -> str:
    conversation = [
        {
            "role": "system",
            "content": "You are an AI that can extract action items from a conversation. You can create a list of actionable tasks or follow-ups mentioned during the call, along with the responsible party (if mentioned).",
        },
        {"role": "user", "content": transcript},
        {"role": "user", "content": "Extract action items from the conversation."},
    ]
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=conversation,
    )
    return chat_completion.choices[0].message.content

@st.cache
def call_summary_generation(transcript: str) -> str:
    conversation = [
        {
            "role": "system",
            "content": "You are an AI that can generate a summary of a conversation. You can output a concise, easy-to-read summary of the call, highlighting key points, action items, sentiment, and any other significant insights.",
        },
        {"role": "user", "content": transcript},
        {"role": "user", "content": "Generate a summary of the conversation."},
    ]
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=conversation,
    )
    return chat_completion.choices[0].message.content



# Create the buttons

t1, t2, t3 = st.columns(3)

if t1.button("Content Understanding"):
    st.write("Content Understanding:\n\n")
    st.markdown(content_understanding(input_text))

if t2.button("Response Recommendation"):
    st.write("Response Recommendation:\n\n")
    st.markdown(response_recommendation(input_text))

if t3.button("Urgency Detection"):
    st.write("Urgency Detection:\n\n")
    st.markdown(urgency_detection(input_text))

t4, t5, t6 = st.columns(3)

if t4.button("Keyword Analysis"):
    st.write("Keyword Analysis:\n\n")
    st.markdown(keyword_analysis(input_text))

if t5.button("Sentiment and Satisfaction Analysis"):
    st.write("Sentiment and Satisfaction Analysis:\n\n")
    st.markdown(sentiment_and_satisfaction_analysis(input_text))

if t6.button("Competitor Mention Analysis"):
    st.write("Competitor Mention Analysis:\n\n")
    st.markdown(competitor_mention_analysis(input_text))

t7, t8, t9 = st.columns(3)

if t7.button("Sales Opportunity Detection"):
    st.write("Sales Opportunity Detection:\n\n")
    st.markdown(sales_opportunity_detection(input_text))

if t8.button("Call Duration Analysis"):
    st.write("Call Duration Analysis:\n\n")
    st.markdown(call_duration_analysis(input_text))

if t9.button("Action Item Extraction"):
    st.write("Action Item Extraction:\n\n")
    st.markdown(action_item_extraction(input_text))

t10, t11, _ = st.columns(3)

if t10.button("Call Summary Generation"):
    st.write("Call Summary Generation:\n\n")
    st.markdown(call_summary_generation(input_text))

