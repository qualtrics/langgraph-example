from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool
import requests

url = 'https://pdx1.qualtrics.com/inbound-event/v1/events/json/triggers?urlTokenId=603bfb63-acb9-4cd4-9448-8b93a4475c62'

@tool
def postSlackMessage(query: str):
    """Send a POST request with the given query to the specified Slack URL and return the response text."""
    response = requests.post(url, data=query)
    return response.text

tools = [TavilySearchResults(max_results=1), postSlackMessage]
