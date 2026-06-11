# ByteGame
ByteGame is a Python game supporting both two-player gameplay and single-player mode against an AI-controlled opponent.

## Features
- Socket-based communication
- Message encryption using the Bifid cipher
- Implementation of the RC6 symmetric encryption algorithm
- OFB (Output Feedback) mode for secure data transmission
- File transfer between clients
- Encryption of transferred files using the implemented cryptographic algorithms
- File integrity verification using the SHA-1 hashing algorithm

## Technologies Used
- Python

## How It Works
- Clients establish a connection through the server.
- Messages are encrypted before transmission.
- Encrypted data is sent through socket connections.
- The receiving client decrypts the data.
- For file transfers:
  - The file is converted into a byte array.
  - The byte array is encrypted.
  - The encrypted data is transmitted.
  - The receiver decrypts and reconstructs the file.
  - SHA-1 hashes are compared to verify file integrity.

## How To Run The Application
### 1. Clone the repository
```bash
git clone <repo-url>
cd your-project-folder
```
### 2. Install server dependencies
Go to the server directory and install required packages:

```bash
cd server
npm install
```
### 3. Start the server
```bash
npm start
```
The server will run on:
```bash
ws://localhost:3000
```
### 4. Run the client
Open the client folder and start `index.html`.

> **Recommended way:**  
> Use VS Code Live Server extension  
> Right click `index.html` → “Open with Live Server”

## Screenshots
### Initial State of the Application


### Active Chat (Messages Sent)



## Project Information
- Developed: 2023  
- Improved: 2026  
- Type: Academic Project

## Author
- Andjela Djordjevic
