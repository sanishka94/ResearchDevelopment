import React from 'react';

import Auxilary from '../../hoc/Auxilary';
import classes from './Layout.module.css';
import Toolbar from '../Navigation/Toolbar/Toolbar';

const layout = (props) => (
    <Auxilary>
        <Toolbar />
        <main className={classes.Content}>
            {props.children}
        </main>
    </Auxilary>
);

export default layout;