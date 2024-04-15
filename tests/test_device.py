from ckb_commander.device import Device

device = Device("/dev/input/ckb1")


class TestFileProperties:
    def test_dpi(self) -> None:
        assert device.dpi == ""

    def test_features(self) -> None:
        assert (
            device.features
            == "corsair k70mk2 rgb pollrate adjrate bind notify fwupdate"
        )

    def test_fwversion(self) -> None:
        assert device.fwversion == "3.24\n3.3"

    def test_layout(self) -> None:
        assert device.layout == "iso"

    def test_model(self) -> None:
        assert device.model == "CORSAIR K70 RGB MK.2 Mechanical Gaming Keyboard"

    def test_pollrate(self) -> None:
        assert device.pollrate == "1 ms"

    def test_productid(self) -> None:
        assert device.productid == "1b49"

    def test_serial(self) -> None:
        assert device.serial == "0902B01FAF7A8C095F6236EAF5001BC6"


class TestGetProperties:
    def test_rgb(self) -> None:
        assert device.rgb.startswith("mode")

    # def test_hwrgb(self) -> None:
    #     self.assertEqual(device.hwrgb, "d")


class TestSendCommand:
    def turn_on_indicator(self) -> None:
        device.turn_on_indicator("caps")
