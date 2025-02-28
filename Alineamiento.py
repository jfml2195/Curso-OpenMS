###### Juan Francisco Moreno Luna.Curso de OpenMS juan.moreno@cinvestav.mx
import pyopenms as oms
import os

# Ruta donde están tus archivos featureXML
base_path = "/home/jfml/Videos/Analisis/Curso/Map_Alignment"
feature_files = [
    "131_B_FiltNoise_filtered.featureXML",
    "131_C_FiltNoise_filtered.featureXML",
    "132_A_FiltNoise_filtered.featureXML",
]

feature_maps = []

# Cargar archivos featureXML
for feature_file in feature_files:
    file_path = os.path.join(base_path, feature_file)  # Ruta completa del archivo
    feature_map = oms.FeatureMap()
    oms.FeatureXMLFile().load(file_path, feature_map)
    feature_maps.append(feature_map)

# Selección del mapa de referencia 
ref_index = [
    i[0]
    for i in sorted(
        enumerate([fm.size() for fm in feature_maps]), key=lambda x: x[1]
    )
][-1]

# Inicializar el alineador Pose Clustering y establecer el mapa de referencia
aligner = oms.MapAlignmentAlgorithmPoseClustering()
aligner.setReference(feature_maps[ref_index])

# Alinear los mapas y transformar los tiempos de retención
for feature_map in feature_maps[:ref_index] + feature_maps[ref_index + 1:]:
    trafo = oms.TransformationDescription()
    aligner.align(feature_map, trafo)
    transformer = oms.MapAlignmentTransformer()
    transformer.transformRetentionTimes(feature_map, trafo, True)

# Guardar los mapas alineados
for i, feature_map in enumerate(feature_maps):
    aligned_file = os.path.join(base_path, f"aligned_{feature_files[i]}")
    oms.FeatureXMLFile().store(aligned_file, feature_map)
    print(f"Archivo alineado guardado en: {aligned_file}")

