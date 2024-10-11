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

  const addFormContainer = document.getElementById('add-menu-form');
  if (addFormContainer) {
    addFormContainer.classList.remove('hidden');
  }

  const addCategoryFormContainer = document.getElementById('add-category-form');
  if (addCategoryFormContainer) {
    addCategoryFormContainer.classList.add('hidden');
  }
}

// Function to update an existing menu item
// Function to update an existing menu item
function updateMenu() {
  const menuId = document.getElementById('menu-edit-form').getAttribute('data-menu-id');
  const updatedMenu = {
    name: document.getElementById('menu-name').value,
    price: parseFloat(document.getElementById('menu-price').value),
    description: document.getElementById('menu-description').value,
    category: document.getElementById('menu-category').value,  // Assuming category is a dropdown with value as ID
  };
  console.log('Updated Menu:', updatedMenu);

  fetch(`/menu/manage/update/${menuId}/`, {
    method: 'PUT',  // Use POST instead of PUT
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
    },
    body: JSON.stringify(updatedMenu),
  })
    .then((response) => {
      if (response.ok) {
        console.log('Menu updated successfully');
        window.location.reload(); // Reload the page to see the updated menu
      } else {
        console.error('Failed to update menu:', response.statusText);
      }
    })
    .catch((error) => console.error('Error:', error));
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

function editCategoryName(method) {
  switch (method) {
    case 'edit_category':
      updateCategoryName();
      break;
    case 'delete_category':
      deleteCategory();
      break;
    default:
      console.error('Invalid method:', method);
  }
}

function updateCategoryName(){
  const categoryId = document.getElementById('category-id').value;
  const updatedName = document.getElementById('category-name').value;

  fetch(`/menu/manage/category/update/${categoryId}/`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
    },
    body: JSON.stringify({ name: updatedName }),  // Send updated category name
  })
    .then((response) => {
      if (response.ok) {
        console.log('Category updated successfully');
        window.location.reload();  // Reload the page to see the updated category
      } else {
        console.error('Failed to update category:', response.statusText);
      }
    })
    .catch((error) => console.error('Error:', error));
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