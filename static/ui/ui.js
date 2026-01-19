const CART_KEY = "chained_cart";
const ANIMATION_KEY = "chained_animations";

const getCart = () => {
  try {
    return JSON.parse(localStorage.getItem(CART_KEY)) || [];
  } catch (error) {
    return [];
  }
};

const saveCart = (items) => {
  localStorage.setItem(CART_KEY, JSON.stringify(items));
};

const formatPrice = (value) => new Intl.NumberFormat("ru-RU").format(value);

const updateCounters = (items) => {
  const totalCount = items.reduce((sum, item) => sum + item.quantity, 0);
  document.querySelectorAll(".js-cart-count").forEach((node) => {
    node.textContent = totalCount;
  });
};

const renderCart = (items) => {
  const list = document.querySelector(".js-cart-items");
  const totalNode = document.querySelector(".js-cart-total");
  if (!list || !totalNode) return;

  list.innerHTML = "";
  if (items.length === 0) {
    list.innerHTML = "<div class=\"ui-cart-item-meta\">Корзина пуста. Выберите товары из каталога.</div>";
  }

  let total = 0;
  items.forEach((item) => {
    total += item.price * item.quantity;
    const wrapper = document.createElement("div");
    wrapper.className = "ui-cart-item";
    wrapper.innerHTML = `
      <div>
        <div class="ui-cart-item-title">${item.title}</div>
        <div class="ui-cart-item-meta">${item.quantity} × ${formatPrice(item.price)} ₽</div>
      </div>
      <button type="button" data-remove="${item.id}">Удалить</button>
    `;
    list.appendChild(wrapper);
  });

  totalNode.textContent = formatPrice(total);

  list.querySelectorAll("[data-remove]").forEach((button) => {
    button.addEventListener("click", () => {
      const id = button.getAttribute("data-remove");
      const next = items.filter((item) => item.id !== id);
      saveCart(next);
      updateCounters(next);
      renderCart(next);
    });
  });
};

const addToCart = (product) => {
  const items = getCart();
  const existing = items.find((item) => item.id === product.id);
  if (existing) {
    existing.quantity += 1;
  } else {
    items.push({ ...product, quantity: 1 });
  }
  saveCart(items);
  updateCounters(items);
  renderCart(items);
};

const setupCart = () => {
  const cartButton = document.querySelectorAll(".js-cart-toggle");
  const body = document.body;

  cartButton.forEach((button) => {
    button.addEventListener("click", () => {
      body.classList.toggle("cart-open");
    });
  });

  const items = getCart();
  updateCounters(items);
  renderCart(items);

  document.querySelectorAll("[data-product]").forEach((node) => {
    node.addEventListener("click", () => {
      const title = node.getAttribute("data-product");
      const price = Number(node.getAttribute("data-price"));
      if (!title || !price) return;
      addToCart({
        id: node.getAttribute("data-id") || title,
        title,
        price,
      });
      body.classList.add("cart-open");
    });
  });
};

const setupAnimationToggle = () => {
  const toggle = document.querySelector(".js-animations-toggle");
  if (!toggle) return;

  const applyState = (enabled) => {
    document.body.classList.toggle("animations-off", !enabled);
    toggle.classList.toggle("is-active", enabled);
    toggle.setAttribute("aria-pressed", enabled ? "true" : "false");
  };

  const saved = localStorage.getItem(ANIMATION_KEY);
  const enabled = saved !== "off";
  applyState(enabled);

  toggle.addEventListener("click", () => {
    const currentlyEnabled = !document.body.classList.contains("animations-off");
    const next = !currentlyEnabled;
    localStorage.setItem(ANIMATION_KEY, next ? "on" : "off");
    applyState(next);
  });
};

window.addEventListener("DOMContentLoaded", () => {
  setupCart();
  setupAnimationToggle();
});
