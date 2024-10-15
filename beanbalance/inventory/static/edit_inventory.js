let errorMessage = document.querySelector('.name .error-message');

function renderEditInventory(itemId) {
  errorMessage?.remove();
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

  const addInventoryForm = document.querySelector('#add-inventory-form form');
  if (addInventoryForm) {
    addInventoryForm.addEventListener('submit', function(event) {
      event.preventDefault();

      const formData = new FormData(addInventoryForm);

      fetch(addInventoryForm.action, {
        method: 'POST',
        body: formData,
        headers: {
          'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        }
      })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          window.location.reload(); 
        } else {
          handleFormErrors(data.errors);
        }
      })
      .catch(error => console.error('Error:', error));
    });
  }
}

function handleFormErrors(errors) {
  document.querySelectorAll('.error-message').forEach(error => error.remove());

  for (let field in errors) {
    let fieldElement = document.querySelector(`#add-inventory-form [name="${field}"]`);
    if (fieldElement) {
      let errorMessage = document.createElement('p');
      errorMessage.classList.add('text-red-500', 'text-sm', 'mt-2', 'error-message');
      errorMessage.textContent = errors[field];
      fieldElement.parentElement.appendChild(errorMessage);
    }
  }
}


function updateInventory() {
  const itemId = document.getElementById('edit-form').getAttribute('data-item-id');
  const nameInput = document.querySelector('#edit-inventory-form input[name="name"]');
  const enteredName = nameInput.value.trim().toLowerCase();

  const isDuplicate = inventoryNames.some((name, index) => {
      const itemIdFromList = document.querySelectorAll('.item-card')[index].dataset.id;
      return name === enteredName && itemIdFromList !== itemId;
  });

  if (isDuplicate) {
      // let errorMessage = document.querySelector('.name .error-message');
      if (!errorMessage) {
          errorMessage = document.createElement('p');
          errorMessage.classList.add('text-red-500', 'text-sm', 'mt-2', 'error-message');
          errorMessage.textContent = `The '${nameInput.value}' already exists.`;
          nameInput.parentElement.appendChild(errorMessage);
      }
      return;
  } else {
      // let errorMessage = document.querySelector('.name .error-message');
      if (errorMessage) {
          errorMessage.remove();
      }

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
      .then(response => {
          if (response.ok) {
              console.log('Inventory updated successfully');
              window.location.reload();
          } else {
              console.error('Failed to update inventory:', response.statusText);
          }
      })
      .catch(error => console.error('Error:', error));
  }
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

document.addEventListener('DOMContentLoaded', function() {
  const searchElement = document.getElementById('search');
  if (searchElement) {
      searchElement.addEventListener('input', function() {
          const searchTerm = this.value.toLowerCase();
          document.querySelectorAll('.item-card').forEach(item => {
              const name = item.querySelector('h3').textContent.toLowerCase();
              if (name.includes(searchTerm)) {
                  item.style.display = '';
              } else {
                  item.style.display = 'none';
              }
          });
      });
  }
});
