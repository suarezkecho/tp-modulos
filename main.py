from src.elementos_de_programa import crear_persona, obtener_inputs
from src.calculadora_indices import calcular_IMC, calcular_porcentaje_grasa, calcular_calorias_en_reposo, calcular_calorias_en_actividad, consumo_calorias_recomendado_para_adelgazar

if __name__ == "__main__":
    peso,altura_metros,altura_centimetros,edad,genero,actividad = obtener_inputs()
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