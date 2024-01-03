function showSchedule(vehicleType) {
    // Hide all schedule tables
    $('#taxi-schedule, #jeep-schedule').hide();
    // Hide other schedule tables here if needed

    // Show the selected schedule table
    $('#' + vehicleType + '-schedule').show();
}