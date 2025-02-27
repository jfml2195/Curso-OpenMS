import pyopenms as oms
import matplotlib.pyplot as plt

def get_ms1_spectra(exp):
    """Filtra y retorna solo los espectros MS1 de un experimento."""
    return [spec for spec in exp.getSpectra() if spec.getMSLevel() == 1]

# Cargar archivos
input_file = "/media/jfml/483BD23D11A233FF/Zuriel_datos/cd/680_CD1-1neg.mzML"
smoothed_file = "/media/jfml/483BD23D11A233FF/680_CD.mzML"

exp_original = oms.MSExperiment()
exp_smoothed = oms.MSExperiment()

oms.MzMLFile().load(input_file, exp_original)
oms.MzMLFile().load(smoothed_file, exp_smoothed)

# Obtener solo espectros MS1
ms1_original = get_ms1_spectra(exp_original)
ms1_smoothed = get_ms1_spectra(exp_smoothed)

# Verificar que hay suficientes espectros MS1
if len(ms1_original) == 0 or len(ms1_smoothed) == 0:
    raise ValueError("No hay espectros MS1 en el archivo.")
    
# Ejemplo: Comparar el primer espectro MS1 disponible
spectrum_original = ms1_original[0]  # Primer MS1
spectrum_smoothed = ms1_smoothed[0]

# Obtener todos los m/z e intensidades (no un índice fijo)
mz_original, intensity_original = spectrum_original.get_peaks()
mz_smoothed, intensity_smoothed = spectrum_smoothed.get_peaks()

plt.figure(figsize=(12, 6))

# Espectro original (todos los puntos)
plt.plot(mz_original, intensity_original, label="Original (MS1)", color='blue', alpha=0.7)

# Espectro suavizado (todos los puntos)
plt.plot(mz_smoothed, intensity_smoothed, label="Suavizado (MS1)", color='red', alpha=0.5)

plt.title("Comparación de Espectros MS1 Original vs. Suavizado")
plt.xlabel("m/z")
plt.ylabel("Intensidad")
plt.legend()
plt.show()
