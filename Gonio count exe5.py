def count_ex (data, x):
    """
    Desc: return how many exercises have been done by the patient  

    Input: data(list(tuples(int))) -- list of tuples in the form of (time, angle) 
            x(int) -- angle min of an exercise
    Output: nbr_ex(int)

    Example:
    >>> print(nbr_exercices([(1,30),(1,50),(1,40),(1,60),(1,100),(1,99),(1,100),(1,90)]))

    3
    """
    count=0
    ang=creat_li_ang (data)
    prev_amp=0
    i=0  
    while i<len((ang)-1) and abs(prev_amp<=x): #initialisationdu premier angle de plus de x degrés (prev_amp)
        prev_amp=ang[i+1]-ang[i]
        i+=1
    for i in range(len(ang)-1): #compte des mvmts
        count+=1
        amp=ang[i+1]-ang[i]
        if abs(amp) <=x : #mvmt décompté si angle plus petit que x degrés
            count-=1
        elif (amp<=0 and prev_amp<=0)or(amp>0 and prev_amp>0): #mvmt décompté si suite d'une flex/ext interrompue par un faux-mvmt
            count-=1
		else:
			prev_amp=amp
    return count

def creat_li_ang (data):
    """
    Desc: return the list of all the local max or min of the data[i][1]

    Input: data(list(tuples(int))) -- list of tuples in the form of (time, angle) 
    Output: ang(list(int))
    """
    ang=[]
    ang.append(data[0][1])
    if data[0][1]<data[1][1]:
        exercice = "extension"
    else:
        exercice = "flexion"
    for i in range(len(data)-1):
        if exercice== 'extension':
            if data[i+1][1]<data[i][1]:
                ang.append(data[i][1])
                exercice='flexion'                
        if exercice =='flexion':
            if data[i+1][1]> data[i][1]:
                ang.append(data[i][1])
                exercice = 'extension'
    ang.append(data[-1][1]) #ajoute la dernière valeur de la liste pour compter le dernier mvmt
    return (ang)
