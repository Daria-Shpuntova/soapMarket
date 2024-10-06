function applyFilters() {
    var selectedCategories = getSelectedValues('.filter');
    var selectedSkinTypes = getSelectedValues('.filter_skin');
    var selectedEffect = getSelectedValues('.filter_effect');
    var selectedIngredient = getSelectedValues('.filter_ingredient');
    var showOnlyAvailable = document.querySelector('.filter_quantity').checked;

    document.querySelectorAll('.prod').forEach(function(product) {
        if ((selectedCategories.length === 0 || selectedCategories.includes(product.dataset.category)) &&
            (selectedSkinTypes.length === 0 || selectedSkinTypes.includes(product.dataset.skintype)) &&
            (selectedEffect.length === 0 || selectedEffect.includes(product.dataset.effect)) &&
            (selectedIngredient.length === 0 || selectedIngredient.includes(product.dataset.ingredient)) &&
            (!showOnlyAvailable || parseInt(product.dataset.quantity) > 0)){
            product.style.display = 'grid';
        } else {
            product.style.display = 'none';
        }
    });
}

function getSelectedValues(selector) {
    var selectedFilters = document.querySelectorAll(selector + ':checked');
    return Array.from(selectedFilters).map(function(filter) {
        return filter.value;
    });
}

document.querySelectorAll('.filter').forEach(function(filter) {
    filter.addEventListener('change', function() {
        if (this.value === 'all_a' && this.checked) {
            document.querySelectorAll('.filter').forEach(function(f) {
                if (f.value !== 'all_a') {
                    f.checked = true;
                }
            });
        }
        applyFilters();
    });
});

document.querySelectorAll('.filter_skin').forEach(function(filter) {
    filter.addEventListener('change', function() {
        if (this.value === 'all_st' && this.checked) {
            document.querySelectorAll('.filter_skin').forEach(function(f) {
                if (f.value !== 'all_st') {
                    f.checked = true;
                }
            });
        }
        applyFilters();
    });
});

document.querySelectorAll('.filter_effect').forEach(function(filter) {
    filter.addEventListener('change', function() {
        if (this.value === 'all_ef' && this.checked) {
            document.querySelectorAll('.filter_effect').forEach(function(f) {
                if (f.value !== 'all_ef') {
                    f.checked = true;
                }
            });
        }
        applyFilters();
    });
});

document.querySelectorAll('.filter_ingredient').forEach(function(filter) {
    filter.addEventListener('change', function() {
        if (this.value === 'all_in' && this.checked) {
            document.querySelectorAll('.filter_ingredient').forEach(function(f) {
                if (f.value !== 'all_in') {
                    f.checked = true;
                }
            });
        }
        applyFilters();
    });
});

document.querySelector('.filter_quantity').addEventListener('change', function() {
    applyFilters();
});