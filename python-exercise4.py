def analisis():
    
    veces = int(input())
    lista_precipitacion=[]
    lista_profundidad=[]
    matrix_precipitacion=[]
    matrix_profundidad=[]
    por_zona=[]
    final_zona=[]
    mayorzona=[]
    menorzona=[]
    sumamente=0
    moderadamente=0
    marginalmente=0
    noapto=0
    
    for i in range (0, veces):
        precipitacion = input()
        lista_precipitacion = precipitacion.split()
        matrix_precipitacion.append(lista_precipitacion)
    for i in range (0, veces):
        profundidad = input()
        lista_profundidad = profundidad.split()
        matrix_profundidad.append(lista_profundidad)
    for l, m in zip(matrix_precipitacion,matrix_profundidad):
        for n, o in zip(l,m):
            n=float(n)
            o=float(o)
            if (1799.00 < n <=2599.00) and (o > 100.00):
                sumamente = sumamente + 1
                por_zona.append(1)
            elif (1799.00 < n <=2599.00) and (50.00 < o <= 100.00):
                moderadamente = moderadamente + 1
                por_zona.append(2)                
            elif (1799.00 < n <=2599.00) and (25.00 <= o <= 50.00):
                marginalmente = marginalmente + 1
                por_zona.append(3)
            elif (1799.00 < n <=2599.00) and (o < 25.00):
                noapto = noapto + 1
                por_zona.append(4)
            elif ((2599.00 < n <=3199.00)or(1499.00 < n <=1799.00)) and (o > 50.00):
                moderadamente = moderadamente + 1
                por_zona.append(2)
            elif ((2599.00 < n <=3199.00)or(1499.00 < n <=1799.00)) and (25.00 <= o <= 50.00):
                marginalmente = marginalmente + 1
                por_zona.append(3)
            elif ((2599.00 < n <=3199.00)or(1499.00 < n <=1799.00)) and (o < 25.00):
                noapto = noapto + 1
                por_zona.append(4)
            elif ((3199.00 < n <=3800.00)or(1200.00 <= n <=1499.00)) and (o >= 25.00):
                marginalmente = marginalmente + 1
                por_zona.append(3)
            else:
                noapto = noapto + 1
                por_zona.append(4)
                
    print(str(noapto) + ' ' + str(marginalmente) + ' ' + str(moderadamente) + ' ' + str(sumamente))
    
    for i in range(0, len(por_zona), 7):
        final_zona.append(por_zona[i:i+7])
    for i in final_zona:
        w=float(i.count(1))
        x=float(i.count(2))
        y=float(i.count(3))
        z=float(i.count(4))
        if ((w >= x) and (w >= y) and (w >= z)):
            mayorzona.append('sumamente apto')
        if ((x > w) and (x >= y) and (x >= z)):
            mayorzona.append('moderadamente apto')
        if ((y > w) and (y > x) and (y >= z)):
            mayorzona.append('marginalmente apto')
        if ((z > w) and (z > x) and (z > y)):
            mayorzona.append('no apto')
    
    for i in final_zona:
        w=float(i.count(1))
        x=float(i.count(2))
        y=float(i.count(3))
        z=float(i.count(4))
        if w == 0:
            w = w + 10
        if x == 0:
            x = x + 10
        if y == 0:
            y = y + 10
        if z == 0:
            z = z + 10
        if ((z < w) and (z < x) and (z < y)):
            resumen = 4
        if ((y < w) and (y < x) and (y <= z)):
            resumen = 3
        if ((x < w) and (x <= y) and (x <= z)):
            resumen = 2
        if ((w <= x) and (w <= y) and (w <= z)):
            resumen = 1
        if resumen == 1:
            menorzona.append('sumamente apto')
        if resumen == 2:
            menorzona.append('moderadamente apto')
        if resumen == 3:
            menorzona.append('marginalmente apto')
        if resumen == 4:
            menorzona.append('no apto')
            
    print(','.join(mayorzona))
    print(','.join(menorzona))
            
if __name__ == '__main__':
    analisis()