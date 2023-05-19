# Minnow - USB-C DAM Tool

Minnow is a tool for using DAM (Debug Accessory Mode), providing an interface to the SWD/JTAG and/or UART from the device. It expands upon [this concept](https://github.com/BitterAndReal/SWD-over-USB-C) to include a USB-UART and some utility for use within test rigs. It could be considered SWD over DAM with a sprinkling of [USB cereal](https://github.com/oxda/usb-cereal) - unlike usb-cereal it does not use the Chomebook UART mapping in favour of maintaining USB-C rotational symmetry.

* Enables and interfaces USB DAM configured in image below; SWD/JTAG over USB-C.
* Provides board designer the option of using RX+ for NRST/RXD and RX- for SWO/TXD - either single-wire trace communication or UART
* Four configurable GPIO on FT230 for test rig control of UUT: power enable; RX pin control; reset.
* TagConnect TC2030 and ARM 10-pin header.
* USB pass-through or FT230 USB UART to device.
* VTARGET reference from device or external.
* Maintains USB-C rotational symmetry.

![./media/swd_dam_pinout.png](./media/swd_dam_pinout.png)
[Orignal reference](https://github.com/BitterAndReal/SWD-over-USB-C/blob/main/images/SWD%20over%20USB-C%20Pinout-01.png) modified to include option of UART.

# Usage

![./media/minnow-pcb.jpg](./media/minnow-pcb.jpg)

## Cable

The cable between Minnow and the target device needs to be a **complete USB-C cable** with all [Alternate Mode](https://en.wikipedia.org/wiki/USB-C#Alternate_Mode) wires. USB 3.1+, DisplayPort, Thunderbolt and HDMI rated cables _should_ include these. It may seem obvious but this is something to double check if things are not working as expected - not all cables are created equally!

The cable to the host can be a USB 2.0.

## Example Device 

I've included an example schematic for the device end: './example-dev/usb-dam.kicad\_pro'. It can be used for testing and as a foundation for a project with DAM. There are clearly altnative design choices that can be made based on the requirements of the device but it is a good starting point. The layout was done in haste as a means to test the Minnow board!

# Useful Links

* [SWD over USB-C](https://github.com/BitterAndReal/SWD-over-USB-C)
* [USB Type-C](https://www.usb.org/sites/default/files/USB%20Type-C%20Spec%20R2.0%20-%20August%202019.pdf)
* [ARM JTAG/SWD Interface](https://developer.arm.com/documentation/101636/0100/Debug-and-Trace/JTAG-SWD-Interface)
