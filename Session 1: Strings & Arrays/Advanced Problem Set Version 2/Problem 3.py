def shuffle(message, indices):
    res=""
    for i in indices:
        res+=message[i]
    print(res)
	    
	    
message = "evil"
indices = [3, 1, 2, 0]
shuffle(message, indices)

message = "findme"
indices = [0, 1, 2, 3, 4, 5]
shuffle(message, indices)
