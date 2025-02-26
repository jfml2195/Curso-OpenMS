from pyopenms import MSExperiment, MzMLFile  # Importar solo lo necesario

def get_file_info(filename):
    # Cargar el archivo .mzML
    exp = MSExperiment()
    MzMLFile().load(filename, exp)
    
    # Metadatos básicos
    num_spectra = exp.getNrSpectra()
    num_chroms = exp.getNrChromatograms()
    rt_range = (exp.getMinRT()/60, exp.getMaxRT()/60)  # en minutos
    mz_range = (exp.getMinMZ(), exp.getMaxMZ())
    
    # Contar niveles de MS (MS1 vs MS2)
    ms1 = 0
    ms2 = 0
    for spec in exp:
        if spec.getMSLevel() == 1:
            ms1 += 1
        elif spec.getMSLevel() == 2:
            ms2 += 1
    
    # Información del instrumento (si está disponible)
    instrument = "No disponible"
    if exp.getInstrument() is not None:
        instrument = exp.getInstrument().getName()
    
    # Imprimir resumen
    print(f"Archivo: {filename}")
    print(f"- Espectros totales: {num_spectra}")
    print(f"- Cromatogramas: {num_chroms}")
    print(f"- MS1: {ms1} | MS2: {ms2}")
    print(f"- RT (min): [{rt_range[0]:.2f}, {rt_range[1]:.2f}]")
    print(f"- m/z: [{mz_range[0]:.2f}, {mz_range[1]:.2f}]")
    print(f"- Instrumento: {instrument}")

# Ejemplo de uso
get_file_info("/media/jfml/483BD23D11A233FF/Zuriel_datos/cd/680_CD1-1neg.mzML")
