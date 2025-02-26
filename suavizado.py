import pyopenms as oms

# Define las rutas de entrada y salida
input_file = "/home/jfml/Desktop/LCMS_290824/126_C.mzML"
output_file = "/home/jfml/Videos/Analisis/Curso/Smoothing/126C_smoothed.mzML"


# Crea el objeto MSExperiment y el filtro Gaussiano
exp = oms.MSExperiment()
gf = oms.GaussFilter()

# Obtén los parámetros del filtro Gaussiano y ajusta el ancho
param = gf.getParameters()
param.setValue("gaussian_width", 1.0)  # Ajusta según el nivel de suavizado deseado
gf.setParameters(param)

# Carga el archivo mzML en el objeto de experimento
oms.MzMLFile().load(input_file, exp)

# Aplica el filtro Gaussiano
gf.filterExperiment(exp)

# Guarda el archivo suavizado
oms.MzMLFile().store(output_file, exp)

print(f"El archivo suavizado se ha guardado en: {output_file}")

