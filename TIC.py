###### Juan Francisco Moreno Luna.Curso de OpenMS juan.moreno@cinvestav.mx

import pyopenms as oms
import matplotlib.pyplot as plt

# Cargar el archivo mzML
exp = oms.MSExperiment()
oms.MzMLFile().load("/media/jfml/483BD23D11A233FF/Zuriel_datos/cd/680_CD1-1neg.mzML", exp)

# Obtener la lista de espectros
spectra = exp.getSpectra()

# Inicializar listas para tiempos de retención y TIC
retention_times = []
tic_values = []

# Iterar sobre los espectros MS1 para calcular el TIC
for spectrum in spectra:
    if spectrum.getMSLevel() == 1:  # Asegurarse de usar espectros MS1
        rt = spectrum.getRT()  # Obtener el tiempo de retención
        intensities = spectrum.get_peaks()[1]  # Obtener las intensidades de los picos
        tic = sum(intensities)  # Sumar todas las intensidades (TIC)
        
        retention_times.append(rt)
        tic_values.append(tic)

# Graficar el TIC
plt.figure(figsize=(10, 6))
plt.plot(retention_times, tic_values, label='TIC', color='blue')
plt.xlabel('Tiempo de retención (s)')
plt.ylabel('Intensidad total (TIC)')
plt.title('Cromatograma de iones totales (TIC)')
plt.grid(True)
plt.legend()
plt.show()
	
