import React, { useState } from 'react';
import PropTypes from 'prop-types';

import './AddTodo.css';

function AddTodo({onComplete}) {
    const [title, setTitle] = useState('');

    return (
        <form className="TodoForm">
            <input className="InputText" type="text" name="title" placeholder="Add Todo..." onChange={(e) => setTitle(e.target.value)}/>
            <input type="button" value="Submit" className="InputButton" onClick={(e) => onComplete(title)}/>
        </form>
    );
}

AddTodo.propTypes = {
    onComplete: PropTypes.func.isRequired
};

export default AddTodo;