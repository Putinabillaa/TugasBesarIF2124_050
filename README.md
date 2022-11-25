# Parser Bahasa JavaScript (Node.js)
Tugas Besar IF2124 Teori Bahasa Formal dan Otomata

## Daftar Isi
* [Penjelasan Ringkas Program](#penjelasan-ringkas-program)
* [Cara Kompilasi Program](#cara-kompilasi-program)
* [Cara Menjalankan Program](#cara-menjalankan-program)
* [Pembagian Tugas](#pembagian-tugas)
* [Daftar Fitur](#daftar-fitur)
* [Status Pengerjaan](#status-pengerjaan)
* [Screenshot program](#screenshot-program)
* [Struktur Program](#struktur-program)
* [Kontributor](#kontribtor)


## Penjelasan Ringkas Program
BNMO

## Cara Kompilasi
1. Pastikan pada device sudah terinstall gcc compiler
2. Pada root directory jalankan command `sh compile.sh`
3. Jika berhasil dilakukan kompilasi akan muncul file `main.exe` pada root directory

## Cara Menjalankan Program
1. Pastikan sudah melakukan kompilasi pada program
2. Pada root directory jalankan command `./main`
3. Jika berhasil di run, akan muncul splash screen 

## Pembagian Tugas
| PIC                               	| JOBDESC                                                                                                                                                                                                                         	|
|-----------------------------------	|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| 13521050 Naufal Syifa Firdaus    	| Finite Automata Ekspresi<br> Laporan Bab 1, 2, 3, 4     	|
| 13521077 Husnia Munzayana       	| Pre-process<br>AFintie Automata Variabel, Bilangan, dan String<br> Laporan Bab 1, 2, 3, 4, 5     	|
| 13521088 Puti Nabilla Aidira     	| Grammar<br> CNF Converter <br> Laporan Bab 1, 2, 3     	|

## Daftar Fitur
1. Validasi Variabel dengan Finite Automata
2. Validasi Ekspresi dengan Finite Automata
3. Parsing program .js dengan konsep Context-Free Grammar

## Status Pengerjaan
* Seluruh fitur selesai dikerjakan. 

## Screenshot Program
![Javascript Parser Program](./program.jpg)

## Struktur Program
```bash
└───TubesAlstrukdat-K1C
    ├───doc
    │   └───
    ├───test
    │   ├───inputAcc1.js
    │   ├───inputAcc2.js
    │   ├───inputAcc3.js
    │   ├───inputReject1.js
    │   ├───inputReject2.js
    │   └───inputReject3.js
    ├───CFGDescription.txt
    ├───CNF.txt
    ├───main.py
    ├───globalVariable.py
    ├───validNumber.py 
    ├───validVariable.py 
    ├───expressionCheck.py
    ├───CNFconverter.py
    ├───CYK.py
    └───README.md
```
## Kontributor
1. Naufal Syifa Firdaus     13521050
2. Husnia Munzayana         13521077
3. Puti Nabilla Aidira      13521088


----------------------------------------------------------------------------------------------------------
# TugasBesarIF2124_050
## Tugas Besar IF2124 Teori Bahasa Formal dan Otomata Parser Bahasa JavaScript (Node.js)

GITHUB      : https://github.com/Putinabillaa/TugasBesarIF2124_050.git
<br>
LAPORAN     : https://docs.google.com/document/d/1HhXz45MD3ONAw3p7mACvJmtcekjKlBM2rQ5wuz785mI/edit?usp=sharing
<br>

SPESIFIKASI : https://docs.google.com/document/d/1JodthYhXxtxvxZXdkrC29XP6AzYEQSi7ll9z_fTseA0/edit?usp=sharing
<br>
QnA         : https://docs.google.com/spreadsheets/d/1wdoJPKM_Q4bYNAW7EXH1M5vGi5FSL18DvNo970oaWxQ/edit?usp=sharing
<br>
SUBMISI     : https://forms.gle/fVRxWGW9Km2ozHdq9
<br>

REFERENSI : <br>
Grammar           : https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference <br>

Tracking

CFG:
- [x] break
- [x] const 
- [x] case
- [x] catch
- [x] continue
- [x] default (apakah maksudnya default parameters??)
- [x] delete
- [x] else
- [ ] false
- [x] finally
- [x] for
- [x] function
- [x] if
- [x] let
- [ ] null
- [x] return
- [x] switch
- [x] throw
- [x] try
- [ ] true
- [x] var
- [x] while

FA:
- [x] Variable name
- [x] Function name
- [ ] Expression (operator precedence)

Lain-Lainnyaa:
- [ ] CFG TO CNF
- [ ] CNF TO DICT
- [ ] CYK (dan segala hal sampai selesai 😀)
