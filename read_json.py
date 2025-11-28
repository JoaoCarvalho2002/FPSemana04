import json

def OpenRecievedFile(filedata):
    if(filedata=="data.json"):
        filedata=open("data.json", "r", encoding="utf-8")
        lines=filedata.read()

        VerifyType(lines)
        
        filedata.close()
        
    else:
        return print("Erro: Ficheiro Não Encontrado!")

def VerifyType(lines):
    try:
        tempval=json.loads(lines)
        
        IsEmpty(lines)
    except json.JSONDecodeError:
        print("Erro: Ficheiro Não Contém JSON Válido!")
        

def IsEmpty(lines):
   
    if lines == "":
        print("Erro: Ficheiro Vazio!")
        
    else:
        AllCamps(lines) 

def AllCamps(lines):
    data=json.loads(lines)
    for k in data.items():
        if(k[1]==""):
            print("Erro: Campos Obrigatórios em Falta!")
            break
        else:
            return print(data)

filedata=input()
OpenRecievedFile(filedata)
print("Processo Concluído!")