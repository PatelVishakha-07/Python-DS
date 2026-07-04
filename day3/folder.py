""" H2) You're building a file size calculator like Windows Explorer's "Properties". A folder can contain files OR more folders. Calculate the total size of any folder recursively. """

def calculateSize(idx, s, f):

    for i in range(idx, len(f)):
        if f[i]["type"] == "folder":
            s = calculateSize(0,s, f[i]["files"])
        else: 
            s += f[i]["size"]            
    return s

f = [
    {"filename":"DS.pdf", "size":20, "type":"file"},
    {"filename":"Python", "size":25, "type":"file"},
    {"filename":"CS", "type":"folder", "files":[
        {"filename":"Java", "size":35, "type":"file"},

        {"filename":"CS", "type":"folder", "files":[
            {"filename":"DS.pdf", "size":20, "type":"file"},
            {"filename":"Python", "size":25, "type":"file"},
        ]},

        {"filename":"C", "size":45, "type":"file"}
    ]},
    {"filename":"PHP", "size":15, "type":"file"},
]

print("Total size:",calculateSize(0, 0, f)) 

