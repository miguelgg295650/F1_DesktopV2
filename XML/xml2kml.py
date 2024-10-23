import xml.etree.ElementTree as ET
import os


def read_xml(file_path):
    if not os.path.isfile(file_path):
        print(f"El archivo {file_path} no encontrado.")
    
    tree = ET.parse(file_path)
    root = tree.getroot()

    namespace = {'ns': 'http://www.uniovi.es'}

    coordenadas = []
    for tramo in root.findall('.//ns:tramo', namespace):
        longitud = tramo.find('.//ns:longitud', namespace).text
        latitud = tramo.find('.//ns:latitud', namespace).text
        altitud = tramo.find('.//ns:altitud', namespace).text
        coordenadas.append(f"{longitud},{latitud},{altitud}")
    
    return coordenadas
   

def write_kml(coordenadas, output_kml):
    with open(output_kml, 'w') as kml_file:
        
        kml_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        kml_file.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
        kml_file.write('  <Document>\n')
        kml_file.write('    <name>Circuito de las Américas</name>\n')
        kml_file.write('    <Style id="lineStyle">\n')
        kml_file.write('      <LineStyle>\n')
        kml_file.write('        <color>ff0000ff</color>\n')
        kml_file.write('        <width>4</width> \n')
        kml_file.write('      </LineStyle>\n')
        kml_file.write('    </Style>\n')
        kml_file.write('    <Placemark>\n')
        kml_file.write('      <styleUrl>#lineStyle</styleUrl>\n')
        kml_file.write('      <LineString>\n')
        kml_file.write('        <coordinates>\n')
        
        for coord in coordenadas:
            kml_file.write(f"          {coord}\n")
        
        kml_file.write('        </coordinates>\n')
        kml_file.write('      </LineString>\n')
        kml_file.write('    </Placemark>\n')
        kml_file.write('  </Document>\n')
        kml_file.write('</kml>\n')



if __name__ == "__main__":
    xml_file = 'circuitoEsquema.xml'
    kml_output = 'circuito.kml'

    coordenadas = read_xml(xml_file)

    if coordenadas:
        write_kml(coordenadas, kml_output)
        print(f"Archivo KML '{kml_output}' generado correctamente.")