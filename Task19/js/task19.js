
// Add item button 
function addItem() {
    const input = document.getElementById('textInput');
    const text = input.value.trim();

    if (text !== '') {
        addItemToList(text);

        const items = JSON.parse(localStorage.getItem('items')) || [];
        items.push(text);
        saveItems(items);

        input.value = '';
    }
}
// Save items to local storage
function saveItems(items) {
    localStorage.setItem('items', JSON.stringify(items));
}

// Add item to the list
function addItemToList(text) {
    const itemList = document.getElementById('itemList');
    const item = document.createElement('li');
    item.textContent = text;

    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'Delete';
    deleteButton.addEventListener('click', function () {
        deleteItem(item);
    });

    item.appendChild(deleteButton);
    itemList.appendChild(item);
}

// Delete item from the list
function deleteItem(item) {
    localStorage.removeItem("items");
    const itemList = document.getElementById('itemList');
    itemList.removeChild(item);
}



//     const items = JSON.parse(localStorage.getItem('items')) || [];
//     const itemIndex = items.indexOf(item.textContent);
//     if (itemIndex !== -1) {
//         items.splice(itemIndex, 1);
//         saveItems(items);
//     }
// }


//  // Load stored items from local storage
// function loadItems() {
//     const items = JSON.parse(localStorage.getItem('items')) || [];
//     items.forEach(item => addItemToList(item));
//   }
