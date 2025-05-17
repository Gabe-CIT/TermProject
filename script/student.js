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

function profileLogout() {
  const logoutItem = document.getElementById("logout");
  logoutItem.style.display = logoutItem.style.display === "none" ? "block" : "none";
}

function buttonLogout() {
  document.getElementById("logoutModal").style.display = "block";
}

function closeLogoutModal() {
  document.getElementById("logoutModal").style.display = "none";
}

function confirmLogout() {
  closeLogoutModal();
  window.location.href = ".html"; // This needs to be changed to index.html
}

function sendAppointment() {
  document.getElementById("sendModal").style.display = "block";
}