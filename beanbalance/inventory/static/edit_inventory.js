// Function to render the edit form and populate fields
function renderEditInventory(itemId) {
  // Find the item based on the data attribute
  const itemCard = document.querySelector(`[data-id="${itemId}"]`);

  if (itemCard) {
    // Extract data attributes from the selected item
    const name = itemCard.dataset.name;
    const price = itemCard.dataset.price;
    const quantity = itemCard.dataset.quantity;

    // Hide the add form if it is visible
    const addFormContainer = document.getElementById('add-inventory-form');
    if (addFormContainer) {
      addFormContainer.classList.add('hidden');
    }

    // Show and populate the edit form
    const editFormContainer = document.getElementById('edit-inventory-form'); // Ensure this matches your form container
    if (editFormContainer) {
      editFormContainer.classList.remove('hidden'); // Make sure the form is visible

      // Populate form fields with the item data
      document.getElementById('inventory-name').value = name || '';
      document.getElementById('inventory-price').value = price || '';
      document.getElementById('inventory-quantity').value = quantity || '';

      // Store the item ID for further operations
      document.getElementById('edit-form').setAttribute('data-item-id', itemId);
    }
  } else {
    console.error('Inventory item not found for ID:', itemId);
  }
}

// Function to render the add form
function renderAddInventory() {
  // Hide the edit form if it is visible
  const editFormContainer = document.getElementById('edit-inventory-form');
  if (editFormContainer) {
    editFormContainer.classList.add('hidden');
  }

  // Show the add form
  const addFormContainer = document.getElementById('add-inventory-form'); // Ensure this matches your form container
  if (addFormContainer) {
    addFormContainer.classList.remove('hidden'); // Make sure the form is visible
  }
}


// Function to handle updating the inventory
function updateInventory() {
  const itemId = document.getElementById('edit-form').getAttribute('data-item-id');
  const updatedItem = {
    name: document.getElementById('inventory-name').value,
    price: parseFloat(document.getElementById('inventory-price').value),
    quantity: parseInt(document.getElementById('inventory-quantity').value, 10),
  };

  fetch(`/inventory/update/${itemId}/`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
    },
    body: JSON.stringify(updatedItem),
  })
    .then((response) => {
      if (response.ok) {
        console.log('Inventory updated successfully');
        window.location.reload(); // Reload the page to see the updated inventory
      } else {
        console.error('Failed to update inventory:', response.statusText);
      }
    })
    .catch((error) => console.error('Error:', error));
}

// Function to delete an inventory item
function deleteInventory() {
  // Get the item ID from the edit form
  const itemId = document.getElementById('edit-form').getAttribute('data-item-id');
  
  // Confirm before deleting the item
  if (!confirm("Are you sure you want to delete this inventory item?")) {
      return; // If the user cancels, stop the function
  }

  // Send the DELETE request
  fetch(`/inventory/delete/${itemId}/`, {
      method: 'DELETE',
      headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
      },
  })
  .then((response) => {
      if (response.ok) {
          console.log('Inventory item deleted successfully');
          window.location.reload(); // Reload the page to see the updated inventory
      } else {
          console.error('Failed to delete inventory item:', response.statusText);
      }
  })
  .catch((error) => console.error('Error:', error));
}
