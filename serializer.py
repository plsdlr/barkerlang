_type = {0:"XENOTATIONS",
         1:"HYPERGLYPHS"}

def serialize(data,datatype,value):
    new_type = _type[datatype]
    return {"data_string":data,"value":value,"datatype":new_type}
