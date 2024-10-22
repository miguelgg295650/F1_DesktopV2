import os
import xml.etree.ElementTree as ET

# Definir las dimensiones del SVG
SVG_WIDTH = 800  # Anchura del SVG
SVG_HEIGHT = 400  # Altura del SVG
MARGIN = 50  # Margen alrededor del gráfico
ALTITUDE_SCALE = 2  # Escala para la altitud

# Leer el archivo XML
def read_circuito_xml(filename):
        
    tree = ET.parse(filename)
    root = tree.getroot()
    print(tree)
    # Listas para almacenar distancias y altitudes
    distances = []
    altitudes = []

    # Recorrer los tramos en el archivo XML y extraer distancias y altitudes
    for tramo in root.findall('tramo'):
        distancia = float(tramo.find('distancia').text)
        altitud = float(tramo.find('coordenada').find('altitud').text)
        print(distancia)
        print(altitud)
        distances.append(distancia)
        altitudes.append(altitud)

    return distances, altitudes

# Generar archivo SVG
def generate_svg(filename, distances, altitudes):
    # Normalizar las distancias y altitudes para ajustarlas al tamaño del SVG
    max_distance = max(distances)
    max_altitude = max(altitudes)
    
    # Crear el archivo SVG
    svg_content = f'<svg width="{SVG_WIDTH}" height="{SVG_HEIGHT}" xmlns="http://www.w3.org/2000/svg">\n'
    svg_content += f'<rect width="100%" height="100%" fill="white"/>\n'
    
    # Generar la polilínea que representará la altimetría
    polyline_points = ""

    for i, (dist, alt) in enumerate(zip(distances, altitudes)):
        # Convertir las distancias y altitudes a coordenadas X e Y en el SVG
        x = MARGIN + (dist / max_distance) * (SVG_WIDTH - 2 * MARGIN)
        y = SVG_HEIGHT - MARGIN - (alt / max_altitude) * (SVG_HEIGHT - 2 * MARGIN)
        polyline_points += f"{x},{y} "

    # Cerrar la polilínea para hacer efecto de suelo
    polyline_points += f"{SVG_WIDTH - MARGIN},{SVG_HEIGHT - MARGIN} {MARGIN},{SVG_HEIGHT - MARGIN} "
    
    # Dibujar la polilínea
    svg_content += f'<polyline points="{polyline_points}" fill="lightblue" stroke="black" stroke-width="2"/>\n'
    
    # Cerrar el archivo SVG
    svg_content += "</svg>"

    # Escribir el contenido en un archivo
    with open(filename, "w") as f:
        f.write(svg_content)

# Función principal
def main():
    # Archivo XML que contiene los datos del circuito
    input_xml = "circuitoEsquema.xml"
    output_svg = "altimetria.svg"

    # Leer el archivo XML y extraer distancias y altitudes
    distances, altitudes = read_circuito_xml(input_xml)

    # Generar el archivo SVG
    generate_svg(output_svg, distances, altitudes)

    print(f"Archivo SVG generado: {output_svg}")

if __name__ == "__main__":
    main()
