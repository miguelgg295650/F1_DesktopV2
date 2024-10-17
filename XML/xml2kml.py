import xml.etree.ElementTree as ET
#from fpdf import FPDF
import os

# Función para leer el XML y extraer coordenadas
def read_xml(file_path):
    try:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"El archivo {file_path} no existe en el directorio actual.")
        
        # Parsear el archivo XML
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Namespace del XML
        namespace = {'ns': 'http://www.uniovi.es'}

        # Extraer las coordenadas de los tramos
        coordenadas = []
        for tramo in root.findall('.//ns:tramo', namespace):
            longitud = tramo.find('.//ns:longitud', namespace).text
            latitud = tramo.find('.//ns:latitud', namespace).text
            altitud = tramo.find('.//ns:altitud', namespace).text
            coordenadas.append(f"{longitud},{latitud},{altitud}")
        
        return coordenadas
    except ET.ParseError as e:
        print(f"Error al parsear el archivo XML: {e}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Función para escribir el archivo KML
def write_kml(coordenadas, output_kml):
    with open(output_kml, 'w') as kml_file:
        # Prologo KML
        kml_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        kml_file.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
        kml_file.write('  <Document>\n')
        kml_file.write('    <name>Circuito de las Américas</name>\n')
        kml_file.write('    <Placemark>\n')
        kml_file.write('      <LineString>\n')
        kml_file.write('        <coordinates>\n')
        
        # Coordenadas
        for coord in coordenadas:
            kml_file.write(f"          {coord}\n")
        
        # Epilogo KML
        kml_file.write('        </coordinates>\n')
        kml_file.write('      </LineString>\n')
        kml_file.write('    </Placemark>\n')
        kml_file.write('  </Document>\n')
        kml_file.write('</kml>\n')

# Función para generar un PDF de la planimetría (planimetría simplificada)
def create_pdf(output_pdf, coordenadas):
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Planimetría del Circuito", ln=True, align="C")
    
    pdf.ln(10)
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt="Coordenadas del circuito:", ln=True)
    
    pdf.ln(5)
    for coord in coordenadas:
        pdf.cell(200, 10, txt=coord, ln=True)
    
    # Guardar el PDF
    pdf.output(output_pdf)

# Main function
if __name__ == "__main__":
    xml_file = 'F1_DesktopV2-main/XML/circuitoEsquema.xml'
    kml_output = 'F1_DesktopV2-main/XML/circuito.kml'
    pdf_output = 'planimetria.pdf'

    # Leer coordenadas del XML
    coordenadas = read_xml(xml_file)

    if coordenadas:
        # Generar archivo KML
        write_kml(coordenadas, kml_output)
        print(f"Archivo KML '{kml_output}' generado correctamente.")

        # Generar archivo PDF con la planimetría
        create_pdf(pdf_output, coordenadas)
        print(f"Archivo PDF '{pdf_output}' generado correctamente.")
