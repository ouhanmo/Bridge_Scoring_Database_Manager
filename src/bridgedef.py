suit_dict = {
"S" : "Spade" ,
"H" : "Heart" ,
"D" : "Diamond" ,
"C" : "Club" ,
"N" : "NoTrump",
"s" : "Spade" ,
"h" : "Heart" ,
"d" : "Diamond" ,
"c" : "Club" ,
"n" : "NoTrump",
}
pos_dict = {
"N" : "North",
"E" : "East",
"S" : "South",
"W" : "West",
"n" : "North",
"e" : "East",
"s" : "South",
"w" : "West",
}
position = ("North","East","South","West")
vul = ("NONE","N-S","E-W","BOTH")
penalty = ("NONE","Double","ReDouble")
def getVul (gameNum) :
    idx = (gameNum-1)%4+(gameNum-1)/4
    return vul[idx%4]
