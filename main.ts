basic.forever(function () {
    serial.writeValue("x", input.acceleration(Dimension.X))
    serial.writeValue("y", input.acceleration(Dimension.Y))
    serial.writeValue("z", input.acceleration(Dimension.Z))
})
