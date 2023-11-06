duracion_promedio=4
duracion_maxima=7
duracion_minima=2.5
duracion_actual=1.5

dif_curso_rapido=100-(duracion_actual*100/duracion_minima)
dif_curso_lento=100-(duracion_actual*100/duracion_maxima)
dif_curso_promedio=100-(duracion_actual*100/duracion_promedio)
print(f"El curso es {dif_curso_rapido}% mas rapido que el curso mas rapido")
print(f"El curso es {dif_curso_lento}% mas rapido que el curso mas rapido")
print(f"El curso es {dif_curso_promedio}% mas rapido que el curso el promedio de los cursos")

crudo_promedio=5
crudo_actual=3.5

Inservible_promedio=100-(duracion_promedio*100/crudo_promedio)
inservible_actual=100-(duracion_actual*100/crudo_actual)

print(f"los cursos promedio tuvieron un porcentaje de {Inservible_promedio}% material inservible")
print(f"Este curso tuvo un porcentaje de {inservible_actual}% material inservible")



    