# Web E-Sisfo by Kevin Harada
aplikasi E-sisfo solusi untuk urusan surat-menyurat pada instansi pemerintahan. aplikasi ini  menggunakan django serta dalam menjalankan webaplikasi ini menggunakan docker.
yang mana supaya docker dapat berjalan penulis menggunakan sistem operasi linux sebgai sistem operasinya.
#DISCLAMMER APLIKASI WEB INI DILARANG UNTUK DI PERJUALBELIKAN HANYA UNTUK PEMBELAJARAN SEMATA DI LUAR ITU PENULIS DAN PEMBUAT APLIKASI INI TIDAK BERTANGGUNG JAWAB.!!!


#berikut ini merupak penjelasan dari cara membuat dan menjelaskan skenario CI/CD dengan membuat simulasi deployment sebuah aplikasi ke suatu server dengan menggunakan Jenkins.
#alat dan bahan
- 1 Server Virtual (disini saya menggunakan virtual server lokal dengan sistem operasi ubuntu server 20.04)
- 1 web aplikasi yang ceritanya sedang di deploy yaitu bernama (E-sifo).
- software tunneling bernama (ngrok) untuk mengubah ip private(local) menjadi ip public (yang dapat diexpose oleh github)
- service jenkins, docker(sebagai media untuk tempat menaruh web app pada virtual server).

#berikut ini langkah langkah untuk mendeploy sebuah web aplikasi menggunakan jenkins service yang menerapkan konsep CI/CD untuk deploymen web aplikasi.
1. install service dependencies untuk jenkins yaitu OPENJDK11 karena jenkins ini merupakan software yg menggunakan bahasa pemograman java.
2. install terlebih dahulu service jenkins pada virtual server.
3. start service jenkinsnya
4. jalankan aplikasi ngrok untuk mentranslatekan ip address local kita menjadi ip address public.
5. lalu setelah terinstall step selanjutnya adalah mengkonfigurasi dari jenkins kita dengan membuka web browser dan copy paste domain yang sudah tertranslate menggunakan ngrok.
6. setelah itu nanti akan diminta untuk login akun jenkins kita bila baru pertama kali menggunakan jenkins nanti akan diminta untuk menginstall plugin untuk dapat menjalankan jenkins dengan semestinya.
7. lalu bila ingin mendeploy web aplikasi menggunakan jenkins kita pilih new item untuk membuat item web app mana yg ingin dikelola oleh jenkins.
8. lalu beri nama item kita sesuaikan dengan nama web app yg lagi dideploy.
9. dan setelah itu pilih menu configure untuk mengatur web applikasi yg dideploy supaya dapat singkron dengan github kita. tujuannya apabila didalam web aplikasi yang disimpan di repo githib terdapat pembaharuan data maka nanti server akan memperbaharuinya dengan automatis dengan service jenkins kita.
10. pada saat configure kita pilih credentials git untuk dapat singkron dengan repo github kita.
11. Disini saya menggunakan repositori bernama KevinHarada123 yang manan didalamnya ada web aplikasi yg sedang dideploy.
12. lalu konfigurasi pada repositori github kita dengan pergi ke setting lalu pilih webhooks dan pilih add webhooks lalu pilih event yang kita inginkan untuk dapat di intruksikan pada github dengan jenkins nantinya. 
13. bila sudah terkonfigurasi repo github kita selanjutnya adalah menjalankan item yang telah kita konfigurasi pada jenkins kita.
14. untuk menjalankan item pada jenkins yg telah kita configure pada step sebelumnya ialah dengan memilih menu build pada item di dashboard jenkins kita. nanti jenkins akan menjalankan perintah yg telah kita buat pada configure item jenkins kita tanpa harus kita konfigurasi manual yang berulang setiap ada pembahruan dari bagian developer dengan kita di server.
15. setelah build selesai dengan succes maka proses dari deploy pada jenkins kita telah berhasil dan selesai dengan benar.

Terimakasih

Kevin Harada
