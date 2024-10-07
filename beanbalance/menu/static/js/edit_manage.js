function renderPage(method, id=null) {
  const editFormContainer = document.getElementById('add-menu-form');
  const addCategoryForm = document.getElementById('add-category-form');
  const editMenuForm = document.getElementById('edit-menu-form');

  editFormContainer.classList.add('hidden');
  addCategoryForm.classList.add('hidden');
  editMenuForm.classList.add('hidden');

  switch (method) {
    case 'add_menu':
      editFormContainer.classList.remove('hidden');
      break;
    case 'add_category':
      addCategoryForm.classList.remove('hidden');
      break;
    case 'edit_menu':
      editMenuForm.classList.remove('hidden');
      if (id) {
        // Send the ID to the view using a GET request
        fetch(`/menu/edit-menu?id=${id}/`)
          .then(response => response.json())
          .then(data => {
            console.log(data);
            // You can use data to pre-populate the form fields here
          })
          .catch(error => console.error('Error:', error));
      }
      break;
  }
}

