import os
import xml.etree.ElementTree as ET

# Definir las dimensiones del SVG
SVG_WIDTH = 800  # Anchura del SVG
SVG_HEIGHT = 400  # Altura del SVG
MARGIN = 50  # Margen alrededor del gráfico
ALTITUDE_SCALE = 2  # Escala para la altitud

ns = {'ns': 'http://www.uniovi.es'}

# Definir colores para cada sector
SECTOR_COLORS = {
    "sector1": "lightblue",
    "sector2": "lightgreen",
    "sector3": "lightcoral",
    "sector4": "lightyellow",
    # Agrega más sectores y colores según sea necesario
}

# Leer el archivo XML
def read_circuito_xml(filename):
        
    tree = ET.parse(filename)
    root = tree.getroot()

    distances = []
    altitudes = []
    sectors = []  # Lista para guardar los sectores

    # Buscar el elemento <tramos> y luego los <tramo>
    tramos_element = root.find('ns:tramos', ns)
    if tramos_element is not None:
        for tramo in tramos_element.findall('ns:tramo', ns):
            try:
                distancia = float(tramo.find('ns:distancia', ns).text)
                altitud = float(tramo.find('ns:coordenada/ns:altitud', ns).text)
                sector = tramo.find('ns:sector', ns).text  # Suponiendo que hay un campo <sector>
                
                distances.append(distancia)
                altitudes.append(altitud)
                sectors.append(sector)  # Agregar el sector correspondiente
            except Exception as e:
                print(f"Error al procesar tramo: {e}")

    # Eliminar el último elemento, si se requiere
    distances.pop()
    altitudes.pop()
    sectors.pop()
    
    print(f"Distancias: {distances}")
    print(f"Altitudes: {altitudes}")
    print(f"Sectores: {sectors}")

    return distances, altitudes, sectors

# Generar archivo SVG
def generate_svg(filename, distances, altitudes, sectors):
    # Normalizar las distancias y altitudes para ajustarlas al tamaño del SVG
    max_distance = sum(distances)  # La distancia total es la suma de todas las distancias
    max_altitude = max(altitudes)
    min_altitude = min(altitudes)  # Encuentra la altitud mínima
    
    # Crear el archivo SVG
    svg_content = f'<svg width="{SVG_WIDTH}" height="{SVG_HEIGHT}" xmlns="http://www.w3.org/2000/svg">\n'
    svg_content += f'<rect width="100%" height="100%" fill="white"/>\n'
    
    # Acumulador para la distancia
    accumulated_distance = 0
    previous_x, previous_y = None, None  # Variables para rastrear el punto anterior

    for dist, alt, sector in zip(distances, altitudes, sectors):
        accumulated_distance += dist  # Acumulamos la distancia
        # Convertir las distancias y altitudes a coordenadas X e Y en el SVG
        x = MARGIN + (accumulated_distance / max_distance) * (SVG_WIDTH - 2 * MARGIN)
        y = SVG_HEIGHT - MARGIN - ((alt - min_altitude) / (max_altitude - min_altitude)) * (SVG_HEIGHT - 2 * MARGIN)

        # Si es el primer punto, simplemente lo guardamos
        if previous_x is None or previous_y is None:
            previous_x, previous_y = x, y
            continue

        # Dibujar la línea del segmento en el color correspondiente al sector
        color = SECTOR_COLORS.get(sector, "gray")  # Color por defecto si el sector no está definido
        svg_content += f'<line x1="{previous_x}" y1="{previous_y}" x2="{x}" y2="{y}" stroke="{color}" stroke-width="2"/>\n'

        # Actualizar el punto anterior
        previous_x, previous_y = x, y

    # Dibujar la línea del suelo
    svg_content += f'<line x1="{MARGIN}" y1="{SVG_HEIGHT - MARGIN}" x2="{SVG_WIDTH - MARGIN}" y2="{SVG_HEIGHT - MARGIN}" stroke="black" stroke-width="2"/>\n'

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
    distances, altitudes, sectors = read_circuito_xml(input_xml)

    # Generar el archivo SVG
    generate_svg(output_svg, distances, altitudes, sectors)

    print(f"Archivo SVG generado: {output_svg}")

if __name__ == "__main__":
    main()
