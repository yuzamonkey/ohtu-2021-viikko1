import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.huono_varasto = Varasto(-10, -10)
        self.ylimaara_varasto = Varasto(10, 20)

    def test_nollaa_huonon_varaston_tilavuus(self):
        self.assertAlmostEqual(self.huono_varasto.tilavuus, 0.0)
    
    def test_nollaa_huonon_varaston_saldo(self):
        self.assertAlmostEqual(self.huono_varasto.saldo, 0.0)

    def test_saldo_on_tilavuus_kun_saldo_suurempi_kuin_tilavuus(self):
        self.assertAlmostEqual(self.ylimaara_varasto.saldo, 10)
        self.assertAlmostEqual(self.ylimaara_varasto.tilavuus, 10)
        self.assertAlmostEqual(self.ylimaara_varasto.saldo, self.ylimaara_varasto.tilavuus)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisaa_varastoon_neg_ei_muuta_mitaan(self):
        tilavuus = self.varasto.tilavuus
        saldo = self.varasto.saldo

        self.varasto.lisaa_varastoon(-10)
        self.assertAlmostEqual(tilavuus, self.varasto.tilavuus)
        self.assertAlmostEqual(saldo, self.varasto.saldo)

    def test_lisaa_varastoon_enemman_mita_voi_tasaa_saldon_ja_tilavuuden(self):
        maara = self.varasto.paljonko_mahtuu() + 10
        self.varasto.lisaa_varastoon(maara)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ota_varastosta_neg_maara_ei_muuta_mitaan(self):
        saldo = self.varasto.saldo
        tilavuus = self.varasto.tilavuus
        self.varasto.ota_varastosta(-10)
        self.assertAlmostEqual(tilavuus, self.varasto.tilavuus)
        self.assertAlmostEqual(saldo, self.varasto.saldo)

    def test_ota_kaikki(self):
        saldo = self.varasto.saldo
        maara = saldo + 10
        arvo = self.varasto.ota_varastosta(maara)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)
        self.assertAlmostEqual(arvo, saldo)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_to_string_metodi(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
