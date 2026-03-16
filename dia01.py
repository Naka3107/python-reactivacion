# Día 1 - Variables y tipos de datos

# Texto (String)
nombre = "Carlos"
ciudad = "Barcelona"
profesion = "Compositor y pianista"
meta = "Conseguir trabajo como programador en 4 meses"
# Números
edad = 28

# Imprimir todo
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Ciudad: {ciudad}")
print(f"Profesión anterior: {profesion}")
print(f"Meta: {meta}")

###############################################

meses = 4
horas = 2
semanas_por_mes = 4
dias_semana = 6

horas_semana = horas * dias_semana
semanas_totales = semanas_por_mes * meses
horas_totales = horas_semana * semanas_totales

print(f"Horas por semana: {horas_semana}")
print(f"Semanas totales: {semanas_totales}")
print(f"Horas totales de estudio: {horas_totales}")

###################################################
horas_hoy = 2

if horas_hoy==0:
    print("Hoy no estudiaste nada. ¡Mañana sin excusas!")
elif horas_hoy==1:
    print("Estudiaste poco, pero algo es algo.")
elif horas_hoy==2:
    print("¡Objetivo cumplido!")
else:
    print("¡Por encima del objetivo! Excelente.")

######################################################
tecnologias = ["Python","JavaScript","SQL","Git","Docker"]
for i, v in enumerate(tecnologias):
    print(f"{i+1}. {v}")

#########################################################
def calcular_progreso(dias_estudiados, dias_totales):
    progreso = round(dias_estudiados*100/dias_totales,2)
    print(f"Llevas {dias_estudiados} de {dias_totales} días.\nProgreso: {progreso}%")

calcular_progreso(10,112)