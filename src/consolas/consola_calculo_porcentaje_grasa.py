from elementos_de_programa import crear_persona, obtener_inputs
from src.calculadora_indices import calcular_porcentaje_grasa

if __name__ == '__main__':
    peso,altura_metros,altura_centimetros,edad,genero,actividad = obtener_inputs()
    
    persona = crear_persona(peso, altura_metros, altura_centimetros, edad, genero, actividad)

    respuesta_GC, mensaje_GC = calcular_porcentaje_grasa(persona["peso"],persona["altura_m"],persona["edad"],persona["valor_genero_GC"])
    print(f"Tu porcentaje de grasa es: {respuesta_GC}, {mensaje_GC}")