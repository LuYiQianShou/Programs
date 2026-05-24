def rev(obj:list|str):
    return obj[::-1]
def rev_ins(obj:list|str,insert,count:int):
    List=obj
    for i in range(count):
        List=List[::-1]
        if isinstance(List,list):
            List.append(insert)
        else:
            if isinstance(insert,str):
                List+=insert
            else:
                List+=str(insert)
    return List
def kaisa(obj:str,shift=1):
    Result=""
    for i in obj:
        Result+=chr(ord(i)+shift)
    return Result
def rev_ins_kaisa(obj:str,insert,count:int,shift=1,enc_insert=True):
    Result=obj
    for i in range(count):
        Result=Result[::-1]
        if enc_insert:
            if isinstance(insert,str):
                Result+=insert
            else:
                Result+=str(insert)
            Result=kaisa(Result,shift)
        else:
            Result=kaisa(Result,shift)
            if isinstance(insert,str):
                Result+=insert
            else:
                Result+=str(insert)
    return Result
def rev_ins_kaisa_pro(
    obj:str,
    insert,
    count:int,
    shift:int=1,
    enc_insert:bool=True,
    add_shift:int=0
):
    Result=obj
    Shift=shift
    for i in range(count):
        Result=Result[::-1]
        if enc_insert:
            if isinstance(insert,str):
                Result+=insert
            else:
                Result+=str(insert)
            Result=kaisa(Result,Shift)
        else:
            Result=kaisa(Result,Shift)
            if isinstance(insert,str):
                Result+=insert
            else:
                Result+=str(insert)
        if add_shift!=0:
            Shift+=add_shift
    return Result
print(rev_ins_kaisa_pro("Hello World","ABC",4,1,True,2))