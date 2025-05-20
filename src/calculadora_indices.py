def calcular_IMC(peso: float, altura_m: float) -> float:
    """
    Calcula el IMC en base a:
        - peso/(altura_m)**2\n
    *parm peso (float): Peso de la persona en kilogramos.\n
    *parm altura_m (float): Altura de la persona en metros.\n
    Retorno IMC(float) Índice de masa corporal de la persona, type_imc(str) la categoria a la que pertenece segun el IMC calculado\n

    Valor de IMC Categoría:\n
    <16 = Delgadez severa\n 
    16 - 16.99 = Delgadez moderada\n
    17 - 18.49 = Delgadez aceptable\n
    18.5 - 24.99 = Peso normal\n
    25 - 29.99 = Sobrepeso\n
    30 - 34.99 = Obesidad tipo I\n
    35 - 39.99 = Obesidad tipo II\n
    40 - 49.99 = Obesidad tipo III o mórbida\n
    >50 = Obesidad tipo IV o extrema\n
    """
    
    try:
        IMC = round(float(peso/(altura_m)**2),2)
        
        if IMC < 16:
            return IMC,"Delgadez severa"
        elif 16 < IMC < 16.99:
            return IMC,"Delgadez moderada"
        elif 17 < IMC < 18.49:
            return IMC,"Delgadez aceptable"
        elif 18.5 < IMC < 24.99:
            return IMC,"Peso normal"
        elif 25 < IMC < 29.99:
            return IMC,"Sobrepeso"
        elif 30 < IMC < 34.99:
            return IMC,"Obesidad tipo I" 
        elif 35 < IMC < 39.99:
            return IMC,"Obesidad tipo II"
        elif 40 < IMC < 49.99: 
            return IMC,"Obesidad tipo III o mórbida"
        elif IMC > 50: 
            return IMC,"Obesidad tipo IV o extrema"
        else:
            return IMC,"Valores no contemplados"
        
    except ZeroDivisionError as zd:
        return f"Error de divison por cero: {zd}"
    except ValueError as ve:
        return ve
    except TypeError as tp:
        return f"Error de tipado {tp}"
    

def calcular_porcentaje_grasa(peso:float, altura_m:float, edad:int, valor_genero:float, IMC:float=None) -> float:
    """
    %GC: Medida (porcentual) que permite establecer si una persona tiene un nivel adecuado o excesivo de grasa en su cuerpo.\n
        - %GC = 1.2 * IMC + 0.23 * edad(años) - 5.4 - valor_genero
    *parm peso (float): Peso de la persona en kilogramos.\n
    *parm altura_m (float): Altura de la persona en metros.\n
    *parm edad (int): Edad de la persona en años.\n
    *parm valor_genero (float): Valor que varía según el género de la persona: en caso de ser masculino debe ser 10.8 y en caso de ser femenino debe ser 0.\n

    Retorno (float): El porcentaje de grasa que tiene el cuerpo de la persona y un mensaje de lo recomendado.\n
    """
    """
    rango_de_edad: 20 - 29; hombres: 11% - 20%; mujeres: 16% - 28%
    rango_de_edad: 30 - 39; hombres: 12% - 21%; mujeres: 17% - 29%
    rango_de_edad: 40 - 49; hombres: 14% - 23%; mujeres: 18% - 30%
    rango_de_edad: 50 - 59; hombres: 15% - 24%; mujeres: 19% - 31%
    """
    try:
        if IMC is None:
            IMC,_ = calcular_IMC(peso, altura_m)
        
        GC = round(1.2 * IMC + 0.23 * edad - 5.4 - valor_genero,2)

        if valor_genero == 10.8: # Es hombre
            if 20 <= edad <= 29 and 11<= GC <=20:
                return GC, f"El indice de grasa {GC} es lo recomendado para hombres entre 20 y 29 años."
            elif 30 <= edad <= 39 and 12<= GC <=21:
                return GC, f"El indice de grasa {GC} es lo recomendado para hombres entre 30 y 39 años."
            elif 40 <= edad <= 49 and 14<= GC <=23:
                return GC, f"El indice de grasa {GC} es lo recomendado para hombres entre 40 y 49 años."
            elif 50 <= edad <= 59 and 15<= GC <=24:
                return GC, f"El indice de grasa {GC} es lo recomendado para hombres entre 50 y 59 años."
            else:
                return GC,f"Tu indice de grasa corporal ({GC}) esta fuera del rango recomendado"
        if valor_genero == 0: # Es mujer
            if 20 <= edad <= 29 and 16< GC <28:
                return GC, f"El indice de grasa {GC} es lo recomendado para mujeres entre 20 y 29 años."
            elif 30 <= edad <= 39 and 17<= GC <=29:
                return GC, f"El indice de grasa {GC} es lo recomendado para mujeres entre 30 y 39 años."
            elif 40 <= edad <= 49 and 18<= GC <=30:
                return GC, f"El indice de grasa {GC} es lo recomendado para mujeres entre 40 y 49 años."
            elif 50 <= edad <= 59 and 19<= GC <=31:
                return GC, f"El indice de grasa {GC} es lo recomendado para mujeres entre 50 y 59 años."
            else:
                return f"Tu indice de grasa corporal ({GC}) esta fuera del rango recomendado para tu edad"
        # return round(float(GC),2)
    except ValueError as va:
        return va


def calcular_calorias_en_reposo(peso:float, altura_cm:float, edad:int, valor_genero:int)-> float:
    """
    Calcula la cantidad de calorías que una persona quema estando en reposo
        - TMB = (10*peso) + (6.25*altura_cm) - (5*edad) + valor_genero 
    *parm peso (float): Peso de la persona en kilogramos.\n
    *parm altura_cm (float): Altura de la persona en centimetros.\n
    *parm edad (int): Edad de la persona en años.\n
    *parm valor_genero (int): Valor que varía según el género de la persona:
        - En caso de ser masculino: 5
        - En caso de ser femenino: -161\n
    Retornado (float) La cantidad de calorías que la persona quema en reposo.\n
    """
    try:
        TMB = (10*peso) + (6.25*altura_cm) - (5*edad) + valor_genero

        return round(TMB,2)
    except ValueError as va:
        return va
    except TypeError as tp:
        return tp


def calcular_calorias_en_actividad(peso:float, altura_cm:float, edad:int, valor_genero:float, valor_actividad:float, TMB:float=None) -> float:
    """
    Calcula la cantidad de calorías que una persona quema al realizar algún tipo de actividad física:
        - TMB_(actividad_fisica) = TMB * valor_actividad 

    *parm TMB (float): Tasa metabólica basal.\n
    *parm peso (float): Peso de la persona en kilogramos.\n
    *parm altura_cm (float): Altura de la persona en centimetros.\n
    *parm edad (int): Edad de la persona en años.\n
    *parm valor_genero (int): Valor que varía según el género de la persona: en caso de ser masculino debe ser 5 y en caso de ser femenino debe ser -161.\n
    *parm valor_actividad (float): Valor que depende de la actividad física semanal y toma los valores:
        - 1.2: poco o ningún ejercicio 
        - 1.375: ejercicio ligero (1 a 3 días a la semana) 
        - 1.55: ejercicio moderado (3 a 5 días a la semana) 
        - 1.72: deportista (6 -7 días a la semana) 
        - 1.9: atleta (entrenamientos mañana y tarde. 

    Retorno (float): La cantidad de calorías que una persona quema, al realizar algún tipo de actividad física semanalmente. 
    """
    if TMB is None:
        TMB = calcular_calorias_en_reposo(peso,altura_cm,edad,valor_genero)

    TMB_actividad_fisica = TMB * valor_actividad
    return round(TMB_actividad_fisica,2)


def consumo_calorias_recomendado_para_adelgazar(peso: float, altura_cm: float, edad: int, valor_genero: int, TMB:float=None) -> str:
    """
    Calcula el rango de calorías recomendado, que debe consumir una persona diariamente en caso de que desee adelgazar.\n
        - calorias_recomendadas: TMB - 15% o 20%

    *parm TMB (float): Tasa metabólica basal.\n
    *parm peso (float): Peso de la persona en kilogramos.\n
    *parm altura (float): Altura de la persona en centimetros.\n
    *parm edad (int): Edad de la persona en años.\n
    *parm valor_genero (int): Valor que varía según el género de la persona: en caso de ser masculino debe ser 5 y en caso de ser femenino debe ser -161.\n
    """
    if TMB is None:
        TMB = calcular_calorias_en_reposo(peso, altura_cm, edad, valor_genero)
        
    valor_minimo_para_adelgazar = (TMB*15)/100
    valor_maximo_para_adelgazar = (TMB*20)/100
    
    calorias_minimas_recomendadas_para_adelgazar = round(TMB - valor_minimo_para_adelgazar,2)
    calorias_maximas_recomendadas_para_adelgazar = round(TMB - valor_maximo_para_adelgazar,2)

    return f"Para adelgazar es recomendado que consumas entre: {calorias_maximas_recomendadas_para_adelgazar} y {calorias_minimas_recomendadas_para_adelgazar} calorías al día." 
