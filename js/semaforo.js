class Semaforo {
  constructor() {
      this.levels = [0.2, 0.5, 0.8];
      this.lights = 4;
      this.unload_moment = null;
      this.clic_moment = null;
      this.difficulty = this.levels[Math.floor(Math.random() * this.levels.length)];

      // Crear la estructura del semáforo en el documento
      this.createStructure();
  }

  createStructure() {
      const main = document.querySelector('main');
      main.innerHTML = ''; // Limpia cualquier contenido existente en main

      // Crear luces del semáforo
      for (let i = 0; i < this.lights; i++) {
          const light = document.createElement('div');
          light.classList.add('light');
          main.appendChild(light);
      }

      // Crear botón de arranque
      const startButton = document.createElement('button');
      startButton.textContent = 'Arranque';
      startButton.onclick = () => this.initSequence(startButton);
      main.appendChild(startButton);

      // Crear botón de reacción
      const reactionButton = document.createElement('button');
      reactionButton.textContent = 'Reacción';
      reactionButton.disabled = true; // Deshabilitado inicialmente
      reactionButton.onclick = () => this.stopReaction(reactionButton, startButton);
      main.appendChild(reactionButton);

      const result = document.createElement('p');
      result.classList.add('result');
      main.appendChild(result);
  }

  initSequence(startButton) {
      const main = document.querySelector('main');
      const lights = main.querySelectorAll('.light');
      startButton.disabled = true; // Deshabilitar el botón de arranque

      // Encender luces con un intervalo
      lights.forEach((light, index) => {
          setTimeout(() => {
              light.style.backgroundColor = 'red';
          }, index * 500);
      });

      // Programar el apagado del semáforo
      setTimeout(() => {
          this.unload_moment = new Date();
          this.endSequence();
      }, 2000 + this.difficulty * 100);
  }

  endSequence() {
      const main = document.querySelector('main');
      const lights = main.querySelectorAll('.light');
      const reactionButton = main.querySelectorAll('button')[1]; // Segundo botón (Reacción)

      // Apagar las luces
      lights.forEach((light) => {
          light.style.backgroundColor = 'black';
      });

      // Habilitar el botón de reacción
      reactionButton.disabled = false;
  }

  stopReaction(reactionButton, startButton) {
      const main = document.querySelector('main');
      const lights = main.querySelectorAll('.light');

      // Obtener el momento de clic
      this.clic_moment = new Date();

      // Calcular el tiempo de reacción
      const reactionTime = ((this.clic_moment - this.unload_moment) / 1000).toFixed(3);

      const result = main.querySelector('.result');
      result.textContent = `Tu tiempo de reacción es: ${reactionTime} segundos`;
      
      // Restablecer las luces
      lights.forEach((light) => {
          light.style.backgroundColor = '';
      });

      // Habilitar el botón de arranque y deshabilitar el de reacción
      startButton.disabled = false;
      reactionButton.disabled = true;
  }
}

// Inicializar el semáforo cuando se carga el archivo
new Semaforo();
