/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Evan
 * Created on: Feb 2026
 * This program will show the temperature
*/

basic.clearScreen()
basic.showIcon(IconNames.Happy)

//temperature
input.onButtonPressed(Button.A, function () {
    const temperature = input.temperature()
    basic.clearScreen()
    basic.showString("The temperature is:" + (temperature) + "C.")
})
