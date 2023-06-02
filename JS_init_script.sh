#!/bin/bash

JUICE_SHOP_DIR="juice-shop"

# Sprawdzenie, czy folder "juice-shop" już istnieje
if [ -d "$JUICE_SHOP_DIR" ]; then
    echo "Folder 'juice-shop' już istnieje."
    echo "Uruchamianie OWASP Juice Shop..."
    cd $JUICE_SHOP_DIR
    npm start
    exit 0
fi

# Aktualizacja pakietów systemowych
sudo apt update
sudo apt upgrade -y

# Instalacja wymaganych zależności
sudo apt install -y curl gnupg2

# Importowanie klucza GPG dla repozytorium Node.js
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -

# Instalacja Node.js
sudo apt install -y nodejs

# Pobieranie kodu źródłowego OWASP Juice Shop
git clone https://github.com/bkimminich/juice-shop.git $JUICE_SHOP_DIR

# Przejście do katalogu z kodem źródłowym OWASP Juice Shop
cd $JUICE_SHOP_DIR

# Instalacja zależności Node.js
npm install

# Uruchomienie OWASP Juice Shop
npm start

