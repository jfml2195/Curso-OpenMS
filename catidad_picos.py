import pyopenms
import matplotlib.pyplot as plt

# Cargar el archivo mzML
exp = pyopenms.MSExperiment()
pyopenms.MzMLFile().load("/home/jfml/Desktop/LCMS_290824/126_C.mzML", exp)

# Obtener la lista de espectros
spectra = exp.getSpectra()

# Buscar el espectro con el mayor número de picos
espectro_max_picos = None
max_picos = 0

for spectrum in spectra:
    num_picos = spectrum.size()
    
    if num_picos > max_picos:
        max_picos = num_picos
        espectro_max_picos = spectrum

# Verificar si se encontró el espectro con más picos
if espectro_max_picos:
    # Obtener tiempo de retención (RT) y scan number
    tiempo_retencion = espectro_max_picos.getRT()
    
    # Extraer scan number desde el native ID
    native_id = espectro_max_picos.getNativeID()
    # Suponiendo que el scan number está en el formato "scan=<número>", extraemos el número
    scan_number = native_id.split('=')[-1] if 'scan=' in native_id else 'Desconocido'

    # Imprimir la información
    print(f"Espectro con más picos: {max_picos} picos")
    print(f"Tiempo de retención: {tiempo_retencion} segundos")
    print(f"Scan number: {scan_number}")

    # Extraer valores m/z e intensidades
    mz_values, intensity_values = espectro_max_picos.get_peaks()

    # Graficar el espectro
    plt.plot(mz_values, intensity_values)
    plt.xlabel('m/z')
    plt.ylabel('Intensidad')
    plt.title(f'Espectro con {max_picos} picos')
    plt.show()
else:
    print("No se encontró un espectro con picos.")

