import React from 'react';
import TodoItem from './TodoItem';
import PropTypes from 'prop-types';

function TodoList({data, onItemUpdate, onItemRemove}) {
    const onMarked = (item) => {
        onItemUpdate({...item, completed: !item.completed});
    };

    const onDelete = (id) => {
        onItemRemove(id);
    };
    
    return data.map((todo) => (
        <TodoItem key={todo.id} item={todo} onMarked={onMarked} onDelete={onDelete}/>
    ));
}

TodoList.propTypes = {
    data: PropTypes.array.isRequired,
    onItemUpdate: PropTypes.func.isRequired,
    onItemRemove: PropTypes.func.isRequired
};

export default TodoList;