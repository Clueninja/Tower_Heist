#ROOMS
#A room is simply a 2D list containing rows with tile strings in them, tile string all have corresponding directories which can be used to load their textures

room_1 = [
["ctl1","wh1","wh1","wh1","wh1","wh1","wh1","c1","wh1","wh1","wh1","wh1","wh1","wh1","c1","wh1","wh1","wh1","wh1","wh1","wh1","c1","wh1","wh1","wh1","wh1","wh1","wh1","c1","wh1","wh1","wh1","wh1","wh1","wh1","ctr1",""],
["wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""],
["wv1","f1","f1","f3","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f2","f1","f1","f1","wv1",""],
["wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""],
["wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f2","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""],
["wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f3","f1","f1","f1","f1","wv1",""],
["wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""],
["wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""],
["wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""],
["ctl1","wh1","wh1","f1","f1","wh1","wh1","wh1","wh1","wh1","f1","f1","wh1","wh1","wh1","wh1","wh1","f1","f1","wh1","wh1","wh1","wh1","wh1","f1","f1","wh1","wh1","wh1","wh1","wh1","f1","f1","wh1","wh1","ctr1",""],
["wv1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","cbl1", "ctr1"],
["wv1","f1","f1","f1","f1","f2","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","","wv1"],
["wv1","f1","f1","f1","f1","f1","f1","f1","f1","f2","f1","f1","f1","f1","f1","f1","f3","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","ex1","wv1"],
["wv1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f3","f1","f1","f1","ctl1", "cbr1"],
["ctl1","wh1","wh1","f1","f1","wh1","wh1","c1","wh1","wh1","f1","f1","wh1","wh1","c1","wh1","wh1","f1","f1","wh1","wh1","c1","wh1","wh1","f1","f1","wh1","wh1","c1","wh1","wh1","f1","f1","wh1","wh1","ctr1",""],
["wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""],
["wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""],
["wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f2","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""], 
["wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f2","f1","f1","wv1","f1","f1","f3","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""],
["wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f2","f1","f1","f1","wv1",""],
["wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f3","f1","f1","wv1",""],
["wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f2","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""],
["wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""],
["cbl1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","cbr1",""]]

room_2 = [
["","ctl1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","c1","wh1","wh1","wh1","wh1","wh1","wh1","c1","wh1","wh1","wh1","wh1","wh1","wh1","c1","wh1","wh1","wh1","wh1","wh1","wh1","ctr1",""],
["","wv1","f3","f2","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""],
["","wv1","f3","f2","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""],
["","wv1","f3","f2","f1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","wv1",""],
["","wv1","f2","f1","f1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","wv1",""],
["","ctl1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","c1","wh1","wh1","wh1","f1","f1","wh1","c1","wh1","wh1","wh1","wh1","wh1","wh1","c1","wh1","wh1","f1","f1","wh1","wh1","ctr1",""],
["","wv1","f1","f1","f1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""],
["","wv1","f1","f2","f3","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f2","f1","f1","f1","wv1",""],
["","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","wv1",""],
["","wv1","f2","f1","f1","f1","f1","f1","wv1","f1","f2","wv1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""],
["","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f3","f1","f1","f1","f1","wv1",""],
["","wv1","f1","f1","wh1","wh1","wh1","wh1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""],
["","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""],
["","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""],
["","ctl1","wh1","wh1","f1","f1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","f1","f1","wh1","wh1","wh1","wh1","wh1","f1","f1","wh1","wh1","wh1","wh1","wh1","f1","f1","wh1","wh1","ctr1",""],
["ctl1","cbr1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","cbl1", "ctr1"],
["wv1","","f1","f1","f1","f1","f2","f1","f1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","","wv1"],
["wv1","en1","f1","f1","f1","f1","f1","f1","f1","f1","f2","f1","f1","f1","f1","wv1","f1","f3","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","ex1","wv1"],
["cbl1","ctr1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f3","f1","f1","f1","ctl1", "cbr1"],
["","ctl1","wh1","wh1","f1","f1","wh1","wh1","c1","wh1","wh1","f1","f1","wh1","wh1","c1","wh1","wh1","f1","f1","wh1","wh1","c1","wh1","wh1","f1","f1","wh1","wh1","c1","wh1","wh1","f1","f1","wh1","wh1","ctr1",""],
["","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""],
["","wv1","f1","f1","f2","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""],
["","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f2","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""], 
["","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f2","f1","f1","wv1","f1","f1","f3","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""],
["","wv1","f1","f1","f3","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f2","f1","f1","f1","wv1",""],
["","wv1","f2","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f3","f1","f1","wv1",""],
["","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f2","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""],
["","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""],
["","cbl1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","cbr1",""]]

room_3 = [
["","ctl1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","c1","wh1","wh1","wh1","wh1","wh1","wh1","ctr1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","","wv1"],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","ex1","wv1"],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1","","ctr1"],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1","","cbr1"],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","cbl1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","cbr1",""]]

room_4 = [
["","ctl1","wh1","wh1","wh1","c1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","c1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","c1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","c1","wh1","wh1","wh1","wh1","wh1","wh1","ctr1",""],
["","wv1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""],
["","wv1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","wv1",""],
["","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","wv1",""],
["","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","wv1",""],
["","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","","wv1"],
["","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","ex1","wv1"],
["","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","wv1",""],
["","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","wv1",""],
["","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","ctr1",""],
["ctl1","cbr1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","cbl1", "ctr1"],
["wv1","","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","","wv1"],
["wv1","en1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","ex1","wv1"],
["cbl1","ctr1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","ctl1", "cbr1"],
["","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","ctr1",""],
["","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","wv1",""],
["","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","wv1",""],
["","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","wv1",""], 
["","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","wv1",""],
["","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","wv1",""],
["","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","f1","wv1","f1","f1","wv1",""],
["","wv1","f1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","wv1",""],
["","wv1","f1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","f1","f1","f1","f1","f1","wv1","f1","f1","wv1",""],
["","cbl1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","cbr1",""]]

room_5 = [
["ctl1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","c1","wh1","wh1","wh1","wh1","wh1","wh1","ctr1",""],
["wv1","en1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["wv1","en1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","cbl1","ctl1"],
["cbl1","ctr1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","","wv1"],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","ex1","wv1"],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","wh1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wh1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","ctl1","cbr1"],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","wh1","f5","f5","f5","f5","f5","f5","f5","f5","f5","wh1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wh1","f5","f5","f5","f5","f5","wh1","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","wv1","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","f5","wv1",""],
["","cbl1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","cbr1",""]]

room_6 = [
["","","","","","","","","","","wh1","","","","","","wh1","","","","","","wh1","","","","","","wh1","","","","","","wh1","","",""],
["","ctl1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","f1","wh1","wh1","wh1","wh1","wh1","f1","wh1","wh1","wh1","wh1","wh1","f1","wh1","wh1","wh1","wh1","wh1","f1","wh1","wh1","wh1","wh1","wh1","f1","wh1","ctr1",""],
["ctl1","cbr1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","cbl1", "ctr1"],
["wv1","","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","","wv1"],
["wv1","en1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","ex1","wv1"],
["cbl1","ctr1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","ctl1", "cbr1"],
["","cbl1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","f1","wh1","wh1","wh1","wh1","wh1","f1","wh1","wh1","wh1","wh1","wh1","f1","wh1","wh1","wh1","wh1","wh1","f1","wh1","wh1","wh1","wh1","wh1","f1","wh1","cbr1",""],
["","","","","","","","","","","wh1","","","","","","wh1","","","","","","wh1","","","","","","wh1","","","","","","wh1","","",""]]

room_7 = [
["","ctl1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","ctr1",""],
["","wv1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","wv1",""],
["","wv1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","wv1",""],
["","wv1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","wv1",""],
["","wv1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","wv1",""],
["","wv1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","wv1",""],
["ctl1","cbr1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","cbl1", "ctr1"],
["wv1","","f1","f1","f1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","f1","f1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","f1","f1","f1","f1","","wv1"],
["wv1","en1","f1","f1","f1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","f1","f1","f1","f1","ex1","wv1"],
["cbl1","ctr1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","ctl1", "cbr1"],
["","wv1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","wv1",""],
["","wv1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","wv1",""],
["","wv1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","wv1",""],
["","wv1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","wv1",""], 
["","wv1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","f1","wv1",""],
["","cbl1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","wh1","cbr1",""]]

