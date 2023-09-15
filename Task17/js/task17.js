function convertUnits() {

    var inputNumber = parseFloat(document.getElementById("inputNumber").value);


    var meter = inputNumber;
    var feet = inputNumber * 3.281;


    var liter = inputNumber;
    var gallon = inputNumber * 0.264;


    var kilogram = inputNumber;
    var pound = inputNumber * 2.204;


    // meter = meter.toFixed(3);
    // feet = feet.toFixed(3);
    // liter = liter.toFixed(3);
    // gallon = gallon.toFixed(3);
    // kilogram = kilogram.toFixed(3);
    // pound = pound.toFixed(3);


    document.getElementById("lengthResult").innerHTML = + meter + " meters - " + feet + " feet";
    document.getElementById("volumeResult").innerHTML = + liter + " liters - " + gallon + " gallons";
    document.getElementById("massResult").innerHTML = + kilogram + " kilograms - " + pound + " pounds";
}