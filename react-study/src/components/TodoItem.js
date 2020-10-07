import React from 'react';
import PropTypes from 'prop-types';

import './TodoItem.css';

function TodoItem({item, onMarked, onDelete}) {
    const getStyle = () => {
        return {
            textDecoration: item.completed ? 'line-through':'none'
        }
    };

    return (
        <div className="TodoItem" style={getStyle()}>
            <p>
                <input type="checkbox" onChange={() => onMarked(item)} checked={item.completed}/>
                {' ' + item.title}
                <button className="DeleteButton" onClick={() => onDelete(item.id)}>x</button>
            </p>
        </div>
    );
}

TodoItem.propTypes = {
    item: PropTypes.object.isRequired,
    onMarked: PropTypes.func.isRequired,
    onDelete: PropTypes.func.isRequired
};

export default TodoItem;