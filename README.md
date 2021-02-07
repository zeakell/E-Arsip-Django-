# EsisfoKH
aplikasi E-sisfo solusi untuk urusan surat-menyurat pada instansi pemerintahan. aplikasi ini  menggunakan django serta dalam menjalankan webaplikasi ini menggunakan docker.
yang mana supaya docker dapat berjalan penulis menggunakan sistem operasi linux sebgai sistem operasinya.
#DISCLAMMER APLIKASI WEB INI DILARANG UNTUK DI PERJUALBELIKAN HANYA UNTUK PEMBELAJARAN SEMATA DI LUAR ITU PENULIS DAN PEMBUAT APLIKASI INI TIDAK BERTANGGUNG JAWAB.!!!

#berikut ini adalah panduan untuk membangun / menjalankan web aplikasi ini

#INSTALL DOCKER ENGINE 
untuk dapat membuat docker, anda harus menginstall docker engine berikut ini adalah link video dari cara install docker engine pada ubuntu
-http://bit.ly/installdockerengine

#INSTALL DOCKER COMPOSE
bila sudah terinstall docker enginne selanjutnya adalah melakukan installasi docker compose
- sudo apt install docker-compose

#INSTALL PACKAGE DEPENDENCIES / PENDUKUNG 
untuk database
- sudo apt install mysql-server mysql-client
- sudo apt install python3-dev python3-pip libmysqlclient-dev

#BUKA TERMINAL DAN MASUK KE FOLDER PROYEK YANG SUDAH DI DOWNLOAD 
LALU KETIKKAN PERINTAH 
- sudo docker-compose up --build
#maksud code konfigurasi diatas adalah untuk dapat menghidupkan service docker compose serta membangun / menyatukan container yang sudah dibuat pada file docker-compose.yml dan Dockerfile pada proyek tersebut.
#yang biasa disebut dengan DOCKER IMAGES.
#VIDEO TUTOR ADA PADA LINK BERIKUT
-https://www.youtube.com/watch?v=wCbW6aTnF5Q
# RESTART DOCKER-COMPOSE
- sudo docker-compose down
- sudo docker-compose up
#MELIHAT DOCKER IMAGES YANG BERJALAN PADA DOCKER 
- sudo docker ps -a
- sudo docker volume ls
- sudo docker network ls
