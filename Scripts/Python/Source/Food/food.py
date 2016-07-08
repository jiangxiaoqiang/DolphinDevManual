#coding=utf-8
# help  
# python json_format.py json_text  
import os  
import sys  
import json  
  
length = len(sys.argv)  
  
print ("==================================")  
if length > 1:    
    jsonstr = sys.argv[1]  
    jsonObj = json.loads(jsonstr)      
    formatJsonStr = json.dumps(jsonObj,indent=4,ensure_ascii=False,sort_keys=True)  
  
    print (formatJsonStr)  
    
else :  
    print ("argv's length is 1, no json text input.")  
print ("==================================") 