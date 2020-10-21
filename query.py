import json

inp_str = input()

operators={"||":"or", "&&":"and"}

'''Function to Check if Syntax is Valid
Used stack logic to match brackets'''
def check_syntax_validity(inp_str):
    s = []
    i=0
    flag = True
    while (i < len(inp_str) and flag == True):
        if inp_str[i] == '(':
            s.append(inp_str[i])
        elif inp_str[i] == ')':
            if len(s) == 0:
                flag = False
            else:
                s.pop()
        i+=1

    if (flag == True and len(s)==0):
        return(True)
    else:
        return(False)

'''Function to find the root operator'''
def find_main_op(val):
    for i in range(len(val)):
        if (val[i] == "|" and val[i+1] == "|" and val[i-1] == ")" and val[i+2]=="("):
            return "||"
            break;
        elif (val[i] == "&" and val[i+1] == "&" and val[i-1] == ")" and val[i+2]=="("):
            return "&&"
            break;
    return None

'''Appending the Dictionary'''
def main_op_ad(val):
    operator = find_main_op(val)
    temp = val.split(operator)
    out_str["query"][operators[operator]]=[]
    return temp, operator


'''Operation at leaf level'''
def leaf_op(temp , prev_op):
    for i in range(0, len(temp)):
        temp[i] = temp[i].replace("(","")
        temp[i] = temp[i].replace(")","")
        if ("&&" in temp[i]):
            out_str["query"][operators[prev_op]].append( {"and" : {x.split('=')[0]:int(x.split('=')[1]) for x in temp[i].split("&&")}})
        elif ("||" in temp[i]):
            out_str["query"][operators[prev_op]].append({"or":{x.split('=')[0]:int(x.split('=')[1]) for x in temp[i].split("||")}})
    return temp



if (check_syntax_validity(inp_str)==False):
    print("Syntax Invalid")

else:
    out_str = {"query": {}}
    inp_str = inp_str.replace(" ","") #Removing all whitespaces
    inp_str , prev_op = main_op_ad(inp_str)
    inp_str = leaf_op(inp_str , prev_op)
    print(json.dumps(out_str, indent = 2))
    
