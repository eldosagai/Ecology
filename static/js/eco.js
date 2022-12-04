const id = localStorage.getItem('id');
const topicsItemTemplate = document.querySelector('[data-topics-template]');
const topicsItemContainer = document.querySelector('[data-topics-item-container]');

fetch(`https://baizaknews.herokuapp.com/eco/${id}`)
    .then(res => res.json())
    .then(data => {

        const mainTitle = document.querySelector('[data-title]');
        const mainText = document.querySelector('[data-p-introduction]')
        mainTitle.textContent = data[0].title;
        mainText.textContent = data[0].maintext;

        data.map(template => {

            if(template.subtitle !== undefined) {

                const item = topicsItemTemplate.content.cloneNode(true).children[0];
                const itemImg = item.querySelector('[data-img]');
                const itemTitle = item.querySelector('[data-title]');
                const itemText = item.querySelector('[data-p]');
                itemImg.src = template.img;
                itemTitle.textContent = template.subtitle;
                itemText.textContent = template.submainText;

                topicsItemContainer.append(item)
                
            }

        })
    })