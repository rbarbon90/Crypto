import streamlit as st
import requests
import time

# Lista de pares que queremos monitorar
PAIRS = ["SUIUSDT", "BTCUSDT", "ETHUSDT", "UNIUSDT"]

# URL da API da Binance para obter os preços
BINANCE_API_URL = "https://api.binance.com/api/v3/ticker/price"

st.title("Atualização de Preços - Binance")
st.write("Atualização a cada 10 segundos")

# Função para buscar os preços dos pares
def fetch_prices():
    prices = {}
    for pair in PAIRS:
        try:
            response = requests.get(BINANCE_API_URL, params={"symbol": pair})
            response.raise_for_status()
            data = response.json()
            prices[pair] = data['price']
        except requests.exceptions.RequestException as e:
            st.error(f"Erro ao obter preço para {pair}: {e}")
    return prices

# Loop de atualização dos preços
while True:
    prices = fetch_prices()
    st.subheader("Preços Atualizados")
    for pair, price in prices.items():
        st.write(f"{pair}: {price} USDT")
    
    # Atualiza a cada 10 segundos
    time.sleep(10)
    st.experimental_rerun()
