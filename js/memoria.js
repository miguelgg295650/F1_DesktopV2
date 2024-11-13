class Memoria {
  constructor() {
    this.hasFlippedCard = false;
    this.lockBoard = false;
    this.firstCard = null;
    this.secondCard = null;

    this.cards= [
      { card: "RedBull", source: "https://upload.wikimedia.org/wikipedia/de/c/c4/Red_Bull_Racing_logo.svg" },
      { card: "McLaren", source: "https://upload.wikimedia.org/wikipedia/en/6/66/McLaren_Racing_logo.svg" },
      { card: "Alpine", source: "https://upload.wikimedia.org/wikipedia/fr/b/b7/Alpine_F1_Team_2021_Logo.svg" },
      { card: "AstonMartin", source: "https://upload.wikimedia.org/wikipedia/fr/7/72/Aston_Martin_Aramco_Cognizant_F1.svg" },
      { card: "Ferrari", source: "https://upload.wikimedia.org/wikipedia/de/c/c0/Scuderia_Ferrari_Logo.svg" },
      { card: "Mercedes", source: "https://upload.wikimedia.org/wikipedia/commons/f/fb/Mercedes_AMG_Petronas_F1_Logo.svg" },
      
      
      { card: "RedBull", source: "https://upload.wikimedia.org/wikipedia/de/c/c4/Red_Bull_Racing_logo.svg" },
      { card: "McLaren", source: "https://upload.wikimedia.org/wikipedia/en/6/66/McLaren_Racing_logo.svg" },
      { card: "Alpine", source: "https://upload.wikimedia.org/wikipedia/fr/b/b7/Alpine_F1_Team_2021_Logo.svg" },
      { card: "AstonMartin", source: "https://upload.wikimedia.org/wikipedia/fr/7/72/Aston_Martin_Aramco_Cognizant_F1.svg" },
      { card: "Ferrari", source: "https://upload.wikimedia.org/wikipedia/de/c/c0/Scuderia_Ferrari_Logo.svg" },
      { card: "Mercedes", source: "https://upload.wikimedia.org/wikipedia/commons/f/fb/Mercedes_AMG_Petronas_F1_Logo.svg" }
    ];
  }

  shuffleElements() {
    for (let i = this.cards.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [this.cards[i], this.cards[j]] = [this.cards[j], this.cards[i]];
    }
  }

  unflipCards() {
    this.lockBoard = true;
    setTimeout(() => {
      this.firstCard.flipped = false;
      this.secondCard.flipped = false;
      this.resetBoard();
    }, 1500); 
  }

 
  resetBoard() {
    [this.hasFlippedCard, this.lockBoard] = [false, false];
    [this.firstCard, this.secondCard] = [null, null];
  }

  
  checkForMatch() {
    this.firstCard.card === this.secondCard.card ? this.disableCards() : this.unflipCards();
  }

  disableCards() {
    this.firstCard.dataState = 'revealed';
    this.secondCard.dataState = 'revealed';
    this.resetBoard();
  }

  createElements() {
    const gameSection = document.querySelector('.memory-game');

    if (!gameSection) {
      console.error('El contenedor de la clase .memory-game no se encuentra en el DOM.');
      return;
    }

    this.cards.forEach(({ card, source }) => {
      const article = document.createElement('article');
      article.classList.add('memory-card');
      article.setAttribute('data-element', card);

      const header = document.createElement('h3');
      header.textContent = "Memory Card";
      article.appendChild(header);

      const img = document.createElement('img');
      img.src = source;
      img.alt = card;
      img.classList.add('card-image');
      img.style.display = 'none';
      article.appendChild(img);

      // Llamar a handleCardClick al hacer clic en el artículo
      article.addEventListener('click', () => {
        this.setAttribute('data-state', 'flip');
        
        setTimeout(() => {
          this.removeAttribute('data-state');
        }, 2500);
      });

      gameSection.appendChild(article);
    });
  }
}

var juegoMemoria = new Memoria();
juegoMemoria.createElements();

 


 