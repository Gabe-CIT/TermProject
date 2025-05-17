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
  const logoutItem = document.getElementById("logout");
  logoutItem.style.display = "none";
}

function confirmLogout() {
  closeLogoutModal();
  window.location.href = "booking.html";
}

function sendAppointment() {
  document.getElementById("sendModal").style.display = "block";
}

function confirmSend() {
  document.getElementById("sendModal").style.display = "none";

  const sendMessage = document.getElementById("send-message");
  sendMessage.textContent = "The comment has been sent.";
  sendMessage.style.display = "block";

  const commentField = document.getElementById("comment-field");
  commentField.value = "";

  document.getElementById("comment-section").style.display = "none";

  setTimeout(function() {
    sendMessage.style.display = "none";
  }, 3000);
}


function closeSend() {
  document.getElementById("sendModal").style.display = "none";
}

function editAppointment() {
  const editOptions = document.getElementById("edit-options");
  
  if (editOptions.style.display === "none" || editOptions.style.display === "") {
      editOptions.style.display = "flex"; 
  } else {
      editOptions.style.display = "none";
  }
}

function closeEditOptions() {
  document.getElementById("edit-options").style.display = 'none';
}

function confirmEdit() {
  const selectedTime = document.getElementById("time").value;
  closeEditOptions();
  const editMessage = document.getElementById("edit-message");
  editMessage.style.display = "block";
  setTimeout(function() {
    editMessage.style.display = "none";
  }, 3000);
}

function sendMessage() {
  const commentSection = document.getElementById("comment-section");
  commentSection.style.display = "block";
}

function sendComment() {
  const commentField = document.getElementById("comment-field");
  const commentText = commentField.value;
  if (commentText.trim() !== "") {
    document.getElementById("sendModal").style.display = "block";
  }
}

function confirmCancel() {
  closeModal();
  const cancelMessage = document.getElementById("cancel-message");
  cancelMessage.textContent = "This appointment has been cancelled.";
  cancelMessage.style.display = "block";
}
