import unittest

from ckb_commander.device import Device

device = Device("/dev/input/ckb1")


class TestDevice(unittest.TestCase):
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

    def test_rgb(self) -> None:
        self.assertTrue(device.rgb.startswith("mode"))


if __name__ == "__main__":
    unittest.main()
