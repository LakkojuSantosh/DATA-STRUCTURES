#Balanced parenthesis using Stack
s=input("Enter the input : ")
st=[]
balanced=True
for char in s:
    if (char=="{" or char=="[" or char=="("):
        st.append(char)
    elif(char == "}"):
        if(len(st) and st.pop()!="{"):
            balanced=False
            break
    elif(char == "]"):
        if(len(st) and st.pop()!="["):
            balanced=False
            break
    elif(char == ")"):
        if(len(st) and st.pop()!="("):
            balanced=False
            break
    else:
        balanced=False
        break
if(balanced==False or len(st)):
    print("Not Balanced")
else:
    print("Balanced")