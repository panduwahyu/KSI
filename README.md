<h1>Substitution</h1>
<h2>Perhitungan Kompleksitas Waktu</h2>
<h3>Enkripsi:</h3>
<ul>
    <li>Membuat dictionary (dict1) yang berisi mapping karakter asli ke karakter terenkripsi. Kompleksitas waktu: O(52), karena string.ascii_letters memiliki 52 karakter.</li>
    <li>Menggunakan loop for untuk membuat dictionary dict1. Kompleksitas waktu: O(52)</li>
    <li>Membaca input key dari pengguna. Kompleksitas waktu: O(1)</li>
    <li>Membaca input teks yang akan dienkripsi. Kompleksitas waktu: Bergantung pada panjang input teks, mari kita sebut n.</li>
    <li>Mengenkripsi setiap karakter dalam teks input. Iterasi melalui setiap karakter dalam teks input memiliki kompleksitas waktu O(n). Untuk setiap karakter, pencarian dalam all_letters memiliki kompleksitas waktu O(52). </li>
    <li>Menggabungkan teks terenkripsi menjadi satu string. Kompleksitas waktu O(m)</li>
</ul>
<p>Jadi, kompleksitas waktu keseluruhan dari program ini adalah O(52) + O(52) + O(1) + O(n) + O(n) + O(m).</p>

<h3>Deskrip:</h3>
<ul>
    <li>Membaca input teks yang akan didekripsi. Kompleksitas waktu: O(n).</li>
    <li>Membuat loop for untuk mencoba setiap kemungkinan kunci (dari 1 hingga 25). Kompleksitas waktu: O(25), yang dapat disederhanakan menjadi O(1) karena ini adalah jumlah iterasi yang tetap.</li>
    <li>Memanggil fungsi decrypt_txt() untuk setiap iterasi. Kompleksitas waktu untuk setiap pemanggilan: O(n), karena kita harus memproses setiap karakter dalam teks yang akan didekripsi.</li>
</ul>
<p>Jadi, kompleksitas waktu keseluruhan dari program ini adalah O(n) * O(1) = O(n), di mana n adalah panjang teks yang akan didekripsi.</p>

<h1>Transposition</h1>
<h2>Perhitungan Kompleksitas Waktu</h2>
<h3>Encrypt Messages</h3>
<ul>
    <li>Membaca input dan membuat variabel yang berkaitan dengan panjang pesan, panjang kunci, dan jumlah baris dan kolom dalam matriks. Kompleksitas waktu: O(1)</li>
    <li>Membuat matriks berdasarkan panjang pesan dan panjang kunci. Kompleksitas waktu: O(n), di mana n adalah panjang pesan</li>
    <li>Mengurutkan key (kunci). Kompleksitas waktu: O(k log k), di mana k adalah panjang key</li>
    <li>Melakukan iterasi melalui matriks untuk menghasilkan teks terenkripsi. Kompleksitas waktu: O(n), di mana n adalah panjang pesan</li>
</ul>
<p> Kompleksitas waktu keseluruhan dari encryptMessage adalah O(n + k log k)</p>
