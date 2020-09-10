import React from 'react';

const UserOutput = props => {
    const style = {
        display: 'flex',
        margin: 'auto',
        width: '600px',
        textAlign: 'left'
    }

    return (
        <div className="UserOutput">
            <div style={style}>
                <p>{props.username} is simply dummy text of the printing
                and typesetting industry. {props.username} has been
                the industry's standard dummy text ever since the
                1500s, when an unknown printer took a galley of
                type and scrambled it to make a type specimen book.</p>
                <p>{props.username} is simply dummy text of the printing
                and typesetting industry. {props.username} has been
                the industry's standard dummy text ever since the
                1500s, when an unknown printer took a galley of
                type and scrambled it to make a type specimen book.</p>
            </div>
        </div>
    )
};

export default UserOutput;