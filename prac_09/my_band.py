from musician import Musician
from guitar import Guitar
from band import Band


def main():
    band = Band("Extreme")

    nuno = Musician("Nuno Bettencourt")
    nuno.add(Guitar("Washburn N4", 1990, 2499.95))
    nuno.add(Guitar("Takamine acoustic", 1986, 1200.00))

    gary = Musician("Gary Cherone")

    pat = Musician("Pat Badger")
    pat.add(Guitar("Mouradian CS-74 Bass", 2009, 1500.00))

    kevin = Musician("Kevin Figueiredo")

    band.add(nuno)
    band.add(gary)
    band.add(pat)
    band.add(kevin)

    print("band (str)")
    print(band)

    print("band.play()")
    band.play()


if __name__ == "__main__":
    main()
