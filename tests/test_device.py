import unittest

from ckb_commander.device import Device

device = Device("/dev/input/ckb1")


class TestFileProperties(unittest.TestCase):
    def test_dpi(self) -> None:
        self.assertEqual(device.dpi, "")

    def test_features(self) -> None:
        self.assertEqual(
            device.features, "corsair k70mk2 rgb pollrate adjrate bind notify fwupdate"
        )

    def test_fwversion(self) -> None:
        self.assertEqual(device.fwversion, "3.24\n3.3")

    def test_layout(self) -> None:
        self.assertEqual(device.layout, "iso")

    def test_model(self) -> None:
        self.assertEqual(
            device.model, "CORSAIR K70 RGB MK.2 Mechanical Gaming Keyboard"
        )

    def test_pollrate(self) -> None:
        self.assertEqual(device.pollrate, "1 ms")

    def test_productid(self) -> None:
        self.assertEqual(device.productid, "1b49")

    def test_serial(self) -> None:
        self.assertEqual(device.serial, "0902B01FAF7A8C095F6236EAF5001BC6")


class TestGetProperties(unittest.TestCase):
    def test_rgb(self) -> None:
        self.assertTrue(device.rgb.startswith("mode"))

    # def test_hwrgb(self) -> None:
    #     self.assertEqual(device.hwrgb, "d")


class TestSendCommand(unittest.TestCase):
    def turn_on_indicator(self) -> None:
        device.turn_on_indicator("caps")


if __name__ == "__main__":
    unittest.main()
