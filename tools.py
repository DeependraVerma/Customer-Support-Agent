from crewai_tools import SerperDevTool,ScrapeWebsiteTool, WebsiteSearchTool, DirectoryReadTool, FileReadTool
from dotenv import load_dotenv
load_dotenv()
import os

os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

docs_scrape_tool = ScrapeWebsiteTool(
   website_url="https://cloud.google.com/speech-to-text/docs/speech-to-text-requests")

#Website_Search_Tool = WebsiteSearchTool("https://cloud.google.com/speech-to-text/docs/speech-to-text-requests")
# Initialize the tool for internet searching capabilities
#tool = SerperDevTool()