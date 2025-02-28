import pyopenms as oms
import os

# Ruta base donde están almacenados los archivos localmente
base_path = "/home/jfml/Videos/Analisis/Curso/Map_Alignment"

# Lista de archivos featureXML
feature_files = [
    "aligned_131_B_FiltNoise_filtered.featureXML",
    "aligned_131_C_FiltNoise_filtered.featureXML",
    "aligned_132_A_FiltNoise_filtered.featureXML",
]

feature_maps = []

# Cargar los archivos directamente desde la carpeta local
for feature_file in feature_files:
    file_path = os.path.join(base_path, feature_file)  # Construir la ruta completa
    if os.path.exists(file_path):  # Verificar que el archivo existe
        feature_map = oms.FeatureMap()
        oms.FeatureXMLFile().load(file_path, feature_map)  # Cargar el archivo
        feature_maps.append(feature_map)
        print(f"Archivo cargado: {file_path}")
    else:
        print(f"Error: No se encontró el archivo {file_path}")

feature_grouper = oms.FeatureGroupingAlgorithmKD()

consensus_map = oms.ConsensusMap()
file_descriptions = consensus_map.getColumnHeaders()

for i, feature_map in enumerate(feature_maps):
    file_description = file_descriptions.get(i, oms.ColumnHeader())
    file_description.filename = os.path.basename(
        feature_map.getMetaValue("spectra_data")[0].decode()
    )
    file_description.size = feature_map.size()
    file_descriptions[i] = file_description

feature_grouper.group(feature_maps, consensus_map)
consensus_map.setColumnHeaders(file_descriptions)
consensus_map.setUniqueIds()
oms.ConsensusXMLFile().store("FeatureMatrix.consensusXML", consensus_map)

