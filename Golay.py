###### Juan Francisco Moreno Luna.Curso de OpenMS juan.moreno@cinvestav.mx
import pyopenms as oms

# Rutas de entrada y salida
input_file = "/media/jfml/483BD23D11A233FF/Zuriel_datos/cd/680_CD1-1neg.mzML"
output_file = "/media/jfml/483BD23D11A233FF/680_CD_savgol.mzML"

# Crear objeto MSExperiment y filtro Savitzky-Golay
exp = oms.MSExperiment()
sg_filter = oms.SavitzkyGolayFilter()

# Configurar parámetros del filtro
params = sg_filter.getParameters()
params.setValue("frame_length", 11)          # Tamaño de la ventana (debe ser impar, ej: 5, 7, 11)
params.setValue("polynomial_order", 3)       # Orden del polinomio (ej: 2, 3)
sg_filter.setParameters(params)

# Cargar archivo
oms.MzMLFile().load(input_file, exp)

# Aplicar filtro
sg_filter.filterExperiment(exp)

# Guardar resultado
oms.MzMLFile().store(output_file, exp)

print(f"Archivo suavizado con Savitzky-Golay guardado en: {output_file}")
