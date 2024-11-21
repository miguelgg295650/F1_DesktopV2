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
    getWeatherForecastAndRender(city, containerSelector) {

      const apiKey = "388ebd4309dbd39c0e616d14faa71388"; 
      const baseUrl = "https://api.openweathermap.org/data/2.5/forecast";
      const units = "metric";
      const lang = "es";
          const url = `${this.baseUrl}?q=${city}&units=${this.units}&lang=${this.lang}&mode=xml&appid=${this.apiKey}`;
  
          $.ajax({
              url: url,
              method: "GET",
              dataType: "xml",
              success: function (data) {
                  const container = $(containerSelector);
                  container.empty(); // Limpiar contenido previo
  
                  const forecasts = $(data).find("time");
                  for (let i = 0; i < 40; i += 8) { // Procesar datos cada 8 intervalos (24h)
                      const dayForecast = forecasts.eq(i);
                      const date = dayForecast.attr("from").split("T")[0];
                      const tempMin = dayForecast.find("temperature").attr("min");
                      const tempMax = dayForecast.find("temperature").attr("max");
                      const humidity = dayForecast.find("humidity").attr("value");
                      const weatherIcon = dayForecast.find("symbol").attr("var");
                      const rain = dayForecast.find("precipitation").attr("value") || "0";
  
                      // Crear artículo para el pronóstico
                      const article = `
                          <article class="weather-day">
                              <h2>${date}</h2>
                              <img src="https://openweathermap.org/img/wn/${weatherIcon}.png" alt="Icono del tiempo">
                              <p><strong>Temp. Máx:</strong> ${tempMax}°C</p>
                              <p><strong>Temp. Mín:</strong> ${tempMin}°C</p>
                              <p><strong>Humedad:</strong> ${humidity}%</p>
                              <p><strong>Lluvia:</strong> ${rain} mm</p>
                          </article>
                      `;
                      container.append(article);
                  }
              },
              error: function (xhr, status, error) {
                  console.error("Error al obtener el pronóstico:", error);
                  alert("No se pudo obtener el pronóstico del tiempo. Inténtalo más tarde.");
              },
          });
      }
  }

var p = new Pais("Estados Unidos","Washington DC",334914895,"República federal democrática","América del Norte");
p.asignaDatosCircuito("Circuito de las Américas",-97.63984493885772,30.13187637998579 ,155);
p.escribirInfromacion();
pais.getWeatherForecastAndRender("Austin", "section#forecast");

 