from elementos_de_programa import crear_persona, obtener_inputs
from src.calculadora_indices import calcular_IMC

if __name__ == '__main__':
    peso,altura_metros,altura_centimetros,edad,genero,actividad = obtener_inputs()

    persona = crear_persona(peso, altura_metros, altura_centimetros, edad, genero, actividad)

    respuesta_IMC,mensaje = calcular_IMC(persona["peso"], persona["altura_m"])
    print(f"Tu IMC: {respuesta_IMC}, {mensaje}")
