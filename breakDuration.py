from connectorr import updateValue , fetchOutput


def cons_limit(comf):
    counter=fetchOutput("notQvalue","conslimit",1,"comf",False)
    if comf== "yes" and counter <20:
        counter +=1 
        updateValue("notQvalue","conslimit",counter,"comf",1)

        
a=cons_limit("yes")
print(a)

