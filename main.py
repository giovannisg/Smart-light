def on_button_pressed_a():
    pins.digital_write_pin(DigitalPin.P1, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    if pins.analog_read_pin(AnalogPin.P0) < 200:
        pins.digital_write_pin(DigitalPin.P1, 1)
        basic.show_string("it is night time!")
    else:
        pins.digital_write_pin(DigitalPin.P1, 0)
basic.forever(on_forever)
