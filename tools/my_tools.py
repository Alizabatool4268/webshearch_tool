import os
from agents import function_tool,RunContextWrapper
from tavily import TavilyClient
from pydantic import BaseModel
from dotenv import load_dotenv



class TavilySearchInput(BaseModel):
    query: str
   
load_dotenv(override=True)    
tavily_key = os.getenv("tvly-YOUR_API_KEY")
tavily_client = TavilyClient(api_key=tavily_key)


@function_tool
async def web_search(ctx: RunContextWrapper, args: TavilySearchInput):
    result = tavily_client.search(args.query)
    return result
