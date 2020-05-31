grade = []
i = 0 
iterasi = True
from operator import itemgetter
print ("------------------------")
print ("-Seleksi Mahasiswa Baru-")
print ("Teknik Industri UNS 2021")
print ("------------------------")
print ("Kuota Mahasiswa Teknik Industri UNS 2021")
print ("\nSNMPTN : 5 orang \nSBMPTN : 10 orang \nUMPTN : 7 orang")
print ("Jalur Masuk, \nbila SNMPTN : 1 \nbila SBMPTN : 2 \nbila UMPTN : 3")
while iterasi :
    jm = input("Input Jalur Masuk : ")
    if jm == "1" :
        pt = {}
        pt["Jalur"] = ("SNMPTN")
        pt["Nama"] = input("Nama :")
        print ("Input Nilai Rata-rata Rapot Semester 3-5")
        fis = float(input("Input nilai Fisika :"))
        bio = float(input("Input nilai Biologi :"))
        kim = float(input("Input nilai Kimia:"))
        mat = float(input("Input nilai Matematika:"))
        bindo = float(input("Input nilai Bahasa Indonesia:"))
        bing = float(input("Input nilai Bahasa Inggris:"))
        pt["Nilai_Rapot"] = int(fis*0.2+kim*0.2+mat*0.2+bio*0.15+bing*0.15+bindo*0.1)
        print (pt)
        grade.append(pt)
        nextdata=input("Tambah data (y/n) ? : ")
        if nextdata != "y" :
            iterasi = False
    sorted_pt = sorted(pt, key=itemgetter("Nilai_Rapot"), reverse=True)
    print(sorted_pt)
    yo1 = 0
    while yo1 < len(sorted_pt):
        rank = sorted_pt[yo1]
        yo1 += 1 
        if yo1 > 5:
            ValueError
        print() 
        p1=print(f"Daftar Peserta SNMPTN ke-{yo1}:")
        p2=print("Nama:",rank["Nama"])
        p3=print("Nilai Rapot:",rank["Nilai_Rapot"])
    if jm == "2" :        
        pt = {}
        pt["Jalur"] = ("SBMPTN")
        pt["Nama"] = input("Nama :")
        print ("Input Nilai TPA dan TPS")
        print ("Bobot nilai : \nTPA : 60% \nTPS : 40%")
        tpa = int(input("Input Nilai TPA :"))
        tps = int(input("Input Nilai TPS :"))
        NA = int(tpa*0.6+tps*0.4)
        pt["NA"] = NA
        print (pt)
        grade.append(pt)
        nextdata=input("Tambah data (y/n) ? : ")
        if nextdata != "y" :
            iterasi = False        
    sorted_pt = sorted(pt, key=itemgetter("NA"), reverse=True)
    print(sorted_pt)
    yo2 = 0
    while yo1 < len(sorted_pt):
        rank = sorted_pt[yo2]
        yo2 += 1
        if yo2 > 10 :
            ValueError
        print() 
        p4=print(f"Daftar Peserta SBMPTN ke-{yo1}:")
        p5=print("Nama:",rank["Nama"])
        p6=print("Nilai Akhir:",rank["NA"])
else :
    pt = {}
    pt["Jalur"] = ("UMPTN")
    pt["Nama"] = input("Nama :")
    sbm=int(input("Input nilai SBMPTN:"))
    um=int(input("Input nilai UMPTN:"))
    NA =int(sbm*0.5+um*0.5)
    pt["Nilai Total"]= (NA)
    print(pt)
    grade.append(pt)
    nextdata=input("Tambah data (y/n) ? : ")
    if nextdata != "y" :
        iterasi = False
        sorted_pt = sorted(pt,key=itemgetter("Nilai Total"),reverse=True)
        print(sorted_pt)
        yo3 = 0
        while yo1 < len(sorted_pt):
            rank = sorted_pt[yo3]
            yo3 += 1
            if yo3 > 7 :
                ValueError
            print() 
            p7=print(f"Daftar Peserta UMPTN ke-{yo1}:")
            p8=print("Nama:",rank["Nama"])
            p9=print("Nilai Akhir:",rank["Nilai Akhir"]) 

print(p1,p4,p7)
print(p2,p5,p8)
print(p3,p6,p9) 
