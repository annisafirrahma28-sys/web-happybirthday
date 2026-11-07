import streamlit as st

# Mengatur judul halaman web
st.set_page_config(page_title="Happy Birthday Tiara! 🎂", page_icon="🎉", layout="centered")

# Custom CSS untuk tampilan estetik dan ceria
st.markdown("""
    <style>
    .title-font { font-size:26px !important; font-weight: bold; color: #89CFF0; text-align: center; }
    .text-font { font-size:18px !important; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="title-font">🎉 DETEKTOR HARI SPESIAL SAHABAT v1.0 🎉</p>', unsafe_allow_index=True)

# Membuat session state untuk menyimpan memori klik web
if 'hitung' not in st.session_state:
    st.session_state.hitung = 0
if 'selesai' not in st.session_state:
    st.session_state.selesai = False

# Tampilan Utama (Sebelum target menyerah)
if not st.session_state.selesai:
    # GIF Kucing lucu ulang tahun
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYXZjdGFycWd4OGIxMTFxcGJ0MnAxZDZ2YzFuOWg2d29rNGdlcXZvbyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/uyfgCPQeCjYMVxt2m3/giphy.gif", width=250)
    st.markdown('<p class="text-font">Denger-denger hari ini ada yang makin tua nih... Kamu ulang tahun hari ini kan? 👀</p>', unsafe_allow_index=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Iya bener! 🎂✨", use_container_width=True):
            st.session_state.selesai = True
            st.rerun()
            
    with col2:
        if st.button("Nggak / Salah Orang 🤫", use_container_width=True):
            st.session_state.hitung += 1
            
    # Rentetan respon drama kalau dia tidak mau mengaku
    if st.session_state.hitung > 0:
        h = st.session_state.hitung
        if h == 1:
            st.warning("Masa sih salah? Jangan bohong ah, notifikasi kalenderku gak pernah salah! 🧐")
        elif h == 2:
            st.error("Mengelak terus nih... Bilang aja iya biar dapet selamat! 🥺")
        elif h == 3:
            st.error("Duh, kamu meragukan ingatan ku tentang km yh? 💔")
        elif h == 4:
            st.info("Tombol 'Nggak' ini sengaja aku pasang biar kamu capek ngeklik. Pencet yang iya kocak")
        else:
            st.warning("Gak mau tahu, pokoknya web ini bakal ngambek terus sampai kamu ngaku kalau kamu ulang tahun! 😤")

# Tampilan Akhir (Ketika dia klik "Iya bener!")
else:
    st.balloons() # Efek balon terbang meriah!
    st.snow()     # Efek salju/konfeti jatuh!
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYXZjdGFycWd4OGIxMTFxcGJ0MnAxZDZ2YzFuOWg2d29rNGdlcXZvbyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/TjSPQgowhhJdHgvnwA/giphy.gif", width=250)
    
    st.markdown('<p class="title-font">Happy Birthday, Bsf! 🥳🎈</p>', unsafe_allow_index=True)
    st.markdown("""
    <p class="text-font">
    Happy Birthday my dearest beloved best friend. 17 tahun astagaa, BUAT KTP WOY!! tapi gausah buru buru buat KTP nya sih,
    nanti kamu tersadar kalau kamu ini WNI wkekekekek. Wish you all the best yahh kekasih Furuya Rei!! OMG im lucky to meet you dah
    asli. Mungkin you lah alasan gw lahir ke bumi. pas dikasih 77 pertanyaan terselip pertanyaan ''Apakah kamu mau lahir ke bumi? disana ada Tiara''
    gw be like ''Lho ya boleh wong ditawari'' :vvVVvV SORRYY FREAK BGT YYHHHH wkekekek maaf <br><br>
    Satu pertanyaan terakhir... <b>Kapan nih kita bertemu humph?</b> Ditunggu undangannya! 🍕🍰✨
    </p>
    """, unsafe_allow_index=True)
    
    if st.button("Ulangi Kejutan 🔄"):
        st.session_state.hitung = 0
        st.session_state.selesai = False
        st.rerun()
