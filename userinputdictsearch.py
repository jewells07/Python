#Dictionary search
statesAndCapitals = { 
                     'Gujarat' : 'Gandhinagar', 
                     'Maharashtra' : 'Mumbai', 
                     'Rajasthan' : 'Jaipur', 
                     'Bihar' : 'Patna'
                    } 
                      
val=input(" Enter the value ")
  
# Iterating over keys 
for state in statesAndCapitals: 
    if val==state:
        print(statesAndCapitals[val]) 
   
       
        
    
        
