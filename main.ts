input.onButtonPressed(Button.A, function () {
    pins.digitalWritePin(DigitalPin.P1, 0)
})
basic.forever(function () {
    if (pins.analogReadPin(AnalogPin.P0) < 200) {
        pins.digitalWritePin(DigitalPin.P1, 1)
        basic.showString("it is night time!")
    } else {
        pins.digitalWritePin(DigitalPin.P1, 0)
    }
})
