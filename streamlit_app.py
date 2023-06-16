import streamlit as st
import openai

# Set OpenAI API key
openai.api_key = "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"
# Interface
st.title("CSM Call Analysis Dashboard")
# Define the input text
input_text = st.text_area("Enter the conversation transcript:", max_chars=60000)


# Define the functions
@st.cache(allow_output_mutation=True)
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

@st.cache(allow_output_mutation=True)
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

@st.cache(allow_output_mutation=True)
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

@st.cache(allow_output_mutation=True)
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

@st.cache(allow_output_mutation=True)
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

@st.cache(allow_output_mutation=True)
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

@st.cache(allow_output_mutation=True)
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

@st.cache(allow_output_mutation=True)
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

@st.cache(allow_output_mutation=True)
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

@st.cache(allow_output_mutation=True)
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

if st.button("Analyze"):
    st.header("Analysis Results")
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Content Understanding")
        st.write(content_understanding(transcript))

        st.subheader("Response Recommendation")
        st.write(response_recommendation(transcript))

        st.subheader("Urgency Detection")
        st.write(urgency_detection(transcript))

        st.subheader("Keyword Analysis")
        st.write(keyword_analysis(transcript))

        st.subheader("Sentiment and Satisfaction Analysis")
        st.write(sentiment_and_satisfaction_analysis(transcript))

    with col2:
        st.subheader("Competitor Mention Analysis")
        st.write(competitor_mention_analysis(transcript))

        st.subheader("Sales Opportunity Detection")
        st.write(sales_opportunity_detection(transcript))

        st.subheader("Call Duration Analysis")
        st.write(call_duration_analysis(transcript))

        st.subheader("Action Item Extraction")
        st.write(action_item_extraction(transcript))

        st.subheader("Call Summary Generation")
        st.write(call_summary_generation(transcript))

