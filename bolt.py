


class Bolt:
    """
    A vásárlásokat kezelő osztály. Az osztály egyetlen attribútuma a kosarak listája.
    """

    def __init__(self):
        """
        A bolt létrehozásakor beállítja az osztály attribútumait.
        """
        pass

    def feladat_1(self,lista:list) -> None:
        """
        Beolvassa a fájlból a kosarak tartalmát.

        :param filepath: A kosarak tartalmát tartalmazó fájl elérési útvonala.
        """


        #filepath = "kosar.txt"
        #fileobject = open(filepath, "r")

        #s=0
        #for line in fileobject:
        #   s=s+1


        s=0
        lista = []
        fileobject = open('kosar.txt')
        for sor in fileobject:
            lista.append(sor.strip())
            s=s+1
        fileobject.close()


        print("\n")
        print("elso feladt beolvasás készen")
        print(s,"elem")
    def feladat_2(self,lista:list) -> None:
        """
        Kiírja, hányan fizettek a pénztárnál.
        """
        fizettek = 0
        for line in list:
           if line=='F':
               fizettek=fizettek+1


        print("ennyien fizettek a pénztárnál: ", fizettek)


    def feladat_3(self, lista: list) -> None:
        """
        Bekéri egy vásárlás sorszámát és kiírja:
            - hány darab árucikk volt a kosárban,
            - mely árucikkekből és milyen mennyiségben vásároltak,
            - a vásárlás összegét.
        """
        print("kérem a vásárlás számát(csak számot): ")
        vasarlasszam=0

        try:
            vasarlasszam = input()
        except ValueError:
            print("helytelen értéket adott meg.")

        vasarlasszam=vasarlasszam-1

        vasarlasdb=0

        vasarlasar=0
        vasarlasmennyiseg=0
        for line in list:
            if list[line] == 'F':
                vasarlasdb= vasarlasdb+1

            if vasarlasdb == vasarlasszam:

                while list[line]=="F":
                    vasarlasmennyiseg=vasarlasmennyiseg+1
                    print(list[line])
            if vasarlasmennyiseg==1:
                vasarlasar=1000
            if vasarlasmennyiseg==2:
                vasarlasar=1000+900
        for i in range[vasarlasmennyiseg]:
            vasarlasar=vasarlasar+800

        vasarlasar=vasarlasar+200+100

        print("a vásárlás ennyi forintba került: ",vasarlasar)
        print("ennyi árut vettek: ", vasarlasmennyiseg)
    def feladat_4(self, lista:list) -> None:
        """
        Bekéri egy árucikk nevét és kiírja:
            - melyik vásárlásnál vettek először a termékből
            - melyik vásárlásnál vettek utoljára a termékből
            - összesen hány alkalommal vásároltak a termékből
        """
        print("kérek egy árucikket:")
        arucikk=""
        try:
            arucikk=input()
        except ValueError:
            print("helytelen értéket adott meg.")
        elsoindex=0
        utolsoindex=0
        alkalom=0
        for line in list:
            if list[line]==arucikk:
                alkalom=alkalom+1
                utolsoindex=line

            print("ennyiszer vásároltak a(z)" ,arucikk, "árucikkből: " , alkalom)
            print("az első vásárlás a(z)" ,arucikk, "árucikkből: ", elsoindex)
            print("utolső vásárlás a(z)" ,arucikk, "árucikkből: ", utolsoindex)


        pass

    def feladat_5(self, filepath: str) -> None:
        """
        Elmenti a megadott fájlba a vásárlásonként fizetendő összeget.
        Beolvassa a fájlból a kosarak tartalmát.

        :param filepath: A kosarak tartalmát tartalmazó fájl elérési útvonala.
        """



        pass
