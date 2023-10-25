document.addEventListener('DOMContentLoaded', function () {
    const addBookForm = document.querySelector('#add-book-form');
    if (addBookForm) {
      addBookForm.addEventListener('submit', function (event) {
        event.preventDefault();
  
        const title = document.querySelector('#title').value;
        const author = document.querySelector('#author').value;
  
        // Make an AJAX request to add the book
        fetch('/add_book', {
          method: 'POST',
          body: JSON.stringify({ title: title, author: author }),
          headers: {
            'Content-Type': 'application/json',
          },
        })
          .then((response) => response.json())
          .then((data) => {
            if (data.success) {
              // Book added successfully, perform any desired UI update
              console.log('Book added successfully');
              // Optionally, you can reload the page or update the book list.
            } else {
              // Handle the error case
              console.error('Failed to add book');
            }
          });
      });
    }
  
    document.addEventListener('DOMContentLoaded', function () {
        const updateBookForms = document.querySelectorAll('.update-book-form');
        const deleteBookForms = document.querySelectorAll('.delete-book-form');
      
        // Function to send AJAX request for updating a book
        function updateBook(event, bookId) {
          event.preventDefault();
      
          const title = document.querySelector(`#title-${bookId}`).value;
          const author = document.querySelector(`#author-${bookId}`).value;
      
          fetch(`/update_book/${bookId}`, {
            method: 'POST',
            body: JSON.stringify({ title: title, author: author }),
            headers: {
              'Content-Type': 'application/json',
            },
          })
            .then((response) => response.json())
            .then((data) => {
              if (data.success) {
                // Book updated successfully, perform any desired UI update
                console.log('Book updated successfully');
                // Optionally, you can reload the page or update the book list.
              } else {
                // Handle the error case
                console.error('Failed to update book');
              }
            });
        }
      
        // Function to send AJAX request for deleting a book
        function deleteBook(event, bookId) {
          event.preventDefault();
      
          fetch(`/delete_book/${bookId}`, {
            method: 'POST',
          })
            .then((response) => response.json())
            .then((data) => {
              if (data.success) {
                // Book deleted successfully, perform any desired UI update
                console.log('Book deleted successfully');
                // Optionally, you can reload the page or update the book list.
              } else {
                // Handle the error case
                console.error('Failed to delete book');
              }
            });
        }
      
        // Attach event listeners to update and delete forms
        if (updateBookForms) {
          updateBookForms.forEach((form) => {
            form.addEventListener('submit', (event) => {
              const bookId = form.getAttribute('data-book-id');
              updateBook(event, bookId);
            });
          });
        }
      
        if (deleteBookForms) {
          deleteBookForms.forEach((form) => {
            form.addEventListener('submit', (event) => {
              const bookId = form.getAttribute('data-book-id');
              deleteBook(event, bookId);
            });
          });
        }
      });
  });