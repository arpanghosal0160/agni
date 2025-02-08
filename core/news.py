import requests
import cohere
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def get_news(category='general'):
    api_key = '913676556ca74622a485f609c48f7f06'  # Replace with your NewsAPI key
    url = f'https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={api_key}'
    
    response = requests.get(url)
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get('articles', [])
        top_news = [{'title': article['title'], 'description': article['description']} for article in articles]
        return top_news
    else:
        print("Failed to fetch news")
        return []

def summarize_text(text, sentences_count=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return " ".join([str(sentence) for sentence in summary])

def categorize_news(query):
    co = cohere.Client('ilAww2FKbcYb0nT7N5FmnosPvHxJtx7MXGw7hFgU')  # Replace with your Cohere API key
    response = co.classify(
        model='large',
        inputs=[query],
        examples=[
            {'text': 'sports news', 'label': 'sports'},
            {'text': 'technology news', 'label': 'technology'},
            {'text': 'business news', 'label': 'business'},
            {'text': 'entertainment news', 'label': 'entertainment'},
            {'text': 'health news', 'label': 'health'},
            {'text': 'science news', 'label': 'science'},
            {'text': 'general news', 'label': 'general'}
        ]
    )
    return response.classifications[0].prediction

# Example usage
if __name__ == "__main__":
    query = "Tell me about the latest technology news"
    category = categorize_news(query)
    news = get_news(category)
    for article in news:
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        summary = summarize_text(article['description'])
        print(f"Summary: {summary}")
        print()
