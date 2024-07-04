const drag = (event) => {
    event.dataTransfer.setData("text/plain", event.target.id);
};

const allowDrop = (ev) => {
    ev.preventDefault();
    if (hasClass(ev.target, "dropzone")) {
        addClass(ev.target, "droppable");
    }
};

const clearDrop = (ev) => {
    removeClass(ev.target, "droppable");
};

const drop = (event) => {
    event.preventDefault();
    const data = event.dataTransfer.getData("text/plain");
    const element = document.querySelector(`#${data}`);

    try {
        event.target.removeChild(event.target.firstChild);
        event.target.appendChild(element);
        unwrap(event.target);

        const taskId = element.id.split('-')[1]; 
        const newStatus = event.target.dataset.status;

        updateTaskStatus(taskId, newStatus); 
    } catch (error) {
        console.warn("Can't move the item to the same place");
    }
    updateDropzones();
};

const updateTaskStatus = (taskId, newStatus) => {
    fetch(`/update_task_status/${taskId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({ status: newStatus }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log('Task status updated successfully:', data);
    })
    .catch(error => {
        console.error('Error updating task status:', error);
    });
};

const updateDropzones = () => {
    $('.dropzone').remove();

    const dz = $('<div class="dropzone rounded" ondrop="drop(event)" ondragover="allowDrop(event)" ondragleave="clearDrop(event)"> &nbsp; </div>');
    dz.insertAfter('.card.draggable');

    $(".items:not(:has(.card.draggable))").append(dz);
};

const updateProjectStatus = (projectId, newStatus) => {
    fetch('/update_project_status/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'), 
        },
        body: JSON.stringify({ id: projectId, status: newStatus }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log('Project status updated successfully:', data);
    })
    .catch(error => {
        console.error('Error updating project status:', error);
    });
};

function hasClass(element, className) {
    return (' ' + element.className + ' ').indexOf(' ' + className + ' ') > -1;
}

function addClass(element, className) {
    if (!hasClass(element, className)) {
        element.className += ' ' + className;
    }
}

function removeClass(element, className) {
    element.className = element.className.replace(new RegExp('(?:^|\\s)' + className + '(?!\\S)', 'g'), '');
}

function unwrap(node) {
    node.replaceWith(...node.childNodes);
}