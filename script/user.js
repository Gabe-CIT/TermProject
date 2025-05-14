function cancelAppointment() {
    document.getElementById("cancelModal").style.display = "flex";
  }
  
  function closeModal() {
    document.getElementById("cancelModal").style.display = "none";
  }
  
  function confirmCancel() {
    closeModal();
    const msg = document.getElementById("cancel-message");
    msg.style.display = "block";
    msg.textContent = "This appointment has been cancelled.";
  }
  
