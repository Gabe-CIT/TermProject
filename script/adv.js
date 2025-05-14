// Function to show the modal
function cancelAppointment() {
    document.getElementById("cancelModal").style.display = "block";
}

// Function to close the modal
function closeModal() {
    document.getElementById("cancelModal").style.display = "none";
}

// Function to handle confirmation
function confirmCancel() {
    // Hide the modal
    closeModal();

    // Show the cancellation message
    const cancelMessage = document.getElementById("cancel-message");
    cancelMessage.textContent = "This appointment has been cancelled.";
    cancelMessage.style.display = "block";
}
