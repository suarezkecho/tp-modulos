import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.elementos_de_programa import crear_persona, obtener_inputs
from src.calculadora_indices import calcular_calorias_en_actividad

if __name__ == '__main__':
    peso,altura_metros,altura_centimetros,edad,genero,actividad = obtener_inputs()

    persona = crear_persona(peso, altura_metros, altura_centimetros, edad, genero, actividad)

    respuesta_calorias_actividad = calcular_calorias_en_actividad(persona["peso"], persona["altura_cm"], persona["edad"], persona["valor_genero_TMB"], persona["valor_actividad"])
    print(f"Las calorias que gastas en actividad: {respuesta_calorias_actividad}")