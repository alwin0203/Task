document.addEventListener("DOMContentLoaded", function () {
    var cartCountElement = document.getElementById("cartCount");
    var totalPriceElement = document.getElementById("totalPrice");
    var clearButton = document.getElementById("clearButton");
    var addToCartButtons = document.getElementsByClassName("add-to-cart-button");
    // var stockCountElement = document.getElementById("stockCount1");



    var cartCount = 0;
    var totalPrice = 0;
    var cartItems = [];
    // var stockCount1 = 10

    // Load cart items from local storage if available
    if (localStorage.getItem("cartItems")) {
        cartItems = JSON.parse(localStorage.getItem("cartItems"));
        cartCount = cartItems.length;
        // stockCount1= cartItems.length;
        totalPrice = calculateTotalPrice(cartItems);
        updateCartCount();
        updateTotalPrice();
    }

    // Update the count in the circle
    function updateCartCount() {
        cartCountElement.innerHTML = cartCount;
        // stockCountElement.innerHTML = stockCount1


    }

    // Update the total price

    function updateTotalPrice() {
        totalPriceElement.innerHTML = "$" + totalPrice;
    }

    // Calculate the total price of all cart items
    function calculateTotalPrice(items) {
        var total = 0;
        for (var i = 0; i < items.length; i++) {
            total += items[i].price;
        }
        return total;
    }


    // Add item to the cart
    function addToCart(item) {
        var stock = parseInt(item.getAttribute("data-stock"));




        if (stock > 0) {
            stock--;
            item.setAttribute("data-stock", stock);


            var newItem = {
                name: item.parentNode.querySelector("p").innerText,
                price: parseInt(item.getAttribute("data-price"))
            };
            cartItems.push(newItem);

            cartCount++;
            // stockCount1--;

            totalPrice += newItem.price;

            updateCartCount();
            updateTotalPrice();

            // Update local storage
            localStorage.setItem("cartItems", JSON.stringify(cartItems));
        } else {
            alert("Out of stock!");
        }
    }

    // Event listener for Add to Cart buttons
    for (var i = 0; i < addToCartButtons.length; i++) {
        addToCartButtons[i].addEventListener("click", function () {
            addToCart(this);
        });

    }



    // Clear the cart and local storage
    function clearCart() {
        cartItems = [];
        // stockCount1 = 10
        cartCount = 0;
        totalPrice = 0;
        updateCartCount();
        updateTotalPrice();
        localStorage.removeItem("cartItems");
    }

    clearButton.addEventListener("click", function () {
        clearCart();
    });
});


// function decrement() {
//     document.getElementById("stockCount2").innerHTML = stockCount2--;
// }
document.addEventListener("DOMContentLoaded", function () {
    var stock = 10;

    // Event listener for Add to Cart buttons
    var addToCartButtons = document.getElementsByClassName("product1");
    for (var i = 0; i < addToCartButtons.length; i++) {
        addToCartButtons[i].addEventListener("click", function () {
            var stockElement = this.parentNode.querySelector(".stockone");
            var currentStock = parseInt(stockElement.innerText);

            if (currentStock > 0) {
                currentStock--;
                stockElement.innerText = currentStock;
                stock--;
            } else {
                alert("Out of stock!");
            }
        });
    }
});

document.addEventListener("DOMContentLoaded", function () {
    var stock = 3;

    // Event listener for Add to Cart buttons
    var addToCartButtons = document.getElementsByClassName("product2");
    for (var i = 0; i < addToCartButtons.length; i++) {
        addToCartButtons[i].addEventListener("click", function () {
            var stockElement = this.parentNode.querySelector(".stocktwo");
            var currentStock = parseInt(stockElement.innerText);

            if (currentStock > 0) {
                currentStock--;
                stockElement.innerText = currentStock;
                stock--;
            } else {
                alert("Out of stock!");
            }
        });
    }
});


document.addEventListener("DOMContentLoaded", function () {
    var stock = 5;

    // Event listener for Add to Cart buttons
    var addToCartButtons = document.getElementsByClassName("product3");
    for (var i = 0; i < addToCartButtons.length; i++) {
        addToCartButtons[i].addEventListener("click", function () {
            var stockElement = this.parentNode.querySelector(".stockthree");
            var currentStock = parseInt(stockElement.innerText);

            if (currentStock > 0) {
                currentStock--;
                stockElement.innerText = currentStock;
                stock--;
            } else {
                alert("Out of stock!");
            }
        });
    }
});

