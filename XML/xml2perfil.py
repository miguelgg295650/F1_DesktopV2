import os
import xml.etree.ElementTree as ET

# Definir las dimensiones del SVG
SVG_WIDTH = 1000  # Anchura del SVG
SVG_HEIGHT = 600  # Altura del SVG
MARGIN = 50  # Margen alrededor del gráfico

ns = {'ns': 'http://www.uniovi.es'}

def read_circuito_xml(filename):
        
    tree = ET.parse(filename)
    root = tree.getroot()

    distances = []
    altitudes = []

    tramos_element = root.find('ns:tramos', ns)
    if tramos_element is not None:
        for tramo in tramos_element.findall('ns:tramo', ns):
            try:
                distancia = float(tramo.find('ns:distancia', ns).text)
                altitud = float(tramo.find('ns:coordenada/ns:altitud', ns).text)
                
                distances.append(distancia)
                altitudes.append(altitud)
            except Exception as e:
                print(f"Error al procesar tramo: {e}")

    distances.pop()
    altitudes.pop()
    
    print(f"Distancias: {distances}")
    print(f"Altitudes: {altitudes}")

    return distances, altitudes, 

def generate_svg(filename, distances, altitudes):
    max_distance = sum(distances)  
    max_altitude = max(altitudes)
    min_altitude = min(altitudes)

    svg_content = f'<svg width="{SVG_WIDTH}" height="{SVG_HEIGHT}" xmlns="http://www.w3.org/2000/svg">\n'
    svg_content += f'<rect width="100%" height="100%" fill="white"/>\n'
    
    accumulated_distance = 0
    previous_x, previous_y = None, None

    for dist, alt in zip(distances, altitudes):
        accumulated_distance += dist  # Acumula la distancia

        # Calcula coordenadas X e Y
        x = MARGIN + (accumulated_distance / max_distance) * (SVG_WIDTH - 2 * MARGIN)
        # Cambia el cálculo de Y para que el eje Y sea correcto
        y = SVG_HEIGHT - MARGIN - ((alt - min_altitude) / (max_altitude - min_altitude)) * (SVG_HEIGHT - 2 * MARGIN)

        # Dibuja la línea desde el punto anterior al nuevo punto
        if previous_x is not None and previous_y is not None:
            svg_content += f'<line x1="{previous_x}" y1="{previous_y}" x2="{x}" y2="{y}" stroke="black" stroke-width="2"/>\n'

        # Actualiza el punto anterior
        previous_x, previous_y = x, y

    # Dibuja la línea del suelo
    svg_content += f'<line x1="{MARGIN}" y1="{SVG_HEIGHT - MARGIN}" x2="{SVG_WIDTH - MARGIN}" y2="{SVG_HEIGHT - MARGIN}" stroke="black" stroke-width="2"/>\n'
    
    # Conecta el último punto al suelo
    if previous_x is not None and previous_y is not None:
        svg_content += f'<line x1="{previous_x}" y1="{previous_y}" x2="{previous_x}" y2="{SVG_HEIGHT - MARGIN}" stroke="black" stroke-width="2"/>\n'

    # Cierra el archivo SVG
    svg_content += "</svg>"

    # Escribe el contenido en un archivo
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
