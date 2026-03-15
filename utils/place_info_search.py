import os 
import json
from langchain_tavily import TavilySearch
from langchain_google_community import GooglePlacesTool, GooglePlacesAPIWrapper

class GooglePlaceSearchTool:
    def __init__(self, api_key:str):
        self.places_wrapper = GooglePlacesAPIWrapper(gplaces_api_key = api_key)
        self.places_tool = GooglePlacesTool(api_wrapper=self.places_wrapper)

    def google_search_attractions(self, place:str) -> dict:
        """
        Searches for attractions in the specified place using Google Places API.
        """
        return self.places_tool.run(f"Top attractive places in and around {place}")

    def google_search_restaurants(self, place:str) -> dict:
        """
        Searches for restaurants in the specified place using Google Places API.
        """
        return self.places_tool.run(f"Top 10 restaurants and eateries in and around {place}")
    
    def google_search_activity(self, place:str) -> dict:
        """
        Searches for activities in the specified place using Google Places API.
        """
        return self.places_tool.run(f"Top activities in and around {place}")

    def google_search_transportation(self, place:str) -> dict:
        """
        Searches for transportation options in the specified place using Google Places API.
        """
        return self.places_tool.run(f"What are different modes of transportation options in and around {place}")

class TavilyPlaceSearchTool:
    def __init__(self, api_key:str):
        pass

    def tavily_search_attractions(self, place:str) -> dict:
        """
        Searches for attractions in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic='general', include_answer='advanced')
        result = tavily_tool.invoke({"query": f"Top attractive places in and around {place}"})
        if isinstance(result, dict) and result.get('answer'):
            return result['answer']
        return result

    def tavily_search_restaurants(self, place:str) -> dict:
        """
        Searches for restaurants in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic='general', include_answer='advanced')
        result = tavily_tool.invoke({"query": f"Top 10 restaurants and eateries in and around {place}"})
        if isinstance(result, dict) and result.get('answer'):
            return result['answer']
        return result
    
    def tavily_search_activity(self, place:str) -> dict:
        """
        Searches for activities in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic='general', include_answer='advanced')
        result = tavily_tool.invoke({"query": f"Top activities in and around {place}"})
        if isinstance(result, dict) and result.get('answer'):
            return result['answer']
        return result

    def tavily_search_transportation(self, place:str) -> dict:
        """
        Searches for transportation options in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic='general', include_answer='advanced')
        result = tavily_tool.invoke({"query": f"What are different modes of transportation options in and around {place}"})
        if isinstance(result, dict) and result.get('answer'):
            return result['answer']
        return result
