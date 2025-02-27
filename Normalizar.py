###### Juan Francisco Moreno Luna.Curso de OpenMS juan.moreno@cinvestav.mx

import pyopenms as oms
import matplotlib.pyplot as plt

# Ruta al archivo suavizado
input_file = '/home/jfml/Videos/Analisis/Curso/Smoothing/126C_smoothed.mzML'

# Crear un objeto MSExperiment para almacenar los datos
exp = oms.MSExperiment()

# Cargar el archivo mzML suavizado
oms.MzMLFile().load(input_file, exp)

# Visualizar el espectro original (antes de la normalización)
plt.figure(figsize=(10, 6))
plt.title("Espectro Original")
plt.bar(exp.getSpectrum(0).get_peaks()[0], exp.getSpectrum(0).get_peaks()[1], snap=False)
plt.xlabel("m/z")
plt.ylabel("Intensidad")
plt.show()

# Crear un objeto Normalizer
normalizer = oms.Normalizer()

# Obtener los parámetros del normalizador
param = normalizer.getParameters()

# Establecer el método de normalización (normalizar a 1)
param.setValue("method", "to_one")

# Establecer los parámetros de normalización
normalizer.setParameters(param)

# Aplicar la normalización al espectro
normalizer.filterPeakMap(exp)

# Visualizar el espectro después de la normalización
plt.figure(figsize=(10, 6))
plt.title("Espectro Normalizado")
plt.bar(exp.getSpectrum(0).get_peaks()[0], exp.getSpectrum(0).get_peaks()[1], snap=False)
plt.xlabel("m/z")
plt.ylabel("Intensidad Normalizada")
plt.show()

# Guardar el archivo mzML normalizado
output_file = '/home/jfml/Videos/Analisis/Curso/Spectrum_Normalization/126_C_normalized.mzML'
oms.MzMLFile().store(output_file, exp)
print(f"Archivo normalizado guardado como: {output_file}")

