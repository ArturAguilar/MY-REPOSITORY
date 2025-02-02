document.getElementById('search').addEventListener('input', function() {
    let filter = this.value;
    let sections = document.querySelectorAll('.conteiner');
    
    sections.forEach(section => {
        let links = section.querySelectorAll('a');
        let hasVisibleLink = false;
        
        links.forEach(link => {
            let linkText = link.textContent;
            if (linkText.includes(filter)) {
                link.style.display = "inline-block";
                hasVisibleLink = true;
            } else {
                link.style.display = "none";
            }
        });
        
        section.style.display = hasVisibleLink ? "block" : "none";
    });
});
