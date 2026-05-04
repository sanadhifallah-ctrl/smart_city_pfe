import re

def clean_text(text:str)-> str:
    text=text.lower()
    text= re.sub= (r'\s+' , ' ', text)
    text=re.strip()
    return text

def normalise_text(text:str)-> str:
    text= re.sub= (r'[إأآا]', 'ا', text)
    text= re.sub= (r'ى', 'ي', text)
    text = re.sub (r'[\u0617-\u061A\u064B-\u065F]', '', text)         
    return text

tunisian_dialect_map = {
    'مش':    'ليس',    
    'ماش':   'ليس',     
    'باهي':  'جيد',         
    'برشا':  'كثير',    
    'توا':   'الان',    
    'علاش':  'لماذا',  
    'كيفاش': 'كيف',     
    'شنو':   'ماذا',    
    'منين':  'من اين',  
    'وقتاش': 'متى',     
    'فاما':  'هناك',  
    'زبالة':   'نفايات',       
    'الزبالة': 'النفايات',    
    'الزبل':   'النفايات',     
    'پوبيل':   'حاوية النفايات',  
    'بوبيل':   'حاوية النفايات',  
    'الپوبيل': 'حاوية النفايات',  
    'ينظف':    'يقوم بالتنظيف',   
    'نظفو':    'قاموا بالتنظيف',  
    'نظفت':    'قامت بالتنظيف',  

}    
def standardise_text(text=str)-> str:
  for tunisian_dialect, arabic_word in tunisian_dialect_map.items():
    text= re.sub (r'\b'+ tunisian_dialect + r'\b',  arabic_word , text)
  return text

spell_map=  {
'هاذا':    'هذا',
    'هاذه':    'هذه',
    'هاذي':    'هذه',


}

def correct_spelling(text : str)-> str:
  for wrong_spelling, right_spelling in spell_map.items():
   text = re.sub(r'\b'+ wrong_spelling + r'\b' , right_spelling, text )
  return text

def text_normalizer(text: str) -> str:
 
    text = clean_text(text)      
    text = normalise_text(text)   
    text = standardise_text(text) 
    text = correct_spelling(text) 
 
    return text