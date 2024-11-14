import streamlit as st
import requests
import time

# Pares de criptomoedas que queremos monitorar
PAIRS = ["SUIUSDT", "BTCUSDT", "ETHUSDT", "UNIUSDT"]

# URL da API da Binance para consultar os preços dos pares
BASE_URL = "https://api.binance.com/api/v3/ticker/price"

st.title("Atualização de Preços - Binance")
st.write("Atualização a cada 10 segundos para os pares:", ", ".join(PAIRS))

# Função para obter preços da API da Binance
def fetch_prices():
    prices = {}
    try:
        for pair in PAIRS:
            response = requests.get(BASE_URL, params={"symbol": pair})
            response.raise_for_status()
            data = response.json()
            prices[pair] = data['price']
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao obter dados da API da Binance: {e}")
    return prices

# Loop de atualização automática
while True:
    prices = fetch_prices()
    st.subheader("Preços Atualizados")
    for pair, price in prices.items():
        st.write(f"{pair}: {price} USDT")
    time.sleep(10)  # Pausa de 10 segundos antes de atualizar novamente
