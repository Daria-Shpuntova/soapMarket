document.querySelectorAll('.filter').forEach(function(filter) {
    filter.addEventListener('change', function() {
        if (this.value === 'all' && this.checked) {
            document.querySelectorAll('.filter').forEach(function(f) {
                if (f.value !== 'all') {
                    f.checked = false;
                    document.querySelector('.filter[value="all"]').checked = false;
                    document.querySelectorAll('.prod').forEach(function(product){
                        product.style.display = 'grid';
                    });
                }
            });
        } else {
            var selectedFilters = document.querySelectorAll('.filter:checked');
            var selectedCategories = Array.from(selectedFilters).map(function(filter) {
                return filter.value;
            });
            document.querySelectorAll('.prod').forEach(function(product) {
                if (selectedCategories.length === 0 || selectedCategories.includes(product.dataset.category)) {
                    product.style.display = 'grid';

                } else {
                    product.style.display = 'none';
                }
            });
        }
    });
});

document.querySelectorAll('.filter_skin').forEach(function(filter) {
    filter.addEventListener('change', function() {
        if (this.value === 'all' && this.checked) {
            document.querySelectorAll('.filter_skin').forEach(function(f) {
                if (f.value !== 'all') {
                    f.checked = false;
                    document.querySelector('.filter_skin[value="all"]').checked = false;
                    document.querySelectorAll('.prod').forEach(function(product){
                        product.style.display = 'grid';
                    });
                }
            });
        } else {
            var selectedFilters = document.querySelectorAll('.filter_skin:checked');
            var selectedSkin = Array.from(selectedFilters).map(function(filter_skin) {
                return filter_skin.value;
            });
            document.querySelectorAll('.prod').forEach(function(product) {
                if (selectedSkin.length === 0 || selectedSkin.includes(product.dataset.skintype)) {
                    product.style.display = 'grid';

                } else {
                    product.style.display = 'none';
                }
            });
        }
    });
});