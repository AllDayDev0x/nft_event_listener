# BAYC NFT Transfer Event Listener

## Overview

The BAYC NFT Transfer Event Listener is a Django application designed to listen for transfer events of the Bored Ape Yacht Club (BAYC) NFTs. This application captures and stores these events in a database for easy retrieval and analysis.

## Setup Instructions

Follow the steps below to set up and run the project locally:

```bash
cd nft_transfer_listener
```

## 1. Install Dependencies
Create a virtual environment (recommended) and install the necessary dependencies:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```
## 3. Configure Environment Variables
Set up your Infura project and the NFT contract address by creating a .env file in the events directory. Add the following lines:
```bash
INFURA_API_KEY=[Your Infura Key]
NFT_ADDRESS=0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2
```
Make sure to replace [Your Infura Key] with your actual Infura API key.

## 4. Run Migrations
Apply the necessary database migrations by running:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
## 5. Start Event Subscription
In a separate terminal, start the event subscription to listen for NFT transfer events:
```sh
python3 manage.py subscribe_to_events
```
## 6. Run the Development Server
Finally, run the Django development server:
```bash
python3 manage.py runserver
```