from creacion_de_persona import crear_persona
from src.calculadora_indices import calcular_IMC, calcular_porcentaje_grasa, calcular_calorias_en_reposo, calcular_calorias_en_actividad, consumo_calorias_recomendado_para_adelgazar

if __name__ == "__main__":
    peso = float(input("Ingrese su peso en kg: "))
    altura_metros = float(input("Ingrese su altura en metros (ej. 1.75): "))
    altura_centimetros = int(altura_metros * 100)
    edad = int(input("Ingrese su edad: "))
    genero = input("Ingrese su genero:\nm: masculino\nf: femenino\n")
    actividad = input("Ingrese el numero segun corresponda a su actividad fisica: \n1: poco o ningún ejercicio\n2: ejercicio ligero (1 a 3 días a la semana)\n3: ejercicio moderado (3 a 5 días a la semana)\n4: deportista (6 -7 días a la semana)\n5: atleta (entrenamientos mañana y tarde)\n")

    persona = crear_persona(peso, altura_metros, altura_centimetros, edad, genero, actividad)

    respuesta_IMC, mensaje_IMC = calcular_IMC(persona["peso"], persona["altura_m"])
    print(f"Tu IMC: {respuesta_IMC}, {mensaje_IMC}")
    respuesta_GC, mensaje_GC = calcular_porcentaje_grasa(persona["peso"],persona["altura_m"],persona["edad"],persona["valor_genero_GC"],respuesta_IMC)
    print(f"Tu porcentaje de grasa es: {respuesta_GC}, {mensaje_GC}")
    respuesta_TMB = calcular_calorias_en_reposo(persona["peso"],persona["altura_cm"], persona["edad"], persona["valor_genero_TMB"])
    print(f"Calculo de calorias en reposo: {respuesta_TMB}")
    respuesta_calc_calorias_actividad = calcular_calorias_en_actividad(persona["peso"], persona["altura_cm"], persona["edad"], persona["valor_genero_TMB"], persona["valor_actividad"],respuesta_TMB)
    print(f"Las calorias que gastas en actividad: {respuesta_calc_calorias_actividad}")
    respuesta_recomendacion_adelgazar = consumo_calorias_recomendado_para_adelgazar(persona["peso"], persona["altura_cm"], persona["edad"], persona["valor_genero_TMB"],respuesta_TMB)
    print(respuesta_recomendacion_adelgazar)