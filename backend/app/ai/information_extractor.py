import json 
import re

with open("tunisian_dic.json", "r", encoding ="utf-8" ) as f:
    KEYWORDS= json.load(f)

def extract_category(text: str)-> str:
   for category, keyword in KEYWORDS["category"].items():
      for keyword in keywords:
         if keyword in text:
           return category 
   return "nolabel"        

def extract_priority(text: str)-> str:  
    for priority, keyword in KEYWORDS["priority"]["high"]:
        if keyword in text: 
            return "high"

def extract_priority(text: str)-> str:  
    for priority, keyword in KEYWORDS["priority"]["mediun"]:
        if keyword in text:
            return "medium"
        
    return"low"

def extract_location(text: str) -> str:
    words = text.split()
    for i, word in enumerate(words):
        if word in KEYWORDS["location_indicators"]:
            location_words = words[i:i+4]
            return " ".join(location_words)
            
    return "nolabel"
    
def extract_infomation_extractor(text: str) -> dict:
  category      = extract_category(text)   
  priority      = extract_priority(text)   
  location      = extract_location(text)  

  result = {
        "category":      category,
        "priority":      priority,
        "location":      location,
    }
 
  return "result"

        
        
