from igc_processor.parser import igc2df


def test_igc2df():
    text = """ALXV5KS,FLIGHT:1
HFDTE110323
HFFXA015
HFPLTPILOTINCHARGE:
HFCM2CREW2:
HFGTYGLIDERTYPE:HOGE
HFGIDGLIDERID:FUGA
HFDTM100GPSDATUM:WGS-1984
HFRFWFIRMWAREVERSION:03.23 with WGS84 Ellipsoid GPS altitude datum
HFRHWHARDWAREVERSION:9
HFFTYFRTYPE:LXNAV,NANO4
HFGPSMANUFACTURERSNAME:UBLOX,NEO7,56,max50000m
HFPRSPRESSALTSENSOR:INTERSEMA,MS5611,max16000m
HFALGALTGPS:ELL
HFMOPSENSOR:LXNAV,ON,Internal Acoustic - Peak 8KHz
HFCIDCOMPETITIONID:
HFCCLCOMPETITIONCLASS:Standard
I053638FXA3941ENL4246GSP4749TRT5052MOP
B0350213612961N13924777EA-00710007800501000027000011
F03502126310407080916212718808273
B0350223612961N13924777EA-00720007800501200055000015
B0350233612961N13924777EA-00710007800501300050000014
B0350243612961N13924777EA-00700007800501500039000010
B0350253612961N13924777EA-00720007700501200017000014
B0350263612961N13924777EA-00710007700501400053000014
B0350273612961N13924777EA-00710007700501200057000014
B0350283612959N13924777EA-00710007700501300009000010"""
    igc2df(text)
