function confirmCancel() {
    const confirmed = confirm("Are you sure you want to cancel your appointment?");
    if (confirmed) {
        alert("Appointment cancelled.");
    }
}