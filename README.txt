Blockchain-Based PKI System (CLI)

Objective
---------
This project implements a menu-driven, command-line Public Key Infrastructure (PKI) system using a local Ethereum blockchain (Ganache) to securely manage the issuance, verification, and revocation of digital certificates. It removes the need for a centralized Certificate Authority using blockchain’s immutability and RSA cryptography.

Features
--------
- RSA-based certificate generation
- Digital signature creation
- Certificate issuance with expiry
- Certificate revocation
- Certificate verification with expiry and revocation checks
- Local blockchain backend using Ganache
- Menu-driven CLI (no Flask, no React/UI)

Folder Structure
----------------
pki_blockchain_cli/
├── CertificateRegistry.sol       # Solidity smart contract
├── cert_generator.py             # RSA key generation and signing
├── blockchain_interface.py       # Smart contract interaction (Web3)
├── deploy_contract.py            # Deploys smart contract to Ganache
├── menu.py                       # Menu-driven CLI
├── compiled_contract.json        # Generated after deployment
├── requirements.txt              # Python dependencies
├── README.txt                    # Instructions
└── certs/                        # Stores user certificates and keys

Installation Guide (Windows)
----------------------------

1. Install Python
   - Download Python 3.9+ from: https://www.python.org/downloads/windows/
   - During installation, check the box that says “Add Python to PATH”
   - Verify installation:
     python --version

2. Install Node.js & npm
   - Download from: https://nodejs.org
   - Choose the LTS version for better stability.
   - Verify installation:
     node -v
     npm -v

3. Install Ganache CLI
   - Open Command Prompt or PowerShell and run:
     npm install -g ganache
   - To run Ganache CLI:
     ganache

4. Install Python Dependencies
   - Navigate to the project folder:
     cd pki_blockchain_cli
   - Run:
     pip install -r requirements.txt

Running the Project
-------------------

Step 1: Start Ganache
   ganache

Step 2: Deploy the Smart Contract
   python deploy_contract.py

Step 3: Start the PKI System (Menu)
   python menu.py

You’ll see the following menu:

=== Blockchain PKI System ===
1. Generate Certificate
2. Issue Certificate
3. Verify Certificate
4. Revoke Certificate
5. Exit

Example Workflow
----------------
1. Generate Certificate: RSA keygen, sign data, save cert
2. Issue Certificate: Save hash and expiry on blockchain
3. Verify Certificate: Check hash, revocation and expiry
4. Revoke Certificate: Set cert as revoked on blockchain

Notes
-----
- Works entirely locally (no real ETH or internet needed)
- Ganache provides test accounts with free ETH
- Private keys never leave your machine

Author

