portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
 
def permutations(route, ports):

    if len(ports) == 0:
      print(' '.join([portnames[j] for j in route]))
      return
      
    for i in range(len(ports)): 
       m = route.copy()
       m.append(ports[i])
       remLst = ports[:i] + ports[i+1:]
       permutations(m,remLst)
    
    return 

permutations([0], list(range(1, len(portnames))))
