import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.calculadora_indices import consumo_calorias_recomendado_para_adelgazar
from src.elementos_de_programa import crear_persona, obtener_inputs

if __name__ == '__main__':
    peso,altura_metros,altura_centimetros,edad,genero,actividad = obtener_inputs()

    persona = crear_persona(peso, altura_metros, altura_centimetros, edad, genero, actividad)

    respuesta_recomendacion_adelgazar = consumo_calorias_recomendado_para_adelgazar(persona["peso"], persona["altura_cm"], persona["edad"], persona["valor_genero_TMB"])
    print(respuesta_recomendacion_adelgazar)