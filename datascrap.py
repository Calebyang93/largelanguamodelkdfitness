from firecrawl import Firecrawl 
from pydantic import BaseModel 

firecrawl = Firecrawl(api_key="fc-e9e5af0759ad4ba4be2008d7ed09b07d") # type: ignore
# Scrape a website:
doc = firecrawl.scrape("https://firecrawl.dev", formats=["markdown", "html"]) # type: ignore
print(doc) # type: ignore
docs = firecrawl.crawl(url="https://docs.firecrawl.dev", limit=10) # type: ignore
print(docs) # type: ignore
status = firecrawl.get_crawl_status("<crawl-id>") # type: ignore
print(status) # type: ignore

app = Firecrawl(api_key="") # type: ignore

class RacquetInfo(BaseModel):
    brand_name: str
    sport_name: str
    material_name: str 
    racquet_price: float

racquetresult = app.scrape(
    'https://firecrawl.dev',
    formats = [{
        "type": "json",
        "schema": RacquetInfo.model_json_schema()               
    }],
    only_main_content= False,
    timeout=120000
)
print(racquetresult)

class SportsWearInfo(BaseModel):
    brand_name: str
    gender_name: str
    sportswear_price: float 
    size_name: str

sportswearresult = app.scrape(
    'https://firecrawl.dev',
    formats = [{
        "type": "json",
        "schema": SportsWearInfo.model_json_schema()
    }],
    only_main_content=False,
    timeout=120000
)
print(sportswearresult)
    
class SupplementInfo(BaseModel):
    brand_name: str
    ingredient_name: str
    label_skucode: str
    product_price: float 

supplementresult = app.scrape(
    'https://firecrawl.dev',
    formats = [{
        "type": "json",
        "schema": SupplementInfo.model_json_schema()     
    }],
    only_main_content=False,
    timeout=120000    
)
print(supplementresult)

class dietplanInfo(BaseModel):
    diet_name = str
    dietpack_ingredients = str 
    

class CompanyInfo(BaseModel):
    company_mission: str
    supports_sso: bool
    is_open_source: bool
    is_in_yc: bool

result = app.scrape( # type: ignore
    'https://firecrawl.dev',
    formats=[{
      "type": "json",
      "schema": CompanyInfo.model_json_schema()
    }],
    only_main_content=False,
    timeout=120000
)
print(result) # type: ignore

results = firecrawl.search( # type: ignore
    query="firecrawl",
    limit=3,
)
print(results) # type: ignore
