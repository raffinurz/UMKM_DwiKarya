import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Dwikarya | Furniture",
    page_icon="🪑",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}
.stApp {
    margin: 0;
    padding: 0;
}
iframe {
    display: block;
    width: 100%;
    border: none;
}
</style>
""", unsafe_allow_html=True)

html = r"""<!DOCTYPE html>
<html lang="id" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Dwikarya | Furniture</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
  
  <style>
    body { font-family: 'Poppins', sans-serif; }

    /* Kelas untuk elemen sebelum animasi section */
    .section-animate {
      opacity: 0;
      transform: translateY(40px);
      transition: opacity 0.8s ease-out, transform 0.8s ease-out;
    }
    /* Kelas untuk elemen setelah animasi aktif */
    .section-animate.is-visible {
      opacity: 1;
      transform: translateY(0);
    }
    
    /* Kelas untuk mengaktifkan overlay transisi halaman */
    #page-transition-overlay.is-active {
      opacity: 1;
    }
  </style>
  
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-MVLSSKZHQY"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-MVLSSKZHQY');
  </script>
</head>
<body id="top" class="text-white">

    <div id="page-transition-overlay" class="fixed inset-0 bg-black bg-opacity-50 z-50 opacity-0 pointer-events-none transition-opacity duration-300"></div>

    <header class="sticky top-0 left-0 w-full z-30 px-6 md:px-12 py-4 flex justify-between items-center bg-black bg-opacity-60 backdrop-blur">
        <h1 class="text-white font-bold text-xl">DWIKARYA</h1>
        <nav class="hidden md:flex space-x-4 text-sm md:text-base">
             <a href="#produk" class="hover:underline">Produk</a>
             <a href="#tentang" class="hover:underline">Tentang Kami</a>
             <a href="#testimoni" class="hover:underline">Testimoni</a>
             <a href="#galeri" class="hover:underline">Galeri</a>
             <a href="#keuntungan" class="hover:underline">Keuntungan</a>
             <a href="#daftar" class="hover:underline">Daftar</a>
        </nav>
        <div class="md:hidden">
            <button id="hamburger-button" class="text-white focus:outline-none">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path></svg>
            </button>
        </div>
    </header>

    <nav id="mobile-menu" class="hidden md:hidden bg-black bg-opacity-80 backdrop-blur text-center py-4 absolute w-full z-20">
        <a href="#produk" class="block py-2 hover:underline">Produk</a>
        <a href="#tentang" class="block py-2 hover:underline">Tentang Kami</a>
        <a href="#testimoni" class="block py-2 hover:underline">Testimoni</a>
        <a href="#galeri" class="block py-2 hover:underline">Galeri</a>
        <a href="#keuntungan" class="block py-2 hover:underline">Keuntungan</a>
        <a href="#daftar" class="block py-2 hover:underline">Daftar</a>
    </nav>

  <section class="relative h-[650px] md:h-[700px] bg-cover bg-center flex items-center" style="background-image: url('https://www.woodleys.com/blog/wp-content/uploads/sites/105/2022/02/8-Living-Room-Furniture-Ideas-for-Your-New-Home.jpg');">
    <div class="absolute inset-0 bg-black bg-opacity-60"></div>
    <div class="relative z-10 max-w-7xl mx-auto flex flex-col justify-center px-6 md:px-12">
      <div class="w-full md:w-1/2">
        <h1 class="text-4xl md:text-5xl font-bold mb-4 leading-tight tracking-widest">DWIKARYA</h1>
        <p class="mb-6 text-lg">Pilihan terbaik untuk Furniture Anda — Desain modern, awet, dan GRATIS antar jemput.</p>
        <a href="https://wa.me/6283876788630" target="_blank" class="bg-white text-blue-600 font-semibold px-6 py-3 rounded-full hover:bg-gray-100 transition">PESAN DISINI</a>
      </div>
    </div>
    <div class="hidden md:block absolute right-6 md:right-20 bottom-16 z-20 w-[300px] bg-white text-gray-800 rounded-xl shadow-xl overflow-hidden">
      <div class="p-4 border-b text-sm font-bold text-center bg-gray-100">LAYANAN UNGGULAN</div>
      <img src="https://media.dekoruma.com/catalogue/GRV-432954.jpg?dpr=1&fit=bounds&height=1000&optimize=high&quality=60&trim-color=ffffff&width=1000" alt="lemari" class="w-full h-48 object-cover" />
      <div class="p-4 text-center">
        <h3 class="text-lg font-bold mb-1">Furniture Modern</h3>
        <p class="text-sm">Cocok untuk ruang yg bergaya modern dan tetap elegan.</p>
      </div>
    </div>
    <div class="absolute bottom-6 left-6 text-xs md:text-sm z-20">
        <p class="font-semibold">CONTACT US</p>
        <p>DWIKARYA<br>
        <a href="https://www.google.com/maps/place/Jl.+Imogiri+Barat+Km+12,+Denokan,+Trimulyo,+Jetis,+Bantul,+Yogyakarta" target="_blank" class="underline hover:text-blue-300">
            Jl. Imogiri Barat Km 12, Denokan, Trimulyo, Jetis, Bantul, Yogyakarta
        </a><br>
        www.dwikarya.id
        </p>
    </div>
    <div class="absolute bottom-6 right-6 text-sm z-20 flex items-center gap-2">
      <img src="https://img.icons8.com/ios-glyphs/30/ffffff/instagram-new.png" class="w-5 h-5" />
      <p>@dwikarya</p>
    </div>
    <div class="absolute bottom-0 w-full text-center text-xs text-white pb-2 z-20">
      © 2025 DWIKARYA
    </div>
  </section>
  
  <section id="tentang" class="bg-white text-gray-800 py-16 px-6 md:px-12 text-center section-animate">
    <h2 class="text-3xl font-bold mb-6">Tentang Kami</h2>
    <p class="max-w-3xl mx-auto text-lg">
    DWIKARYA adalah produsen dan penyedia furniture modern yang berkomitmen menghadirkan kualitas, keindahan, dan kenyamanan dalam setiap produk. Berdiri sejak 2015, kami telah melayani ribuan pelanggan dari berbagai daerah. Dengan konsep desain minimalis, kami percaya bahwa furniture bukan hanya pelengkap ruang — tetapi bagian dari gaya hidup Anda.
    </p>
  </section>

  <section id="produk" class="bg-gray-100 text-gray-800 py-16 px-6 md:px-12 section-animate">
     <div class="max-w-6xl mx-auto">
      <h2 class="text-3xl font-bold mb-10 text-center">Produk Terkini Kami</h2>
      <div class="flex flex-wrap justify-center gap-6">
        <div class="w-full max-w-xs sm:w-[250px] bg-white rounded-xl shadow-xl overflow-hidden">
          <div class="p-4 border-b text-sm font-bold text-center bg-gray-100">PRODUK</div>
          <img src="https://events.rumah123.com/wp-content/uploads/sites/38/2022/11/03161311/Furniture-Minimalis-Ruang-Tamu-Kayu-Rotan-1024x682.jpg" alt="kursi" class="w-full h-48 object-cover" />
          <div class="p-4 text-center">
            <h3 class="text-lg font-bold mb-1">Kursi Modern</h3>
            <h3 class="text-lg font-bold mb-1"> ★ 8/10</h3>
            <p class="text-sm"><s>Rp. 500.000</s></p>
            <p class="text-sm font-bold">Rp. 250.000</p>
          </div>
        </div>
        <div class="w-full max-w-xs sm:w-[250px] bg-white rounded-xl shadow-xl overflow-hidden">
          <div class="p-4 border-b text-sm font-bold text-center bg-gray-100">PRODUK</div>
          <img src="https://cdn.scgcbm.id/wp-content/uploads/2023/07/image-22-1024x723.png" alt="lemari" class="w-full h-48 object-cover" />
          <div class="p-4 text-center">
            <h3 class="text-lg font-bold mb-1">Lemari Modern</h3>
            <h3 class="text-lg font-bold mb-1"> ★ 9/10</h3>
            <p class="text-sm"><s>Rp. 2.700.000</s></p>
            <p class="text-sm font-bold">Rp. 1.620.000</p>
          </div>
        </div>
        <div class="w-full max-w-xs sm:w-[250px] bg-white rounded-xl shadow-xl overflow-hidden">
          <div class="p-4 border-b text-sm font-bold text-center bg-gray-100">PRODUK</div>
          <img src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/x/photo/2025/01/17/715790494.jpg" alt="meja" class="w-full h-48 object-cover" />
          <div class="p-4 text-center">
            <h3 class="text-lg font-bold mb-1">Meja Modern</h3>
            <h3 class="text-lg font-bold mb-1"> ★ 8.5/10</h3>
            <p class="text-sm"><s>Rp. 1.500.000</s></p>
            <p class="text-sm font-bold">Rp. 1.050.000</p>
          </div>
        </div>
        <div class="w-full max-w-xs sm:w-[250px] bg-white rounded-xl shadow-xl overflow-hidden">
            <div class="p-4 border-b text-sm font-bold text-center bg-gray-100">PRODUK</div>
            <img src="https://hogfurniture.co/cdn/shop/articles/Home_collection.png?v=1657288179&width=900" alt="sofa" class="w-full h-48 object-cover" />
            <div class="p-4 text-center">
              <h3 class="text-lg font-bold mb-1">Sofa Modern</h3>
              <h3 class="text-lg font-bold mb-1"> ★ 10/10</h3>
              <p class="text-sm"><s>Rp. 2.100.000</s></p>
              <p class="text-sm font-bold">Rp. 1.260.000</p>
            </div>
          </div>
        <div class="w-full max-w-xs sm:w-[250px] bg-white rounded-xl shadow-xl overflow-hidden">
            <div class="p-4 border-b text-sm font-bold text-center bg-gray-100">PRODUK UNGGULAN</div>
            <img src="https://blog.atome.id/wp-content/uploads/2022/03/9-rekomendasi-furniture-stores-atau-toko-furnitur-terbaik.jpg" alt="set lengkap" class="w-full h-48 object-cover" />
            <div class="p-4 text-center">
              <h3 class="text-lg font-bold mb-1">Set Lengkap Modern</h3>
              <h3 class="text-lg font-bold mb-1"> ★ 10/10</h3>
              <p class="text-sm"><s>Rp. 6.250.000</s></p>
              <p class="text-sm font-bold">Rp. 3.750.000</p>
            </div>
          </div>
      </div>
    </div>
  </section>

  <section id="testimoni" class="bg-white text-gray-800 py-16 px-6 md:px-12 section-animate">
     <div class="max-w-6xl mx-auto text-center">
        <h2 class="text-3xl font-bold mb-10">Apa Kata Mereka Tentang DWIKARYA</h2>
        <div class="flex flex-wrap justify-center gap-8">
            <div class="w-full md:w-1/3 lg:w-1/4 bg-gray-50 p-6 rounded-xl shadow-lg flex flex-col items-center">
                <img src="https://i.pravatar.cc/150?img=1" alt="Pelanggan 1" class="w-20 h-20 rounded-full mb-4 object-cover">
                <p class="text-gray-600 italic mb-4">"Pelayanannya ramah banget dan pengirimannya super cepat. Kualitas furniture-nya juga nggak main-main, kokoh dan desainnya modern. Sangat puas!"</p>
                <div class="text-yellow-500 mb-2">★★★★★</div>
                <h4 class="font-bold text-lg">Andi Cobra</h4>
                <p class="text-sm text-gray-500">Gunungkidul</p>
            </div>
            <div class="w-full md:w-1/3 lg:w-1/4 bg-gray-50 p-6 rounded-xl shadow-lg flex flex-col items-center">
                <img src="https://i.pravatar.cc/150?img=5" alt="Pelanggan 2" class="w-20 h-20 rounded-full mb-4 object-cover">
                <p class="text-gray-600 italic mb-4">"Awalnya ragu beli furniture online, tapi Dwikarya membuktikan kualitasnya. Timnya responsif dan pesanan saya sampai dengan aman. Gratis ongkirnya sangat membantu!"</p>
                <div class="text-yellow-500 mb-2">★★★★★</div>
                <h4 class="font-bold text-lg">Kkajhe</h4>
                <p class="text-sm text-gray-500">Klaten</p>
            </div>
            <div class="w-full md:w-1/3 lg:w-1/4 bg-gray-50 p-6 rounded-xl shadow-lg flex flex-col items-center">
                <img src="https://i.pravatar.cc/150?img=8" alt="Pelanggan 3" class="w-20 h-20 rounded-full mb-4 object-cover">
                <p class="text-gray-600 italic mb-4">"Desain set lengkapnya pas banget buat apartemen baru saya. Harganya juga worth it dengan diskon yang diberikan. Pasti bakal rekomendasiin ke teman-teman."</p>
                <div class="text-yellow-500 mb-2">★★★★☆</div>
                <h4 class="font-bold text-lg">Celloz</h4>
                <p class="text-sm text-gray-500">Yogyakarta</p>
            </div>
        </div>
    </div>
  </section>

  <section id="galeri" class="bg-gray-100 text-gray-800 py-20 px-6 md:px-12 section-animate">
      <div class="max-w-7xl mx-auto text-center">
        <h2 class="text-3xl md:text-4xl font-bold mb-4 relative inline-block px-4">
            Galeri Furniture
            <span class="absolute -bottom-2 left-1/2 -translate-x-1/2 w-1/2 h-1 bg-blue-600"></span>
        </h2>
        <p class="max-w-2xl mx-auto text-lg text-gray-600 mb-12 mt-6">
            Setiap furnitur adalah karya seni yang kami rancang dengan penuh dedikasi untuk Anda.
        </p>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-6">
            <div class="overflow-hidden rounded-lg shadow-lg">
                <img src="https://cdn.pixabay.com/photo/2019/03/31/17/21/chair-4093520_1280.jpg" alt="Galeri Kursi Modern" class="w-full h-full object-cover transition-transform duration-300 hover:scale-110">
            </div>
            <div class="overflow-hidden rounded-lg shadow-lg">
                <img src="https://cdn.pixabay.com/photo/2018/07/12/09/58/create-3532937_1280.jpg" alt="Galeri Dekorasi Ruangan" class="w-full h-full object-cover transition-transform duration-300 hover:scale-110">
            </div>
            <div class="overflow-hidden rounded-lg shadow-lg">
                <img src="https://cdn.pixabay.com/photo/2016/11/18/17/20/living-room-1835923_1280.jpg" alt="Galeri Ruang Tamu" class="w-full h-full object-cover transition-transform duration-300 hover:scale-110">
            </div>
            <div class="overflow-hidden rounded-lg shadow-lg">
                <img src="https://cdn.pixabay.com/photo/2019/04/30/08/08/wardrobe-4167975_1280.jpg" alt="Galeri Lemari Pakaian" class="w-full h-full object-cover transition-transform duration-300 hover:scale-110">
            </div>
            <div class="overflow-hidden rounded-lg shadow-lg">
                <img src="https://images.pexels.com/photos/276583/pexels-photo-276583.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" alt="Galeri Sofa Nyaman" class="w-full h-full object-cover transition-transform duration-300 hover:scale-110">
            </div>
            <div class="overflow-hidden rounded-lg shadow-lg">
                <img src="https://images.pexels.com/photos/1571460/pexels-photo-1571460.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" alt="Galeri Desain Interior" class="w-full h-full object-cover transition-transform duration-300 hover:scale-110">
            </div>
            <div class="overflow-hidden rounded-lg shadow-lg">
                <img src="https://images.pexels.com/photos/37347/office-sitting-room-executive-sitting.jpg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" alt="Galeri Meja Kerja" class="w-full h-full object-cover transition-transform duration-300 hover:scale-110">
            </div>
            <div class="overflow-hidden rounded-lg shadow-lg">
                <img src="https://images.pexels.com/photos/2082092/pexels-photo-2082092.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" alt="Galeri Rak Buku" class="w-full h-full object-cover transition-transform duration-300 hover:scale-110">
            </div>
        </div>
    </div>
  </section>

  <section id="keuntungan" class="bg-white text-gray-800 py-16 px-6 md:px-12 text-center section-animate">
     <div class="max-w-6xl mx-auto">
        <h2 class="text-3xl font-bold mb-4">Keuntungan Menjadi Mitra DWIKARYA</h2>
        <p class="max-w-3xl mx-auto text-lg mb-12">
            Kami membuka kesempatan bagi Anda yang ingin menjadi bagian dari perjalanan kami. Mitra DWIKARYA akan mendapatkan dukungan, pelatihan, dan peluang usaha yang menguntungkan.
        </p>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="p-6 bg-gray-100 rounded-lg shadow-lg transform hover:-translate-y-2 transition-transform">
                <h3 class="text-xl font-semibold mb-2">Tanpa Modal Besar</h3>
                <p class="text-sm">Mulai usaha furniture tanpa harus stok barang sendiri.</p>
            </div>
            <div class="p-6 bg-gray-100 rounded-lg shadow-lg transform hover:-translate-y-2 transition-transform">
                <h3 class="text-xl font-semibold mb-2">Dukungan Penuh</h3>
                <p class="text-sm">Kami menyediakan katalog, materi promosi, dan support marketing.</p>
            </div>
            <div class="p-6 bg-gray-100 rounded-lg shadow-lg transform hover:-translate-y-2 transition-transform">
                <h3 class="text-xl font-semibold mb-2">Keuntungan Menarik</h3>
                <p class="text-sm">Setiap transaksi mitra akan mendapatkan komisi langsung.</p>
            </div>
        </div>
    </div>
  </section>

  <section id="daftar" class="bg-gray-800 text-white py-20 px-6 md:px-12 section-animate">
       <div class="max-w-md mx-auto text-center">
        <h2 class="text-3xl font-bold mb-4">Tertarik Bergabung?</h2>
        <p class="text-gray-300 mb-10">Daftarkan diri Anda melalui formulir di bawah ini dan tim kami akan segera menghubungi Anda.</p>
        <div class="bg-white p-8 rounded-xl shadow-lg text-gray-800">
            <h3 class="text-2xl font-semibold mb-6 text-center">Formulir Pendaftaran Mitra</h3>
            <form action="https://wa.me/6283876788630" method="get" target="_blank">
                <div class="mb-4">
                    <label class="block text-gray-700 mb-2 text-left" for="store-name">Nama Store</label>
                    <input type="text" id="store-name" name="store" required class="w-full px-4 py-2 border rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
                </div>
                <div class="mb-4">
                    <label class="block text-gray-700 mb-2 text-left" for="email">Email</label>
                    <input type="email" id="email" name="email" required class="w-full px-4 py-2 border rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
                </div>
                <div class="mb-6">
                    <label class="block text-gray-700 mb-2 text-left" for="phone">No Telepon</label>
                    <input type="tel" id="phone" name="phone" required class="w-full px-4 py-2 border rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
                </div>
                <button type="submit" class="w-full bg-blue-600 text-white font-semibold px-6 py-3 rounded-full shadow-md hover:bg-blue-700 transition">
                    Daftar Menjadi Mitra
                </button>
            </form>
        </div>
    </div>
  </section>

  <footer class="bg-gray-900 text-gray-300 pt-16 pb-8 px-6 md:px-12 section-animate">
        <div class="max-w-7xl mx-auto">
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 mb-12">
                <div>
                    <h3 class="font-bold text-white text-xl mb-4">DWIKARYA</h3>
                    <p class="text-sm leading-relaxed">Menghadirkan kualitas, keindahan, dan kenyamanan dalam setiap produk untuk momen spesial di rumah Anda.</p>
                    <div class="flex space-x-4 mt-5">
                        <a href="#" aria-label="Facebook" class="hover:text-white"><svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v2.385z"></path></svg></a>
                        <a href="#" aria-label="Instagram" class="hover:text-white"><svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.85s-.011 3.584-.069 4.85c-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07s-3.584-.012-4.85-.07c-3.252-.148-4.771-1.691-4.919-4.919-.058-1.265-.069-1.645-.069-4.85s.011-3.584.069-4.85c.149-3.225 1.664-4.771 4.919-4.919 1.266-.057 1.644-.069 4.85-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948s.014 3.667.072 4.947c.2 4.359 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072s3.667-.014 4.947-.072c4.359-.2 6.78-2.618 6.98-6.98.058-1.281.072-1.689.072-4.948s-.014-3.667-.072-4.947c-.2-4.359-2.618-6.78-6.98-6.98-1.281-.059-1.689-.073-4.948-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.162 6.162 6.162 6.162-2.759 6.162-6.162-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4s1.791-4 4-4 4 1.79 4 4-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44 1.441-.645 1.441-1.44-.645-1.44-1.441-1.44z"></path></svg></a>
                        <a href="#" aria-label="Twitter" class="hover:text-white"><svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616v.064c0 2.299 1.634 4.218 3.803 4.661-.62.167-1.282.226-1.961.226-.305 0-.6-.03-1.175-.114.632 1.956 2.448 3.379 4.604 3.417-1.77 1.39-3.995 2.226-6.417 2.226-.42 0-.835-.025-1.243-.073 2.289 1.474 5.043 2.333 8.016 2.333 9.491 0 14.681-7.868 14.681-14.681 0-.224-.005-.447-.015-.669.998-.724 1.864-1.635 2.559-2.659z"></path></svg></a>
                    </div>
                </div>
                <div>
                    <h3 class="font-bold text-white text-lg mb-4">Navigasi</h3>
                    <ul class="space-y-3 text-sm">
                        <li><a href="#top" class="hover:text-white">Beranda</a></li>
                        <li><a href="#tentang" class="hover:text-white">Tentang Kami</a></li>
                        <li><a href="#produk" class="hover:text-white">Produk</a></li>
                        <li><a href="#testimoni" class="hover:text-white">Testimoni</a></li>
                         <li><a href="#galeri" class="hover:text-white">Galeri</a></li>
                        <li><a href="#keuntungan" class="hover:text-white">Daftar Mitra</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="font-bold text-white text-lg mb-4">Kontak</h3>
                    <address class="not-italic space-y-3 text-sm">
                        <p>Jl. Imogiri Barat Km 12, Denokan, Trimulyo, Jetis, Bantul, Yogyakarta</p>
                        <p><a href="tel:+6283876788630" class="hover:text-white">+62 838 7678 8630</a></p>
                        <p><a href="mailto:info@dwikarya.id" class="hover:text-white">info@dwikarya.id</a></p>
                    </address>
                </div>
                <div>
                    <h3 class="font-bold text-white text-lg mb-4">Jam Buka</h3>
                    <div class="space-y-3 text-sm">
                        <p>Senin - Jumat : 08:00 - 20:00</p>
                        <p>Sabtu : 09:00 - 17:00</p>
                        <p>Minggu & Hari Libur : Tutup</p>
                    </div>
                </div>
            </div>
            <div class="border-t border-gray-700 pt-8 text-center text-sm">
                <p class="italic mb-4">"Bukan sekadar furnitur, tapi awal dari cerita di rumah Anda."</p>
                <p>© 2025 DWIKARYA. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <button id="scroll-to-top-button" class="hidden fixed bottom-24 right-6 z-50 bg-gray-600 text-white p-3 rounded-full shadow-lg transition-opacity hover:bg-gray-700 focus:outline-none">
        <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M5 15l7-7 7 7" />
        </svg>
    </button>
    <div id="whatsapp-chat-widget" class="fixed bottom-6 right-6 z-50">
        <button id="wa-icon-button" class="bg-green-500 text-white p-4 rounded-full shadow-xl transition-transform hover:scale-110 focus:outline-none">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" fill="currentColor" viewBox="0 0 16 16">
                <path d="M13.601 2.326A7.85 7.85 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.9 7.9 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.9 7.9 0 0 0 13.6 2.326zM7.994 14.521a6.6 6.6 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.56 6.56 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592m3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.73.73 0 0 0-.529.247c-.182.198-.691.677-.691 1.654s.71 1.916.81 2.049c.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943s-.182-.133-.38-.232z"/>
            </svg>
        </button>
        <div id="wa-chat-box" class="hidden w-80 bg-white rounded-lg shadow-xl transition-all duration-300 transform scale-95 opacity-0">
            <header class="bg-green-500 text-white flex items-center justify-between p-3 rounded-t-lg">
                <div class="flex items-center gap-3">
                    <svg xmlns="http://www.w3.org/2000/svg" class="w-7 h-7" fill="currentColor" viewBox="0 0 16 16">
                        <path d="M13.601 2.326A7.85 7.85 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.9 7.9 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.9 7.9 0 0 0 13.6 2.326zM7.994 14.521a6.6 6.6 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.56 6.56 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592z"/>
                    </svg>
                    <h3 class="font-semibold text-lg">WhatsApp</h3>
                </div>
                <button id="wa-close-button" class="focus:outline-none hover:opacity-80">
                    <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>
            </header>
            <main class="p-4 bg-gray-50 text-gray-800 space-y-3">
                <div class="max-w-max bg-gray-200 p-3 rounded-lg rounded-bl-none">
                    <p class="text-sm">Hi 👋, welcome to <strong>DWIKARYA</strong></p>
                </div>
                <div class="max-w-max bg-gray-200 p-3 rounded-lg rounded-bl-none">
                    <p class="text-sm">Can we help you?</p>
                </div>
            </main>
            <footer class="p-4 bg-white rounded-b-lg">
                <a href="https://wa.me/6283876788630" 
                   target="_blank" 
                   rel="noopener noreferrer"
                   class="flex items-center justify-center gap-3 w-full bg-green-500 text-white font-semibold p-3 rounded-lg shadow-md hover:bg-green-600 transition-colors">
                   <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="currentColor" viewBox="0 0 16 16"><path d="M8.051 1.999h.089c.822.003 1.542.57 1.834 1.386l.002.002.001.002h.002c.03.076.054.155.07.236.053.27.06.553.037.833a.9.9 0 0 1-.229.479l-.002.002-3.33 3.33a.9.9 0 0 1-.48.253.9.9 0 0 1-.48-.253l-1.39-1.39a.9.9 0 0 1-.253-.48.9.9 0 0 1 .253-.48l3.33-3.33a.9.9 0 0 1 .479-.229c.28-.023.564-.016.833.037.081.016.16.04.236.07h.002s.001 0 .002.001l.002.002c.816.292 1.386.99 1.386 1.834v.09c0 .822-.57 1.542-1.386 1.834l-.002.002-.001.002h-.002a1.8 1.8 0 0 1-.236.07c-.27.053-.553.06-.833.037a.9.9 0 0 1-.479-.229l-.002-.002-3.33-3.33a.9.9 0 0 1-.253-.48.9.9 0 0 1 .253-.48l1.39-1.39a.9.9 0 0 1 .48-.253c.16-.027.324-.037.488-.037z"/></svg>
                    Open Chat
                </a>
            </footer>
        </div>
    </div>

<script>
    // Script untuk Hamburger Menu, Widget, Scroll, Animasi, dan Transisi Halaman

    // Elemen DOM
    const hamburgerButton = document.getElementById('hamburger-button');
    const mobileMenu = document.getElementById('mobile-menu');
    const waIconButton = document.getElementById('wa-icon-button');
    const waChatBox = document.getElementById('wa-chat-box');
    const waCloseButton = document.getElementById('wa-close-button');
    const scrollToTopButton = document.getElementById('scroll-to-top-button');
    const animatedSections = document.querySelectorAll('.section-animate');
    const transitionOverlay = document.getElementById('page-transition-overlay');
    const navLinks = document.querySelectorAll('nav a[href^="#"]');

    // Fungsi untuk Hamburger Menu
    hamburgerButton.addEventListener('click', () => mobileMenu.classList.toggle('hidden'));

    // Fungsi untuk Widget WhatsApp
    waIconButton.addEventListener('click', () => {
        waIconButton.classList.add('opacity-0', 'scale-95', 'pointer-events-none');
        waChatBox.classList.remove('hidden');
        setTimeout(() => waChatBox.classList.remove('opacity-0', 'scale-95'), 10);
    });
    waCloseButton.addEventListener('click', () => {
        waChatBox.classList.add('opacity-0', 'scale-95');
        setTimeout(() => {
            waChatBox.classList.add('hidden');
            waIconButton.classList.remove('opacity-0', 'scale-95', 'pointer-events-none');
        }, 300);
    });

    // Fungsi untuk Tombol Scroll to Top
    window.addEventListener('scroll', () => {
        if (window.scrollY > 400) {
            scrollToTopButton.classList.remove('hidden');
        } else {
            scrollToTopButton.classList.add('hidden');
        }
    });
    scrollToTopButton.addEventListener('click', () => {
        // Gunakan fungsi transisi halaman jika tersedia, jika tidak, scroll biasa
        handlePageTransition('#top');
    });

    // Fungsi untuk Animasi Section saat Scroll
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });
    animatedSections.forEach(section => observer.observe(section));
    
    // Fungsi untuk Transisi Halaman
    const handlePageTransition = (targetId) => {
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            transitionOverlay.classList.add('is-active');
            setTimeout(() => {
                targetElement.scrollIntoView({ behavior: 'smooth' });
                transitionOverlay.classList.remove('is-active');
                mobileMenu.classList.add('hidden');
            }, 300);
        }
    };

    // Terapkan fungsi transisi pada semua link navigasi
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            handlePageTransition(targetId);
        });
    });
</script>

</body>
</html>
"""

components.html(
    html,
    height=7500,
    scrolling=True,
)