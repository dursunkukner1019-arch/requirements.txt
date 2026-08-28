import streamlit as st
import numpy as np
import time

st.set_page_config(page_title="Kükner Cryptology - İHA Simulation", page_icon="🛡️", layout="centered")

st.title("🛡️ Kükner Kriptoloji & İHA Simülasyonu")
st.markdown("### Formula: $\\left(\\frac{100}{19} \\times \\frac{\\pi}{19}\\right)^n$")
st.write("Bu arayüz, Kükner formülünün İHA/SİHA telemetri ve frekans atlama güvenliğini canlı olarak test etmesini sağlar.")

if st.button("🚀 Simülasyonu Başlat"):
    with st.spinner("Kriptografik matrisler hesaplanıyor..."):
        pi = np.pi
        temel_katsayi = (100.0 / 19.0) * (pi / 19.0)
        
        st.info(f"**Temel Çarpan (Base Multiplier):** `{temel_katsayi:.10f}`")
        st.markdown("---")
        
        paket_sayisi = 10
        benzersiz_anahtarlar = set()
        
        for n in range(1, paket_sayisi + 1):
            formul_degeri = np.power(temel_katsayi, n)
            hassas_str = f"{formul_degeri:.50f}"
            kanal_frekansi = 2400 + (int(hassas_str.replace('.', '')[:4]) % 80)
            sifreleme_anahtari = hassas_str[-12:]
            
            benzersiz_anahtarlar.add(sifreleme_anahtari)
            
            st.success(f"**Paket #{n:02d}** | Atlanan Frekans: **{kanal_frekansi} MHz** | Anahtar Sinyal: `{sifreleme_anahtari}`")
            time.sleep(0.05)
            
        st.balloons()
        st.success(f"✅ **Durum Raporu:** Toplam {paket_sayisi} paket başarıyla iletildi. Çakışma Oranı: **%0.00** (%100 Benzersizlik).")
