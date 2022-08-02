from tabulate import tabulate as tbl

airfoil = input("Enter NACA: ")
print("PS: LES VALEUR EN % SANS EN POURCENTAGE DE LA CORDE")
if len(airfoil) == 4 :
    cambrureMax =  airfoil[0]
    pointCambrureMax = int(airfoil[1])*10
    eppesseurMax =airfoil[2]+airfoil[3]
    infos=[[cambrureMax,pointCambrureMax,eppesseurMax]]
    head=["Cambrure maximale (%)", "point de cambrure maximale/ la corde", "eppesseur maximal (%)"]
    print(tbl(infos, headers=head, tablefmt="grid"))

if len(airfoil)== 5:
    Cp = 0.15 * int(airfoil[0])
    pointCambrureMax = (int(airfoil[1])/20)*100
    if airfoil[2] == '0':
        cambrureType = 'cambrure simple'
    else:
        cambrureType = 'cambrure double'
    eppesseurMax =airfoil[3]+airfoil[4]
    infos=[[Cp,pointCambrureMax,cambrureType,eppesseurMax]]
    head=["Cofficient de portance(%)", "point de cambrure maximale/ la corde","Type de cambrure", "eppesseur maximal(%)"]
    print(tbl(infos, headers=head, tablefmt="grid"))

if len(airfoil) == 6 and airfoil[0] == '1':
    pressionMin = int(airfoil[1])*10
    Cp = int(airfoil[3])/10
    eppesseurMax =airfoil[4]+airfoil[5]
    infos=[[pressionMin,Cp,eppesseurMax]]
    head=["Pression minimale / la corde","Cofficient de portance(%)", "eppesseur maximal(%)"]
    print(tbl(infos, headers=head))

if len(airfoil) == 7 and airfoil[0] == '6':
    pressionMin = int(airfoil[1])*10
    CdFaible = int(airfoil[2])/10
    Cp = int(airfoil[4])/10
    eppesseurMax =airfoil[5]+airfoil[6]
    infos=[[pressionMin,CdFaible,Cp,eppesseurMax]]
    head=["Pression minimale / la corde","Cd faible au dessous et au dessus de Cp(%)","Cofficient de portance(%)", "eppesseur maximal(%)"]
    print(tbl(infos, headers=head,tablefmt="grid" ))

if len(airfoil) == 7 and airfoil[0] == '7' and airfoil[3]=='A':
    pressionMinSsup = int(airfoil[1])*10
    pressionMinSinf = int(airfoil[2])*10
    Cp = int(airfoil[4])/10
    eppesseurMax =airfoil[5]+airfoil[6]
    infos=[[pressionMinSsup,pressionMinSinf,Cp,eppesseurMax]]
    head=["P min/la corde sur la surface sup", "P min/la corde sur la surface inf","Cofficient de portance(%)", "eppesseur maximal(%)"]
    print(tbl(infos, headers=head, tablefmt="grid"))