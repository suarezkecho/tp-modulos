def crear_persona(peso: float, altura_m: float, altura_cm: int, edad:int, genero:str, actividad:str):
    try:
        if genero.lower() == 'm':
            if actividad.replace(" ","") == "1":
                valor_actividad = 1.2
            elif actividad.replace(" ","") == "2":
                valor_actividad = 1.375
            elif actividad.replace(" ","") == "3":
                valor_actividad = 1.55
            elif actividad.replace(" ","") == "4":
                valor_actividad = 1.725
            elif actividad.replace(" ","") == "5":
                valor_actividad = 1.9

            hombre={
                "peso": peso,
                "altura_m": altura_m,
                "altura_cm": altura_cm,
                "edad": edad,
                "valor_genero_GC": 10.8,
                "valor_genero_TMB": 5,
                "valor_actividad": valor_actividad}
            return hombre

        elif genero.lower() == 'f':
            if actividad.replace(" ","") == "1":
                valor_actividad = 1.2
            elif actividad.replace(" ","") == "2":
                valor_actividad = 1.375
            elif actividad.replace(" ","") == "3":
                valor_actividad = 1.55
            elif actividad.replace(" ","") == "4":
                valor_actividad = 1.725
            elif actividad.replace(" ","") == "5":
                valor_actividad = 1.9

            mujer={
                "peso":peso,
                "altura_m":altura_m,
                "altura_cm":altura_cm,
                "edad":edad,
                "valor_genero_GC": 0,
                "valor_genero_TMB": -161,
                "valor_actividad": valor_actividad}
            return mujer
    
    except TypeError as tp:
        return tp
    except ValueError as ve:
        return ve
    

def obtener_inputs() -> list:
    """
    Solicita el ingreso por consola y retorna los siguientes datos:
        - peso (float): Peso de la persona en kg.
        - altura_metros (float): Altura de la persona en metros.
        - altura_centimetros (int): Se calcula a partir de la "altura_metros".
        - edad (int): Edad de la persona.
        - genero (str): El genero de la persona dando por opcion (m=masculino; f=femenino;)
        - actividad (str): Se obtiene un valor númerico en base a la cantidad de ejercicio que realice durante la semana.
    Retorna todos los valores como una lista. [peso, altura_metros, altura_centimetros, edad, genero, actividad]
    """
    try:
        peso = float(input("Ingrese su peso en kg: "))
        altura_metros = float(input("Ingrese su altura en metros (ej. 1.75): "))
        altura_centimetros = int(altura_metros * 100)
        edad = int(input("Ingrese su edad: "))
        genero = input("Ingrese su genero:\nm: masculino\nf: femenino\n")
        actividad = input("Ingrese el numero segun corresponda a su actividad fisica: \n1: poco o ningún ejercicio\n2: ejercicio ligero (1 a 3 días a la semana)\n3: ejercicio moderado (3 a 5 días a la semana)\n4: deportista (6 -7 días a la semana)\n5: atleta (entrenamientos mañana y tarde)\n")

        return [peso,altura_metros,altura_centimetros,edad,genero,actividad]

    except Exception as ex:
        return ex