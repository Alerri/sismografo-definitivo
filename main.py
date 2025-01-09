def on_forever():
    serial.write_value("x", input.acceleration(Dimension.X))
    serial.write_value("y", input.acceleration(Dimension.Y))
    serial.write_value("z", input.acceleration(Dimension.Z))
basic.forever(on_forever)
