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
  const homeItem = document.getElementById("home");
  logoutItem.style.display = logoutItem.style.display === "none" ? "block" : "none";
  homeItem.style.display = homeItem.style.display === "none" ? "block" : "none";
}

function buttonLogout() {
  document.getElementById("logoutModal").style.display = "block";
}

function buttonHome() {
  document.getElementById("homeModal").style.display = "block";
}

function closeLogoutModal() {
  document.getElementById("logoutModal").style.display = "none";
}

function closeHomeModal() {
  document.getElementById("homeModal").style.display = "none";
}

function confirmLogout() {
  closeLogoutModal();
}
