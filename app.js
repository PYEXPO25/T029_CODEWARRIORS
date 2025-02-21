// You can manually set the status for each slot here
document.addEventListener('DOMContentLoaded', () => {
    // Manually set the status for each parking slot
    const slots = document.querySelectorAll('.slot');
  
    // Example of setting the status to "available" or "occupied"
    // You can modify these statuses manually, or they could be updated via an API or from an IoT device.
    updateSlotStatus('slot1', 'available');
    updateSlotStatus('slot2', 'occupied');
    updateSlotStatus('slot3', 'available');
  
    function updateSlotStatus(slotId, status) {
      const slot = document.getElementById(slotId);
      const statusElement = slot.querySelector('.status');
      
      // Set the status text
      statusElement.textContent = status.charAt(0).toUpperCase() + status.slice(1);
      
      // Set the slot color based on status
      if (status === 'available') {
        slot.setAttribute('data-status', 'available');
      } else {
        slot.setAttribute('data-status', 'occupied');
      }
    }
  });