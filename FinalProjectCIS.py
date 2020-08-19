#THE KEY
print ("USER GUIDE:\n"
       "Inputs are case sensitive. Please input as shown.\n"
      "Which element or chemical compound would you like to know about?\n\n"
       "~ELEMENT~\n"
      "input: Hydrogen\n"
      "What would you like to know about Hydrogen?\n"
       "input: Atomic Mass\n"
      "or\n"
      "Input: Symbol\n"
      "or\n"
      "input: Atomic Number\n"
       "or\n"
       "input: Period\n"
       "or\n"
       "input: Group\n\n"
       "---\n"
       "\n~COMPOUND~\n"
      "input: Acetic Acid\n"
      "or\n"
      "input: Iron(II) Sulfate\n"
      "What would you like to know about Iron(II) Sulfate?\n"
      "input: Molar Mass\n"
      "or\n"
      "input: Molecular Formula\n\n") 


Element = input("Which element or chemical compound would you like to know about?: ")

#HYDROGEN
HydrogenSymbol = "H"
HydrogenAtomicNumber = 1
HydrogenAtomicMass = 1.008
HydrogenGroup = 1
HydrogenPeriod = 1

if Element == "Hydrogen":
       Hydrogen = input("What would you like to know about Hydrogen?: ")
       if Hydrogen == "Symbol":
             print(HydrogenAtomicSymbol)
       elif Hydrogen == "Atomic Number":
             print(HydrogenAtomicNumber)
       elif Hydrogen == "Atomic Mass":
           print(HydrogenAtomicMass)
       elif Hydrogen == "Group":
             print(HydrogenGroup)
       elif Hydrogen == "Period":
             print(HydrogenPeriod) 

             
#HELIUM
HeliumSymbol = "He"
HeliumAtomicNumber = 2
HeliumAtomicMass = 4.002602
HeliumGroup = 18
HeliumPeriod = 1

if Element == "Helium":
    Element = input("What would you like to know about Helium?: ")
    if Element == "Atomic Mass":
       print(HeliumAtomicMass)
    elif Element == "Symbol":
       print(HeliumSymbol)
    elif Element == "Atomic Number":
       print(HeliumAtomicNumber)
    elif Element == "Group":
        print(HeliumGroup)
    elif Element == "Period":
        print(HeliumPeriod)

#LITHIUM
LithiumSymbol = "L"
LithiumAtomicNumber = 3
LithiumAtomicMass = 6.94
LithiumGroup = 1
LithiumPeriod = 2

if Element == "Lithium":
    Element = input("What would you like to know about Lithum?: ")
    if Element == "Atomic Mass":
       print(LithiumAtomicMass)
    elif Element == "Symbol":
       print(LithiumSymbol)
    elif Element == "Atomic Number":
       print(LithiumAtomicNumber)
    elif Element == "Group":
        print(LithiumGroup)
    elif Element == "Period":
        print(LithiumPeriod)


#BERYLLIUM
BerylliumSymbol = "Be"
BerylliumAtomicNumber = 4
BerylliumAtomicMass = 9.0121831
BerylliumGroup = 2
BerylliumPeriod = 2

if Element == "Beryllium":
    Element = input("What would you like to know about Beryllium?: ")
    if Element == "Atomic Mass":
       print(BerylliumAtomicMass)
    elif Element == "Symbol":
       print(BerylliumSymbol)
    elif Element == "Atomic Number":
       print(BerylliumAtomicNumber)
    elif Element == "Group":
        print(BerylliumGroup)
    elif Element == "Period":
        print(BerylliumPeriod)

#BORON
BoronSymbol = "B"
BoronAtomicNumber = 5
BoronAtomicMass = 10.81
BoronGroup = 13
BoronPeriod = 2

if Element == "Boron":
    Element = input("What would you like to know about Boron?: ")
    if Element == "Atomic Mass":
       print(BoronAtomicMass)
    elif Element == "Symbol":
       print(BoronSymbol)
    elif Element == "Atomic Number":
       print(BoronAtomicNumber)
    elif Element == "Group":
        print(BoronGroup)
    elif Element == "Period":
        print(BoronPeriod)

#CARBON
CarbonSymbol = "C"
CarbonAtomicNumber = 6
CarbonAtomicMass = 12.011
CarbonGroup = 14
CarbonPeriod = 2

if Element == "Carbon":
    Element = input("What would you like to know about Carbon?: ")
    if Element == "Atomic Mass":
       print(CarbonAtomicMass)
    elif Element == "Symbol":
       print(CarbonSymbol)
    elif Element == "Atomic Number":
       print(CarbonAtomicNumber)
    elif Element == "Group":
        print(CarbonGroup)
    elif Element == "Period":
        print(CarbonPeriod)


#NITROGEN
NitrogenSymbol = "N"
NitrogenAtomicNumber = 7
NitrogenAtomicMass = 14.007
NitrogenPeriod = 7
NitrogenGroup = 15

if Element == "Nitrogen":
    Element = input("What would you like to know about Nitrogen?: ")
    if Element == "Atomic Mass":
       print(NitrogenAtomicMass)
    elif Element == "Symbol":
       print(NitrogenSymbol)
    elif Element == "Atomic Number":
       print(NitrogenAtomicNumber)
    elif Element == "Period":
        print(NitrogenPeriod)
    elif Element == "Group":
        print(NitrogenGroup)


#OXYGEN
OxygenSymbol = "O"
OxygenAtomicNumber = 8
OxygenAtomicMass = 15.999
OxygenGroup = 16
OxygenPeriod = 2

if Element == "Oxygen":
    Element = input("What would you like to know about Oxygen?: ")
    if Element == "Atomic Mass":
       print(OxygenAtomicMass)
    elif Element == "Symbol":
       print(OxygenSymbol)
    elif Element == "Atomic Number":
       print(OxygenAtomicNumber)
    elif Element == "Group":
        print(OxygenGroup)
    elif Element == "Period":
        print(OxygenPeriod)

#FLUORINE
FluorineSymbol = "F"
FluorineAtomicNumber = 9
FluorineAtomicMass = 18.998403163
FluorineGroup = 17
FluorinePeriod = 2

if Element == "Fluorine":
    Element = input("What would you like to know about Fluorine?: ")
    if Element == "Atomic Mass":
       print(FluorineAtomicMass)
    elif Element == "Symbol":
       print(FluorineSymbol)
    elif Element == "Atomic Number":
       print(FluorineAtomicNumber)
    elif Element == "Group":
        print(FluorineGroup)
    elif Element == "Period":
        print(FluorinePeriod)

#NEON
NeonSymbol = "Ne"
NeonAtomicNumber = 10
NeonAtomicMass = 20.1797
NeonGroup = 18
NeonPeriod = 2

if Element == "Neon":
    Element = input("What would you like to know about Neon?: ")
    if Element == "Atomic Mass":
       print(NeonAtomicMass)
    elif Element == "Symbol":
       print(NeonSymbol)
    elif Element == "Atomic Number":
       print(NeonAtomicNumber)
    elif Element == "Group":
        print(NeonGroup)
    elif Element == "Period":
        print(NeonPeriod)

#SODIUM
SodiumSymbol = "Na"
SodiumAtomicNumber = 11
SodiumAtomicMass = 22.98976928
SodiumGroup = 1
SodiumPeriod = 3

if Element == "Sodium":
    Element = input("What would you like to know about Sodium?: ")
    if Element == "Atomic Mass":
       print(SodiumAtomicMass)
    elif Element == "Symbol":
       print(SodiumSymbol)
    elif Element == "Atomic Number":
       print(SodiumAtomicNumber)
    elif Element == "Group":
        print(SodiumGroup)
    elif Element == "Period":
        print(SodiumPeriod)

#MAGNESIUM
MagnesiumSymbol = "Mg"
MagnesiumAtomicNumber = 12
MagnesiumAtomicMass = 24.305
MagnesiumGroup = 2
MagnesiumPeriod = 3

if Element == "Magnesium":
    Element = input("What would you like to know about Magnesium?: ")
    if Element == "Atomic Mass":
       print(MagnesiumAtomicMass)
    elif Element == "Symbol":
       print(MagnesiumSymbol)
    elif Element == "Atomic Number":
       print(MagnesiumAtomicNumber)
    elif Element == "Group":
        print(MagnesiumGroup)
    elif Element == "Period":
        print(MagnesiumPeriod)

#ALUMINIUM
AluminiumSymbol = "Al"
AluminiumAtomicNumber = 13
AluminiumAtomicMass = 26.9815385
AluminiumGroup = 13
AluminiumPeriod = 3

if Element == "Aluminium":
    Element = input("What would you like to know about Aluminium?: ")
    if Element == "Atomic Mass":
       print(AluminiumAtomicMass)
    elif Element == "Symbol":
       print(AluminiumSymbol)
    elif Element == "Atomic Number":
       print(AluminiumAtomicNumber)
    elif Element == "Group":
        print(AluminiumGroup)
    elif Element == "Period":
        print(AluminiumPeriod)

#SILICON
SiliconSymbol = "Si"
SiliconAtomicNumber = 14 
SiliconAtomicMass = 28.085
SiliconGroup = 14
SiliconPeriod = 3

if Element == "Silicon":
    Element = input("What would you like to know about Silicon?: ")
    if Element == "Atomic Mass":
       print(SiliconAtomicMass)
    elif Element == "Symbol":
       print(SiliconSymbol)
    elif Element == "Atomic Number":
       print(SiliconAtomicNumber)
    elif Element == "Group":
        print(SiliconGroup)
    elif Element == "Period":
        print(SiliconPeriod)

#PHOSPHORUS
PhosphorusSymbol = "P"
PhosphorusAtomicNumber = 15
PhosphorusAtomicMass = 30.973761998
PhosphorusGroup = 15
PhosphorusPeriod = 3

if Element == "Phosphorus":
    Element = input("What would you like to know about Phosphorus?: ")
    if Element == "Atomic Mass":
       print(PhosphorusAtomicMass)
    elif Element == "Symbol":
       print(PhosphorusSymbol)
    elif Element == "Atomic Number":
       print(PhosphorusAtomicNumber)
    elif Element == "Group":
        print(PhosphorusGroup)
    elif Element == "Period":
        print(PhosphorusPeriod)

#SULFUR
SulfurSymbol = "S"
SulfurAtomicNumber = 16
SulfurAtomicMass = 32.06
SulfurGroup = 16
SulfurPeriod = 3

if Element == "Sulfur":
    Element = input("What would you like to know about Sulfur?: ")
    if Element == "Atomic Mass":
       print(SulfurAtomicMass)
    elif Element == "Symbol":
       print(SulfurSymbol)
    elif Element == "Atomic Number":
       print(SulfurAtomicNumber)
    elif Element == "Group":
        print(SulfurGroup)
    elif Element == "Period":
        print(SulfurPeriod)

#CHLORINE
ChlorineSymbol = "Cl"
ChlorineAtomicNumber = 17
ChlorineAtomicMass = 35.45
ChlorineGroup = 17
ChlorinePeriod = 3

if Element == "Chlorine":
    Element = input("What would you like to know about Chlorine?: ")
    if Element == "Atomic Mass":
       print(ChlorineAtomicMass)
    elif Element == "Symbol":
       print(ChlorineSymbol)
    elif Element == "Atomic Number":
       print(ChlorineAtomicNumber)
    elif Element == "Group":
        print(ChlorineGroup)
    elif Element == "Period":
        print(ChlorinePeriod)

#ARGON
ArgonSymbol = "Ar"
ArgonAtomicNumber = 18
ArgonAtomicMass = 39.948
ArgonGroup = 18
ArgonPeriod = 3

if Element == "Argon":
    Element = input("What would you like to know about Argon?: ")
    if Element == "Atomic Mass":
       print(ArgonAtomicMass)
    elif Element == "Symbol":
       print(ArgonSymbol)
    elif Element == "Atomic Number":
       print(ArgonAtomicNumber)
    elif Element == "Group":
        print(ArgonGroup)
    elif Element == "Period":
        print(ArgonPeriod)

#POTASSIUM
PotassiumSymbol = "K"
PotassiumAtomicNumber = 19
PotassiumAtomicMass = 39.0983
PotassiumGroup = 15
PotassiumPeriod = 3

if Element == "Potassium":
    Element = input("What would you like to know about Potassium?: ")
    if Element == "Atomic Mass":
       print(PotassiumAtomicMass)
    elif Element == "Symbol":
       print(PotassiumSymbol)
    elif Element == "Atomic Number":
       print(PotassiumAtomicNumber)
    elif Element == "Group":
        print(PotassiumGroup)
    elif Element == "Period":
        print(PotassiumPeriod)

#CALCIUM
CalciumSymbol = "Ca"
CalciumAtomicNumber = 20
CalciumAtomicMass = 40.078
CalciumGroup = 2
CalciumPeriod = 4

if Element == "Calcium":
    Element = input("What would you like to know about Calcium?: ")
    if Element == "Atomic Mass":
       print(CalciumAtomicMass)
    elif Element == "Symbol":
       print(CalciumSymbol)
    elif Element == "Atomic Number":
       print(CalciumAtomicNumber)
    elif Element == "Group":
        print(CalciumGroup)
    elif Element == "Period":
        print(CalciumPeriod)


#SCANDIUM
ScandiumSymbol = "Sc"
ScandiumAtomicNumber = 21
ScandiumAtomicMass = 44.9559
ScandiumGroup = 3
ScandiumPeriod = 4

if Element == "Scandium":
    Element = input("What would you like to know about Scandium?: ")
    if Element == "Atomic Mass":
       print(ScandiumAtomicMass)
    elif Element == "Symbol":
       print(ScandiumSymbol)
    elif Element == "Atomic Number":
       print(ScandiumAtomicNumber)
    elif Element == "Group":
        print(ScandiumGroup)
    elif Element == "Period":
        print(ScandiumPeriod)


#TITANIUM
TitantiumSymbol = "Ti"
TitaniumAtomicNumber = 22
TitaniumAtomicMass = 47.867
TitaniumGroup = 4
TitaniumPeriod = 4

if Element == "Titanium":
    Element = input("What would you like to know about Titanium?: ")
    if Element == "Atomic Mass":
       print(TitaniumAtomicMass)
    elif Element == "Symbol":
       print(TitaniumSymbol)
    elif Element == "Atomic Number":
       print(TitaniumAtomicNumber)
    elif Element == "Group":
        print(TitaniumGroup)
    elif Element == "Period":
        print(TitaniumPeriod)

#VANADIUM
VanadiumSymbol = "V"
VanadiumAtomicNumber = 23
VanadiumAtomicMass = 50.9415
VandiumGroup = 5
VandiumPeriod = 4

if Element == "Vanadium":
    Element = input("What would you like to know about Vanadium?: ")
    if Element == "Atomic Mass":
       print(VanadiumAtomicMass)
    elif Element == "Symbol":
       print(VanadiumSymbol)
    elif Element == "Atomic Number":
       print(VanadiumAtomicNumber)
    elif Element == "Group":
        print(VandiumGroup)
    elif Element == "Period":
        print(VandiumPeriod)

#CHROMIUM
ChromiumSymbol = "Cr"
ChromiumAtomicNumber = 24
ChromiumAtomicMass = 51.9961
ChromiumGroup = 6
ChromiumPeriod = 4

if Element == "Chromium":
    Element = input("What would you like to know about Chromium?: ")
    if Element == "Atomic Mass":
       print(ChromiumAtomicMass)
    elif Element == "Symbol":
       print(ChromiumSymbol)
    elif Element == "Atomic Number":
       print(ChromiumAtomicNumber)
    elif Element == "Group":
        print(ChromiumGroup)
    elif Element == "Period":
        print(ChromiumPeriod)

#MANGANESE
ManganeseSymbol = "Mn"
ManganeseAtomicNumber = 25
ManganeseAtomicMass = 54.938
ManganeseGroup = 7
ManganesePeriod = 4

if Element == "Manganese":
    Element = input("What would you like to know about Manganese?: ")
    if Element == "Atomic Mass":
       print(ManganeseAtomicMass)
    elif Element == "Symbol":
       print(ManganeseSymbol)
    elif Element == "Atomic Number":
       print(ManganeseAtomicNumber)
    elif Element == "Group":
        print(ManganeseGroup)
    elif Element == "Period":
        print(ManganesePeriod)

#IRON
IronSymbol = "Fe"
IronAtomicNumber = 26
IronAtomicMass = 55.845
IronGroup = 8
IronPeriod = 4

if Element == "Iron":
    Element = input("What would you like to know about Iron?: ")
    if Element == "Atomic Mass":
       print(IronAtomicMass)
    elif Element == "Symbol":
       print(IronSymbol)
    elif Element == "Atomic Number":
       print(IronAtomicNumber)
    elif Element == "Group":
        print(IronGroup)
    elif Element == "Period":
        print(IronPeriod)

#COLBALT
ColbaltSymbol = "Co"
ColbaltAtomicNumber = 27
ColbaltAtomicMass = 58.9332
ColbaltGroup = 9 
ColbaltPeriod = 4

if Element == "Colbalt":
    Element = input("What would you like to know about Colbalt?: ")
    if Element == "Atomic Mass":
       print(ColbaltAtomicMass)
    elif Element == "Symbol":
       print(ColbaltSymbol)
    elif Element == "Atomic Number":
       print(ColbaltAtomicNumber)
    elif Element == "Group":
        print(ColbaltGroup)
    elif Element == "Period":
        print(ColbaltPeriod)

#NICKEL
NickelSymbol = "Ni"
NickelAtomicNumber = 28
NickelAtomicMass = 58.6934
NickelGroup = 10
NickelPeriod = 4

if Element == "Nickel":
    Element = input("What would you like to know about Nickel?: ")
    if Element == "Atomic Mass":
       print(NickelAtomicMass)
    elif Element == "Symbol":
       print(NickelSymbol)
    elif Element == "Atomic Number":
       print(NickelAtomicNumber)
    elif Element == "Group":
        print(NickelGroup)
    elif Element == "Period":
        print(NickelPeriod)

#COPPER
CopperSymbol = "Cu"
CopperAtomicNumber = 29
CopperAtomicMass = 63.546
CopperGroup = 11
CopperPeriod = 4

if Element == "Copper":
    Element = input("What would you like to know about Copper?: ")
    if Element == "Atomic Mass":
       print(CopperAtomicMass)
    elif Element == "Symbol":
       print(CopperSymbol)
    elif Element == "Atomic Number":
       print(CopperAtomicNumber)
    elif Element == "Group":
        print(CopperGroup)
    elif Element == "Period":
        print(CopperPeriod)

#ZINC
ZincSymbol = "Zn"
ZincAtomicNumber = 30 
ZincAtomicMass = 65.39
ZincGroup = 12
ZincPeriod = 4

if Element == "Zinc":
    Element = input("What would you like to know about Zinc?: ")
    if Element == "Atomic Mass":
       print(ZincAtomicMass)
    elif Element == "Symbol":
       print(ZincSymbol)
    elif Element == "Atomic Number":
       print(ZincAtomicNumber)
    elif Element == "Group":
        print(ZincGroup)
    elif Element == "Period":
        print(ZincPeriod)

#GALLIUM
GalliumSymbol = "Ga"
GalliumAtomicNumber = 31
GalliumAtomicMass = 69.723
GalliumGroup = 13
GalliumPeriod = 4

if Element == "Gallium":
    Element = input("What would you like to know about Gallium?: ")
    if Element == "Atomic Mass":
       print(GalliumAtomicMass)
    elif Element == "Symbol":
       print(GalliumSymbol)
    elif Element == "Atomic Number":
       print(GalliumAtomicNumber)
    elif Element == "Group":
        print(GalliumGroup)
    elif Element == "Period":
        print(GalliumPeriod)

#GERMANIUM
GermaniumSymbol = "Ge"
GermaniumAtomicNumber = 32
GermaniumAtomicMass = 72.630
GermaniumGroup = 14
GermaniumPeriod = 4

if Element == "Germanium":
    Element = input("What would you like to know about Germanium?: ")
    if Element == "Atomic Mass":
       print(GermaniumAtomicMass)
    elif Element == "Symbol":
       print(GermaniumSymbol)
    elif Element == "Atomic Number":
       print(GermaniumAtomicNumber)
    elif Element == "Group":
        print(GermaniumGroup)
    elif Element == "Period":
        print(GermaniumPeriod)

#ARSENIC
ArsenicSymbol = "As"
ArsenicAtomicNumber = 33
ArsenicAtomicMass = 74.9216
ArsenicGroup = 15
ArsenicPeriod = 4

if Element == "Arsenic":
    Element = input("What would you like to know about Arsenic?: ")
    if Element == "Atomic Mass":
       print(ArsenicAtomicMass)
    elif Element == "Symbol":
       print(ArsenicSymbol)
    elif Element == "Atomic Number":
       print(ArsenicAtomicNumber)
    elif Element == "Group":
        print(ArsenicGroup)
    elif Element == "Period":
        print(ArsenicPeriod)

#SELENIUM
SeleniumSymbol = "Se"
SeleniumAtomicNumber = 34
SeleniumAtomicMass = 78.96
SeleniumGroup = 16
SeleniumPeriod = 4

if Element == "Selenium":
    Element = input("What would you like to know about Selenium?: ")
    if Element == "Atomic Mass":
       print(SeleniumAtomicMass)
    elif Element == "Symbol":
       print(SeleniumSymbol)
    elif Element == "Atomic Number":
       print(SeleniumAtomicNumber)
    elif Element == "Group":
        print(SeleniumGroup)
    elif Element == "Period":
        print(SeleniumPeriod)

#BROMINE
BromineSymbol = "Br"
BromineAtomicNumber = 35
BromineAtomicMass = 79.904
BromineGroup = 17
BrominePeriod = 4

if Element == "Bromine":
    Element = input("What would you like to know about Bromine?: ")
    if Element == "Atomic Mass":
       print(BromineAtomicMass)
    elif Element == "Symbol":
       print(BromineSymbol)
    elif Element == "Atomic Number":
       print(BromineAtomicNumber)
    elif Element == "Group":
        print(BromineGroup)
    elif Element == "Period":
        print(BrominePeriod)

#KRYPTON
KryptonSymbol = "Br"
KryptonAtomicNumber = 36
KryptonAtomicMass = 83.8
KryptonGroup = 18
KryptonPeriod = 4

if Element == "Krypton":
    Element = input("What would you like to know about Krypton?: ")
    if Element == "Atomic Mass":
       print(KryptonAtomicMass)
    elif Element == "Symbol":
       print(KryptonSymbol)
    elif Element == "Atomic Number":
       print(KryptonAtomicNumber)
    elif Element == "Group":
        print(KryptonGroup)
    elif Element == "Period":
        print(KryptonPeriod)

#RUPIDIUM
RupidiumSymbol = "Rb"
RupidiumAtomicNumber = 37
RupidiumAtomicMass = 85.4678
RupidiumGroup = 1
RupidiumPeriod = 5

if Element == "Rupidium":
    Element = input("What would you like to know about Rupidium?: ")
    if Element == "Atomic Mass":
       print(RupidiumAtomicMass)
    elif Element == "Symbol":
       print(RupidiumSymbol)
    elif Element == "Atomic Number":
       print(RupidiumAtomicNumber)
    elif Element == "Group":
        print(RupidiumGroup)
    elif Element == "Period":
        print(RupidiumPeriod)

#STRONTIUM
StrontiumSymbol = "Sr"
StrontiumAtomicNumber = 38
StrontiumAtomicMass = 87.62
StontiumGroup = 2
StontiumPeriod = 5

if Element == "Strontium":
    Element = input("What would you like to know about Strontium?: ")
    if Element == "Atomic Mass":
       print(StrontiumAtomicMass)
    elif Element == "Symbol":
       print(StrontiumSymbol)
    elif Element == "Atomic Number":
       print(StrontiumAtomicNumber)
    elif Element == "Group":
        print(StontiumGroup)
    elif Element == "Period":
        print(StontiumPeriod)

#YTTRIUM
YttriumSymbol = "Y"
YttriumAtomicNumber = 39
YttriumAtomicMass = 88.9059
YttriumGroup = 3
YttriumPeriod = 5

if Element == "Yttrium":
    Element = input("What would you like to know about Yttrium?: ")
    if Element == "Atomic Mass":
       print(YttriumAtomicMass)
    elif Element == "Symbol":
       print(YttriumSymbol)
    elif Element == "Atomic Number":
       print(YttriumAtomicNumber)
    elif Element == "Group":
        print(YttriumGroup)
    elif Element == "Period":
        print(YttriumPeriod)

#ZIRCONIUM
ZirconiumSymbol = "Zr"
ZirconiumAtomicNumber = 40
ZirconiumAtomicMass = 91.224
ZirconiumGroup = 4
ZirconiumPeriod = 5

if Element == "Zirconium":
    Element = input("What would you like to know about Zirconium?: ")
    if Element == "Atomic Mass":
       print(ZirconiumAtomicMass)
    elif Element == "Symbol":
       print(ZirconiumSymbol)
    elif Element == "Atomic Number":
       print(ZirconiumAtomicNumber)
    elif Element == "Group":
        print(ZirconiumGroup)
    elif Element == "Period":
        print(ZirconiumPeriod)

#NIOBIUM
NiobiumSymbol = "Nb"
NiobiumAtomicNumber = 41
NiobiumAtomicMass = 92.9064
NiobiumGroup = 5
NiobiumPeriod = 5

if Element == "Niobium":
    Element = input("What would you like to know about Niobium?: ")
    if Element == "Atomic Mass":
       print(NiobiumAtomicMass)
    elif Element == "Symbol":
       print(NiobiumSymbol)
    elif Element == "Atomic Number":
       print(NiobiumAtomicNumber)
    elif Element == "Group":
        print(NiobiumGroup)
    elif Element == "Period":
        print(NiobiumPeriod)

#MOLYBDENUM
MolybdenumSymbol = "Mo"
MolybdenumAtomicNumber = 42
MolybdenumAtomicMass = 95.94
MolybdenumGroup = 6
MolybdenumPeriod = 5

if Element == "Molybdenum":
    Element = input("What would you like to know about Molybdenum?: ")
    if Element == "Atomic Mass":
       print(MolybdenumAtomicMass)
    elif Element == "Symbol":
       print(MolybdenumSymbol)
    elif Element == "Atomic Number":
       print(MolybdenumAtomicNumber)
    elif Element == "Group":
        print(Molybdenumroup)
    elif Element == "Period":
        print(MolybdenumPeriod)
        
#TECHNETIUM
TechnetiumSymbol = "Tc"
TechnetiumAtomicNumber = 43
TechnetiumAtomicMass = 98
TechhnetiumGroup = 7
TechhnetiumPeriod = 5

if Element == "Technetium":
    Element = input("What would you like to know about Technetium?: ")
    if Element == "Atomic Mass":
       print(TechnetiumAtomicMass)
    elif Element == "Symbol":
       print(TechnetiumSymbol)
    elif Element == "Atomic Number":
       print(TechnetiumAtomicNumber)
    elif Element == "Group":
        print(TechhnetiumGroup)
    elif Element == "Period":
        print(TechhnetiumPeriod)

#RUTHENIUM
RutheniumSymbol = "Ru"
RutheniumAtomicNumber = 44
RutheniumAtomicMass = 101.07
RutheniumGroup = 8
RutheniumPeriod = 5

if Element == "Ruthenium":
    Element = input("What would you like to know about Ruthenium?: ")
    if Element == "Atomic Mass":
       print(RutheniumAtomicMass)
    elif Element == "Symbol":
       print(RutheniumSymbol)
    elif Element == "Atomic Number":
       print(RutheniumAtomicNumber)
    elif Element == "Group":
        print(RutheniumGroup)
    elif Element == "Period":
        print(RutheniumPeriod)

#RHODIUM
RhodiumSymbol = "Rh"
RhodiumAtomicNumber = 45
RhodiumAtomicMass = 102.9055
RhodiumGroup = 9
RhodiumPeriod = 5

if Element == "Rhodium":
    Element = input("What would you like to know about Rhodium?: ")
    if Element == "Atomic Mass":
       print(RhodiumAtomicMass)
    elif Element == "Symbol":
       print(RhodiumSymbol)
    elif Element == "Atomic Number":
       print(RhodiumAtomicNumber)
    elif Element == "Group":
        print(RhodiumGroup)
    elif Element == "Period":
        print(RhodiumPeriod)

#PALLADIUM
PalladiumSymbol = "Pd"
PalladiumAtomicNumber = 46
PalladiumAtomicMass = 106.42
PalladiumGroup = 10
PalladiumPeriod = 5

if Element == "Palladium":
    Element = input("What would you like to know about Palladium?: ")
    if Element == "Atomic Mass":
       print(PalladiumAtomicMass)
    elif Element == "Symbol":
       print(PalladiumSymbol)
    elif Element == "Atomic Number":
       print(PalladiumAtomicNumber)
    elif Element == "Group":
        print(PalladiumGroup)
    elif Element == "Period":
        print(PalladiumPeriod)

#SILVER
SilverSymbol = "Ag"
SilverAtomicNumber = 47
SilverAtomicMass = 107.8682
SilverGroup = 11
SilverPeriod = 5

if Element == "Silver":
    Element = input("What would you like to know about Silver?: ")
    if Element == "Atomic Mass":
       print(SilverAtomicMass)
    elif Element == "Symbol":
       print(SilverSymbol)
    elif Element == "Atomic Number":
       print(SilverAtomicNumber)
    elif Element == "Group":
        print(SilverGroup)
    elif Element == "Period":
        print(SilverPeriod)

#CADMIUM
CadmiumSymbol = "Cd"
CadmiumAtomicNumber = 48
CadmiumAtomicMass = 112.411
CadmiumGroup = 12
CadmiumPeriod = 5

if Element == "Cadmium":
    Element = input("What would you like to know about Cadmium?: ")
    if Element == "Atomic Mass":
       print(CadmiumAtomicMass)
    elif Element == "Symbol":
       print(CadmiumSymbol)
    elif Element == "Atomic Number":
       print(CadmiumAtomicNumber)
    elif Element == "Group":
        print(CadmiumGroup)
    elif Element == "Period":
        print(CadmiumPeriod)

#INDIUM
IndiumSymbol = "In"
IndiumAtomicNumber = 49
IndiumAtomicMass = 114.818
IndiumGroup = 13
IndiumPeriod = 5

if Element == "Indium":
    Element = input("What would you like to know about Indium?: ")
    if Element == "Atomic Mass":
       print(IndiumAtomicMass)
    elif Element == "Symbol":
       print(IndiumSymbol)
    elif Element == "Atomic Number":
       print(IndiumAtomicNumber)
    elif Element == "Group":
        print(IndiumGroup)
    elif Element == "Period":
        print(IndiumPeriod)

#TIN
TinSymbol = "Sn"
TinAtomicNumber = 50
TinAtomicMass = 118.71
TinGroup = 14
TinPeriod = 5

if Element == "Tin":
    Element = input("What would you like to know about Tin?: ")
    if Element == "Atomic Mass":
       print(TinAtomicMass)
    elif Element == "Symbol":
       print(TinSymbol)
    elif Element == "Atomic Number":
       print(TinAtomicNumber)
    elif Element == "Group":
        print(TinGroup)
    elif Element == "Period":
        print(TinPeriod)

#ANTIMONY
AntimonySymbol = "Sb"
AntimonyAtomicNumber = 51
AntimonyAtomicMass = 121.760
AntimonyGroup = 15
AntimonyPeriod = 5

if Element == "Antimony":
    Element = input("What would you like to know about Antimony?: ")
    if Element == "Atomic Mass":
       print(AntimonyAtomicMass)
    elif Element == "Symbol":
       print(AntimonySymbol)
    elif Element == "Atomic Number":
       print(AntimonyAtomicNumber)
    elif Element == "Group":
        print(AntimonyGroup)
    elif Element == "Period":
        print(AntimonyPeriod)

#TELLARIUM

TellariumSymbol = "Te"
TellariumAtomicNumber = 52
TellariumAtomicMass = 127.60
TellariumGroup = 16
TellariumPeriod = 5

if Element == "Tellarium":
    Element = input("What would you like to know about Tellarium?: ")
    if Element == "Atomic Mass":
       print(TellariumAtomicMass)
    elif Element == "Symbol":
       print(TellariumSymbol)
    elif Element == "Atomic Number":
       print(TellariumAtomicNumber)
    elif Element == "Group":
        print(TellariumGroup)
    elif Element == "Period":
        print(TellariumPeriod)

#IODINE

IodineSymbol = "I"
IodineAtomicNumber = 53
IodineAtomicMass = 126.90447
IodineGroup = 17
IodinePeriod = 5

if Element == "Iodine":
    Element = input("What would you like to know about Iodine?: ")
    if Element == "Atomic Mass":
       print(IodineAtomicMass)
    elif Element == "Symbol":
       print(IodineSymbol)
    elif Element == "Atomic Number":
       print(IodineAtomicNumber)
    elif Element == "Group":
        print(IodineGroup)
    elif Element == "Period":
        print(IodinePeriod)

#XENON

XenonSymbol = "Xe"
XenonAtomicNumber = 54
XenonAtomicMass = 131.293
XenonGroup = 18
XenonPeriod = 5

if Element == "Xenon":
    Element = input("What would you like to know about Xenon?: ")
    if Element == "Atomic Mass":
       print(XenonAtomicMass)
    elif Element == "Symbol":
       print(XenonSymbol)
    elif Element == "Atomic Number":
       print(XenonAtomicNumber)
    elif Element == "Group":
        print(XenonGroup)
    elif Element == "Period":
        print(XenonPeriod)

#CAESIUM

CaesiumSymbol = "Cs"
CaesiumAtomicNumber = 55
CaesiumAtomicMass = 132.90545196
CaesiumGroup = 1
CaesiumPeriod = 6

if Element == "Caesium":
    Element = input("What would you like to know about Caesium?: ")
    if Element == "Atomic Mass":
       print(CaesiumAtomicMass)
    elif Element == "Symbol":
       print(CaesiumSymbol)
    elif Element == "Atomic Number":
       print(CaesiumAtomicNumber)
    elif Element == "Group":
        print(CaesiumGroup)
    elif Element == "Period":
        print(CaesiumPeriod)

#BARIUM

BariumSymbol = "Ba"
BariumAtomicNumber = 56
BariumAtomicMass = 137.327

if Element == "Barium":
    Element = input("What would you like to know about Barium?: ")
    if Element == "Atomic Mass":
       print(BariumAtomicMass)
    elif Element == "Symbol":
       print(BariumSymbol)
    elif Element == "Atomic Number":
       print(BariumAtomicNumber)

#LANTHANUM

LanthanumSymbol = "La"
LanthanumAtomicNumber = 57
LanthanumAtomicMass = 138.90547
LanthanumGroup = "none"
LanthanumPeriod = 6

if Element == "Lanthanum":
    Element = input("What would you like to know about Lanthanum?: ")
    if Element == "Atomic Mass":
       print(LanthanumAtomicMass)
    elif Element == "Symbol":
       print(LanthanumSymbol)
    elif Element == "Atomic Number":
       print(LanthanumAtomicNumber)
    elif Element == "Group":
        print(LanthanumGroup)
    elif Element == "Period":
        print(LanthanumPeriod)

#CERIUM

CeriumSymbol = "Ce"
CeriumAtomicNumber = 58
CeriumAtomicMass = 140.116
CeriumGroup = "none"
CeriumPeriod = 6

if Element == "Cerium":
    Element = input("What would you like to know about Cerium?: ")
    if Element == "Atomic Mass":
       print(CeriumAtomicMass)
    elif Element == "Symbol":
       print(CeriumSymbol)
    elif Element == "Atomic Number":
       print(CeriumAtomicNumber)
    elif Element == "Group":
        print(CeriumGroup)
    elif Element == "Period":
        print(CeriumPeriod)

#PRASEODYMIUM

PraseodymiumSymbol = "Pr"
PraseodymiumAtomicNumber = 59
PraseodymiumAtomicMass = 140.90766
PraseodymiumGroup = "none"
PraseodymiumPeriod = 6

if Element == "Praseodymium":
    Element = input("What would you like to know about Praseodymium?: ")
    if Element == "Atomic Mass":
       print(PraseodymiumAtomicMass)
    elif Element == "Symbol":
       print(PraseodymiumSymbol)
    elif Element == "Atomic Number":
       print(PraseodymiumAtomicNumber)
    elif Element == "Group":
        print(PraseodymiumGroup)
    elif Element == "Period":
        print(PraseodymiumPeriod)

#NEODYMIUM

NeodymiumSymbol = "Nd"
NeodymiumAtomicNumber = 60
NeodymiumAtomicMass = 144.242
NeodymiumGroup = "none"
NeodymiumPeriod = 6

if Element == "Neodymium":
    Element = input("What would you like to know about Neodymium?: ")
    if Element == "Atomic Mass":
       print(NeodymiumAtomicMass)
    elif Element == "Symbol":
       print(NeodymiumSymbol)
    elif Element == "Atomic Number":
       print(NeodymiumAtomicNumber)
    elif Element == "Group":
        print(NeodymiumGroup)
    elif Element == "Period":
        print(NeodymiumPeriod)

#PROMETHIUM

PromethiumSymbol = "Pm"
PromethiumAtomicNumber = 61
PromethiumAtomicMass = 145
PromethiumGroup = "none"
PromethiumPeriod = 6

if Element == "Promethium":
    Element = input("What would you like to know about Promethium?: ")
    if Element == "Atomic Mass":
       print(PromethiumAtomicMass)
    elif Element == "Symbol":
       print(PromethiumSymbol)
    elif Element == "Atomic Number":
       print(PromethiumAtomicNumber)
    elif Element == "Group":
        print(PromethiumGroup)
    elif Element == "Period":
        print(PromethiumPeriod)

#SAMARIUM

SamariumSymbol = "Sm"
SamariumAtomicNumber = 62
SamariumAtomicMass = 150.36
SamariumGroup = "none"
SamariumPeriod = 6

if Element == "Samarium":
    Element = input("What would you like to know about Samarium?: ")
    if Element == "Atomic Mass":
       print(SamariumAtomicMass)
    elif Element == "Symbol":
       print(SamariumSymbol)
    elif Element == "Atomic Number":
       print(SamariumAtomicNumber)
    elif Element == "Group":
        print(SamariumGroup)
    elif Element == "Period":
        print(SamariumPeriod)

#EUROPIUM

EuropiumSymbol = "Eu"
EuropiumAtomicNumber = 63
EuropiumAtomicMass = 151.964
EuropiumGroup = "none"
EuropiumPeriod = 6

if Element == "Europium":
    Element = input("What would you like to know about Europium?: ")
    if Element == "Atomic Mass":
       print(EuropiumAtomicMass)
    elif Element == "Symbol":
       print(EuropiumSymbol)
    elif Element == "Atomic Number":
       print(EuropiumAtomicNumber)
    elif Element == "Group":
        print(EuropiumGroup)
    elif Element == "Period":
        print(EuropiumPeriod)

#GADOLINIUM

GadoliniumSymbol = "Gd"
GadoliniumAtomicNumber = 64
GadoliniumAtomicMass = 157.25
GadoliniumGroup = "none"
GadoliniumPeriod = 6

if Element == "Gadolinium":
    Element = input("What would you like to know about Gadolinium?: ")
    if Element == "Atomic Mass":
       print(GadoliniumAtomicMass)
    elif Element == "Symbol":
       print(GadoliniumSymbol)
    elif Element == "Atomic Number":
       print(GadoliniumAtomicNumber)
    elif Element == "Group":
        print(GadoliniumGroup)
    elif Element == "Period":
        print(GadoliniumPeriod)

#TERBIUM

TerbiumSymbol = "Tb"
TerbiumAtomicNumber = 65
TerbiumAtomicMass = 158.92535
TerbiumGroup = "none"
TerbiumPeriod = 6

if Element == "Terbium":
    Element = input("What would you like to know about Terbium?: ")
    if Element == "Atomic Mass":
       print(TerbiumAtomicMass)
    elif Element == "Symbol":
       print(TerbiumSymbol)
    elif Element == "Atomic Number":
       print(TerbiumAtomicNumber)
    elif Element == "Group":
        print(TerbiumGroup)
    elif Element == "Period":
        print(TerbiumPeriod)

#Dysprosium

DysprosiumSymbol = "Dy"
DysprosiumAtomicNumber = 66
DysprosiumAtomicMass = 162.500
DysprosiumGroup = "none"
DysprosiumPeriod = 6

if Element == "Dysprosium":
    Element = input("What would you like to know about Dysprosium?: ")
    if Element == "Atomic Mass":
       print(DysprosiumAtomicMass)
    elif Element == "Symbol":
       print(DysprosiumSymbol)
    elif Element == "Atomic Number":
       print(DysprosiumAtomicNumber)
    elif Element == "Group":
        print(DysprosiumGroup)
    elif Element == "Period":
        print(DysprosiumPeriod)

#Holmium

HolmiumSymbol = "Ho"
HolmiumAtomicNumber = 67
HolmiumAtomicMass = 164.93033
HolmiumGroup = "none"
HolmiumPeriod = 6

if Element == "Holmium":
    Element = input("What would you like to know about Holmium?: ")
    if Element == "Atomic Mass":
       print(HolmiumAtomicMass)
    elif Element == "Symbol":
       print(HolmiumSymbol)
    elif Element == "Atomic Number":
       print(HolmiumAtomicNumber)
    elif Element == "Group":
        print(HolmiumGroup)
    elif Element == "Period":
        print(HolmiumPeriod)

#Erbium

ErbiumSymbol = "Er"
ErbiumAtomicNumber = 68
ErbiumAtomicMass = 167.259
ErbiumGroup = "none"
ErbiumPeriod = 6

if Element == "Erbium":
    Element = input("What would you like to know about Erbium?: ")
    if Element == "Atomic Mass":
       print(ErbiumAtomicMass)
    elif Element == "Symbol":
       print(ErbiumSymbol)
    elif Element == "Atomic Number":
       print(ErbiumAtomicNumber)
    elif Element == "Group":
        print(ErbiumGroup)
    elif Element == "Period":
        print(ErbiumPeriod)

#Thulium

ThuliumSymbol = "Tm"
ThuliumAtomicNumber = 69
ThuliumAtomicMass = 168.93422
ThuliumGroup = "none"
ThuliumPeriod = 6

if Element == "Thulium":
    Element = input("What would you like to know about Thulium?: ")
    if Element == "Atomic Mass":
       print(ThuliumAtomicMass)
    elif Element == "Symbol":
       print(ThuliumSymbol)
    elif Element == "Atomic Number":
       print(ThuliumAtomicNumber)
    elif Element == "Group":
        print(ThuliumGroup)
    elif Element == "Period":
        print(ThuliumPeriod)

#Ytterbium

YtterbiumSymbol = "Yb"
YtterbiumAtomicNumber = 70
YtterbiumAtomicMass = 173.045
YtterbiumGroup = "none"
YtterbiumPeriod = 6

if Element == "Ytterbium":
    Element = input("What would you like to know about Ytterbium?: ")
    if Element == "Atomic Mass":
       print(YtterbiumAtomicMass)
    elif Element == "Symbol":
       print(YtterbiumSymbol)
    elif Element == "Atomic Number":
       print(YtterbiumAtomicNumber)
    elif Element == "Group":
        print(YtterbiumGroup)
    elif Element == "Period":
        print(YtterbiumPeriod)
        
#Lutetium

LutetiumSymbol = "Lu"
LutetiumAtomicNumber = 71
LutetiumAtomicMass = 174.9668
LutetiumGroup = "none"
LutetiumPeriod = 6

if Element == "Lutetium":
    Element = input("What would you like to know about Lutetium?: ")
    if Element == "Atomic Mass":
       print(LutetiumAtomicMass)
    elif Element == "Symbol":
       print(LutetiumSymbol)
    elif Element == "Atomic Number":
       print(LutetiumAtomicNumber)
    elif Element == "Group":
        print(LutetiumGroup)
    elif Element == "Period":
        print(LutetiumPeriod)

#Hafnium

HafniumSymbol = "Hf"
HafniumAtomicNumber = 72
HafniumAtomicMass = 178.49
HafniumGroup = 4
HafniumPeriod = 6

if Element == "Hafnium":
    Element = input("What would you like to know about Hafnium?: ")
    if Element == "Atomic Mass":
       print(HafniumAtomicMass)
    elif Element == "Symbol":
       print(HafniumSymbol)
    elif Element == "Atomic Number":
       print(HafniumAtomicNumber)
    elif Element == "Group":
        print(HafniumGroup)
    elif Element == "Period":
        print(HafniumPeriod)

#Tantalum

TantalumSymbol = "Ta"
TantalumAtomicNumber = 73
TantalumAtomicMass = 180.94788
TantalumGroup = 5
TantalumPeriod = 6

if Element == "Tantalum":
    Element = input("What would you like to know about Tantalum?: ")
    if Element == "Atomic Mass":
       print(TantalumAtomicMass)
    elif Element == "Symbol":
       print(TantalumSymbol)
    elif Element == "Atomic Number":
       print(TantalumAtomicNumber)
    elif Element == "Group":
        print(TantalumGroup)
    elif Element == "Period":
        print(TantalumPeriod)

#Tungsten

TungstenSymbol = "W"
TungstenAtomicNumber = 74
TungstenAtomicMass = 183.84
TungstenGroup = 6
TungstenPeriod = 6

if Element == "Tungsten":
    Element = input("What would you like to know about Tungsten?: ")
    if Element == "Atomic Mass":
       print(TungstenAtomicMass)
    elif Element == "Symbol":
       print(TungstenSymbol)
    elif Element == "Atomic Number":
       print(TungstenAtomicNumber)
    elif Element == "Group":
        print(TungstenGroup)
    elif Element == "Period":
        print(TungstenPeriod)

#Rhenium
RheniumSymbol = "Re"
RheniumAtomicNumber = 75
RheniumAtomicMass = 186.207
RheniumGroup = 7
RheniumPeriod = 6

if Element == "Rhenium":
    Element = input("What would you like to know about Rhenium?: ")
    if Element == "Atomic Mass":
       print(RheniumAtomicMass)
    elif Element == "Symbol":
       print(RheniumSymbol)
    elif Element == "Atomic Number":
       print(RheniumAtomicNumber)
    elif Element == "Group":
        print(RheniumGroup)
    elif Element == "Period":
        print(RheniumPeriod)
              
#Osmium

OsmiumSymbol = "Os"
OsmiumAtomicNumber = 76
OsmiumAtomicMass = 190.23
OsmiumGroup = 8
OsmiumPeriod = 6

if Element == "Osmium":
    Element = input("What would you like to know about Osmium?: ")
    if Element == "Atomic Mass":
       print(OsmiumAtomicMass)
    elif Element == "Symbol":
       print(OsmiumSymbol)
    elif Element == "Atomic Number":
       print(OsmiumAtomicNumber)
    elif Element == "Group":
        print(OsmiumGroup)
    elif Element == "Period":
        print(OsmiumPeriod)

#Iridium

IridiumSymbol = "Ir"
IridiumAtomicNumber = 77
IridiumAtomicMass = 192.217
IridiumGroup = 9
IridiumPeriod = 6
              
if Element == "Iridium":
    Element = input("What would you like to know about Iridium?: ")
    if Element == "Atomic Mass":
       print(IridiumAtomicMass)
    elif Element == "Symbol":
       print(IridiumSymbol)
    elif Element == "Atomic Number":
       print(IridiumAtomicNumber)
    elif Element == "Group":
        print(IridiumGroup)
    elif Element == "Period":
        print(IridiumPeriod)

#Platinum

PlatinumSymbol = "Pt"
PlatinumAtomicNumber = 78
PlatinumAtomicMass = 195.084
PlatinumGroup = 10
PlatinumPeriod = 6

if Element == "Platinum":
    Element = input("What would you like to know about Platinum?: ")
    if Element == "Atomic Mass":
       print(PlatinumAtomicMass)
    elif Element == "Symbol":
       print(PlatinumSymbol)
    elif Element == "Atomic Number":
       print(PlatinumAtomicNumber)
    elif Element == "Group":
        print(PlatinumGroup)
    elif Element == "Period":
        print(PlatinumPeriod)

#Gold

GoldSymbol = "Au"
GoldAtomicNumber = 79
GoldAtomicMass = 196.966569
GoldGroup = 11
GoldPeriod = 6

if Element == "Gold":
    Element = input("What would you like to know about Gold?: ")
    if Element == "Atomic Mass":
       print(GoldAtomicMass)
    elif Element == "Symbol":
       print(GoldSymbol)
    elif Element == "Atomic Number":
       print(GoldAtomicNumber)
    elif Element == "Group":
        print(GoldGroup)
    elif Element == "Period":
        print(GoldPeriod)

#MERCURY
MercurySymbol = "Hg"
MercuryAtomicNumber = 80
MercuryAtomicMass = 200.592
MercuryGroup = 12
MercuryPeriod = 6

if Element == "Mercury":
    Element = input("What would you like to know about Mercury?: ")
    if Element == "Atomic Mass":
       print(MercuryAtomicMass)
    elif Element == "Symbol":
       print(MercurySymbol)
    elif Element == "Atomic Number":
       print(MercuryAtomicNumber)
    elif Element == "Group":
        print(MercuryGroup)
    elif Element == "Period":
        print(MercuryPeriod)

#THALLIUM
ThalliumSymbol = "TI"
ThalliumAtomicNumber = 81
ThalliumAtomicMass = 204.38

if Element == "Thallium":
    Element = input("What would you like to know about Thallium?: ")
    if Element == "Atomic Mass":
       print(ThalliumAtomicMass)
    elif Element == "Symbol":
       print(ThalliumSymbol)
    elif Element == "Atomic Number":
       print(ThalliumAtomicNumber)

#LEAD
LeadSymbol = "Pb"
LeadAtomicNumber = 82
LeadAtomicMass = 207.2
LeadGroup = 14
LeadPeriod = 6

if Element == "Lead":
    Element = input("What would you like to know about Lead?: ")
    if Element == "Atomic Mass":
       print(LeadAtomicMass)
    elif Element == "Symbol":
       print(LeadSymbol)
    elif Element == "Atomic Number":
       print(LeadAtomicNumber)
    elif Element == "Group":
        print(LeadGroup)
    elif Element == "Period":
        print(LeadPeriod)

#BISMUTH
BismuthSymbol = "Bi"
BismuthAtomicNumber = 83
BismuthAtomicMass = 208.98040
BismuthGroup = 15
BismuthPeriod = 6

if Element == "Bismuth":
    Element = input("What would you like to know about Bismuth?: ")
    if Element == "Atomic Mass":
       print(BismuthAtomicMass)
    elif Element == "Symbol":
       print(BismuthSymbol)
    elif Element == "Atomic Number":
       print(BismuthAtomicNumber)
    elif Element == "Group":
        print(BismuthGroup)
    elif Element == "Period":
        print(BismuthPeriod)

#POLONIUM
PoloniumSymbol = "Po"
PoloniumAtomicNumber = 84
PoloniumAtomicMass = 209
PoloniumGroup = 16
PoloniumPeriod = 6

if Element == "Polonium":
    Element = input("What would you like to know about Polonium?: ")
    if Element == "Atomic Mass":
       print(PoloniumAtomicMass)
    elif Element == "Symbol":
       print(PoloniumSymbol)
    elif Element == "Atomic Number":
       print(PoloniumAtomicNumber)
    elif Element == "Group":
        print(PoloniumGroup)
    elif Element == "Period":
        print(PoloniumPeriod)

#ASTATINE
AstatineSymbol = "At"
AstatineAtomicNumber = 85
AstatineAtomicMass = 210
AstatineGroup = 17
AstatinePeriod = 6

if Element == "Astatine":
    Element = input("What would you like to know about Astatine?: ")
    if Element == "Atomic Mass":
       print(AstatineAtomicMass)
    elif Element == "Symbol":
       print(AstatineSymbol)
    elif Element == "Atomic Number":
       print(AstatineAtomicNumber)
    elif Element == "Group":
        print(AstatineGroup)
    elif Element == "Period":
        print(AstatinePeriod)

#RADON
RadonSymbol = "Rn"
RadonAtomicNumber = 86
RadonAtomicMass = 222
RadonGroup = 18
RadonPeriod = 6

if Element == "Radon":
    Element = input("What would you like to know about Radon?: ")
    if Element == "Atomic Mass":
       print(RadonAtomicMass)
    elif Element == "Symbol":
       print(RadonSymbol)
    elif Element == "Atomic Number":
       print(RadonAtomicNumber)
    elif Element == "Group":
        print(RadonGroup)
    elif Element == "Period":
        print(RadonPeriod)

#FRANCIUM
FranciumSymbol = "Fr"
FranciumAtomicNumber = 87
FranciumAtomicMass = 223
FranciumGroup = 1
FranciumPeriod = 7

if Element == "Francium":
    Element = input("What would you like to know about Francium?: ")
    if Element == "Atomic Mass":
       print(FranciumAtomicMass)
    elif Element == "Symbol":
       print(FranciumSymbol)
    elif Element == "Atomic Number":
       print(FranciumAtomicNumber)
    elif Element == "Group":
        print(FranciumGroup)
    elif Element == "Period":
        print(FranciumPeriod)

#RADIUM
RadiumSymbol = "Ra"
RadiumAtomicNumber = 88
RadiumAtomicMass = 226
RadiumGroup = 2
RadiumPeriod = 7

if Element == "Radium":
    Element = input("What would you like to know about Radium?: ")
    if Element == "Atomic Mass":
       print(RadiumAtomicMass)
    elif Element == "Symbol":
       print(RadiumSymbol)
    elif Element == "Atomic Number":
       print(RadiumAtomicNumber)
    elif Element == "Group":
        print(RadiumGroup)
    elif Element == "Period":
        print(RadiumPeriod)

#ACTINIUM
ActiniumSymbol = "Ac"
ActiniumAtomicNumber = 89
ActiniumAtomicMass = 227
ActiniumGroup = "none"
ActiniumPeriod = 7

if Element == "Actinium":
    Element = input("What would you like to know about Actinium?: ")
    if Element == "Atomic Mass":
       print(ActiniumAtomicMass)
    elif Element == "Symbol":
       print(ActiniumSymbol)
    elif Element == "Atomic Number":
       print(ActiniumAtomicNumber)
    elif Element == "Group":
        print(ActiniumGroup)
    elif Element == "Period":
        print(ActiniumPeriod)

#THORIUM
ThoriumSymbol = "Th"
ThoriumAtomicNumber = 90
ThoriumAtomicMass = 232.0377
ThoriumGroup = "none"
ThoriumPeriod = 7

if Element == "Thorium":
    Element = input("What would you like to know about Thorium?: ")
    if Element == "Atomic Mass":
       print(ThoriumAtomicMass)
    elif Element == "Symbol":
       print(ThoriumSymbol)
    elif Element == "Atomic Number":
       print(ThoriumAtomicNumber)
    elif Element == "Group":
        print(ThoriumGroup)
    elif Element == "Period":
        print(ThoriumPeriod)

#PROTACTINIUM
ProtactiniumSymbol = "Pa"
ProtactiniumAtomicNumber = 91
ProtactiniumAtomicMass = 231.03588
ProtactiniumGroup = "none"
ProtactiniumPeriod = 7

if Element == "Protactinium":
    Element = input("What would you like to know about Protactinium?: ")
    if Element == "Atomic Mass":
       print(ProtactiniumAtomicMass)
    elif Element == "Symbol":
       print(ProtactiniumSymbol)
    elif Element == "Atomic Number":
       print(ProtactiniumAtomicNumber)
    elif Element == "Group":
        print(ProtactiniumGroup)
    elif Element == "Period":
        print(ProtactiniumPeriod)

#URANIUM
UraniumSymbol = "U"
UraniumAtomicNumber = 92
UraniumAtomicMass = 238.02891
UraniumGroup = "none"
UraniumPeriod = 7

if Element == "Uranium":
    Element = input("What would you like to know about Uranium?: ")
    if Element == "Atomic Mass":
       print(UraniumAtomicMass)
    elif Element == "Symbol":
       print(UraniumSymbol)
    elif Element == "Atomic Number":
       print(UraniumAtomicNumber)

#NEPTUNIUM
NeptuniumSymbol = "Np"
NeptuniumAtomicNumber = 93
NeptuniumAtomicMass = 237
NeptuniumGroup = "none"
NeptuniumPeriod = 7

if Element == "Neptunium":
    Element = input("What would you like to know about Neptunium?: ")
    if Element == "Atomic Mass":
       print(NeptuniumAtomicMass)
    elif Element == "Symbol":
       print(NeptuniumSymbol)
    elif Element == "Atomic Number":
       print(NeptuniumAtomicNumber)
    elif Element == "Group":
        print(NeptuniumGroup)
    elif Element == "Period":
        print(NeptuniumPeriod)
              
#PLUTONIUM
PlutoniumSymbol = "Pu"
PlutoniumAtomicNumber = 94
PlutoniumAtomicMass = 244
PlutoniumGroup = "none"
PlutoniumPeriod = 7

if Element == "Plutonium":
    Element = input("What would you like to know about Plutonium?: ")
    if Element == "Atomic Mass":
       print(PlutoniumAtomicMass)
    elif Element == "Symbol":
       print(PlutoniumSymbol)
    elif Element == "Atomic Number":
       print(PlutoniumAtomicNumber)
    elif Element == "Group":
        print(PlutoniumGroup)
    elif Element == "Period":
        print(PlutoniumPeriod)

#AMERICIUM
AmericiumSymbol = "Am"
AmericiumAtomicNumber = 95
AmericiumAtomicMass = 243
AmericiumGroup = "none"
AmericiumPeriod = 7

if Element == "Americium":
    Element = input("What would you like to know about Americium?: ")
    if Element == "Atomic Mass":
       print(AmericiumAtomicMass)
    elif Element == "Symbol":
       print(AmericiumSymbol)
    elif Element == "Atomic Number":
       print(AmericiumAtomicNumber)
    elif Element == "Group":
        print(AmericiumGroup)
    elif Element == "Period":
        print(AmericiumPeriod)

#CURIUM
CuriumSymbol = "Cm"
CuriumAtomicNumber = 96
CuriumAtomicMass = 247
CuriumGroup = "none"
CuriumPeriod = 7

if Element == "Curium":
    Element = input("What would you like to know about Curium?: ")
    if Element == "Atomic Mass":
       print(CuriumAtomicMass)
    elif Element == "Symbol":
       print(CuriumSymbol)
    elif Element == "Atomic Number":
       print(CuriumAtomicNumber)
    elif Element == "Group":
        print(CuriumGroup)
    elif Element == "Period":
        print(CuriumPeriod)

#BERKELIUM
BerkeliumSymbol = "Bk"
BerkeliumAtomicNumber = 97
BerkeliumAtomicMass = 247
BerkeliumGroup = "none"
BerkeliumPeriod = 7

if Element == "Berkelium":
    Element = input("What would you like to know about Berkelium?: ")
    if Element == "Atomic Mass":
       print(BerkeliumAtomicMass)
    elif Element == "Symbol":
       print(BerkeliumSymbol)
    elif Element == "Atomic Number":
       print(BerkeliumAtomicNumber)
    elif Element == "Group":
        print(BerkeliumGroup)
    elif Element == "Period":
        print(BerkeliumPeriod)

#CALIFORNIUM
CaliforniumSymbol = "Cf"
CaliforniumAtomicNumber = 98
CaliforniumAtomicMass = 251
CaliforniumGroup = "none"
CaliforniumPeriod = 7

if Element == "Californium":
    Element = input("What would you like to know about Californium?: ")
    if Element == "Atomic Mass":
       print(CaliforniumAtomicMass)
    elif Element == "Symbol":
       print(CaliforniumSymbol)
    elif Element == "Atomic Number":
       print(CaliforniumAtomicNumber)
    elif Element == "Group":
        print(CaliforniumGroup)
    elif Element == "Period":
        print(CaliforniumPeriod)

#EINSTEINIUM
EinsteiniumSymbol = "Es"
EinsteiniumAtomicNumber = 99
EinsteiniumAtomicMass = 252
EinsteiniumGroup = "none"
EinsteiniumPeriod = 7

if Element == "Einsteinium":
    Element = input("What would you like to know about Einsteinium?: ")
    if Element == "Atomic Mass":
       print(EinsteiniumAtomicMass)
    elif Element == "Symbol":
       print(EinsteiniumSymbol)
    elif Element == "Atomic Number":
       print(EinsteiniumAtomicNumber)
    elif Element == "Group":
        print(EinsteiniumGroup)
    elif Element == "Period":
        print(EinsteiniumPeriod)

#FERMIUM
FermiumSymbol = "Fm"
FermiumAtomicNumber = 100
FermiumAtomicMass = 257
FermiumGroup = "none"
FermiumPeriod = 7

if Element == "Fermium":
    Element = input("What would you like to know about Fermium?: ")
    if Element == "Atomic Mass":
       print(FermiumAtomicMass)
    elif Element == "Symbol":
       print(FermiumSymbol)
    elif Element == "Atomic Number":
       print(FermiumAtomicNumber)
    elif Element == "Group":
        print(FermiumGroup)
    elif Element == "Period":
        print(FermiumPeriod)

#MENDELEVIUM
MendeleviumSymbol = "Md"
MendeleviumAtomicNumber = 101
MendeleviumAtomicMass = 258
MendeleviumGroup = "none"
MendeleviumPeriod = 7

if Element == "Mendelevium":
    Element = input("What would you like to know about Mendelevium?: ")
    if Element == "Atomic Mass":
       print(MendeleviumAtomicMass)
    elif Element == "Symbol":
       print(MendeleviumSymbol)
    elif Element == "Atomic Number":
       print(MendeleviumAtomicNumber)
    elif Element == "Group":
        print(MendeleviumGroup)
    elif Element == "Period":
        print(MendeleviumPeriod)

#NOBELIUM
NobeliumSymbol = "No"
NobeliumAtomicNumber = 102
NobeliumAtomicMass = 259
NobeliumGroup = "none"
NobeliumPeriod = 7

if Element == "Nobelium":
    Element = input("What would you like to know about Nobelium?: ")
    if Element == "Atomic Mass":
       print(NobeliumAtomicMass)
    elif Element == "Symbol":
       print(NobeliumSymbol)
    elif Element == "Atomic Number":
       print(NobeliumAtomicNumber)
    elif Element == "Group":
        print(NobeliumGroup)
    elif Element == "Period":
        print(NobeliumPeriod)

#LAWRENCIUM
LawrenciumSymbol = "Lr"
LawrenciumAtomicNumber = 103
LawrenciumAtomicMass = 262
LawrenciumGroup = "none"
LawrenciumPeriod = 7

if Element == "Lawrencium":
    Element = input("What would you like to know about Lawrencium?: ")
    if Element == "Atomic Mass":
       print(LawrenciumAtomicMass)
    elif Element == "Symbol":
       print(LawrenciumSymbol)
    elif Element == "Atomic Number":
       print(LawrenciumAtomicNumber)
    elif Element == "Group":
        print(LawrenciumGroup)
    elif Element == "Period":
        print(LawrenciumPeriod)

#RUTHERFORDIUM
RutherfordiumSymbol = "Rf"
RutherfordiumAtomicNumber = 104
RutherfordiumAtomicMass = 261
RutherfordiumGroup = 4
RutherfordiumPeriod = 7

if Element == "Rutherfordium":
    Element = input("What would you like to know about Rutherfordium?: ")
    if Element == "Atomic Mass":
       print(RutherfordiumAtomicMass)
    elif Element == "Symbol":
       print(RutherfordiumSymbol)
    elif Element == "Atomic Number":
       print(RutherfordiumAtomicNumber)
    elif Element == "Group":
        print(RutherfordiumGroup)
    elif Element == "Period":
        print(RutherfordiumPeriod)

#DUBNIUM
DubniumSymbol = "Db"
DubniumAtomicNumber = 105
DubniumAtomicMass = 262
DubniumGroup = 5
DubniumPeriod = 7

if Element == "Dubnium":
    Element = input("What would you like to know about Dubnium?: ")
    if Element == "Atomic Mass":
       print(DubniumAtomicMass)
    elif Element == "Symbol":
       print(DubniumSymbol)
    elif Element == "Atomic Number":
       print(DubniumAtomicNumber)
    elif Element == "Group":
        print(DubniumGroup)
    elif Element == "Period":
        print(DubniumPeriod)

#SEABORGIUM
SeaborgiumSymbol = "Sg"
SeaborgiumAtomicNumber = 106
SeaborgiumAtomicMass = 266
SeaborgiumGroup = 6
SeaborgiumPeriod = 7

if Element == "Seaborgium":
    Element = input("What would you like to know about Seaborgium?: ")
    if Element == "Atomic Mass":
       print(SeaborgiumAtomicMass)
    elif Element == "Symbol":
       print(SeaborgiumSymbol)
    elif Element == "Atomic Number":
       print(SeaborgiumAtomicNumber)
    elif Element == "Group":
        print(SeaborgiumGroup)
    elif Element == "Period":
        print(SeaborgiumPeriod)

#BOHRIUM
BohriumSymbol = "Bh"
BohriumAtomicNumber = 107
BohriumAtomicMass = 264
BohriumGroup = 7
BohriumPeriod = 7

if Element == "Bohrium":
    Element = input("What would you like to know about Bohrium?: ")
    if Element == "Atomic Mass":
       print(BohriumAtomicMass)
    elif Element == "Symbol":
       print(BohriumSymbol)
    elif Element == "Atomic Number":
       print(BohriumAtomicNumber)
    elif Element == "Group":
        print(BohriumGroup)
    elif Element == "Period":
        print(BohriumPeriod)

#HASSIUM
HassiumSymbol = "Hs"
HassiumAtomicNumber = 108
HassiumAtomicMass = 277
HassiumGroup = 8
HassiumPeriod = 7

if Element == "Hassium":
    Element = input("What would you like to know about Hassium?: ")
    if Element == "Atomic Mass":
       print(HassiumAtomicMass)
    elif Element == "Symbol":
       print(HassiumSymbol)
    elif Element == "Atomic Number":
       print(HassiumAtomicNumber)
    elif Element == "Group":
        print(HassiumGroup)
    elif Element == "Period":
        print(HassiumPeriod)

#MEITNERIUM
MeitneriumSymbol = "Mt"
MeitneriumAtomicNumber = 109
MeitneriumAtomicMass = 268
MeitneriumGroup = 9
MeitneriumPeriod = 7

if Element == "Meitnerium":
    Element = input("What would you like to know about Meitnerium?: ")
    if Element == "Atomic Mass":
       print(MeitneriumAtomicMass)
    elif Element == "Symbol":
       print(MeitneriumSymbol)
    elif Element == "Atomic Number":
       print(MeitneriumAtomicNumber)
    elif Element == "Group":
        print(MeitneriumGroup)
    elif Element == "Period":
        print(MeitneriumPeriod)

#Darmstadtium

DarmstadtiumSymbol = "Ds"
DarmstadtiumAtomicNumber = 110
DarmstadtiumAtomicMass = 281
DarmstadtiumGroup = 10 
DarmstadtiumPeriod = 7

if Element == "Darmstadtium":
    Element = input("What would you like to know about Darmstadtium?: ")
    if Element == "Atomic Mass":
       print(DarmstadtiumAtomicMass)
    elif Element == "Symbol":
       print(DarmstadtiumSymbol)
    elif Element == "Atomic Number":
       print(DarmstadtiumAtomicNumber)
    elif Element == "Group":
        print(DarmstadtiumGroup)
    elif Element == "Period":
        print(DarmstadtiumPeriod)

#Roentgenium

RoentgeniumSymbol = "Rg"
RoentgeniumAtomicNumber = 111
RoentgeniumAtomicMass = 282
RoentgeniumGroup = 11
RoentgeniumPeriod = 7

if Element == "Roentgenium":
    Element = input("What would you like to know about Roentgenium?: ")
    if Element == "Atomic Mass":
       print(RoentgeniumAtomicMass)
    elif Element == "Symbol":
       print(RoentgeniumSymbol)
    elif Element == "Atomic Number":
       print(RoentgeniumAtomicNumber)
    elif Element == "Group":
        print(RoentgeniumGroup)
    elif Element == "Period":
        print(RoentgeniumPeriod)

#Copernicium

CoperniciumSymbol = "Cn"
CoperniciumAtomicNumber = 112
CoperniciumAtomicMass = 285
CoperniciumGroup = 12
CoperniciumPeriod = 7

if Element == "Copernicium":
    Element = input("What would you like to know about Copernicium?: ")
    if Element == "Atomic Mass":
       print(CoperniciumAtomicMass)
    elif Element == "Symbol":
       print(CoperniciumSymbol)
    elif Element == "Atomic Number":
       print(CoperniciumAtomicNumber)
    elif Element == "Group":
        print(CoperniciumGroup)
    elif Element == "Period":
        print(CoperniciumPeriod)

#Ununtrium

UnuntriumSymbol = "Uut"
UnuntriumAtomicNumber = 113
UnuntriumAtomicMass = 286
UnuntriumGroup = 13
UnuntriumPeriod = 7

if Element == "Ununtrium":
    Element = input("What would you like to know about Ununtrium?: ")
    if Element == "Atomic Mass":
       print(UnuntriumAtomicMass)
    elif Element == "Symbol":
       print(UnuntriumSymbol)
    elif Element == "Atomic Number":
       print(UnuntriumAtomicNumber)
    elif Element == "Group":
        print(UnuntriumGroup)
    elif Element == "Period":
        print(UnuntriumPeriod)

#Flerovium

FleroviumSymbol = "Fl"
FleroviumAtomicNumber = 114
FleroviumAtomicMass = 289
FleroviumGroup = 14
FleroviumPeriod = 7

if Element == "Flerovium":
    Element = input("What would you like to know about Flerovium?: ")
    if Element == "Atomic Mass":
       print(FleroviumAtomicMass)
    elif Element == "Symbol":
       print(FleroviumSymbol)
    elif Element == "Atomic Number":
       print(FleroviumAtomicNumber)
    elif Element == "Group":
        print(FleroviumGroup)
    elif Element == "Period":
        print(FleroviumPeriod)

#Ununpentium

UnunpentiumSymbol = "Uup"
UnunpentiumAtomicNumber = 115
UnunpentiumAtomicMass = 289
UnunpentiumGroup = 15
UnunpentiumPeriod = 7

if Element == "Ununpentium":
    Element = input("What would you like to know about Ununpentium?: ")
    if Element == "Atomic Mass":
       print(UnunpentiumAtomicMass)
    elif Element == "Symbol":
       print(UnunpentiumSymbol)
    elif Element == "Atomic Number":
       print(UnunpentiumAtomicNumber)
    elif Element == "Group":
        print(UnunpentiumGroup)
    elif Element == "Period":
        print(UnunpentiumPeriod)

#Livermorium

LivermoriumSymbol = "Lv"
LivermoriumAtomicNumber = 116
LivermoriumAtomicMass = 293
LivermoriumGroup = 16
LivermoriumPeriod = 7

if Element == "Livermorium":
    Element = input("What would you like to know about Livermorium?: ")
    if Element == "Atomic Mass":
       print(LivermoriumAtomicMass)
    elif Element == "Symbol":
       print(LivermoriumSymbol)
    elif Element == "Atomic Number":
       print(LivermoriumAtomicNumber)
    elif Element == "Group":
        print(LivermoriumGroup)
    elif Element == "Period":
        print(LivermoriumPeriod)


#Ununseptium

UnunseptiumSymbol = "Uus"
UnunseptiumAtomicNumber = 117
UnunseptiumAtomicMass = 294
UnunseptiumGroup = 17
UnunseptiumPeriod = 7

if Element == "Ununseptium":
    Element = input("What would you like to know about Ununseptium?: ")
    if Element == "Atomic Mass":
       print(UnunseptiumAtomicMass)
    elif Element == "Symbol":
       print(UnunseptiumSymbol)
    elif Element == "Atomic Number":
       print(UnunseptiumAtomicNumber)
    elif Element == "Group":
        print(UnunseptiumGroup)
    elif Element == "Period":
        print(UnunseptiumPeriod)


#Ununoctium

UnunoctiumSymbol = "Uuo"
UnunoctiumAtomicNumber = 118
UnunoctiumAtomicMass = 294
UnunoctiumGroup = 18
UnunoctiumPeriod = 7

if Element == "Ununoctium":
    Element = input("What would you like to know about Ununoctium?: ")
    if Element == "Atomic Mass":
       print(UnunoctiumAtomicMass)
    elif Element == "Symbol":
       print(UnunoctiumSymbol)
    elif Element == "Atomic Number":
       print(UnunoctiumAtomicNumber)
    elif Element == "Group":
        print(UnunoctiumGroup)
    elif Element == "Period":
        print(UnunoctiumPeriod)

#THE KEY
"""
print("USER GUIDE:\n"
      "Inputs are case sensitive. Please input as shown.\n"
      "What chemical compound would you like to know more about?\n"
      "input: Acetic Acid\n"
      "or\n"
      "input: Iron(II) Sulfate\n"
      "What would you like to know about Iron(II) Sulfate?\n"
      "input: Molar Mass\n"
      "or\n"
      "input: Molecular Formula\n\n")

"""

#1ACETADEHYDE
AcetaldehydeFormula = "C2H4O" 
AcetaldehydeMass = 59.067

if Element == "Acetaldehyde":
    Element = input("What would you like to know about Acetaldehyde? ")
    if Element == "Molar Mass":
        print(AcetaldehydeMass)
    elif Element == "Molecular Formula":
        print(AcetaldehydeFormula)

#2ACETAMIDE
AcetamideFormula = "C2H5NO" 
AcetamideMass = 59.067

if Element == "Acetamide":
    Element = input("What would you like to know about Acetamide? ")
    if Element == "Molar Mass":
        print(AcetamideMass)
    elif Element == "Molecular Formula":
        print(AcetamideFormula)
 
#3ACETICACID
AceticAcidFormula = "CH3COOH" 
AceticAcidMass = 96.086

if Element == "Acetic Acid":
    Element = input("What would you like to know about Acetic Acid? ")
    if Element == "Molar Mass":
        print(AceticAcidMass)
    elif Element == "Molecular Formula":
        print(AceticAcidFormula)

#4ACETONE
AcetoneFormula = "C3H6O" 
AcetoneMass = 17.031

if Element == "Acetone":
    Element = input("What would you like to know about Acetone? ")
    if Element == "Molar Mass":
        print(AcetoneMass)
    elif Element == "Molecular Formula":
        print(AcetoneFormula)
 
 #5ACETONITRILE
AcetoneFormula = "C2H3N" 
AcetoneMass = 77.082

if Element == "Acetone":
    Element = input("What would you like to know about Acetone? ")
    if Element == "Molar Mass":
        print(AcetoneMass)
    elif Element == "Molecular Formula":
        print(AcetoneFormula)
 
#6ALUMINIUMCHLORIDE
AluminiumChlorideFormula = "AICI3" 
AluminiumChlorideMass = 62.068

if Element == "Aluminium Chloride":
    Element = input("What would you like to know about Aluminium Chloride? ")
    if Element == "Molar Mass":
        print(AluminiumChlorideMass)
    elif Element == "Molecular Formula":
        print(AluminiumChlorideFormula)

#7ALUMINIUMNITRATE
AluminiumNitrateFormula = "AI[NO]33" 
AluminiumNitrateMass = 368.343

if Element == "Aluminium Nitrate":
    Element = input("What would you like to know about Aluminium Nitrate? ")
    if Element == "Molar Mass":
        print(AluminiumNitrateMass)
    elif Element =="Molecular Formula":
        print(AluminiumNitrateFormula)

#8ALUMINIUMSULFATE
AluminiumSulfateFormula = "AI2[SO4]3" 
AluminiumSulfateMass = 68.007

if Element == "Aluminium Sulfate":
    Element = input("What would you like to know about Aluminium Sulfate? ")
    if Element == "Molar Mass":
        print(AluminiumSulfateMass)
    elif Element =="Molecular Formula":
        print(AluminiumSulfateFormula)

#9AMMONIA
AmmoniaFormula = "NH3" 
AmmoniaMass = 158.335

if Element == "Ammonia":
    Element = input("What would you like to know about Ammonia? ")
    if Element == "Molar Mass":
        print(AmmoniaMass)
    elif Element =="Molecular Formula":
        print(AmmoniaFormula)

#10AMMONIUMACETATE
AmmoniumAcetateFormula = "CH3COONH4" 
AmmoniumAcetateMass = 41.052

if Element == "Ammonium Acetate":
    Element = input("What would you like to know about Ammonium Acetate? ")
    if Element == "Molar Mass":
        print(AmmoniumAcetateMass)
    elif Element =="Molecular Formula":
        print(AmmoniumAcetateFormula)

#11AMMONIUMCARBONATE
AmmoniumCarbonateFormula = "[NH4]2CO3" 
AmmoniumCarbonateMass = 134.452

if Element == "AmmoniumCarbonate":
    Element = input("What would you like to know about Ammonium Carbonate? ")
    if Element == "Molar Mass":
        print(AmmoniumCarbonateMass)
    elif Element =="Molecular Formula":
        print(AmmoniumCarbonateFormula)

#12AMMONIUMCHLORIDE
AmmoniumChlorideFormula = "NH4Cl" 
AmmoniumChlorideMass = 30.026

if Element == "Ammonium Chloride":
    Element = input("What would you like to know about Ammonium Chloride? ")
    if Element == "Molar Mass":
        print(AmmoniumChlorideMass)
    elif Element =="Molecular Formula":
        print(AmmoniumChlorideFormula)

#13AMMONIUMDICHROMATE
AmmoniumDichromateFormula = "[NH4]2Cr2O7" 
AmmoniumDichromateMass = 278.106

if Element == "Ammonium Dichromate":
    Element = input("What would you like to know about Ammonium Dichromate? ")
    if Element == "Molar Mass":
        print(AmmoniumDichromateMass)
    elif Element =="Molecular Formula":
        print(AmmoniumDichromateFormula)

#14AMMONIUMHYDROXIDE
AmmoniumHydroxideFormula = "NH4OH" 
AmmoniumHydroxideMass = 100.459

if Element == "Ammonium Hydroxide":
    Element = input("What would you like to know about Ammonium Hydroxide? ")
    if Element == "Molar Mass":
        print(AmmoniumHydroxideMass)
    elif Element =="Molecular Formula":
        print(AmmoniumHydroxideFormula)

#15AMMONIUMNITRATE
AmmoniumNitrateFormula = "NH4NO3" 
AmmoniumNitrateMass = 329.244

if Element == "Ammonium Nitrate":
    Element = input("What would you like to know about Ammonium Nitrate? ")
    if Element == "Molar Mass":
        print(AmmoniumNitrateMass)
    elif Element =="Molecular Formula":
        print(AmmoniumNitrateFormula)

#AMMONIUMOXALATE
AmmoniumOxalateFormula = "[NH4]2C2O4" 
AmmoniumOxalateMass = 207.889

if Element == "Ammonium Oxalate":
    Element = input("What would you like to know about Ammonium Oxalate? ")
    if Element == "Molar Mass":
        print(AmmoniumOxalateMass)
    elif Element =="Molecular Formula":
        print(AmmoniumOxalateFormula)

#17AMMONIUMSULFATE
AmmoniumSulfateFormula = "[NH4]2SO4" 
AmmoniumSulfateMass = 84.007

if Element == "Ammonium Sulfate":
    Element = input("What would you like to know about Ammonium Sulfate? ")
    if Element == "Molar Mass":
        print(AmmoniumSulfateMass)
    elif Element =="Molecular Formula":
        print(AmmoniumSulfateFormula)

#18ANTIMONY(III)CHLORIDE
AntimonyIIIChlorideFormula = "SbCl3" 
AntimonyIIIChlorideMass = 46.025

if Element == "Antimony(III) Chloride":
    Element = input("What would you like to know about Antimony(III) Chloride? ")
    if Element == "Molar Mass":
        print(AntimonyIIIChlorideMass)
    elif Element =="Molecular Formula":
        print(AntimonyIIIChlorideFormula)

#19ANTIMONY(V)CHLORIDE
AntimonyVChlorideFormula = "SbCl5" 
AntimonyVChlorideMass = 180.156

if Element == "Antimony(V) Chloride":
    Element = input("What would you like to know about Antimony(V) Chloride? ")
    if Element == "Molar Mass":
        print(AntimonyVChlorideMass)
    elif Element =="Molecular Formula":
        print(AntimonyVChlorideFormula)

#20BARIUMCHLORIDE
BariumChlorideFormula = "BaCl2" 
BariumChlorideMass = 180.156

if Element == "Barium Chloride":
    Element = input("What would you like to know about Barium Chloride? ")
    if Element == "Molar Mass":
        print(BariumChlorideMass)
    elif Element =="Molecular Formula":
        print(BariumChlorideFormula)

#21BARIUMHYDROXIDE
BariumHydroxideFormula = "Ba[OH]2" 
BariumHydroxideMass = 94.111

if Element == "Barium Hydroxide":
    Element = input("What would you like to know about Barium Hydroxide? ")
    if Element == "Molar Mass":
        print(BariumHydroxideMass)
    elif Element =="Molecular Formula":
        print(BariumHydroxideFormula)

#22BARIUMNITRATE
BariumNitrateFormula = "Ba[NO3]2" 
BariumNitrateMass = 56.106

if Element == "Barium Nitrate":
    Element = input("What would you like to know about Barium Nitrate? ")
    if Element == "Molar Mass":
        print(BariumNitrateMass)
    elif Element =="Molecular Formula":
        print(BariumNitrateFormula)

#23BISMUTHIIICHLORIDE
BariumIIIChlorideFormula = "BiCI3" 
BariumIIIChlorideMass = 92.094

if Element == "Barium(III) Chloride":
    Element = input("What would you like to know about Barium(III) Chloride? ")
    if Element == "Molar Mass":
        print(BariumIIIChlorideMass)
    elif Element =="Molecular Formula":
        print(BariumIIIChlorideFormula)

#24BISMUTH(III)NITRATE
BariumIIINitrateFormula = "Bi[NO3]3" 
BariumIIINitrateMass = 214.001

if Element == "Barium(III) Nitrate":
    Element = input("What would you like to know about Barium(III) Nitrate? ")
    if Element == "Molar Mass":
        print(BariumIIINitrateMass)
    elif Element =="Molecular Formula":
        print(BariumIIINitrateFormula)

#25BUTAN1OL
Butan1olFormula = "C4H10O" 
Butan1olMass = 197.998

if Element == "Butan1-ol":
    Element = input("What would you like to know about Butan-1-ol? ")
    if Element == "Molar Mass":
        print(Butan1olMass)
    elif Element =="Molecular Formula":
        print(Butan1olFormula)

#26BUTYRICACID
ButyricAcidFormula = "C4H8O2" 
ButyricAcidMass = 252.065

if Element == "Butyric Acid":
    Element = input("What would you like to know about Butyric Acid? ")
    if Element == "Molar Mass":
        print(ButyricAcidMass)
    elif Element =="Molecular Formula":
        print(ButyricAcidFormula)

#27CADMIUMNITRATE
CadmiumNitrateFormula = "Cd[NO3]2" 
CadmiumNitrateMass = 166.003

if Element == "Cadmium Nitrate":
    Element = input("What would you like to know about Cadmium Nitrate? ")
    if Element == "Molar Mass":
        print(CadmiumNitrateMass)
    elif Element =="Molecular Formula":
        print(CadmiumNitrateFormula)

#28CADMIUMSULFATE
CadmiumSulfateFormula = "CdSO4" 
CadmiumSulfateMass = 172.069

if Element == "Cadmium Sulfate":
    Element = input("What would you like to know about Cadmium Sulfate? ")
    if Element == "Molar Mass":
        print(CadmiumSulfateMass)
    elif Element =="Molecular Formula":
        print(CadmiumSulfateFormula)

#CALCIUMCHLORIDE
CalciumChlorideFormula = "Cacl2" 
CalciumChlorideMass = 339.787

if Element == "Calcium Chloride":
    Element = input("What would you like to know about Calcium Chloride? ")
    if Element == "Molar Mass":
        print(CalciumChlorideMass)
    elif Element =="Molecular Formula":
        print(CalciumChlorideFormula)

#30CALCIUMHYDROXIDE
CalciumHydroxideFormula = "Ca[OH]2" 
CalciumHydroxideMass = 97.995

if Element == "Calcium Hydroxide":
    Element = input("What would you like to know about Calcium Hydroxide? ")
    if Element == "Molar Mass":
        print(CalciumHydroxideMass)
    elif Element =="Molecular Formula":
        print(CalciumHydroxideFormula)

#32CALCIUMNITRATE
CalciumDisulfideFormula = "Ca[NO3]2" 
CalciumDisulfideMass = 101.103

if Element == "Calcium Disulfide":
    Element = input("What would you like to know about Calcium Disulfide? ")
    if Element == "Molar Mass":
        print(CalciumDisulfideMass)
    elif Element =="Molecular Formula":
        print(CalciumDisulfideFormula)

#32CALCIUMSULFATE
CalciumSulfateFormula = "CaSO4" 
CalciumSulfateMass = 39.997

if Element == "Calcium Sulfate":
    Element = input("What would you like to know about Calcium Sulfate? ")
    if Element == "Molar Mass":
        print(CalciumSulfateMass)
    elif Element =="Molecular Formula":
        print(CalciumSulfateFormula)

#33CARBONDISULFIDE
CalciumDisulfideFormula = "CS2" 
CalciumDisulfideMass = 116.072

if Element == "Calcium Disulfide":
    Element = input("What would you like to know about Calcium Disulfide? ")
    if Element == "Molar Mass":
        print(CalciumDisulfideMass)
    elif Element =="Molecular Formula":
        print(CalciumDisulfideFormula)

#34CHLOROACETICACID
ChloroaceticAcidFormula = "C2H3ClO2" 
ChloroaceticAcidMass = 132.140

if Element == "ChloroaceticAcid":
    Element = input("What would you like to know about Chloroacetic Acid? ")
    if Element == "Molar Mass":
        print(ChloroaceticAcidMass)
    elif Element =="Molecular Formula":
        print(ChloroaceticAcidFormula)

#35CHLOROAURICACID
ChloroauricAcidFormula = "HAuCl4" 
ChloroauricAcidMass = 76.141

if Element == "Chloroauric Acid":
    Element = input("What would you like to know about Chloroauric Acid? ")
    if Element == "Molar Mass":
        print(ChloroauricAcidMass)
    elif Element =="Molecular Formula":
        print(ChloroauricAcidFormula)

#36CLOROFORM
ChloroaceticAcidFormula = "C2H3CIO2" 
ChloroaceticAcidMass = 132.140

if Element == "Chloroacetic Acid":
    Element = input("What would you like to know about Chloroacetic Acid? ")
    if Element == "Molar Mass":
        print(ChloroaceticAcidMass)
    elif Element =="Molecular Formula":
        print(ChloroaceticAcidFormula)

#37chloroplatinicacid
ChloroplatinicAcidFormula = "H2PtCl6" 
ChloroplatinicAcidMass = 228.119

if Element == "Chloroplatinic Acid":
    Element = input("What would you like to know about Chloroplatinic Acid? ")
    if Element == "Molar Mass":
        print(ChloroplatinicAcidMass)
    elif Element =="Molecular Formula":
        print(ChloroplatinicAcidFormula)

#38chromiumIIIchloride
ChromiumIIIChlorideFormula = "CrCl3" 
ChromiumIIIChlorideMass = 144.092

if Element == "Chromium(III) Chloride":
    Element = input("What would you like to know about Chromium(III) Chloride? ")
    if Element == "Molar Mass":
        print(ChromiumIIIChlorideMass)
    elif Element =="Molecular Formula":
        print(ChromiumIIIChlorideFormula)

#39chromiumIIInitrate
ChromiumIIINitrateFormula = "Cr[NO3]3" 
ChromiumIIINitrateMass = 158.034

if Element == "Chromium(III) Nitrate":
    Element = input("What would you like to know about Chromium(III) Nitrate? ")
    if Element == "Molar Mass":
        print(ChromiumIIINitrateMass)
    elif Element =="Molecular Formula":
        print(ChromiumIIINitrateFormula)

#40chromiumIIIsulfate
ChromiumIIISulfateFormula = "Cr2[SO4]3" 
ChromiumIIISulfateMass = 68.995

if Element == "Chromium(III) Sulfate":
    Element = input("What would you like to know about Chromium(III) Sulfate? ")
    if Element == "Molar Mass":
        print(ChromiumIIISulfateMass)
    elif Element =="Molecular Formula":
        print(ChromiumIIISulfateFormula)

#41chromiumvioxide
ChromiumVIOxideFormula = "CrO3" 
ChromiumVIOxideMass = 102.894

if Element == "Chromium(VI) Oxide":
    Element = input("What would you like to know about Chromium(VI) Oxide? ")
    if Element == "Molar Mass":
        print(ChromiumVIOxideMass)
    elif Element =="Molecular Formula":
        print(ChromiumVIOxideFormula)

#42citricacid
CitricAcidFormula = "C6H8O7" 
CitricAcidMass = 80.043

if Element == "Citric Acid":
    Element = input("What would you like to know about Citric Acid? ")
    if Element == "Molar Mass":
        print(CitricAcidMass)
    elif Element =="Molecular Formula":
        print(CitricAcidFormula)

#43cobaltIInitrate
CobaltIINitrateFormula = "Co[NO3]2" 
CobaltIINitrateMass = 85.104

if Element == "Cobalt(II) Nitrate":
    Element = input("What would you like to know about Cobalt(II) Nitrate? ")
    if Element == "Molar Mass":
        print(CobaltIINitrateMass)
    elif Element =="Molecular Formula":
        print(CobaltIINitrateFormula)

#44cobaltsulfate
CobaltIISulfateFormula = "CoSO4" 
CobaltIISulfateMass = 84.995

if Element == "Cobalt(II) Sulfate":
    Element = input("What would you like to know about Cobalt(II) Sulfate? ")
    if Element == "Molar Mass":
        print(CobaltIISulfateMass)
    elif Element =="Molecular Formula":
        print(CobaltIISulfateFormula)

#45copperIchloride
CopperIChlorideFormula = "Cu2Cl2" 
CopperIChlorideMass = 284.047

if Element == "Copper(I) Chloride":
    Element = input("What would you like to know about Copper(I) Chloride? ")
    if Element == "Molar Mass":
        print(CopperIChlorideMass)
    elif Element =="Molecular Formula":
        print(CopperIChlorideFormula)

#46copperIIchloride
CopperIIChlorideFormula = "CuCl2" 
CopperIIChlorideMass = 151.908

if Element == "Copper(II) Chloride":
    Element = input("What would you like to know about Copper(II) Chloride? ")
    if Element == "Molar Mass":
        print(CopperIIChlorideMass)
    elif Element =="Molecular Formula":
        print(CopperIIChlorideFormula)

#47copperIInitrate
CopperIINitrateFormula = "Cu[NO3]2" 
CopperIINitrateMass = 79.100

if Element == "Copper(II) Nitrate":
    Element = input("What would you like to know about Copper(II) Nitrate? ")
    if Element == "Molar Mass":
        print(CopperIINitrateMass)
    elif Element =="Molecular Formula":
        print(CopperIINitrateFormula)

#48copperIIsulfate
CopperIISulfateFormula = "CuSO4" 
CopperIISulfateMass = 158.526

if Element == "Copper(II) Sulfate":
    Element = input("What would you like to know about Copper(II) Sulfate? ")
    if Element == "Molar Mass":
        print(CopperIISulfateMass)
    elif Element =="Molecular Formula":
        print(CopperIISulfateFormula)

#49dichloroaceticacid
DichloroaceticAcidFormula = "C2H2Cl2H2" 
DichloroaceticAcidMass = 299.025

if Element == "Dichloroacetic Acid":
    Element = input("What would you like to know about Dichloroacetic Acid? ")
    if Element == "Molar Mass":
        print(DichloroaceticAcidMass)
    elif Element =="Molecular Formula":
        print(DichloroaceticAcidFormula)

#50diethylether
DiethylEtherFormula = "[C2H5]2O" 
DiethylEtherMass = 342.296

if Element == "Diethyl Ether":
    Element = input("What would you like to know about Diethyl Ether? ")
    if Element == "Molar Mass":
        print(DiethylEtherMass)
    elif Element =="Molecular Formula":
        print(DiethylEtherFormula)

#51Dimethylglyoxime
DimethylglyoximeFormula = "[CH3CNOH]2" 
DimethylglyoximeMass = 148.315

if Element == "Dimethylglyoxime":
    Element = input("What would you like to know about Dimethylglyoxime? ")
    if Element == "Molar Mass":
        print(DimethylglyoximeMass)
    elif Element =="Molecular Formula":
        print(DimethylglyoximeFormula)

#52DisodiumSalt
DisodiumSaltFormula = "NA2C10H14N2O8" 
DisodiumSaltMass = 120.368

if Element == "Disodium Salt":
    Element = input("What would you like to know about Disodium Salt? ")
    if Element == "Molar Mass":
        print(DisodiumSaltMass)
    elif Element =="Molecular Formula":
        print(DisodiumSaltFormula)

#53Ethanol
EthanolFormula = "C2H5OH" 
EthanolMass = 104.061 

if Element == "Ethanol":
    Element = input("What would you like to know about Ethanol? ")
    if Element == "Molar Mass":
        print(EthanolMass)
    elif Element =="Molecular Formula":
        print(EthanolFormula)

#54EthyleneGlycol
EthyleneGlycolFormula = "[CH2OH]2" 
EthyleneGlycolMass = 125.844

if Element == "Ethylene Glycol":
    Element = input("What would you like to know about Ethylene Glycol? ")
    if Element == "Molar Mass":
        print(EthyleneGlycolMass)
    elif Element =="Molecular Formula":
        print(EthyleneGlycolFormula)

#55Formaldehyde
FormaldehydeFormula = "CH20" 
FormaldehydeMass = 182.172

if Element == "Formaldehyde":
    Element = input("What would you like to know about Formaldehyde? ")
    if Element == "Molar Mass":
        print(FormaldehydeMass)
    elif Element =="Molecular Formula":
        print(FormaldehydeFormula)

#56FormicAcid
FormicAcidFormula = "CH2O2" 
FormicAcidMass = 171.342

if Element == "Formic Acid":
    Element = input("What would you like to know about Formic Acid? ")
    if Element == "Molar Mass":
        print(FormicAcidMass)
    elif Element =="Molecular Formula":
        print(FormicAcidFormula)

#57Fructose
FructoseFormula = "C6H12O6" 
FructoseMass = 296.653

if Element == "Fructose":
    Element = input("What would you like to know about Fructose? ")
    if Element == "Molar Mass":
        print(FructoseMass)
    elif Element =="Molecular Formula":
        print(FructoseFormula)

#58Glucose
GlucoseFormula = "C6H12O6" 
GlucoseMass = 74.079

if Element == "Glucose":
    Element = input("What would you like to know about Glucose? ")
    if Element == "Molar Mass":
        print(GlucoseMass)
    elif Element =="Molecular Formula":
        print(GlucoseFormula)

#59Glycerol
GlycerolFormula = "C3H8O3"
GlycerolMass = 32.042

if Element == "Glycerol":
    Element = input("What would you like to know about Glycerol? ")
    if Element == "Molar Mass":
        print(GlycerolMass)
    elif Element =="Molecular Formula":
        print(GlycerolFormula)

#60HexafluorosilicicAcid
HexafluorosilicicAcidFormula = "H2SiF6"
HexafluorosilicicAcidMass = 315.339

if Element == "Hexafluorosilicic Acid":
    Element = input("What would you like to know about Hexafluorosilicic Acid? ")
    if Element == "Molar Mass":
        print(HexafluorosilicicAcidMass)
    elif Element =="Molecular Formula":
        print(HexafluorosilicicAcidFormula)

#61Hydrazine
HydrazineFormula = "N2H4" 
HydrazineMass = 154.756

if Element == "Hydrazine":
    Element = input("What would you like to know about Hydrazine? ")
    if Element == "Molar Mass":
        print(HydrazineMass)
    elif Element =="Molecular Formula":
        print(HydrazineFormula)

#62HydrobromicAcid
HydrobromicAcidFormula = "HBr" 
HydrobromicAcidMass = 53.491

if Element == "Hydrobromic Acid":
    Element = input("What would you like to know about Hydrobromic Acid? ")
    if Element == "Molar Mass":
        print(HydrobromicAcidMass)
    elif Element =="Molecular Formula":
        print(HydrobromicAcidFormula)

#63HydrochloricAcid
HydrochloricAcidFormula = "HCI" 
HydrochloricAcidMass = 124.096

if Element == "Hydrochloric Acid":
    Element = input("What would you like to know about Hydrochloric Acid? ")
    if Element == "Molar Mass":
        print(HydrochloricAcidMass)
    elif Element =="Molecular Formula":
        print(HydrochloricAcidFormula)

#64HydrocyanicAcid
HydrocyanicAcidFormula = "HCN" 
HydrocyanicAcidMass = 35.046

if Element == "Hydrocyanic Acid":
    Element = input("What would you like to know about Hydrocyanic Acid? ")
    if Element == "Molar Mass":
        print(HydrocyanicAcidMass)
    elif Element =="Molecular Formula":
        print(HydrocyanicAcidFormula)

#65HydrofluoricAcid
HydrofluoricAcidFormula = "HF" 
HydrofluoricAcidMass = 208.233

if Element == "Hydrofluoric Acid":
    Element = input("What would you like to know about Hydrofluoric Acid? ")
    if Element == "Molar Mass":
        print(HydrofluoricAcidMass)
    elif Element =="Molecular Formula":
        print(HydrofluoricAcidFormula)

#66HydrogenPeroxide
HydrogenPeroxideFormula = "H2O2" 
HydrogenPeroxideMass = 106.441

if Element == "Hydrogen Peroxide":
    Element = input("What would you like to know about Hydrogen Peroxide? ")
    if Element == "Molar Mass":
        print(HydrogenPeroxideMass)
    elif Element =="Molecular Formula":
        print(HydrogenPeroxideFormula)

#67HydroiodcAcid
HydroiodcAcidFormula = "HI" 
HydroiodcAcidMass = 119.378

if Element == "Hydroiodc Acid":
    Element = input("What would you like to know about Hydroiodc Acid? ")
    if Element == "Molar Mass":
        print(HydroiodcAcidMass)
    elif Element =="Molecular Formula":
        print(HydroiodcAcidFormula)

#68IodicAcid
IodicAcidFormula = "HIO3" 
IodicAcidMass = 409.818

if Element == "Iodic Acid":
    Element = input("What would you like to know about Iodic Acid? ")
    if Element == "Molar Mass":
        print(IodicAcidMass)
    elif Element =="Molecular Formula":
        print(IodicAcidFormula)

#69IronIIAmmoniumSulfate
IronIIAmmoniumSulfateFormula = "FeSO4[NH4]2SO4" 
IronIIAmmoniumSulfateMass = 189.616

if Element == "Iron(II) Ammonium Sulfate":
    Element = input("What would you like to know about Iron(II) Ammonium Sulfate? ")
    if Element == "Molar Mass":
        print(IronIIAmmoniumSulfateMass)
    elif Element =="Molecular Formula":
        print(IronIIAmmoniumSulfateFormula)

#70IronIISulfate
IronIISulfateFormula = "FeSO4" 
IronIISulfateMass = 163.941

if Element == "Iron(II) Sulfate":
    Element = input("What would you like to know about Iron(II) Sulfate? ")
    if Element == "Molar Mass":
        print(IronIISulfateMass)
    elif Element =="Molecular Formula":
        print(IronIISulfateFormula)

#71IronIIIChloride
IronIIIChlorideFormula = "FeCl3" 
IronIIIChlorideMass = 32.045

if Element == "Iron(III) Chloride":
    Element = input("What would you like to know about Iron(III) Chloride? ")
    if Element == "Molar Mass":
        print(IronIIIChlorideMass)
    elif Element =="Molecular Formula":
        print(IronIIIChlorideFormula)

#72IronIIINitrate
IronIIINitrateFormula = "Fe[NO3]3" 
IronIIINitrateMass = 174.259

if Element == "Iron(III) Nitrate":
    Element = input("What would you like to know about Iron(III) Nitrate? ")
    if Element == "Molar Mass":
        print(IronIIINitrateMass)
    elif Element =="Molecular Formula":
        print(IronIIINitrateFormula)

#73IronIIISulfate
IronIIISulfateFormula = "Fe2[SO4]3" 
IronIIISulfateMass = 210.159

if Element == "Iron(III) Sulfate":
    Element = input("What would you like to know about Iron(III) Sulfate? ")
    if Element == "Molar Mass":
        print(IronIIISulfateMass)
    elif Element =="Molecular Formula":
        print(IronIIISulfateFormula)

#74Isobutanol
IsobutanolFormula = "C4H10O" 
IsobutanolMass = 122.549

if Element == "Isobutanol":
    Element = input("What would you like to know about Isobutanol? ")
    if Element == "Molar Mass":
        print(IsobutanolMass)
    elif Element =="Molecular Formula":
        print(IsobutanolFormula)

#75LacticAcid
LacticAcidFormula = "C3H6O3" 
LacticAcidMass = 394.995

if Element == "Lactic Acid":
    Element = input("What would you like to know about Lactic Acid? ")
    if Element == "Molar Mass":
        print(LacticAcidMass)
    elif Element =="Molecular Formula":
        print(LacticAcidFormula)

#76Lactose
LactoseFormula = "C12H22O11" 
LactoseMass = 74.551

if Element == "Lactose":
    Element = input("What would you like to know about Lactose? ")
    if Element == "Molar Mass":
        print(LactoseMass)
    elif Element =="Molecular Formula":
        print(LactoseFormula)

#77LeadIIAcetate
LeadIIAcetateFormula = "Pb[C2H3O2]2" 
LeadIIAcetateMass = 133.341

if Element == "Lead(II) Acetate":
    Element = input("What would you like to know about Lead(II) Acetate? ")
    if Element == "Molar Mass":
        print(LeadIIAcetateMass)
    elif Element =="Molecular Formula":
        print(LeadIIAcetateFormula)

#78LeadIIChloride
LeadIIChlorideFormula = "PbCl2" 
LeadIIChlorideMass = 127.912

if Element == "Lead(II) Chloride":
    Element = input("What would you like to know about Lead(II) Chloride? ")
    if Element == "Molar Mass":
        print(LeadIIChlorideMass)
    elif Element =="Molecular Formula":
        print(LeadIIChlorideFormula)

#79LeadIINitrate
LeadIINitrateFormula = "Pb[NO3]2" 
LeadIINitrateMass = 60.095

if Element == "Lead(II) Nitrate":
    Element = input("What would you like to know about Lead(II) Nitrate? ")
    if Element == "Molar Mass":
        print(LeadIINitrateMass)
    elif Element =="Molecular Formula":
        print(LeadIINitrateFormula)

#80LeadIVAcetate
LeadIVAcetateFormula = "Pb[C2H3O2]4" 
LeadIVAcetateMass = 212.996

if Element == "Lead(IV) Acetate":
    Element = input("What would you like to know about Lead(IV) Acetate? ")
    if Element == "Molar Mass":
        print(LeadIVAcetateMass)
    elif Element =="Molecular Formula":
        print(LeadIVAcetateFormula)

#81LithiumChloride
LithiumChlorideFormula = "LiCl" 
LithiumChlorideMass = 80.912

if Element == "Lithium Chloride":
    Element = input("What would you like to know about Lithium Chloride? ")
    if Element == "Molar Mass":
        print(LithiumChlorideMass)
    elif Element =="Molecular Formula":
        print(LithiumChlorideFormula)

#82MagnesiumChloride
MagnesiumChlorideFormula = "MgCl2" 
MagnesiumChlorideMass = 36.461

if Element == "Magnesium Chloride":
    Element = input("What would you like to know about Magnesium Chloride? ")
    if Element == "Molar Mass":
        print(MagnesiumChlorideMass)
    elif Element =="Molecular Formula":
        print(MagnesiumChlorideFormula)

#83MagnesiumNitrate
MagnesiumNitrateFormula = "Mg[NO3]2" 
MagnesiumNitrateMass = 158.260

if Element == "Magnesium Nitrate":
    Element = input("What would you like to know about Magnesium Nitrate? ")
    if Element == "Molar Mass":
        print(MagnesiumNitrateMass)
    elif Element =="Molecular Formula":
        print(MagnesiumNitrateFormula)

#84MagnesiumSulfate
MagnesiumSulfateFormula = "MgSO4" 
MagnesiumSulfateMass = 142.042

if Element == "Magnesium Sulfate":
    Element = input("What would you like to know about Magnesium Sulfate? ")
    if Element == "Molar Mass":
        print(MagnesiumSulfateMass)
    elif Element =="Molecular Formula":
        print(MagnesiumSulfateFormula)

#85MaleicAcid
MaleicAcidFormula = "C4H4O4" 
MaleicAcidMass = 74.122

if Element == "Maleic Acid":
    Element = input("What would you like to know about Maleic Acid? ")
    if Element == "Molar Mass":
        print(MaleicAcidMass)
    elif Element =="Molecular Formula":
        print(MaleicAcidFormula)

#86MalonicAcid
MalonicAcidFormula = "C3H4O4" 
MalonicAcidMass = 88.105

if Element == "Malonic Acid":
    Element = input("What would you like to know about Malonic Acid? ")
    if Element == "Molar Mass":
        print(MalonicAcidMass)
    elif Element =="Molecular Formula":
        print(MalonicAcidFormula)

#87Maltose
MaltoseFormula = "C12H22O11" 
MaltoseMass = 194.190

if Element == "Maltose":
    Element = input("What would you like to know about Maltose? ")
    if Element == "Molar Mass":
        print(MaltoseMass)
    elif Element =="Molecular Formula":
        print(MaltoseFormula)

#88ManganeseIIChloride
ManganeseIIChlorideFormula = "MnCl2" 
ManganeseIIChlorideMass = 27.025

if Element == "Manganese(II) Chloride":
    Element = input("What would you like to know about Manganese(II) Chloride? ")
    if Element == "Molar Mass":
        print(ManganeseIIChlorideMass)
    elif Element =="Molecular Formula":
        print(ManganeseIIChlorideFormula)

#89ManganeseIISulfate
ManganeseIISulfateFormula = "MnSO4" 
ManganeseIISulfateMass = 78.045

if Element == "Manganese(II) Sulfate":
    Element = input("What would you like to know about Manganese(II) Sulfate? ")
    if Element == "Molar Mass":
        print(ManganeseIISulfateMass)
    elif Element =="Molecular Formula":
        print(ManganeseIISulfateFormula)

#90Mannitol
MannitolFormula = "C6H14O6" 
MannitolMass = 65.116

if Element == "Mannitol":
    Element = input("What would you like to know about Mannitol? ")
    if Element == "Molar Mass":
        print(MannitolMass)
    elif Element =="Molecular Formula":
        print(MannitolFormula)

#91MercuryIIChloride
MercuryIIChlorideFormula = "HgCl2" 
MercuryIIChlorideMass = 20.006

if Element == "Mercury(II) Chloride":
    Element = input("What would you like to know about Mercury(II) Chloride? ")
    if Element == "Molar Mass":
        print(MercuryIIChlorideMass)
    elif Element =="Molecular Formula":
        print(MercuryIIChlorideFormula)

#92MercuryIINitrate
MercuryIINitrateFormula = "Hg[NO3]2" 
MercuryIINitrateMass = 226.268

if Element == "Mercury(II) Nitrate":
    Element = input("What would you like to know about Mercury(II) Nitrate? ")
    if Element == "Molar Mass":
        print(MercuryIINitrateMass)
    elif Element =="Molecular Formula":
        print(MercuryIINitrateFormula)

#93MercuryIISulfate
MercuryIISulfateFormula = "HgSO4" 
MercuryIISulfateMass = 126.043

if Element == "Mercury(II) Sulfate":
    Element = input("What would you like to know about Mercury(II) Sulfate? ")
    if Element == "Molar Mass":
        print(MercuryIISulfateMass)
    elif Element =="Molecular Formula":
        print(MercuryIISulfateFormula)

#94Methanol
MethanolFormula = "CH3OH" 
MethanolMass = 294.185

if Element == "Methanol":
    Element = input("What would you like to know about Methanol? ")
    if Element == "Molar Mass":
        print(MethanolMass)
    elif Element =="Molecular Formula":
        print(MethanolFormula)

#95MethylAcetate
MethylAcetateFormula = "C3H6O2" 
MethylAcetateMass = 58.079

if Element == "Methyl Acetate":
    Element = input("What would you like to know about Methyl Acetate? ")
    if Element == "Molar Mass":
        print(MethylAcetateMass)
    elif Element =="Molecular Formula":
        print(MethylAcetateFormula)

#96NickelChloride
NickelChlorideFormula = "NiCl2" 
NickelChlorideMass = 34.015

if Element == "Nickel Chloride":
    Element = input("What would you like to know about Nickel Chloride? ")
    if Element == "Molar Mass":
        print(NickelChlorideMass)
    elif Element =="Molecular Formula":
        print(NickelChlorideFormula)

#97NickelNitrate
NickelNitrateFormula = "Ni[NO3]2" 
NickelNitrateMass = 97.181

if Element == "Nickel Nitrate":
    Element = input("What would you like to know about Nickel Nitrate? ")
    if Element == "Molar Mass":
        print(NickelNitrateMass)
    elif Element =="Molecular Formula":
        print(NickelNitrateFormula)

#98NickelSulfate
NickelSulfateFormula = "NiSO4" 
NickelSulfateMass = 194.050

if Element == "Nickel Sulfate":
    Element = input("What would you like to know about Nickel Sulfate? ")
    if Element == "Molar Mass":
        print(NickelSulfateMass)
    elif Element =="Molecular Formula":
        print(NickelSulfateFormula)

#99Nicotine
NicotineFormula = "C10H14N2" 
NicotineMass = 136.086

if Element == "Nicotine":
    Element = input("What would you like to know about Nicotine? ")
    if Element == "Molar Mass":
        print(NicotineMass)
    elif Element =="Molecular Formula":
        print(NicotineFormula)

#100NitricAcid
NitricAcidFormula = "HNO3" 
NitricAcidMass = 236.421
 
if Element == "Nitric Acid":
    Element = input("What would you like to know about Nitric Acid? ")
    if Element == "Molar Mass":
        print(NitricAcidMass)
    elif Element =="Molecular Formula":
        print(NitricAcidFormula)

#101OXALICACID
OxalicAcidFormula = "H2C2O4" 
OxalicAcidMass = 208.474

if Element == "Oxalic Acid":
    Element = input("What would you like to know about Oxalic Acid? ")
    if Element == "Molar Mass":
        print(OxalicAcidMass)
    elif Element =="Molecular Formula":
        print(OxalicAcidFormula)

#102PENTAN-1-OL

Pentan1olFormula = "C5H11OH"
Pentan1olMass = 44.053

if Element == "Pentan-1-ol":
    Element = input("What would you like to know about Pentan-1-ol? ")
    if Element == "Molar Mass":
        print(Pentan1olMass)
    elif Element =="Molecular Formula":
        print(Pentan1olFormula)

#103PERCHLORICACID

PerchloricAcidFormula = "HClO4" 
PerchloricAcidMass = 110.984

if Element == "Perchloric Acid":
    Element = input("What would you like to know about Perchloric Acid? ")
    if Element == "Molar Mass":
        print(PerchloricAcidMass)
    elif Element =="Molecular Formula":
        print(PerchloricAcidFormula)



#104PHENOL

PhenolFormula = "C6H6O" 
PhenolMass = 151.001

if Element == "Phenol":
    Element = input("What would you like to know about Phenol? ")
    if Element == "Molar Mass":
        print(PhenolMass)
    elif Element =="Molecular Formula":
        print(PhenolFormula)

#105PHOSPHORICACID

PhosphoricAcidFormula = "H3PO4" 
PhosphoricAcidMass = 261.337

if Element == "Phosphoric Acid":
    Element = input("What would you like to know about Phosphoric Acid? ")
    if Element == "Molar Mass":
        print(PhosphoricAcidMass)
    elif Element =="Molecular Formula":
        print(PhosphoricAcidFormula)

#106POTASSIUMBICARBONATE

PotassiumBicarbonateFormula = "KHCO3" 
PotassiumBicarbonateMass = 392.180

if Element == "Potassium Bicarbonate":
    Element = input("What would you like to know about Potassium Bicarbonate? ")
    if Element == "Molar Mass":
        print(PotassiumBicarbonateMass)
    elif Element =="Molecular Formula":
        print(PotassiumBicarbonateFormula)

#107PotassiumBromate

PotassiumBromateFormula = "KBrO3" 
PotassiumBromateMass = 99.994

if Element == "Potassium Bromate":
    Element = input("What would you like to know about Potassium Bromate? ")
    if Element == "Molar Mass":
        print(PotassiumBromateMass)
    elif Element =="Molecular Formula":
        print(PotassiumBromateFormula)

#108PotassiumBromide

PotassiumBromideFormula = "KBr" 
PotassiumBromideMass = 192.124

if Element == "Potassium Bromide":
    Element = input("What would you like to know about Potassium Bromide? ")
    if Element == "Molar Mass":
        print(PotassiumBromideMass)
    elif Element =="Molecular Formula":
        print(PotassiumBromideFormula)

#109PotassiumCarbonate

PotassiumCarbonateFormula = "K2CO3" 
PotassiumCarbonateMass = 187.556

if Element == "Potassium Carbonate":
    Element = input("What would you like to know about Potassium Carbonate? ")
    if Element == "Molar Mass":
        print(PotassiumCarbonateMass)
    elif Element =="Molecular Formula":
        print(PotassiumCarbonateFormula)

#110PotassiumChlorate

PotassiumChlorateFormula = "KCIO3" 
PotassiumChlorateMass = 336.206

if Element == "Potassium Chlorate":
    Element = input("What would you like to know about Potassium Chlorate? ")
    if Element == "Molar Mass":
        print(PotassiumChlorateMass)
    elif Element =="Molecular Formula":
        print(PotassiumChlorateFormula)

#111PotassiumChloride

PotassiumChlorideFormula = "KCI" 
PotassiumChlorideMass = 175.911

if Element == "Potassium Chloride":
    Element = input("What would you like to know about Potassium Chloride? ")
    if Element == "Molar Mass":
        print(PotassiumChlorideMass)
    elif Element =="Molecular Formula":
        print(PotassiumChlorideFormula)

#112PotassiumChromate

PotassiumChromateFormula = "K2CrO4" 
PotassiumChromateMass = 342.296

if Element == "Potassium Chromate":
    Element = input("What would you like to know about Potassium Chromate? ")
    if Element == "Molar Mass":
        print(PotassiumChromateMass)
    elif Element =="Molecular Formula":
        print(PotassiumChromateFormula)

#113PotassiumCyanide

PotassiumCyanideFormula = "KCN" 
PotassiumCyanideMass = 128.942

if Element == "Potassium Cyanide":
    Element = input("What would you like to know about Potassium Cyanide? ")
    if Element == "Molar Mass":
        print(PotassiumCyanideMass)
    elif Element =="Molecular Formula":
        print(PotassiumCyanideFormula)

#114PotassiumDichromate

PotassiumDichromateFormula = "K2Cr2O7" 
PotassiumDichromateMass = 331.210

if Element == "Potassium Dichromate":
    Element = input("What would you like to know about Potassium Dichromate? ")
    if Element == "Molar Mass":
        print(PotassiumDichromateMass)
    elif Element =="Molecular Formula":
        print(PotassiumDichromateFormula)

#115PotassiumDihydrogenPhosphate

PotassiumDihydrogenPhosphateFormula = "KH2PO4" 
PotassiumDihydrogenPhosphateMass = 42.394

if Element == "Potassium Dihydrogen Phosphate":
    Element = input("What would you like to know about Potassium Dihydrogen Phosphate? ")
    if Element == "Molar Mass":
        print(PotassiumDihydrogenPhosphateMass)
    elif Element =="Molecular Formula":
        print(PotassiumDihydrogenPhosphateFormula)

#116PotassiumHexacynoferateII

PotassiumHexacynoferateIIFormula = "K4FeCN6" 
PotassiumHexacynoferateIIMass = 129.599

if Element == "Potassium Hexacynoferate(II)":
    Element = input("What would you like to know about Potassium Hexacynoferate(II)? ")
    if Element == "Molar Mass":
        print(PotassiumHexacynoferateIIMass)
    elif Element =="Molecular Formula":
        print(PotassiumHexacynoferateIIFormula)

#117PotassiumHexacynoferateIII

PotassiumHexacynoferateIIIFormula = "K3FeCN6" 
PotassiumHexacynoferateIIIMass = 182.703

if Element == "Potassium Hexacynoferate(III)":
    Element = input("What would you like to know about Potassium Hexacynoferate(III)? ")
    if Element == "Molar Mass":
        print(PotassiumHexacynoferateIIIMass)
    elif Element =="Molecular Formula":
        print(PotassiumHexacynoferateIIIFormula)

#118PotassiumHydrogenPhosphate

PotassiumHydrogenPhosphateFormula = "K2HPO4" 
PotassiumHydrogenPhosphateMass = 63.013

if Element == "Potassium Hydrogen Phosphate":
    Element = input("What would you like to know about Potassium Hydrogen Phosphate? ")
    if Element == "Molar Mass":
        print(PotassiumHydrogenPhosphateMass)
    elif Element =="Molecular Formula":
        print(PotassiumHydrogenPhosphateFormula)

#119PotassiumHydroxide

PotassiumHydroxideFormula = "KOH" 
PotassiumHydroxideMass = 100.115

if Element == "Potassium Hydroxide":
    Element = input("What would you like to know about Potassium Hydroxide? ")
    if Element == "Molar Mass":
        print(PotassiumHydroxideMass)
    elif Element =="Molecular Formula":
        print(PotassiumHydroxideFormula)

#120PotassiumIodate

PotassiumIodateFormula = "KIO3" 
PotassiumIodateMass = 119.002

if Element == "Potassium Iodate":
    Element = input("What would you like to know about Potassium Iodate? ")
    if Element == "Molar Mass":
        print(PotassiumIodateMass)
    elif Element =="Molecular Formula":
        print(PotassiumIodateFormula)

#121PotassiumIodide

PotassiumIodideFormula = "KI" 
PotassiumIodideMass = 138.206

if Element == "Potassium Iodide":
    Element = input("What would you like to know about Potassium Iodide? ")
    if Element == "Molar Mass":
        print(PotassiumIodideMass)
    elif Element =="Molecular Formula":
        print(PotassiumIodideFormula)

#122PotassiumNitrate

PotassiumNitrateFormula = "KNO3" 
PotassiumNitrateMass = 60.095

if Element == "Potassium Nitrate":
    Element = input("What would you like to know about Potassium Nitrate? ")
    if Element == "Molar Mass":
        print(PotassiumNitrateMass)
    elif Element =="Molecular Formula":
        print(PotassiumNitrateFormula)

#123PotassiumNitrite

PotassiumNitriteFormula = "KNO2" 
PotassiumNitriteMass = 311.799

if Element == "Potassium Nitrite":
    Element = input("What would you like to know about Potassium Nitrite? ")
    if Element == "Molar Mass":
        print(PotassiumNitriteMass)
    elif Element =="Molecular Formula":
        print(PotassiumNitriteFormula)

#124PotassiumPermanganate

PotassiumPermanganateFormula = "KMnO4" 
PotassiumPermanganateMass = 105.988

if Element == "Potassium Permanganate":
    Element = input("What would you like to know about Potassium Permanganate? ")
    if Element == "Molar Mass":
        print(PotassiumPermanganateMass)
    elif Element =="Molecular Formula":
        print(PotassiumPermanganateFormula)

#125PotassiumSulfate

PotassiumSulfateFormula = "K2SO4" 
PotassiumSulfateMass = 158.108

if Element == "Potassium Sulfate":
    Element = input("What would you like to know about Potassium Sulfate? ")
    if Element == "Molar Mass":
        print(PotassiumSulfateMass)
    elif Element =="Molecular Formula":
        print(PotassiumSulfateFormula)

#126PotassiumSulfite

PotassiumSulfiteFormula = "K2SO3" 
PotassiumSulfiteMass = 82.079

if Element == "Potassium Sulfite":
    Element = input("What would you like to know about Potassium Sulfite? ")
    if Element == "Molar Mass":
        print(PotassiumSulfiteMass)
    elif Element =="Molecular Formula":
        print(PotassiumSulfiteFormula)

#127PotassiumTartrate

PotassiumTartrateFormula = "K2C4H4O6" 
PotassiumTartrateMass = 163.387

if Element == "Potassium Tartrate":
    Element = input("What would you like to know about Potassium Tartrate? ")
    if Element == "Molar Mass":
        print(PotassiumTartrateMass)
    elif Element =="Molecular Formula":
        print(PotassiumTartrateFormula)

#128PotassiumThiocyanate

PotassiumThiocyanateFormula = "KCNS" 
PotassiumThiocyanateMass = 60.055

if Element == "Potassium Thiocyanate":
    Element = input("What would you like to know about Potassium Thiocyanate? ")
    if Element == "Molar Mass":
        print(PotassiumThiocyanateMass)
    elif Element =="Molecular Formula":
        print(PotassiumThiocyanateFormula)

#129Propan-1-ol

Propan1olFormula = "CH3CH2CH2OH" 
Propan1olMass = 161.973

if Element == "Propan-1-ol":
    Element = input("What would you like to know about Propan-1-ol? ")
    if Element == "Molar Mass":
        print(Propan1olMass)
    elif Element =="Molecular Formula":
        print(Propan1olFormula)

#130Propan-2-ol

Propan2olFormula = "CH3CHOHCH3" 
Propan2olMass = 258.069

if Element == "Propan-2-ol":
    Element = input("What would you like to know about Propan-2-ol? ")
    if Element == "Molar Mass":
        print(Propan2olMass)
    elif Element =="Molecular Formula":
        print(Propan2olFormula)

#131Pyridine

PyridineFormula = "C5H5N" 
PyridineMass = 58.443

if Element == "Pyridine":
    Element = input("What would you like to know about Pyridine? ")
    if Element == "Molar Mass":
        print(PyridineMass)
    elif Element =="Molecular Formula":
        print(PyridineFormula)

#132Resorcinol

ResorcinolFormula = "C6H6O2" 
ResorcinolMass = 261.968

if Element == "Resorcinol":
    Element = input("What would you like to know about Resorcinol? ")
    if Element == "Molar Mass":
        print(ResorcinolMass)
    elif Element =="Molecular Formula":
        print(ResorcinolFormula)

#133Saccharose

SaccharoseFormula = "C12H22O11" 
SaccharoseMass = 119.977

if Element == "Saccharose":
    Element = input("What would you like to know about Saccharose? ")
    if Element == "Molar Mass":
        print(SaccharoseMass)
    elif Element =="Molecular Formula":
        print(SaccharoseFormula)

#134SilverNitrate

SilverNitrateFormula = "AgNO3" 
SilverNitrateMass = 174.176

if Element == "Silver Nitrate":
    Element = input("What would you like to know about Silver Nitrate? ")
    if Element == "Molar Mass":
        print(SilverNitrateMass)
    elif Element =="Molecular Formula":
        print(SilverNitrateFormula)

#135SilverSulfate

SilverSulfateFormula = "Ag2SO4" 
SilverSulfateMass = 141.959

if Element == "Silver Sulfate":
    Element = input("What would you like to know about Silver Sulfate? ")
    if Element == "Molar Mass":
        print(SilverSulfateMass)
    elif Element =="Molecular Formula":
        print(SilverSulfateFormula)

#136SodiumAcetate

SodiumAcetateFormula = "NaC2H3O2" 
SodiumAcetateMass = 342.151

if Element == "Sodium Acetate":
    Element = input("What would you like to know about Sodium Acetate? ")
    if Element == "Molar Mass":
        print(SodiumAcetateMass)
    elif Element =="Molecular Formula":
        print(SodiumAcetateFormula)

#137SodiumArsenate

SodiumArsenateFormula = "Na3AsO4" 
SodiumArsenateMass = 238.011

if Element == "Sodium Arsenate":
    Element = input("What would you like to know about Sodium Arsenate? ")
    if Element == "Molar Mass":
        print(SodiumArsenateMass)
    elif Element =="Molecular Formula":
        print(SodiumArsenateFormula)

#138SodiumBromide

SodiumBromideFormula = "NaBr" 
SodiumBromideMass = 182.943

if Element == "Sodium Bromide":
    Element = input("What would you like to know about Sodium Bromide? ")
    if Element == "Molar Mass":
        print(SodiumBromideMass)
    elif Element =="Molecular Formula":
        print(SodiumBromideFormula)

#139SodiumCarbonate

SodiumCarbonateFormula = "Na2CO3" 
SodiumCarbonateMass = 159.609

if Element == "Sodium Carbonate":
    Element = input("What would you like to know about Sodium Carbonate? ")
    if Element == "Molar Mass":
        print(SodiumCarbonateMass)
    elif Element =="Molecular Formula":
        print(SodiumCarbonateFormula)

#140SodiumChlorate

SodiumChlorateFormula = "NaClO3" 
SodiumChlorateMass = 46.068

if Element == "Sodium Chlorate":
    Element = input("What would you like to know about Sodium Chlorate? ")
    if Element == "Molar Mass":
        print(SodiumChlorateMass)
    elif Element =="Molecular Formula":
        print(SodiumChlorateFormula)

#141SodiumChloride

SodiumChlorideFormula = "NaCl" 
SodiumChlorideMass = 162.204

if Element == "Sodium Chloride":
    Element = input("What would you like to know about Sodium Chloride? ")
    if Element == "Molar Mass":
        print(SodiumChlorideMass)
    elif Element =="Molecular Formula":
        print(SodiumChlorideFormula)

#142SodiumChromate

SodiumChromateFormula = "Na2CrO4" 
SodiumChromateMass = 325.288

if Element == "Sodium Chromate":
    Element = input("What would you like to know about Sodium Chromate? ")
    if Element == "Molar Mass":
        print(SodiumChromateMass)
    elif Element =="Molecular Formula":
        print(SodiumChromateFormula)

#143SodiumCitrate

SodiumCitrateFormula = "Na3C6H5O7" 
SodiumCitrateMass = 116.119

if Element == "Sodium Citrate":
    Element = input("What would you like to know about Sodium Citrate? ")
    if Element == "Molar Mass":
        print(SodiumCitrateMass)
    elif Element =="Molecular Formula":
        print(SodiumCitrateFormula)

#144SodiumDichromate

SodiumDichromateFormula = "Na2Cr2O7" 
SodiumDichromateMass = 443.376

if Element == "Sodium Dichromate":
    Element = input("What would you like to know about Sodium Dichromate? ")
    if Element == "Molar Mass":
        print(SodiumDichromateMass)
    elif Element =="Molecular Formula":
        print(SodiumDichromateFormula)

#145SodiumDihydrogenPhosphate

SodiumDihydrogenPhosphateFormula = "NaH2PO4" 
SodiumDihydrogenPhosphateMass = 95.211

if Element == "Sodium Dihydrogen Phosphate":
    Element = input("What would you like to know about Sodium Dihydrogen Phosphate? ")
    if Element == "Molar Mass":
        print(SodiumDihydrogenPhosphateMass)
    elif Element =="Molecular Formula":
        print(SodiumDihydrogenPhosphateFormula)

#146SodiumFormate

SodiumFormateFormula = "HCOONa" 
SodiumFormateMass = 271.496

if Element == "Sodium Formate":
    Element = input("What would you like to know about Sodium Formate? ")
    if Element == "Molar Mass":
        print(SodiumFormateMass)
    elif Element =="Molecular Formula":
        print(SodiumFormateFormula)

#147SodiumHydrogenCarbonate

SodiumHydrogenCarbonateFormula = "NaHCO3" 
SodiumHydrogenCarbonateMass = 162.232

if Element == "Sodium Hydrogen Carbonate":
    Element = input("What would you like to know about Sodium Hydrogen Carbonate? ")
    if Element == "Molar Mass":
        print(SodiumHydrogenCarbonateMass)
    elif Element =="Molecular Formula":
        print(SodiumHydrogenCarbonateFormula)

#148SodiumHydrogenPhosphate

SodiumHydrogenPhosphateFormula = "Na2HPO4" 
SodiumHydrogenPhosphateMass = 90.035

if Element == "SodiumHydrogen Phosphate":
    Element = input("What would you like to know about Sodium Hydrogen Phosphate? ")
    if Element == "Molar Mass":
        print(SodiumHydrogenPhosphateMass)
    elif Element =="Molecular Formula":
        print(SodiumHydrogenPhosphateFormula)

#149SodiumHydrogenTartrate

SodiumHydrogenTartrateFormula = "NaHC4H4O6" 
SodiumHydrogenTartrateMass = 88.148

if Element == "Sodium Hydrogen Tartrate":
    Element = input("What would you like to know about Sodium Hydrogen Tartrate? ")
    if Element == "Molar Mass":
        print(SodiumHydrogenTartrateMass)
    elif Element =="Molecular Formula":
        print(SodiumHydrogenTartrateFormula)

#150SodiumHydroxide

SodiumHydroxideFormula = "NaOH" 
SodiumHydroxideMass = 167.000

if Element == "Sodium Hydroxide":
    Element = input("What would you like to know about Sodium Hydroxide? ")
    if Element == "Molar Mass":
        print(SodiumHydroxideMass)
    elif Element =="Molecular Formula":
        print(SodiumHydroxideFormula)

#151SodiumNitrate

SodiumNitrateFormula = "NaNO3" 
SodiumNitrateMass = 110.111

if Element == "Sodium Nitrate":
    Element = input("What would you like to know about Sodium Nitrate? ")
    if Element == "Molar Mass":
        print(SodiumNitrateMass)
    elif Element =="Molecular Formula":
        print(SodiumNitrateFormula)

#152SodiumNitrite

SodiumNitriteFormula = "NaNO2" 
SodiumNitriteMass = 82.034

if Element == "Sodium Nitrite":
    Element = input("What would you like to know about Sodium Nitrite? ")
    if Element == "Molar Mass":
        print(SodiumNitriteMass)
    elif Element =="Molecular Formula":
        print(SodiumNitriteFormula)

#153SodiumPhosphate

SodiumPhosphateFormula = "Na3PO4" 
SodiumPhosphateMass = 324.600

if Element == "Sodium Phosphate":
    Element = input("What would you like to know about Sodium Phosphate? ")
    if Element == "Molar Mass":
        print(SodiumPhosphateMass)
    elif Element =="Molecular Formula":
        print(SodiumPhosphateFormula)

#154SodiumPotassiumTartrate

SodiumPotassiumTartrateFormula = "NaKC4H4O6" 
SodiumPotassiumTartrateMass = 260.522

if Element == "Sodium Potassium Tartrate":
    Element = input("What would you like to know about Sodium Potassium Tartrate? ")
    if Element == "Molar Mass":
        print(SodiumPotassiumTartrateMass)
    elif Element =="Molecular Formula":
        print(SodiumPotassiumTartrateFormula)

#155SodiumSulfate

SodiumSulfateFormula = "Na2SO4" 
SodiumSulfateMass = 211.630

if Element == "Sodium Sulfate":
    Element = input("What would you like to know about Sodium Sulfate? ")
    if Element == "Molar Mass":
        print(SodiumSulfateMass)
    elif Element =="Molecular Formula":
        print(SodiumSulfateFormula)

#156SodiumSulfide

SodiumSulfideFormula = "Na2S" 
SodiumSulfideMass = 76.121

if Element == "Sodium Sulfide":
    Element = input("What would you like to know about Sodium Sulfide? ")
    if Element == "Molar Mass":
        print(SodiumSulfideMass)
    elif Element =="Molecular Formula":
        print(SodiumSulfideFormula)

#157SodiumSulfite

SodiumSulfiteFormula = "Na2SO3" 
SodiumSulfiteMass = 150.087

if Element == "Sodium Sulfite":
    Element = input("What would you like to know about Sodium Sulfite? ")
    if Element == "Molar Mass":
        print(SodiumSulfiteMass)
    elif Element =="Molecular Formula":
        print(SodiumSulfiteFormula)

#158SodiumTartrate

SodiumTartrateFormula = "Na2C4H4O6" 
SodiumTartrateMass = 121.135

if Element == "Sodium Tartrate":
    Element = input("What would you like to know about Sodium Tartrate? ")
    if Element == "Molar Mass":
        print(SodiumTartrateMass)
    elif Element =="Molecular Formula":
        print(SodiumTartrateFormula)

#159SodiumThiosulfate

SodiumThiosulfateFormula = "Na2S2O3" 
SodiumThiosulfateMass = 89.093

if Element == "Sodium Thiosulfate":
    Element = input("What would you like to know about Sodium Thiosulfate? ")
    if Element == "Molar Mass":
        print(SodiumThiosulfateMass)
    elif Element =="Molecular Formula":
        print(SodiumThiosulfateFormula)

#160StrontiumChloride

StrontiumChlorideFormula = "SrCl2" 
StrontiumChlorideMass = 74.122

if Element == "Strontium Chloride":
    Element = input("What would you like to know about Strontium Chloride? ")
    if Element == "Molar Mass":
        print(StrontiumChlorideMass)
    elif Element =="Molecular Formula":
        print(StrontiumChlorideFormula)

#161StrontiumNitrate
StrontiumNitrateFormula = "Sr[NO3]2" 
StrontiumNitrateMass = 342.296

if Element == "Strontium Nitrate":
    Element = input("What would you like to know about Strontium Nitrate? ")
    if Element == "Molar Mass":
        print(StrontiumNitrateMass)
    elif Element == "Molecular Formula":
        print(StrontiumNitrateFormula)

#162StrontiumSulfate
StrontiumSulfateFormula = "SrSO4" 
StrontiumSulfateMass = 183.683

if Element == "Strontium Sulfate":
    Element = input("What would you like to know about Strontium Sulfate? ")
    if Element == "Molar Mass":
        print(StrontiumSulfateMass)
    elif Element == "Molecular Formula":
        print(StrontiumSulfateFormula)

#163SulfuricAcid
SulfuricAcidFormula = "H2SO4" 
SulfuricAcidMass = 74.093

if Element == "Sulfuric Acid":
    Element = input("What would you like to know about Sulfuric Acid? ")
    if Element == "Molar Mass":
        print(SulfuricAcidMass)
    elif Element == "Molecular Formula":
        print(SulfuricAcidFormula)

#164SulfurousAcid
SulfurousAcidFormula = "H2SO3" 
SulfurousAcidMass = 164.088

if Element == "Sulfurous Acid":
    Element = input("What would you like to know about Sulfurous Acid? ")
    if Element == "Molar Mass":
        print(SulfurousAcidMass)
    elif Element == "Molecular Formula":
        print(SulfurousAcidFormula)

#165TartaricAcid
TartaricAcidFormula = "H2C4H4O6" 
TartaricAcidMass = 136.141

if Element == "Tartaric Acid":
    Element = input("What would you like to know about Tartaric Acid? ")
    if Element == "Molar Mass":
        print(TartaricAcidMass)
    elif Element == "Molecular Formula":
        print(TartaricAcidFormula)

#166Thiourea
ThioureaFormula = "CH4N2S" 
ThioureaMass = 225.188

if Element == "Thiourea":
    Element = input("What would you like to know about Thiourea? ")
    if Element == "Molar Mass":
        print(ThioureaMass)
    elif Element == "Molecular Formula":
        print(ThioureaFormula)

#167Tin(II)Chloride
TinIIChlorideFormula = "SnCl2" 
TinIIChlorideMass = 241.860

if Element == "Tin(II) Chloride":
    Element = input("What would you like to know about Tin(II) Chloride? ")
    if Element == "Molar Mass":
        print(TinIIChlorideMass)
    elif Element == "Molecular Formula":
        print(TinIIChlorideFormula)

#168Tin(IV)Chloride
TinIVChlorideFormula = "SnCl4"
TinIVChlorideMass = 399.878

if Element == "Tin(IV) Chloride":
    Element = input("What would you like to know about Tin(IV) Chloride? ")
    if Element == "Molar Mass":
        print(TinIVChlorideMass)
    elif Element == "Molecular Formula":
        print(TinIVChlorideFormula)

#169TrichloroaceticAcid
TrichloroaceticAcidFormula = "CCl3COOH" 
TrichloroaceticAcidMass = 94.497

if Element == "Trichloroacetic Acid":
    Element = input("What would you like to know about Trichloroacetic Acid? ")
    if Element == "Molar Mass":
        print(TrichloroaceticAcidMass)
    elif Element == "Molecular Formula":
        print(TrichloroaceticAcidFormula)

#170TRIS
TRISFormula = "[HOCH]3CNH2" 
TRISMass = 136.286

if Element == "TRIS":
    Element = input("What would you like to know about TRIS? ")
    if Element == "Molar Mass":
        print(TRISMass)
    elif Element == "Molecular Formula":
        print(TRISFormula)

#171Urea
UreaFormula = "[NH2]2CO" 
UreaMass = 189.390

if Element == "Urea":
    Element = input("What would you like to know about Urea? ")
    if Element == "Molar Mass":
        print(UreaMass)
    elif Element == "Molecular Formula":
        print(UreaFormula)

#172Urethane
UrethaneFormula = "C3H7NO2" 
UrethaneMass = 161.443

if Element == "Urethane":
    Element = input("What would you like to know about Urethane? ")
    if Element == "Molar Mass":
        print(UrethaneMass)
    elif Element == "Molecular Formula":
        print(UrethaneFormula)

#173ZincBromide
ZincBromideFormula = "ZnBr2" 
ZincBromideMass = 154.996

if Element == "Zinc Bromide":
    Element = input("What would you like to know about Zinc Bromide? ")
    if Element == "Molar Mass":
        print(ZincBromideMass)
    elif Element == "Molecular Formula":
        print(ZincBromideFormula)

#174ZincChloride
ZincChlorideFormula = "ZnCl2" 
ZincChlorideMass = 90.078

if Element == "Zinc Chloride":
    Element = input("What would you like to know about Zinc Chloride? ")
    if Element == "Molar Mass":
        print(ZincChlorideMass)
    elif Element == "Molecular Formula":
        print(ZincChlorideFormula)

#175ZincNitrate
ZincNitrateFormula = "ZnNO32" 
ZincNitrateMass = "169.873"

if Element == "Zinc Nitrate":
    Element = input("What would you like to know about Zinc Nitrate? ")
    if Element == "Molar Mass":
        print(ZincNitrateMass)
    elif Element == "Molecular Formula":
        print(ZincNitrateFormula)

#176ZincSulfate
ZincSulfateFormula = "ZnSO4" 
ZincSulfateMass = "98.078"

if Element == "Zinc Sulfate":
    Element = input("What would you like to know about Zinc Sulfate? ")
    if Element == "Molar Mass":
        print(ZincSulfateMass)
    elif Element == "Molecular Formula":
        print(ZincSulfateFormula)

else:
    print ("Thank you! Hope that this was helpful! :)")
