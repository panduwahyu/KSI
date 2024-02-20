<h1>Substitution</h1>
<h2>Enkripsi:</h2>
<p></p>
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
