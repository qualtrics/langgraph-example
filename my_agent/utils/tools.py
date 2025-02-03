from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool
import requests

url = 'https://pdx1.qualtrics.com/inbound-event/v1/events/json/triggers?urlTokenId=603bfb63-acb9-4cd4-9448-8b93a4475c62'

@tool
def postSlackMessage(query: str):
  response = requests.post(url, data=query)
  return "success"

tools = [TavilySearchResults(max_results=1), postSlackMessage]
