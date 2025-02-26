import pyopenms as oms
import matplotlib.pyplot as plt

# Rutas de los archivos de entrada
input_file = "/home/jfml/Desktop/LCMS_290824/126_C.mzML"
smoothed_file = "/home/jfml/Videos/Analisis/Curso/Smoothing/126C_smoothed.mzML"

# Crear objetos MSExperiment para cargar los archivos mzML
exp_original = oms.MSExperiment()
exp_smoothed = oms.MSExperiment()

# Cargar los archivos mzML
oms.MzMLFile().load(input_file, exp_original)
oms.MzMLFile().load(smoothed_file, exp_smoothed)

# Extraer los primeros espectros de ambos experimentos
spectrum_original = exp_original.getSpectra()[150]  # Tomamos el primer espectro
spectrum_smoothed = exp_smoothed.getSpectra()[150]  # Tomamos el primer espectro suavizado

# Obtener los datos de m/z (x) e intensidad (y)
mz_original = spectrum_original.get_peaks()[0]  # m/z
intensity_original = spectrum_original.get_peaks()[1]  # Intensidad

mz_smoothed = spectrum_smoothed.get_peaks()[0]  # m/z
intensity_smoothed = spectrum_smoothed.get_peaks()[1]  # Intensidad

# Graficar los espectros
plt.figure(figsize=(10, 6))

# Espectro original
plt.plot(mz_original, intensity_original, label="Original", color='blue', alpha=0.7)

# Espectro suavizado
plt.plot(mz_smoothed, intensity_smoothed, label="Suavizado", color='red', alpha=0.7)

# Agregar detalles a la gráfica
plt.title("Comparación de Espectros Original y Suavizado")
plt.xlabel("m/z")
plt.ylabel("Intensidad")
plt.legend()

# Mostrar la gráfica
plt.show()

