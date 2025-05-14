function cancelAppointment() {
  document.getElementById("cancelModal").style.display = "block";
}

function closeModal() {
  document.getElementById("cancelModal").style.display = "none";
}

function confirmCancel() {
  closeModal();

  const cancelMessage = document.getElementById("cancel-message");
  cancelMessage.textContent = "This appointment has been cancelled.";
  cancelMessage.style.display = "block";
}