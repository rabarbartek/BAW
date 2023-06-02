#!/bin/bash

JUICE_SHOP_DIR="juice-shop"

# Check if the 'juice-shop' folder already exists
if [ -d "$JUICE_SHOP_DIR" ]; then
    echo "Folder 'juice-shop' already exists."
    echo "Running OWASP Juice Shop..."
    cd $JUICE_SHOP_DIR
    npm start
    exit 0
fi

# Function to display an error message and exit the script
error() {
    echo "Error: $1"
    exit 1
}

# Function to check the prerequisites before installation
check_requirements() {
    echo "Checking requirements..."
    
    # Check if git is installed
    if ! command -v git &> /dev/null; then
        error "Git is not installed. Please install it before proceeding."
    fi

    # Check if Node.js is installed
    if ! command -v node &> /dev/null; then
        error "Node.js is not installed. Please install it before proceeding."
    fi
}

# Function to install OWASP Juice Shop
install_juice_shop() {
    echo "Starting OWASP Juice Shop installation..."
    
    # Clone the OWASP Juice Shop source code
    git clone https://github.com/bkimminich/juice-shop.git $JUICE_SHOP_DIR || error "Failed to clone OWASP Juice Shop source code."
    
    # Navigate to the Juice Shop directory
    cd $JUICE_SHOP_DIR
    
    # Install Node.js dependencies
    npm install || error "Failed to install Node.js dependencies."
}

# Function to start OWASP Juice Shop
start_juice_shop() {
    echo "Starting OWASP Juice Shop..."
    
    # Start OWASP Juice Shop
    npm start || error "Failed to start OWASP Juice Shop."
}

# Main script
check_requirements
install_juice_shop
start_juice_shop
