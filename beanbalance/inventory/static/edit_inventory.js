function renderEditInventory(itemId) {
  const itemCard = document.querySelector(`[data-id="${itemId}"]`);

  if (itemCard) {
    const name = itemCard.dataset.name;
    const price = itemCard.dataset.price;
    const quantity = itemCard.dataset.quantity;

    const addFormContainer = document.getElementById('add-inventory-form');
    if (addFormContainer) {
      addFormContainer.classList.add('hidden');
    }

    const editFormContainer = document.getElementById('edit-inventory-form');
    if (editFormContainer) {
      editFormContainer.classList.remove('hidden');

      document.getElementById('inventory-name').value = name || '';
      document.getElementById('inventory-price').value = price || '';
      document.getElementById('inventory-quantity').value = quantity || '';

      document.getElementById('edit-form').setAttribute('data-item-id', itemId);
    }
  } else {
    console.error('Inventory item not found for ID:', itemId);
  }
}

function renderAddInventory() {
  const editFormContainer = document.getElementById('edit-inventory-form');
  if (editFormContainer) {
    editFormContainer.classList.add('hidden');
  }

  const addFormContainer = document.getElementById('add-inventory-form');
  if (addFormContainer) {
    addFormContainer.classList.remove('hidden');
  }
}


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

function deleteInventory() {
  const itemId = document.getElementById('edit-form').getAttribute('data-item-id');
  
  if (!confirm("Are you sure you want to delete this inventory item?")) {
      return; // If the user cancels, stop the function
  }

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
          window.location.reload();
      } else {
          console.error('Failed to delete inventory item:', response.statusText);
      }
  })
  .catch((error) => console.error('Error:', error));
}
