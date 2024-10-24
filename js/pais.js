class Pais {
    constructor(nombrePais, nombreCapital, poblacion, gobierno, regionMayoritaria) {
        this.nombrePais = nombrePais;           
        this.nombreCapital = nombreCapital;      
        this.nombreCircuito = null;     
        this.poblacion = poblacion;              
        this.gobierno = gobierno;                 
        this.coordenadasMeta = { latitud: null, longitud: null ,altura: null};   
        this.regionMayoritaria = regionMayoritaria; 
      }
    asignaDatosCircuito(nombreCircuito,longitud,latitud,altura){
        this.nombreCircuito = nombreCircuito;
        this.coordenadasMeta.latitud = latitud;
        this.coordenadasMeta.longitud = longitud;
        this.coordenadasMeta.altura = altura;
    }

    getNombre(){
        return this.nombrePais;
    }
    getCapital(){
        return this.nombreCapital;
    }
    getInfoSecundariaHTML() {
        return `
          <ul>
            <li>Nombre del Circuito: ${this.nombreCircuito}</li>
            <li>Población: ${this.poblacion} habitantes</li>
            <li>Forma de Gobierno: ${this.gobierno}</li>
            <li>Región Mayoritaria: ${this.regionMayoritaria}</li>
          </ul>
        `;
      }
    
    escribirCoordenadasMeta() {
        document.write(`
        <p>
            Latitud: ${this.coordenadasMeta.latitud}, Longitud: ${this.coordenadasMeta.longitud}, Altura: ${this.coordenadasMeta.altura}
        </p>
        `);
        
    }

    escribirInfromacion(){
        document.write("Pais. " + this.getNombre());
        document.write("Capital: " + this.getCapital());
        document.write(this.getInfoSecundariaHTML());
        this.escribirCoordenadasMeta();
    }
}

var p = new Pais("Estados Unidos","Washington DC",334914895,"República federal democrática","América del Norte");
p.asignaDatosCircuito("Circuito de las Américas",-97.63984493885772,30.13187637998579 ,155);
p.escribirInfromacion();

 