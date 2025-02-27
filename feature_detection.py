
###### Juan Francisco Moreno Luna.Curso de OpenMS juan.moreno@cinvestav.mx
import pyopenms as oms

# Ruta de entrada y salida
input_mzml = "/home/jfml/Videos/Analisis/Curso/Smoothing/126C_smoothed.mzML"
output_feature_map = "/home/jfml/Videos/Analisis/Curso/Feature_Detection/126C_Features.featureXML"

# Crear objeto MSExperiment y cargar el archivo mzML
exp = oms.MSExperiment()
oms.MzMLFile().load(input_mzml, exp)

# Ordenar los espectros por tiempo de retención
exp.sortSpectra(True)

# Inicializar la detección de trazas de masa
mass_traces = []
mtd = oms.MassTraceDetection()
mtd_params = mtd.getDefaults()

# Ajustar los parámetros de detección
mtd_params.setValue("mass_error_ppm", 5.0)  # Error en ppm para m/z
mtd_params.setValue("noise_threshold_int", 1000000.0)  # Umbral de ruido
mtd.setParameters(mtd_params)

# Detectar las trazas de masa
mtd.run(exp, mass_traces, 0)

# Inicializar la detección de picos de elución
mass_traces_split = []
mass_traces_final = []
epd = oms.ElutionPeakDetection()
epd_params = epd.getDefaults()
epd_params.setValue("width_filtering", "fixed")  # Filtro de ancho de pico
epd.setParameters(epd_params)

# Detectar los picos de elución
epd.detectPeaks(mass_traces, mass_traces_split)

# Si el filtro de ancho de pico es automático, se filtran las trazas
if epd.getParameters().getValue("width_filtering") == "auto":
    epd.filterByPeakWidth(mass_traces_split, mass_traces_final)
else:
    mass_traces_final = mass_traces_split

# Inicializar el objeto FeatureFindingMetabo para encontrar las características
fm = oms.FeatureMap()
feat_chrom = []
ffm = oms.FeatureFindingMetabo()

# Ajustar parámetros de FeatureFindingMetabo
ffm_params = ffm.getDefaults()
ffm_params.setValue("isotope_filtering_model", "none")
ffm_params.setValue("remove_single_traces", "true")  # Filtrar trazas con solo un pico
ffm_params.setValue("mz_scoring_by_elements", "false")
ffm_params.setValue("report_convex_hulls", "true")
ffm.setParameters(ffm_params)

# Ejecutar la detección de características
ffm.run(mass_traces_final, fm, feat_chrom)

# Establecer identificadores únicos
fm.setUniqueIds()
fm.setPrimaryMSRunPath([input_mzml.encode()])

# Guardar el resultado en un archivo FeatureXML
oms.FeatureXMLFile().store(output_feature_map, fm)

print(f"Características detectadas y guardadas en: {output_feature_map}")

