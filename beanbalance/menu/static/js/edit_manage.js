// Function to render the edit form and populate fields for editing a menu
function renderEditMenu(menuId) {
  const menuCard = document.querySelector(`[data-id="${menuId}"]`);

  if (menuCard) {
    // Extract menu data from data attributes
    const name = menuCard.dataset.name;
    const price = menuCard.dataset.price;
    const description = menuCard.dataset.description;
    const category = menuCard.dataset.category;

    // Hide the add form if it is visible
    const addFormContainer = document.getElementById('add-menu-form');
    if (addFormContainer) {
      addFormContainer.classList.add('hidden');
    }
    const editCategoryName = document.getElementById('edit-category-form');
    if (editCategoryName) {
      editCategoryName.classList.add('hidden');
    }
    const addCategoryForm = document.getElementById('add-category-form');
    if (addCategoryForm) {
      addCategoryForm.classList.add('hidden');
    }

    // Show and populate the edit form
    const editFormContainer = document.getElementById('edit-menu-form');
    if (editFormContainer) {
      editFormContainer.classList.remove('hidden');

      // Populate the form fields with menu data
      document.getElementById('menu-name').value = name || '';
      document.getElementById('menu-price').value = price || '';
      document.getElementById('menu-description').value = description || '';
      document.getElementById('menu-category').value = category || '';

      // Set the menu ID in a hidden field or the form's data attribute
      document.getElementById('menu-edit-form').setAttribute('data-menu-id', menuId);
    }
  } else {
    console.error('Menu item not found for ID:', menuId);
  }
}

// Function to render the add menu form
function renderAddMenu() {
  const editFormContainer = document.getElementById('edit-menu-form');
  if (editFormContainer) {
    editFormContainer.classList.add('hidden');
  }
  const editCategoryName = document.getElementById('edit-category-form');
  if (editCategoryName) {
    editCategoryName.classList.add('hidden');
  }
  const addFormContainer = document.getElementById('add-menu-form');
  if (addFormContainer) {
    addFormContainer.classList.remove('hidden');
  }

  const addCategoryFormContainer = document.getElementById('add-category-form');
  if (addCategoryFormContainer) {
    addCategoryFormContainer.classList.add('hidden');
  }
}

function updateMenu() {
  const menuId = document.getElementById('menu-edit-form').getAttribute('data-menu-id');

  // Clear previous errors
  document.getElementById('error-name').style.display = 'none';
  document.getElementById('error-price').style.display = 'none';
  document.getElementById('error-description').style.display = 'none';
  document.getElementById('error-category').style.display = 'none';

  // Construct the updated menu object
  const updatedMenu = {
    name: document.getElementById('menu-name').value,
    price: parseFloat(document.getElementById('menu-price').value),  // Convert price to float
    description: document.getElementById('menu-description').value,
    category: parseInt(document.getElementById('menu-category').value),  // Convert category to integer
  };

  console.log('Updated Menu:', updatedMenu);

  // Send the PUT request to the server
  fetch(`/menu/manage/update/${menuId}/`, {
    method: 'PUT',  // Use PUT for updates
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,  // CSRF token for security
    },
    body: JSON.stringify(updatedMenu),  // Convert the updated menu data to JSON
  })
    .then((response) => {
      return response.json().then((data) => {
        if (response.ok) {
          console.log('Menu updated successfully');
          window.location.reload(); // Reload the page to see the updated menu
        } else {
          console.log('Error:', data);

          // Display field-specific error messages
          if (data.errors) {
            if (data.errors.name) {
              const errorElement = document.getElementById('error-name');
              errorElement.innerText = data.errors.name;
              errorElement.style.display = 'block';
            }
            if (data.errors.price) {
              const errorElement = document.getElementById('error-price');
              errorElement.innerText = data.errors.price;
              errorElement.style.display = 'block';
            }
            if (data.errors.description) {
              const errorElement = document.getElementById('error-description');
              errorElement.innerText = data.errors.description;
              errorElement.style.display = 'block';
            }
            if (data.errors.category) {
              const errorElement = document.getElementById('error-category');
              errorElement.innerText = data.errors.category;
              errorElement.style.display = 'block';
            }
          } else if (data.error || data.error_message) {
            // Handle general error
            alert(data.error || data.error_message);
          }
        }
      });
    })
    .catch((error) => {
      console.error('Error:', error);
      alert('An error occurred while updating the menu.');
    });
}



// Function to delete a menu item
function deleteMenu() {
  const menuId = document.getElementById('menu-edit-form').getAttribute('data-menu-id');

  if (!confirm("Are you sure you want to delete this menu item?")) {
    return;
  }

  fetch(`/menu/manage/delete/${menuId}/`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
    },
  })
  .then((response) => {
    if (response.ok) {
      console.log('Menu item deleted successfully');
      window.location.reload();
    } else {
      console.error('Failed to delete menu item:', response.statusText);
    }
  })
  .catch((error) => console.error('Error:', error));
}

// Function to render the add category form
function renderAddCategory() {
  const editMenuFormContainer = document.getElementById('edit-menu-form');
  if (editMenuFormContainer) {
    editMenuFormContainer.classList.add('hidden');
  }

  const addMenuFormContainer = document.getElementById('add-menu-form');
  if (addMenuFormContainer) {
    addMenuFormContainer.classList.add('hidden');
  }
  const editFormContainer = document.getElementById('edit-category-form');
  if (editFormContainer) {
    editFormContainer.classList.add('hidden');
  }
  const addCategoryFormContainer = document.getElementById('add-category-form');
  if (addCategoryFormContainer) {
    addCategoryFormContainer.classList.remove('hidden');
  }
}

function renderEditCategoryName(categoryId, categoryName) {
  // Hide other forms or content if needed
  const addFormContainer = document.getElementById('add-category-form');
  if (addFormContainer) {
    addFormContainer.classList.add('hidden');
  }
  const editMenuFormContainer = document.getElementById('edit-menu-form');
  if (editMenuFormContainer) {
    editMenuFormContainer.classList.add('hidden');
  }

  const addMenuFormContainer = document.getElementById('add-menu-form');
  if (addMenuFormContainer) {
    addMenuFormContainer.classList.add('hidden');
  }

  // Show the edit form
  const editFormContainer = document.getElementById('edit-category-form');
  if (editFormContainer) {
    editFormContainer.classList.remove('hidden');

    // Populate the form fields with category data
    document.getElementById('category-id').value = categoryId;
    document.getElementById('category-name').value = categoryName || '';
      // Set the menu ID in a hidden field or the form's data attribute
    document.getElementById('edit-category-form').setAttribute('data-category-id', categoryId);
    }
  else {
    console.error('Menu item not found for ID:', menuId);
  }

}

function updateCategoryName() {
  const categoryId = document.getElementById('category-id').value;
  const updatedName = document.getElementById('category-name').value;

  // Select the error message div
  const errorElement = document.querySelector('.error-message');

  // Reset error message and hide the div initially
  errorElement.style.display = 'none';
  errorElement.innerText = '';

  // Check if the category name is empty
  if (!updatedName) {
    errorElement.innerText = 'Category name cannot be empty';  // Show error message
    errorElement.style.display = 'block';  // Make the error message div visible
    return;  // Stop the function here
  }

  fetch(`/menu/manage/category/update/${categoryId}/`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
    },
    body: JSON.stringify({ name: updatedName }),  // Send updated category name
  })
    .then((response) => response.json().then((data) => ({ status: response.status, data })))
    .then(({ status, data }) => {
      if (status === 200 && data.message) {
        // If the category is updated successfully
        console.log('Category updated successfully');
        window.location.reload();
      } else {
        // Display the error message
        errorElement.innerText = data.error_message;  // Show error message
        errorElement.style.display = 'block';  // Make the error message div visible
      }
    })
    .catch((error) => {
      console.error('Error:', error);
      errorElement.innerText = 'An unexpected error occurred';  // Show generic error message
      errorElement.style.display = 'block';  // Make the error message div visible
    });
}



function deleteCategory() {
  const categoryId = document.getElementById('category-id').value;

  fetch(`/menu/manage/category/delete/${categoryId}/`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
    },
  })
  .then((response) => {
    if (response.ok) {
      console.log('Category deleted successfully');
      window.location.reload();
    } else {
      console.error('Failed to delete category:', response.statusText);
    }
  })
  .catch((error) => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', function() {
  const searchElement = document.getElementById('search');
  if (searchElement) {
      searchElement.addEventListener('input', function() {
          const searchTerm = this.value.toLowerCase();
          document.querySelectorAll('.menu-card').forEach(item => {
              const name = item.querySelector('h3').textContent.toLowerCase();
              if (name.includes(searchTerm)) {
                  item.style.display = 'block';
              } else {
                  item.style.display = 'none';
              }
          });
      });
  }
});
