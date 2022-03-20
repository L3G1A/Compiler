from scanner import *

tokens = ['library', 'program',  'id', ';',  'var',  ',',   ':',  'currency',   'int', 'sci', #0-9
         'real', 'string',    'start' , ':=', 'integer', 'while',  'fixed' ,'begin', 'return', 'while', #10-19
         'stop', '::', 'device_open', 'file', 'for', '(', ')', 'abs', 'fabs', 'read_from_device', #20-29
         'var', '+', '-', '/', '*', 'write_to_device', 'device_open', 'device_close', '=',  '<',  #30-39
         '>=', '>', '==', '!=','<=','to','do', 'end', 'repeat','until' #40-49
         ,'if','else', 'then', 'writeln', 'readln' ]#50
parse_table = [
                [100,100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,100,100,100,100,100],
                [-2,-5, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,100,100,100,100,100],
                [-3,100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,100,100,100,100,100],
                [1,-1, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,100,100,100,100,100],
                [-1,-1, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,100,100,100,100,100],
                [100,20, -6, 100, -6, 100, 100, 100, 100, 100, 100, 100, -12, 100, 100, 100, 100, 100, 100, 100, 45, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,100,100,100,100,100],
                [100,100, -7, 11, 3, 100, 5, -11, -11, -11, -11, -11, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,100,100,100,100,100],
                [100,100, -8, 11, 100, 100, -6, 100, 100, 100, 100, 100, -5, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,100,100,100,100,100],
                [100,100, -9, 100, 100, 100, -6, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,100,100,100,100,100],
                [100,100, -10, 100, 100, 4, 21, -6, -6, -6, -6, -6, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,100,100,100,100,100],
                [100,100, 2, 100, 100, -9, -6, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,100,100,100,100,100],
                [100,100, 100, -7, 100, 100, 100, 6, 7, 8, 9, 10, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,100,100,100,100,100],
                [100,100, -13, 46, 100, 100, 100, 100, 100, 100, 100, 100, 12, 100, 100, -13, 100, 100, 44, 100, -5, 100, -13, 100, 100, 100, 100, 100, 100, -13, 100, 100, 100, 100, 100, -13, 100, -13, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, -13, 100,-13,100,100,-13,-13],
                [100,100, -15, 100, 100, 100, 100, 100, 100, 100, 100, -15, 100, 100, 100, -15, 100, 100, 100, 100, 100, 100, -15, 100, 100, 100, 100, 100, 100, -15, 100, 100, 100, 100, 100, -15, 100, -15, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, -15, 100,-15,100,100,-15,-15],
                [100,100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,100,100,100,100,100],
                [100,100, 13, 46, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 36, 100, 100, 100, 100, 100, 100, 26, 100, 27, 100, 100, 100, 100, 39, 100, 100, 100, 100, 100, 40, 100, 38, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 28, 100,37,100,100,41,42],
                [100,100,  29, 100, 100, 100, 100, 29,  29,  29,  29,  29,  100, 100, 29, 100, 29, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,100,100,100,100,100],
                [100,100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 30, 31, 32, 33, 34, 35, 100, 100, 100, 100, 100,100,100,100,100,100],
                [100,100, -20, 100, 100, 100, 100, -20, -20, -20, -20, -20, 100, 100, -20, 100, -20, 100, 100, 100, 100, 100, 100, 100, 100, -20, 100, -20, -20, 100, 100, -19, -19, -20, -20, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,100,100,100,100,100],
                [100,100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 22, 23, -21, -21, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,100,100,100,100,100],
                [100,100, -22, 100, 100, 100, 100, -22, -22, -22, -22, -22, 100, 100, -22, 100, -22, 100, 100, 100, 100, 100, 100, 100, 100, -22, 100, -22, -22, 100, 100, 100, 24, 25, -21, -21, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,100,100,100,100,100],
                [100,100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 24, 25, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,100,100,100,100,100],
                [100,100, 15, 14, 100, 100, 100, 6, 7, 8, 9, 10, 100, 100, 16, 100, 43, 100, 100, 100, 100, 100, 100, 100, 100, 18, 100, 17, 19, 100, 100, -18, -18, -18, -18, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,100,100,100,100,100],
                [100,100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,100,100,100,100,100]
              ]

lookahead_dict = {
                    1:[0],
                    2:[2],
                    3:[4,-5],
                    4:[5,2],
                    5:[6],
                    6:[7],
                    7:[8],
                    8:[9],
                    9:[10],
                    10:[11],
                    11:[3],
                    12:[12, -12],
                    13:[2,13,-18],
                    14:[3,-12],
                    15:[2],
                    16:[14],
                    17:[27,25,-18,26],
                    18:[25,-18,26],
                    19:[28,25,-18,26],
                    20:[1,2,3],
                    21:[6],
                    22:[31,-20],
                    23:[32,-20],
                    24:[33,-22],
                    25:[34,-22],
                    26:[22,23,3],
                    27:[24,2,21,2,45,2,46,-12,47,46],
                    28:[48,46,-12,49,25,-16,26,47,46],
                    29:[-18,-17,-18],
                    30:[39],
                    31:[40],
                    32:[41],
                    33:[42],
                    34:[43],
                    35:[44],
                    36:[15,25,-16,26,46,-12,47,46],
                    37:[50,25,-16,26,52,17,-12,47,3,51,17,-12, 47,3],
                    38:[37,23,3,-12],
                    39:[29,23,3,-12],
                    40:[35,23,3,-12],
                    41:[53,25,-18,26],
                    42:[54,25,-8,26,3,-15],
                    43:[16],
                    44:[18,14,3,-12],
                    45:[20],
                    46:[3]

                }

tokens_found, token_values = scanner.scan("sample.txt")
parsable_tokens = []
i = 0
while i < len(tokens_found):
    if(tokens_found[i] != "comment"):
        if(tokens_found[i] == 'reservedword'):
            parsable_tokens.append(token_values[i])

        elif(tokens_found[i] == 'string'):
            parsable_tokens.append(tokens_found[i])
        elif(token_values[i] == 'currency' ):

            parsable_tokens.append(token_values[i])
        elif(tokens_found[i] == 'currency' ):
            parsable_tokens.append(tokens_found[i])

        elif(tokens_found[i] == 'integer'):
            parsable_tokens.append(tokens_found[i])
        elif(token_values[i] == 'sci'):
            parsable_tokens.append(token_values[i])
        elif(token_values[i] == 'real'):
            parsable_tokens.append(token_values[i])
        elif(tokens_found[i] == 'library'):
            parsable_tokens.append(tokens_found[i])
        elif(tokens_found[i] == 'fixed'):
            parsable_tokens.append(tokens_found[i])
        elif(tokens_found[i] == 'file'):
            parsable_tokens.append(tokens_found[i])
        elif(tokens_found[i] == 'id' ):
            parsable_tokens.append(tokens_found[i])
        else:
            parsable_tokens.append(token_values[i])

        
    i+=1

i = 0
tableposition = 1
print(parsable_tokens)
queue = []
queuedTablePosition = 0
while i < len(parsable_tokens):


    token_index = tokens.index(parsable_tokens[i])
    good_move = False
    print(tableposition , " : ", token_index , "(",         parsable_tokens[i] , ") Current Queue: ", queue, "Position: ", queuedTablePosition)
 
    if(len(queue) != 0):
        if(queue[0] == 0):        
            if(parse_table[tableposition][token_index] == 100):
                print("Error")
                break
    if(parse_table[tableposition][token_index] < 0):
        tableposition = abs(parse_table[tableposition][token_index])
 



    else:


        temptableposition = tableposition

        if(len(queue) == 0):
            queue = lookahead_dict[abs(parse_table[tableposition][token_index])].copy()
        else:
            try:
                remove = len(lookahead_dict[abs(parse_table[tableposition][token_index])].copy())
                queue = lookahead_dict[abs(parse_table[tableposition][token_index])].copy() + queue

            except:
                if(queuedTablePosition > 0 and len(queue) > 0):
                    if(queue[0] != 0):
                        tableposition = queuedTablePosition
        try:


            print("Loading Dict: ", lookahead_dict[abs(parse_table[tableposition][token_index])], "with current queue of: ", queue)

            for possible_next in lookahead_dict[abs(parse_table[tableposition][token_index])] :
                temptableposition = tableposition
                print(temptableposition , " : ", token_index , "Current Token: ",         parsable_tokens[i] , "(" , tokens.index(parsable_tokens[i]) ,  ") ", "Move: " , possible_next, "Dict: ", lookahead_dict[abs(parse_table[tableposition][token_index])], " Queue: ", queue, "Position: ", queuedTablePosition)

                while(possible_next < 0):
                    if(parse_table[tableposition][token_index] >= 0):
                        print("Moing Position: ", abs(possible_next))
                        temptableposition = abs(possible_next)
                        break   
                    else:
                        queue.pop(0)
                        temptableposition = abs(parse_table[temptableposition][token_index])

    

                if(tokens.index(parsable_tokens[i]) == possible_next ):
                    print(parsable_tokens[i])
                    good_move = True
                    i += 1
                    queue.pop(0)

                elif( possible_next < 0 and tokens.index(parsable_tokens[i]) != possible_next):
                    print(possible_next)
                    good_move = True

                    queue.pop(0)
                    break
                elif(tokens.index(parsable_tokens[i]) != possible_next):
                    break
        except:
            for possible_next in queue:
                temptableposition = tableposition

                if(queue[0] < 0):
                    print(abs(queue[0]))
                    print(tokens.index(parsable_tokens[i]))
                    print(lookahead_dict[abs(parse_table[abs(queue[0])][tokens.index(parsable_tokens[i])])])
                    if(lookahead_dict[abs(parse_table[abs(queue[0])][tokens.index(parsable_tokens[i])])] != [1, 2, 3]):
                        temptableposition = abs(queue[0] )

                        removal = len(lookahead_dict[abs(parse_table[abs(queue[0])][tokens.index(parsable_tokens[i])])])
                        print("Adding to front of queue", lookahead_dict[abs(parse_table[abs(queue[0])][tokens.index(parsable_tokens[i])])])
                        queue = lookahead_dict[abs(parse_table[abs(queue[0])][tokens.index(parsable_tokens[i])])] + queue
                        print(queue, "remove", removal)
                        queue.pop(removal)
                    else:
                        queue.pop(0)
                        queue.insert(0, tokens.index(parsable_tokens[i]))

                    print(queue)

                print(temptableposition , " : ", tokens.index(parsable_tokens[i]) , "Current Token: ",         parsable_tokens[i] , "(" , tokens.index(parsable_tokens[i]) ,  ") ", "Move: " , possible_next,  "Queue: ", queue, "Position: ", queuedTablePosition)

                if(tokens.index(parsable_tokens[i]) == queue[0] ):
                    print(parsable_tokens[i])
                    good_move = True
                    i += 1
                    queue.pop(0)

                elif( possible_next < 0 and tokens.index(parsable_tokens[i]) != possible_next):
                    queue.pop(0)
                    good_move = True

                    break

    



            
        tableposition = temptableposition
        if(good_move == False):
            print("Parse Error")
            break

        if(len(queue) > 0):
            if(queue[0] != 0): 
                queuedTablePosition = tableposition
